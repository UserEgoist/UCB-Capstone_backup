import os
import datetime
import uuid
import numpy as np
from typing import Union
from pyproj import Transformer
from copy import deepcopy

import matplotlib.pyplot as plt

from hardhat.gis.geojson import process_geojson, coord_array, transformer_from_geom
from hardhat.gis.geometry import Point


class TempFieldWrapper(object):

    def __init__(self, wrapped_value):
        self.wrapped_value = wrapped_value

    def get_wrapped_value(self):
        return self.wrapped_value


class NoORMBase(object):

    def __init__(self, *args, **kwargs):
        self.defined_object_attrs = []
        self.find_and_unwrap_fields()
        self.assign_kwargs(**kwargs)

    def find_and_unwrap_fields(self):
        for field_name in dir(self.__class__):
            if isinstance(getattr(self, field_name), TempFieldWrapper):
                self.defined_object_attrs.append(field_name)
                setattr(self, field_name, getattr(self, field_name).get_wrapped_value())

    def assign_kwargs(self, **kwargs):
        for kwarg in kwargs:
            if kwarg in self.defined_object_attrs:
                setattr(self, kwarg, kwargs[kwarg])

    @classmethod
    def pointer(cls, col_class, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else None)

    @classmethod
    def collection(cls, col_class, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else [])

    @classmethod
    def float_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else 0.0)

    @classmethod
    def int_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else 0)

    @classmethod
    def bool_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else False)

    @classmethod
    def char_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else "")

    @classmethod
    def date_time_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else datetime.date.today())

    @classmethod
    def uuid_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else '')

    @classmethod
    def enum_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else '')

    @classmethod
    def json_field(cls, *args, **kwargs):
        return TempFieldWrapper(kwargs['default'] if 'default' in kwargs else {})

    
model_class = NoORMBase
user_model_class = NoORMBase
    
    
class TerabaseModel(model_class):
    """
    Created by Allan Daly
    Modified, Peter May-Ostendorp

    abstract base model for all Terabase model objects, compatible with ORM or not

    adds the following properties to all Terabase model objects
      - created_at  <-- datetime when object was created
      - created_by  <-- user who created the object
      - modified_at  <-- datetime when the object was last modified
      - modified_by  <-- user who last modified the object

    adds the following class methods
      - list  <-- prints a reasonably formatted list of all the objects in the class
      - show  <-- prints a reasonabley formatted list of all the properties and values for an objects

    """
    created_at = model_class.date_time_field(auto_now_add=True)
    created_by = model_class.pointer(user_model_class, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True)

    modified_at = model_class.date_time_field(auto_now=True)
    modified_by = model_class.pointer(user_model_class, related_name="%(app_label)s_%(class)s_modified_by", null=True, blank=True)

    id = model_class.uuid_field(primary_key=True, editable=False)

    class Meta(object):
        abstract = True

    def __iter__(self):

        for field_name in self._meta.get_fields():
            field_name_only = field_name.name.split('.')[-1]
            value = getattr(self, field_name_only, None)

            yield (field_name_only, value)

    @classmethod
    def list(cls):

        print('\n'.join(
            ['id:{}  name: {}'.format(o.id, o.name if hasattr(o, 'name') else '-') for o in cls.objects.all()]))

    def show(self):

        field_names_and_vals = [[field, val] for field, val in self]
        longest_name_length = max(len(f[0]) for f in field_names_and_vals)

        for f in field_names_and_vals:
            print('{}: {}'.format(f[0].rjust(longest_name_length + 1), f[1]))


class BaseComponent(TerabaseModel):
    """A base class for Terabase digital twin components with a geographic representation.

    :param id: UUID inherited from super class
    :param index: integer index
    :param name: string name
    :param x: x coordinate in UTM
    :param y: y coordinate in UTM
    :param to_utm: pyproj Transformer WGS84 -> UTM
    :param to_wgs: pyproj Transformer UTM -> WGS84
    """
    class Meta:
        abstract = True

    index = model_class.int_field()
    name = model_class.char_field(max_length=256)
    x = model_class.float_field()
    y = model_class.float_field()
    # to_utm = model_class.pointer(Transformer)
    # to_wgs = model_class.pointer(Transformer)

    # todo need to decide how geometry will be saved...
    def __init__(self, *args, geometry:Union[dict, str] = None,
            to_utm:Transformer=None, to_wgs:Transformer=None, **kwargs):
        super(BaseComponent, self).__init__(*args, **kwargs)
        self.geometry = geometry
        self.to_utm = to_utm
        self.to_wgs = to_wgs
        if self.geometry:
            self._process_geometry()

            # calculate the coordinates from geometry if we didn't get x or y
            if (not self.x or not self.y):
                if self.to_utm is None:
                    raise ValueError('When inferring x, y coordinate from geometry, to_utm transformer must be specified.')

                coords = coord_array(self.geometry)
                centroid = coords.mean(axis=0)
                self.x, self.y = self.to_utm.transform(centroid[0], centroid[1])

    def __repr__(self) -> str:
        return f'{self.id if self.id else self.index}: ({self.x:.3f}, {self.y:.3f})'

    def xy(self) -> np.ndarray:
        """Returns the xy coordinates as a numpy vector."""
        return np.array([self.x, self.y]).reshape([1,2]) # Note the order

    def plot(self, utm_transform:bool=False, plot_geom:bool=True, plot_centroid:bool=False, plot_index:bool=False,
            geom_kwargs:dict={}, centroid_kwargs:dict={}, *args, **kwargs):
        """Plot object using Matplotlib.

        Allows plotting of underlying geometry and centroid using Matplotlib. Also
        able to plot all related objects in the model hierarchy using the `plot_children`
        attribute.

        :param utm_transform: Plot in utm coordinates. Defaults to True. The object must
            have a pyproj.Transformer object associated with its to_utm attribute.
        :param plot_geom: Plot the object's geometry, by default True.
        :param plot_centroid: Also plot the object's centroid, by default False.
        :param plot_index: Plot object's index as text.
        :param geom_kwargs: dict of keyword arguments to pass to plotting methods for
            geometry.
        :param centroid_args: dict of keyword arguments for centroid plotting.
        :param args: additional positional arguments will be passed to plotting
        :param kwargs: additional keyword arguments that will be passed to all plotting

        Other *args and **kwargs harvested by Matplotlib.
        """
        if not self.geometry:
            raise ValueError('Cannot plot objects without geometry.')

        to_utm, to_wgs = transformer_from_geom(self.geometry, to_utm=self.to_utm, to_wgs=self.to_wgs)

        geom = deepcopy(self.geometry) # Assumed in WGS84
        centroid = Point([self.x, self.y]) # assumed already in UTM
        # Coordinate conversions as needed
        if utm_transform:
            geom = geom.coord_transform(to_utm)
        else:
            centroid = centroid.coord_transform(to_wgs)

        if plot_geom:
            # Get geom kwargs
            if geom_kwargs:
                geom_kwargs.update(kwargs)
            geom.plot(*args, **geom_kwargs)

        if plot_centroid:
            if centroid_kwargs:
                centroid_kwargs.update(kwargs)
            centroid.plot(*args, **centroid_kwargs)

        if plot_index:
            plt.text(centroid['coordinates'][0], centroid['coordinates'][1], str(self.index))

    def dist_grid(self, obj) -> float:
        """Manhattan distance from one object to another."""
        return np.sum(np.abs(self.xy() - obj.xy()), axis=1)[0]

    def _process_geometry(self):
        """Flexibly post-process geometry passed as string and validate geoJSON"""
        self.geometry = process_geojson(self.geometry)