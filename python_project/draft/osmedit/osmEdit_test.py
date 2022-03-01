#!/usr/bin/python3

import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', 1000)

#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
G = ox.graph_from_xml(filepath='./OSM and GeoJSON/DirectedMap_down_test.osm')
#ox.plot_graph(G)

#point = [42.382225, -121.0197068] # node added by Tao
point = [42.3828528, -121.0199776] # normal node
node = ox.distance.nearest_nodes(G, X = point[1], Y = point[0]) # X longitude, Y latitude
print(node)

gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(G)

#print(gdf_nodes)
print(np.shape(gdf_nodes))
print("-----------------------------------")
print(gdf_nodes.loc[node])

print(np.shape(gdf_edges))
#print(gdf_edges.head(5))

print("node: ", node)
edge = ox.distance.nearest_edges(G, gdf_nodes.loc[node].x, gdf_nodes.loc[node].y)   # todo (u, v, key)
print("edge:", edge)
print("edge-----------------------------------")
print(gdf_edges.loc[edge])
print("width",gdf_edges.loc[edge].width)
print(gdf_edges.loc[edge].width)

#MDGraph_proj = ox.projection.project_graph(MDGraph)
#highway_gdf = ox.geometries.geometries_from_xml('./OSM and GeoJSON/bly_01.osm', tags={'highway':True})

# ox.plot_graph(MDGraph_proj)
# print(np.shape(highway_gdf))
# print(highway_gdf.head())
# print(type(highway_gdf))
# #ox.utils_graph.graph_from_gdfs(highway_gdf)

# highway_gdf.plot(cmap = 'Blues')
# plt.show()

# #ox.plot_footprints(piers)
