"""Helpers for error handling."""

__author__ = 'Peter May-Ostendorp'

from geojson import GeoJSON


def err_on_type(obj, cls, ignore=()):
    """Throw error on incorrect type."""
    if not isinstance(obj, cls):
        if ignore and not isinstance(obj, ignore):
            raise TypeError(f'Expected type(s) {cls} but got {type(obj)}.')

        raise TypeError(f'Expected type(s) {cls} but got {type(obj)}.')


def err_on_tb_properties(geojson:GeoJSON, type=None):
    """Throw error on missing Terabase properties in GeoJSON object. Optionally check
    for right type type."""
    if 'properties' not in geojson:
        raise ValueError('properties field missing from geojson.')

    if 'terabase' not in geojson['properties']:
        raise ValueError('terabase field missing from geojson["properties"].')

    if type:
        if 'type' not in geojson['properties']['terabase']:
            raise ValueError('type field missing from geojson["properties"]["terabase"].')
        if geojson['properties']['terabase']['type'] != type:
            raise ValueError(f'Expected {type} in geojson["properties"]["terabase"]["type"] field, but got {geojson["properties"]["terabase"]["type"]}.')


class PlaceholderException(Exception):
    """Exception to tell us if a negative test has failed."""
    def __init__(self):
        super(PlaceholderException, self).__init__("You shouldn't see this.")
