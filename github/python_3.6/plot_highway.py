#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Reference: todo
Stamp: 11:32PM, 10/02/2021 
Description: todo

todo: 
path planning using GeoDataFrame?
fron GDF to Graph?
'''

import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt

MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
MDGraph_proj = ox.projection.project_graph(MDGraph)
highway_gdf = ox.geometries.geometries_from_xml('./OSM and GeoJSON/bly_01.osm', tags={'highway':True})

print(np.shape(highway_gdf))
print(highway_gdf.head())
print(type(highway_gdf))

highway_gdf.plot(cmap = 'Blues')
plt.show()