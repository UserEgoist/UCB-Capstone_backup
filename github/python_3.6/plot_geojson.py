#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Reference: todo
Stamp: 11:32PM, 10/02/2021 
Description: todo
'''

from bokeh.plotting import curdoc, figure
from bokeh.models import GeoJSONDataSource
 
with open("./OSM and GeoJSON/bly_piers.geojson", encoding="utf8") as f:
  geo_source = GeoJSONDataSource(geojson=f.read())

p = figure(width=500, height=500)
p.patches(xs='xs', ys='ys', source=geo_source)
 
curdoc().add_root(p)