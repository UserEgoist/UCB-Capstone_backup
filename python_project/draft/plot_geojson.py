#!/usr/bin/python3
from bokeh.plotting import curdoc, figure
from bokeh.models import GeoJSONDataSource
 
# read .geojson data and parse to GeoJSONDataSource
with open("./OSM and GeoJSON/bly_piers.geojson", encoding="utf8") as f:
  geo_source = GeoJSONDataSource(geojson=f.read())
# plot
p = figure(width=500, height=500)
# using patches and geo_source to plot the map
p.patches(xs='xs', ys='ys', source=geo_source)
 
curdoc().add_root(p)

#bokeh serve --show plot_geojson.py