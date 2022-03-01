#!/usr/bin/python3

import networkx as nx
import osmnx as ox
from IPython.display import IFrame


# download the street network for Berkeley, CA
G = ox.graph_from_place("Berkeley, California, USA", network_type="drive")


# plot the street network with folium
m1 = ox.plot_graph_folium(G, popup_attribute="name", weight=2, color="#8b0000")

filepath = "data/graph.html"
m1.save(filepath)
IFrame(filepath, width=600, height=500)
