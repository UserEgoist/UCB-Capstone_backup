#!/usr/bin/python3
import sys
import networkx as nx
import osmnx as ox
import numpy as np



north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
G = ox.graph_from_bbox(north, south, east, west)
#G = ox.graph_from_bbox(north, south, east, west, simplify = False)
G_addEdgeLength = ox.distance.add_edge_lengths(G, precision = 3)

#print(type(G.nodes))
Node_list = []
Info_matrix = np.full((np.size(G.nodes), np.size(G.nodes)), float("inf") , dtype = float )

#print(Info_matrix)
print((Info_matrix[0][0]))
for node_temp in G.nodes:
    Node_list.append(node_temp) 

#print(Node_list)

#print(list(G))
#print(G.edges())

for edge_item in G.edges():

    if Info_matrix[Node_list.index(edge_item[0])][Node_list.index(edge_item[1])] > G[edge_item[0]][edge_item[1]][0]['length']:
        Info_matrix[Node_list.index(edge_item[0])][Node_list.index(edge_item[1])] = G[edge_item[0]][edge_item[1]][0]['length']
        Info_matrix[Node_list.index(edge_item[1])][Node_list.index(edge_item[0])] = G[edge_item[0]][edge_item[1]][0]['length']

print(Info_matrix)
#print("G length: ", G[7734934968][7734934993])
#print("G_addEdgeLength length: ", G_addEdgeLength[7734934968][7734934993])
#print("G length: ", G[7734934968][7734934993][0]['length'])

#np.save("Info_matrix.npy", Info_matrix)

ox.plot_graph(G)