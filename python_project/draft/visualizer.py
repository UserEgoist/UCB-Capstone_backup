#!/usr/bin/python3
import sys
import networkx as nx
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt


north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
G = ox.graph_from_bbox(north, south, east, west, network_type = 'drive_service')
#ox.plot_graph(G)

buildings = ox.geometries.geometries_from_bbox(north, south, east, west, tags = {'generator:source': 'solar', 'power': 'line'})


#fig, ax0 = plt.subplots(1)
# plt.plot(-122.27014, 37.873236, 'bo', markersize = 7) # the order matters

fig, ax0 = ox.plot_graph(G, figsize=(8,8), bgcolor = '#fafafa', node_color='r', node_size=25, edge_color='#000000', edge_linewidth=2, show = False, bbox = (north, south, east, west))
fig, ax1 = ox.plot_footprints(buildings, ax = ax0, show = False, bbox = (north, south, east, west))
#ax1.plot(-122.269691, 37.873294, 'bo', markersize = 7) # the order matters
#ax1.plot(-122.268972, 37.872911, 'bo', markersize = 7) # the order matters

plt.show()
#ox.plot_footprints(buildings)

# ox.plot_footprints(buildings, ax = ax1)
# ox.plot_graph(MDGraph_proj, ax = ax1)

#plot.plot_figure_ground(point = (37.87327, -122.26982), dist = 175, network_type='drive')