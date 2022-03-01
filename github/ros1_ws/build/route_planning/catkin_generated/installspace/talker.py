#!/usr/bin/python3
# #!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from rover_msgs.msg import WayPoints_msg_Tao
import networkx as nx
import osmnx as ox
from scipy.interpolate import CubicSpline, splprep, splev, splrep

#-------------------------------------------------------------------------
#Adjustable parameter
origPoint = [42.3828246, -121.0180924] # the coordinates of start point in [latitude, longitude]
destPoint  = [42.3796160, -121.0231100] # the coordinates of goal point in [latitude, longitude]
#destPoint  = [42.3823027, -121.0179955] # test short route
#-------------------------------------------------------------------------

def routePlanner():
    north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421

    MDGraph_pre = ox.graph_from_bbox(north, south, east, west, simplify = True)
    #ox.plot_graph(MDGraph_pre)
    #ox.osm_xml.save_graph_xml(MDGraph_pre, filepath='./OSM and GeoJSON/Bly_pre_Tao.osm')

    MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = False)
    MDGraph_proj = ox.projection.project_graph(MDGraph)
    #ox.plot_graph(MDGraph)

    # get the nearest network nodes to two lat/lng points with the distance module
    orig = ox.distance.nearest_nodes(MDGraph, X=origPoint[1],  Y=origPoint[0])
    dest = ox.distance.nearest_nodes(MDGraph, X=destPoint[1],  Y=destPoint[0])

    # find the shortest path between nodes, minimizing travel time, then plot it
    route = ox.distance.shortest_path(MDGraph, orig, dest, weight="length") #todo travel_time
    #fig, ax = ox.plot_graph_route(MDGraph, route, node_size=5)

    #Linear interpolation according to angle degree
    gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph_proj)
    Route_x = []
    Route_y = []

    Route_NodeList = route
    count = np.size(Route_NodeList)
    for i in range(count):
        Route_x.append(gdf_nodes.loc[Route_NodeList[i]].x)
        Route_y.append(gdf_nodes.loc[Route_NodeList[i]].y)
    
    return Route_x, Route_y


def talker():
    pub = rospy.Publisher('route_output', WayPoints_msg_Tao, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data_temp = WayPoints_msg_Tao()
        data_temp.X, data_temp.Y= routePlanner()
        data_temp.Width = []
        #hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(data_temp)
        pub.publish(data_temp)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
