"""Classes to wrap geojson geometries with some additional functionality."""

__author__ = 'Peter May-Ostendorp'

import geojson
from descartes import PolygonPatch
import matplotlib.pyplot as plt
from pyproj import Transformer


def coord_transform(obj:geojson.GeoJSON, transformer:Transformer) -> dict:
    """Returns version of geojson-like geometry with coordinates transformed with transformer."""
    return geojson.utils.map_tuples(lambda x: transformer.transform(x[0], x[1]), obj)


class Point(geojson.Point):
    """Wrap geojson Point class"""

    def __init__(self, *args, **kwargs):
        super(Point, self).__init__(*args, **kwargs)

    def plot(self, *args, **kwargs):
        """Plot point using Matplotlib."""
        x, y = self['coordinates'][0], self['coordinates'][1]
        plt.plot(x, y, *args, **kwargs)

    def coord_transform(self, transformer:Transformer):
        """Transform coordinates of Point using transformer."""
        obj = coord_transform(self, transformer)
        return Point(obj['coordinates'])


class LineString(geojson.LineString):
    """Wrap geojson LineString class"""

    def __init__(self, *args, **kwargs):
        super(LineString, self).__init__(*args, **kwargs)

    def plot(self, *args, **kwargs):
        """Plot LineString using Matplotlib."""
        x = [c[0] for c in self['coordinates']]
        y = [c[1] for c in self['coordinates']]
        plt.plot(x, y, *args, **kwargs)

    def coord_transform(self, transformer:Transformer):
        """Transform coordinates of LineString using transformer."""
        obj = coord_transform(self, transformer)
        return LineString(obj['coordinates'])


class Polygon(geojson.Polygon):
    """Wrap geojson Polygon class"""

    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def plot(self, *args, **kwargs):
        """Plot Polygon using Matplotlib."""
        patch = PolygonPatch(self, **kwargs)
        ax = plt.gca()
        ax.add_patch(patch)

    def coord_transform(self, transformer:Transformer):
        """Transform coordinates of Polygon using transformer."""
        obj = coord_transform(self, transformer)
        return Polygon(obj['coordinates'])


class Feature(geojson.Feature):
    """Wrap geojson Feature class."""
    __type_map = {'Point': Point, 'LineString': LineString, 'Polygon': Polygon}

    def __init__(self, *args, **kwargs):
        super(Feature, self).__init__(*args, **kwargs)
        # Ensure the underlying geometry is in our new types as well.
        geom_type = self['geometry']['type']
        if geom_type == 'Point':
            self['geometry'] = Point(self['geometry']['coordinates'])
        elif geom_type == 'LineString':
            self['geometry'] = LineString(self['geometry']['coordinates'])
        elif geom_type == 'Polygon':
            self['geometry'] = Polygon(self['geometry']['coordinates'])

    def plot(self, *args, **kwargs):
        """Flexibly plot features based on underlying geometry type."""
        geom_type = self['geometry']['type']

        cls = self.__type_map[geom_type]
        cls(self['geometry']).plot(*args, **kwargs)

    def coord_transform(self, transformer:Transformer):
        """Transform coordinates of feature using transformer."""
        geom = coord_transform(self['geometry'], transformer)
        return Feature(geometry=geom)
