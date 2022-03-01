#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Stamp: 11:32PM, 10/02/2021 
Description: todo

'''
import momepy
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', 1000)
ox.config(use_cache=True, log_console=True)

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
buildings = ox.geometries.geometries_from_bbox(north, south, east, west, tags = {'generator:source': 'solar', 'power': 'line'})

MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/DirectedMap_up.osm', simplify=False)
#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/DirectedMap_down_withRoadInfo.osm', simplify=False)

MDGraph_proj = ox.projection.project_graph(MDGraph)
filter = ['service']

# re = []
# for u,v,k in MDGraph_proj.edges:
#     if ( 'highway' not in MDGraph_proj.edges[u,v,k]):
#         #print('do_1')
#         re.append((u,v,k))
#     elif (MDGraph_proj.edges[u,v,k]['highway'] not in filter):
#         #print('do_2')
#         re.append((u,v,k))
# print(re)
# MDGraph_proj.remove_edges_from(re)
# #G = ox.utils_graph.remove_isolated_nodes(MDGraph_proj)
re = []
for u,v,k in MDGraph.edges:
    if ( 'highway' not in MDGraph.edges[u,v,k]):
        #print('do_1')
        re.append((u,v,k))
    elif (MDGraph.edges[u,v,k]['highway'] not in filter):
        #print('do_2')
        re.append((u,v,k))
print(re)
MDGraph.remove_edges_from(re)
#G = ox.utils_graph.remove_isolated_nodes(MDGraph_proj)
G = ox.utils_graph.remove_isolated_nodes(MDGraph)

#ox.plot_graph(MDGraph)
#ox.plot_graph(MDGraph_proj)

fig, ax0 = ox.plot_footprints(buildings, show = False, bbox = (north, south, east, west))
fig, ax1 = ox.plot_graph(G, ax = ax0, show = False, node_size=1)
#fig, ax0 = ox.plot_graph(G, figsize=(8,8), bgcolor = '#fafafa', node_color='r', node_size=25, edge_color='#000000', edge_linewidth=2, show = False, bbox = (north, south, east, west))


orig = ox.distance.nearest_nodes(MDGraph, X=-121.01810, Y=42.38279)
dest = ox.distance.nearest_nodes(MDGraph, X=-121.0194566, Y=42.3822661) # down 
#dest = ox.distance.nearest_nodes(MDGraph, X=-121.0194802, Y=42.3825222) # up

route = ox.distance.shortest_path(G, orig, dest, weight="length") #G is projected, but can still use node from unporjected!!(not coordinates)

fig, ax2 = ox.plot_graph_route(G, route, node_size=10, ax = ax1)

plt.show()
#origin = [662583, 4693164]