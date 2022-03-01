#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Stamp: 11:32PM, 11/08/2021 
Description: todo

'''
import sys
import networkx as nx
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt

#BerkeleyWay2017
MDGraph = ox.graph_from_point((37.87327, -122.26982), dist = 170, dist_type='bbox', network_type='drive')
#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/BerkeleyWay_1.osm')
#MDGraph_proj = ox.projection.project_graph(MDGraph)
#highway_gdf = ox.geometries.geometries_from_xml('./OSM and GeoJSON/BerkeleyWay_1.osm', tags={'highway':True})

origPoint = [37.873868, -122.268536] # the coordinates of start point in [latitude, longitude]
#origPoint = [37.873858, -122.268651] 
destPoint = [37.873023, -122.268486] # the coordinates of goal point in [latitude, longitude]

orig = ox.distance.nearest_nodes(MDGraph, X=origPoint[1],  Y=origPoint[0])
dest = ox.distance.nearest_nodes(MDGraph, X=destPoint[1],  Y=destPoint[0])

route = ox.distance.shortest_path(MDGraph, dest, orig, weight="length") #todo travel_time
fig, ax = ox.plot_graph_route(MDGraph, route, node_size=5)

#G = ox.graph_from_bbox(north, south, east, west, simplify = False)
MDGraph_addEdgeLength = ox.distance.add_edge_lengths(MDGraph, precision = 3)

#print(type(G.nodes))
Node_list = []
Info_matrix = np.full((np.size(MDGraph.nodes), np.size(MDGraph.nodes)), float("inf") , dtype = float )

#print(Info_matrix)
print((Info_matrix[0][0]))
for node_temp in MDGraph.nodes:
    Node_list.append(node_temp) 

print(Node_list)

print(list(MDGraph))
print(MDGraph.edges())
print(np.size(MDGraph.edges()))

for edge_item in MDGraph.edges():
    if Info_matrix[Node_list.index(edge_item[0])][Node_list.index(edge_item[1])] > MDGraph[edge_item[0]][edge_item[1]][0]['length']:
        Info_matrix[Node_list.index(edge_item[0])][Node_list.index(edge_item[1])] = MDGraph[edge_item[0]][edge_item[1]][0]['length']
        #Info_matrix[Node_list.index(edge_item[1])][Node_list.index(edge_item[0])] = MDGraph[edge_item[0]][edge_item[1]][0]['length']

print(Info_matrix)

#print("G length: ", G[7734934968][7734934993])
#print("G_addEdgeLength length: ", G_addEdgeLength[7734934968][7734934993])
#print("G length: ", G[7734934968][7734934993][0]['length'])

np.save("Info_matrix_BerkeleyWay2017.npy", Info_matrix)

ox.plot_graph(MDGraph)