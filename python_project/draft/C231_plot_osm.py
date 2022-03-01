#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Stamp: 11:32PM, 10/02/2021 
Description: todo

'''

import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt

#BerkeleyWay2017
MDGraph = ox.graph_from_point((37.87327, -122.26982), dist = 170, dist_type='bbox', network_type='drive')
#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/BerkeleyWay_1.osm')
MDGraph_proj = ox.projection.project_graph(MDGraph)
#highway_gdf = ox.geometries.geometries_from_xml('./OSM and GeoJSON/BerkeleyWay_1.osm', tags={'highway':True})

ox.plot_graph(MDGraph_proj)
# print(np.shape(highway_gdf))
# print(highway_gdf.head())
# print(type(highway_gdf))
#ox.utils_graph.graph_from_gdfs(highway_gdf)

# highway_gdf.plot(cmap = 'Blues')
# plt.show()

#ox.plot_footprints(piers)


