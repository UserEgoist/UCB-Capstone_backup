#!/usr/bin/python3
# #!/usr/bin/env python

from __future__ import print_function

from numpy.core.numeric import NaN

import rospy
import numpy as np
import pandas as pd
from std_msgs.msg import String
from rover_msgs.srv import WayPoints_srv_Tao, WayPoints_srv_TaoResponse
import networkx as nx
import osmnx as ox
from scipy.interpolate import CubicSpline, splprep, splev, splrep

#-------------------------------------------------------------------------
#Adjustable parameter
#origPoint = [42.3828246, -121.0180924] # the coordinates of start point in [latitude, longitude]
#destPoint  = [42.3796160, -121.0231100] # the coordinates of goal point in [latitude, longitude]
#destPoint  = [42.3823027, -121.0179955] # test short route
filter = ['service']
ox.settings.useful_tags_node = ['direction']
#-------------------------------------------------------------------------

def handle_routePlanner(req):
    print("Points input to server: \n", req)

    # north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421 # import map rather than search (or param)
    # MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = True)
    # ox.plot_graph(MDGraph)
    # ox.osm_xml.save_graph_xml(MDGraph, filepath='./OSM and GeoJSON/Bly_withSimplify_Tao.osm')
    # MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = False)
    # ox.osm_xml.save_graph_xml(MDGraph, filepath='./OSM and GeoJSON/Bly_Tao.osm')
    # ox.plot_graph(MDGraph)
    
    
    MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/test_maps/up.osm', simplify=False)
    
    # get the nearest network nodes to two lat/lng points with the distance module  
    #todo take care the X, Y order below!!!! change it?
    orig = ox.distance.nearest_nodes(MDGraph, X = req.Start[1], Y = req.Start[0])#X=origPoint[1],  Y=origPoint[0])
    dest = ox.distance.nearest_nodes(MDGraph, X = req.Target[1], Y = req.Target[0] )#X=destPoint[1],  Y=destPoint[0])
    
    if (MDGraph.nodes[dest]["direction"] == 'down'):  # else: remain using up (node info only necessary in up map)
        
        MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/test_maps/down.osm', simplify=False)
        orig = ox.distance.nearest_nodes(MDGraph, X = req.Start[1], Y = req.Start[0]) # redundant if the up and down map structure are the same
        dest = ox.distance.nearest_nodes(MDGraph, X = req.Target[1], Y = req.Target[0])

    MDGraph_proj = ox.projection.project_graph(MDGraph)
    #ox.plot_graph(MDGraph)

    re = []
    for u,v,k in MDGraph.edges:
        if ( 'highway' not in MDGraph.edges[u,v,k]):
            re.append((u,v,k))
        elif (MDGraph.edges[u,v,k]['highway'] not in filter):
            re.append((u,v,k))
    
    MDGraph.remove_edges_from(re)
    G = ox.utils_graph.remove_isolated_nodes(MDGraph)

    # find the shortest path between nodes, minimizing travel time, then plot it
    route = ox.distance.shortest_path(G, orig, dest, weight="length") #todo travel_time
    fig, ax = ox.plot_graph_route(G, route, node_size=5) # check the route in graph

    #gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph)
    gdf_nodes_proj, gdf_edges_proj = ox.utils_graph.graph_to_gdfs(MDGraph_proj)
    Route_x = []
    Route_y = []
    Width = [] 

    Route_NodeList = route
    print(route)
    count = np.size(Route_NodeList)
    for i in range(count):
        Route_x.append(gdf_nodes_proj.loc[Route_NodeList[i]].x)
        Route_y.append(gdf_nodes_proj.loc[Route_NodeList[i]].y)
        edge = ox.distance.nearest_edges(MDGraph_proj, gdf_nodes_proj.loc[Route_NodeList[i]].x, gdf_nodes_proj.loc[Route_NodeList[i]].y)   # todo (u, v, key)
        Width.append(float(gdf_edges_proj.loc[edge].width))
    
    return WayPoints_srv_TaoResponse(Route_x, Route_y, Width)

def routePlanner_server():
    rospy.init_node('routePlanner_server')
    s = rospy.Service('routePlanner', WayPoints_srv_Tao, handle_routePlanner)
    print("Ready to calculate global route.")
    rospy.spin()

if __name__ == "__main__":
    routePlanner_server()
