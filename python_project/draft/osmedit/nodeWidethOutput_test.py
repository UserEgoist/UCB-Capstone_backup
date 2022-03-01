#!/usr/bin/python3
import networkx as nx
import osmnx as ox




#todo

# download/model a street network for some city then visualize it
#G = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
#fig, ax = ox.plot_graph(G)

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = False)
MDGraph_proj = ox.projection.project_graph(MDGraph)
#ox.osm_xml.save_graph_xml(G, filepath='./OSM and GeoJSON/Tao.osm')
print("Is the graph projected? ---- ", ox.projection.is_projected('crs'))
#ox.plot_graph(MDGraph)

# get the nearest network nodes to two lat/lng points with the distance module
orig = ox.distance.nearest_nodes(MDGraph, X=-121.0180924, Y=42.3828246)
#dest = ox.distance.nearest_nodes(MDGraph, X=-121.023110,  Y=42.379616)
dest = ox.distance.nearest_nodes(MDGraph, X=-121.0179955, Y=42.3823027)

print(orig, dest)
# find the shortest path between nodes, minimizing travel time, then plot it
route = ox.distance.shortest_path(MDGraph, orig, dest, weight="length") #todo travel_time
#fig, ax = ox.plot_graph_route(MDGraph, route, node_size=0)

gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph)
print("1Str------------------------------")
print(gdf_nodes.loc[route])
print("1End------------------------------")

gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph_proj)
print("2Str------------------------------")
print(gdf_nodes.loc[route])
print("2End------------------------------")

print(gdf_nodes.loc[route[0]].y)
print(gdf_nodes.loc[route[1]].y)
ox.plot_graph(MDGraph_proj)
fig, ax = ox.plot_graph_route(MDGraph, route, node_size=0)
# how long is our route in meters?
edge_lengths = ox.utils_graph.get_route_edge_attributes(MDGraph, route, "length")
sumRoute = round(sum(edge_lengths))
print("size of route", len(route))
print(route)
print("sumRoute = ", sumRoute)
#fig, ax = ox.plot_graph_route(MDGraph, route, node_size=0)

# how far is it between these two nodes as the crow flies?
# use OSMnx's vectorized great-circle distance (haversine) function
orig_x = MDGraph.nodes[orig]["x"]
orig_y = MDGraph.nodes[orig]["y"]
dest_x = MDGraph.nodes[dest]["x"]
dest_y = MDGraph.nodes[dest]["y"]
sumCircle = round(ox.distance.great_circle_vec(orig_y, orig_x, dest_y, dest_x))
print("sumCircle = ", sumCircle)