"""Classes associated with the eventual solar plant we're constructing. The classes
in the `constructionplant` module act on these to build out the solar plant."""

__author__ = 'Peter May-Ostendorp'

from typing import Union
from geojson import GeoJSON

from hardhat.components import BaseComponent
from hardhat.gis.geometry import Feature, Polygon
from hardhat.gis.geojson import coord_array, process_geojson, filter_features, transformer_from_geom
from hardhat.util.exceptions import err_on_type, err_on_tb_properties


class Table(BaseComponent):
    """A simple dict-like class for PV tables"""

    table_type = BaseComponent.char_field(default='', max_length=125)
    tracker_id = BaseComponent.uuid_field(default=0)
    num_modules = BaseComponent.int_field(default=0)
    assigned = BaseComponent.bool_field(default=False)

    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)

    @classmethod
    def from_geojson(cls, geojson, **kwargs):
        """Generates Table representation from geojson."""
        geojson = process_geojson(geojson)
        err_on_tb_properties(geojson, type='Table')
        err_on_type(geojson, Feature)
        err_on_type(geojson['geometry'], Polygon)

        # Get transformers
        kwargs['to_utm'], kwargs['to_wgs'] = transformer_from_geom(geojson, **kwargs)

        # Now get other properties
        kwds = {'id', 'name', 'tracker_id', 'num_modules', 'table_type'}
        for key, val in geojson['properties']['terabase'].items():
            if key in kwds:
                kwargs[key] = val

        # Assemble rest of kwargs
        kwargs['geometry'] = geojson

        # Now build the instance
        return cls(**kwargs)


class Tracker(BaseComponent):
    """Simple class for trackers"""
    # TODO: transition from IDs to pointers
    tracker_type = BaseComponent.char_field(default='', max_length=125)
    workfront_id = BaseComponent.uuid_field(default=0)
    workfront_ptr = BaseComponent.pointer("Workfront")
    table_list = BaseComponent.collection(Table)
    assigned = BaseComponent.bool_field(default=False)
    num_modules = BaseComponent.int_field(default=0)
    num_tables = BaseComponent.int_field(default=0)

    def __init__(self, *args, **kwargs):
        super(Tracker, self).__init__(*args, **kwargs)
        # Some type checks
        for t in self.table_list:
            err_on_type(t, Table)

        self.num_modules = self._num_modules()
        self.num_tables = self._num_tables()

    def _num_modules(self) -> int:
        return sum([t.num_modules for t in self.table_list])

    def _num_tables(self) -> int:
        return len(self.table_list)

    @classmethod
    def from_geojson(cls, geojson_feature:Union[str,dict,Feature], geojson_extents:Union[str,dict,GeoJSON]={}, **kwargs):
        """Generates model representation from geojson."""
        geojson_feature = process_geojson(geojson_feature)
        err_on_tb_properties(geojson_feature, type='Tracker')
        err_on_type(geojson_feature, Feature)
        err_on_type(geojson_feature['geometry'], Polygon)

        # Get transformers
        kwargs['to_utm'], kwargs['to_wgs'] = transformer_from_geom(geojson_feature, **kwargs)

        # Now get other properties
        kwds = {'id', 'name', 'workfront_id', 'tracker_type'}
        for key, val in geojson_feature['properties']['terabase'].items():
            if key in kwds:
                kwargs[key] = val

        # Assemble rest of kwargs
        kwargs['geometry'] = geojson_feature
        # kwargs['assembly_line_list'] = [] # No assembly sites associated.
        kwargs['table_list'] = [] # No tables associated.

        # NOTE: performs really poorly... probably O(n^2)
        # Gather the associated tables
        if geojson_extents:
            tables = filter_features(
                geojson_extents['features'],
                type='Table',
                tracker_id=kwargs['id']
            )
            kwargs['table_list'] = [Table.from_geojson(f_table) for f_table in tables]

        # Now build the instance
        return cls(**kwargs)

    def assign_tables(self, tables:list[Table]) -> None:
        """Assigns tables to tables using their tracker_id attribute."""
        self.table_list = [tab for tab in tables if tab.tracker_id == self.id]
        self.num_modules = self._num_modules()
        self.num_tables = self._num_tables()
