"""Tools for working with GeoJSON."""

__author__ = 'Peter May-Ostendorp'

from typing import Union
import geojson
from geojson import GeoJSON
from pyproj import CRS, Transformer
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info
import numpy as np

from hardhat.util.exceptions import err_on_type
from hardhat.gis.geometry import Feature, Polygon, LineString, Point


WGS84_CRS = CRS.from_proj4('+proj=latlon')
MAPPED_GEO_CLASSES = (
    geojson.LineString,
    geojson.Point,
    geojson.Polygon,
    geojson.Feature
)


def convert_geojson_types(obj:GeoJSON) -> GeoJSON:
    """Convert any geojson.geometry to in-house types."""
    if 'type' not in obj:
        raise TypeError("obj missing type field. Are you sure it's geoJSON?")

    if obj['type'] == 'Feature':
        kwargs = {}
        if 'properties' in obj:
            kwargs['properties'] = obj['properties']

        if 'id' in obj:
            kwargs['id'] = obj['id']
        return Feature(geometry=obj['geometry'], **kwargs)

    if obj['type'] == 'Point':
        return Point(obj['coordinates'])

    if obj['type'] == 'LineString':
        return LineString(obj['coordinates'])

    if obj['type'] == 'Polygon':
        return Polygon(obj['coordinates'])

    raise TypeError(f'obj is not one of {MAPPED_GEO_CLASSES}.')


def process_geojson(input:Union[str, dict, Polygon, LineString, Point]) -> GeoJSON:
    """Accepts GeoJSON from stream, dict and ensures its in our geoJSON classes.

    This will also check for valid geoJSON and report any errors. Everything is
    converted to existing hardhat wrapper classes here!
    """
    if isinstance(input, dict):
        geom = convert_geojson_types(geojson.geometry.GeoJSON.to_instance(input))
    elif isinstance(input, MAPPED_GEO_CLASSES):
        geom = convert_geojson_types(input)
    elif isinstance(input, (Polygon, LineString, Point, Feature)):
        geom = input # if already one of our supported geometry types
    else: # assume string as a last resort
        geom = convert_geojson_types(geojson.loads(input))

    if 'geometry' not in str(type(geom)):
        raise ValueError(f'Invalid GeoJSON in:\n{type(geom)}\n{geom}.')
    elif not geom.is_valid:
        raise ValueError(f'Invalid GeoJSON in:\n{type(geom)}\n{geom}.\n{geom.errors()}')

    return geom


def filter_features(features:list([Feature]), **kwargs) -> list([Feature]): #Tao: change list to list()
    """Filters list of geoJSON features with Terabase properties. Filters are
    evaluated in combination so all filters must evaluate to true."""
    out_features = []
    for f in features:
        tb_props = f['properties']['terabase']
        if all(item in tb_props.items() for item in kwargs.items()):
            out_features.append(f)

    return out_features


def transform_coords(t:Transformer, coords:list) -> list:
    """Return list of transformed coordinate pairs."""
    return [t.transform(c[0], c[1]) for c in coords]


def coord_array(geom:GeoJSON) -> np.ndarray:
    """Generates a numpy array from object coordinates."""
    return np.array(list(geojson.utils.coords(geom)))


def utm_zone_from_lon(lon:float) -> int:
    """Detects a location's UTM zone from longitude."""
    return int(np.ceil((lon + 180) / 6))


def avg_lon_from_coordinates(geom:GeoJSON) -> float:
    """Provides average longitude from GeoJSON object coordinates."""
    return coord_array(geom)[:,0].mean()


def utm_crs_from_geom(geom:GeoJSON) -> CRS:
    """Generates coordinate reference system for use by PyProj based on GeoJSON
    coordinates."""
    coords = coord_array(geom)
    north = coords[:,1].max()
    east = coords[:,0].max()
    south = coords[:,1].min()
    west = coords[:,0].max()

    utm_crs_list = query_utm_crs_info(
        datum_name="WGS 84",
        area_of_interest=AreaOfInterest(
            west_lon_degree=west,
            south_lat_degree=south,
            east_lon_degree=east,
            north_lat_degree=north,
        )
    )
    return CRS.from_epsg(utm_crs_list[0].code)


def transformer_from_geom(geom:GeoJSON, **kwargs) -> (Transformer, Transformer):
    """Generates a Transformer instance from WGS84 coordinates
    to UTM and its inverse transformer back to WGS84.

    Checks for presence of existing transformers in kwargs and will bypass and
    return those if not present. The naming convention for each is to_utm and
    to_wgs.
    """
    if 'to_utm' not in kwargs or 'to_wgs' not in kwargs:
        utm_crs = utm_crs_from_geom(geom)
        return Transformer.from_crs(WGS84_CRS, utm_crs), Transformer.from_crs(utm_crs, WGS84_CRS)

    err_on_type(kwargs['to_utm'], Transformer)
    err_on_type(kwargs['to_wgs'], Transformer)
    return kwargs['to_utm'], kwargs['to_wgs']
