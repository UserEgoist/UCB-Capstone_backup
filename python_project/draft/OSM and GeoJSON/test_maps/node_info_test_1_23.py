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
import os

pd.set_option('display.max_columns', 1000)
ox.config(use_cache=True, log_console=True)
print(os.getcwd())

ox.settings.useful_tags_node = ['direction']

#north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
#buildings = ox.geometries.geometries_from_bbox(north, south, east, west, tags = {'generator:source': 'solar', 'power': 'line'})

#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/DirectedMap_up.osm', simplify=False)
MDGraph = ox.graph_from_xml(filepath='/home/tao/python_project/draft/OSM and GeoJSON/test_maps/DirectedMap_down_withNodeInfo.osm', simplify=False)

orig = ox.distance.nearest_nodes(MDGraph, X=-121.01810, Y=42.38279)
dest = ox.distance.nearest_nodes(MDGraph, X=-121.0194566, Y=42.3822661) # down 

#print("11111111111111", dest)
#print(MDGraph.nodes[dest])
print(MDGraph.nodes[dest]["direction"])

