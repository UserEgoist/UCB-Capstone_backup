#!/usr/bin/python3
import networkx as nx
import osmnx as ox

G = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
#fig, ax = ox.plot_graph(G)

#north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
#G = ox.graph_from_bbox(north, south, east, west, network_type = 'all')
#ox.plot_graph(G)


bearing = ox.bearing.calculate_bearing(42.3873318, -121.0101128, 42.370086, -121.0317421)
print(bearing)

Gu = ox.bearing.add_edge_bearings(G)
fig, ax = ox.plot_graph(Gu)
#ValueError: graph must be undirected and unprojected to analyze edge bearings
#fig, ax = ox.bearing.plot_orientation(Gu)

