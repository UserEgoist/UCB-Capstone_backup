#!/usr/bin/python3
import networkx as nx
import osmnx as ox

# download/model a street network for some city then visualize it
#G = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
#fig, ax = ox.plot_graph(G)

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
G = ox.graph_from_bbox(north, south, east, west, network_type = 'all')
#ox.plot_graph(G)

# save graph to disk as geopackage (for GIS) or graphml file (for gephi etc)
ox.save_graph_geopackage(G, filepath="./data/rover.gpkg")
ox.save_graphml(G, filepath="./data/rover.graphml")

# get the nearest network nodes to two lat/lng points with the distance module
orig = ox.distance.nearest_nodes(G, X=-121.018095, Y=42.382823)
dest = ox.distance.nearest_nodes(G, X=-121.023000, Y=42.379183) #todo: I set it in the middle but why only return to that node? (maybe only two node in that road)

print(orig, dest)
# find the shortest path between nodes, minimizing travel time, then plot it
route = ox.distance.shortest_path(G, orig, dest, weight="length") #todo travel_time
#fig, ax = ox.plot_graph_route(G, route, node_size=0)

# how long is our route in meters?
edge_lengths = ox.utils_graph.get_route_edge_attributes(G, route, "length")
round(sum(edge_lengths))

# how far is it between these two nodes as the crow flies?
# use OSMnx's vectorized great-circle distance (haversine) function
orig_x = G.nodes[orig]["x"]
orig_y = G.nodes[orig]["y"]
dest_x = G.nodes[dest]["x"]
dest_y = G.nodes[dest]["y"]
round(ox.distance.great_circle_vec(orig_y, orig_x, dest_y, dest_x))