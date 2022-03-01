#!/usr/bin/python3
import networkx as nx
import osmnx as ox

# download/model a street network for some city then visualize it
#G = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
#fig, ax = ox.plot_graph(G)

G = ox.graph_from_xml(filepath='./OSM and GeoJSON/UndirectedMap_orientation_test.osm', simplify=False)
#G = ox.graph_from_xml(filepath='./OSM and GeoJSON/DirectedMap_down.osm')

#north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
#G = ox.graph_from_bbox(north, south, east, west, network_type = 'all')
#ox.plot_graph(G)

# save graph to disk as geopackage (for GIS) or graphml file (for gephi etc)
#ox.save_graph_geopackage(G, filepath="./data/rover.gpkg")
#ox.save_graphml(G, filepath="./data/rover.graphml")

# get the nearest network nodes to two lat/lng points with the distance module
orig = ox.distance.nearest_nodes(G, X=-121.018095, Y=42.382823)
#dest = ox.distance.nearest_nodes(G, X=-121.019849, Y=42.382896)
dest = ox.distance.nearest_nodes(G, X=-121.0197164, Y=42.3816075) 
#dest = ox.distance.nearest_nodes(G, X=-121.019877, Y=42.381586) 

print(orig, dest)
# find the shortest path between nodes, minimizing travel time, then plot it
route = ox.distance.shortest_path(G, orig, dest, weight="length") #todo travel_time
#fig, ax = ox.plot_graph_route(G, route, node_size=0)

# how long is our route in meters?
edge_lengths = ox.utils_graph.get_route_edge_attributes(G, route, "length")
sumRoute = round(sum(edge_lengths))
print(route)
print(sumRoute)
fig, ax = ox.plot_graph_route(G, route, node_size=0)
