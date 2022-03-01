#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Stamp: 11:32PM, 10/02/2021 
Description: todo

'''

import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt


#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/Bly_pre_Tao.osm')
ox.plot_graph(MDGraph)

MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/Bly_Tao.osm')
ox.plot_graph(MDGraph)

MDGraph_proj = ox.projection.project_graph(MDGraph)
highway_gdf = ox.geometries.geometries_from_xml('./OSM and GeoJSON/bly_01.osm', tags={'highway':True})

ox.plot_graph(MDGraph_proj)
print(np.shape(highway_gdf))
print(highway_gdf.head())
print(type(highway_gdf))
#ox.utils_graph.graph_from_gdfs(highway_gdf)

highway_gdf.plot(cmap = 'Blues')
plt.show()

#ox.plot_footprints(piers)


