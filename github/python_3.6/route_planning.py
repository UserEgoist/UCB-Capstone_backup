#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Reference: todo
Stamp: 12:00PM, 11/03/2021 
Description: generate the basic route according to the OSM map given
'''

import networkx as nx
import osmnx as ox

#-------------------------------------------------------------------------
#Adjustable parameter
origPoint = [42.3828246, -121.0180924] # the coordinates of start point in [latitude, longitude]
destPoint  = [42.3796160, -121.0231100] # the coordinates of goal point in [latitude, longitude]
#destPoint  = [42.3823027, -121.0179955] # test short route
degreeInterpolate = 15 # 
smoothingCondition = 25 # the s parameter in scipy.interpolate.splprep
sampleNumber = 10000 # only for plot 
#-------------------------------------------------------------------------

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421 #Tao fix 
G = ox.graph_from_bbox(north, south, east, west)
#G = ox.graph_from_bbox(north, south, east, west, network_type = 'all') #todo: assign network_type
#ox.save_graph_geopackage(G, filepath="./data/rover.gpkg")
#ox.save_graphml(G, filepath="./data/rover.graphml")

orig = ox.distance.nearest_nodes(G, X=origPoint[1], Y=origPoint[0])
dest = ox.distance.nearest_nodes(G, X=destPoint[1],  Y=destPoint[0])

route = ox.shortest_path(G, orig, dest, weight="length") 
fig, ax = ox.plot_graph_route(G, route, node_size=0)

edge_lengths = ox.utils_graph.get_route_edge_attributes(G, route, "length")
round(sum(edge_lengths))

orig_x = G.nodes[orig]["x"]
orig_y = G.nodes[orig]["y"]
dest_x = G.nodes[dest]["x"]
dest_y = G.nodes[dest]["y"]
round(ox.distance.great_circle_vec(orig_y, orig_x, dest_y, dest_x))