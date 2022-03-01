#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Reference: todo
Stamp: 11:32PM, 10/02/2021 
Description: todo

'''

import osmnx as ox

# MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
# MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/map_testTao.osm')
# MDGraph_proj = ox.projection.project_graph(MDGraph)

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
#MDGraph = ox.graph_from_bbox(north, south, east, west)
MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = False)
MDGraph_proj = ox.projection.project_graph(MDGraph)
#ox.osm_xml.save_graph_xml(G, filepath='./OSM and GeoJSON/Tao.osm')
print("Is the graph projected? ---- ", ox.projection.is_projected('crs'))
#ox.plot_graph(MDGraph)

ox.plot_graph(MDGraph_proj)
