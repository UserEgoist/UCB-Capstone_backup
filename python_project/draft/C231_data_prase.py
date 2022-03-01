#!/usr/bin/python3
import sys
import networkx as nx
import osmnx as ox
import numpy as np

data = np.load("route_data.npy", allow_pickle=True)
print(data)