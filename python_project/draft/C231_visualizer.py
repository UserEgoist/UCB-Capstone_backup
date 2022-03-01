#!/usr/bin/python3
import sys
import networkx as nx
import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
pd.set_option('display.max_columns', 1000)

#MDGraph = ox.graph_from_point((37.87327, -122.26982), dist = 170, dist_type='bbox', network_type='drive', simplify=True)
MDGraph = ox.graph_from_point((37.87327, -122.26982), dist = 170, dist_type='bbox', network_type='drive', simplify=False)
MDGraph = ox.utils_graph.remove_isolated_nodes(MDGraph)
gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph)
#ox.osm_xml.save_graph_xml(MDGraph, filepath='./OSM and GeoJSON/BerkeleyWay2017_visualizer.osm')
#MDGraph = ox.graph_from_point((37.87327, -122.26982), dist = 170, dist_type='bbox')
#MDGraph = ox.graph_from_xml(filepath='./OSM and GeoJSON/BerkeleyWay2017_Online.osm')
#MDGraph = ox.projection.project_graph(MDGraph)
# MDGraph_proj = ox.projection.project_graph(MDGraph)
#buildings = ox.geometries.geometries_from_point((37.87327, -122.26982), tags = {'building':True, 'highway':['residential', 'secondary']}, dist = 170)
buildings = ox.geometries.geometries_from_point((37.87327, -122.26982), tags = {'building':True}, dist = 170)

#---------------------------------------------------------------------
#truncate graph

for i in range(3):
    gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph)

    Node_list = []
    edge_list = []
    x_list = []
    y_list = []
    re = []

    for node_temp in MDGraph.nodes:  #todo fail in MDGraph.nodes[0] ?
        Node_list.append(node_temp)
        x_list.append(gdf_nodes.loc[node_temp].x)
        y_list.append(gdf_nodes.loc[node_temp].y)

    for edge_temp in MDGraph.edges:
        edge_list.append(edge_temp)

    for node_temp in Node_list:
        flag = 0
        temp_list = []
        for edge_temp in edge_list:
            if (node_temp == edge_temp[0] or node_temp == edge_temp[1]):
                flag = flag + 1
                temp_list.append(edge_temp)
        if (flag < 2):
            re.append(temp_list)

    for edge_temp in re:
        MDGraph.remove_edges_from(edge_temp)
    MDGraph = ox.utils_graph.remove_isolated_nodes(MDGraph)

for i in range(5):
    gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph)

    Node_list = []
    edge_list = []
    x_list = []
    y_list = []
    re = []

    for node_temp in MDGraph.nodes:  #todo fail in MDGraph.nodes[0] ?
        Node_list.append(node_temp)
        x_list.append(gdf_nodes.loc[node_temp].x)
        y_list.append(gdf_nodes.loc[node_temp].y)

    for edge_temp in MDGraph.edges:
        edge_list.append(edge_temp)

    for node_temp in Node_list:
        flag = 0
        temp_list = []
        for edge_temp in edge_list:
            if (node_temp == edge_temp[0] or node_temp == edge_temp[1]):
                if(MDGraph.edges[edge_temp[0], edge_temp[1], 0]['oneway'] == True): #... its not 'yes', but True
                    flag = flag + 2
                else:
                    flag = flag + 1
                temp_list.append(edge_temp)
        if (flag < 3):
            re.append(temp_list)

    for edge_temp in re:
        MDGraph.remove_edges_from(edge_temp)
    MDGraph = ox.utils_graph.remove_isolated_nodes(MDGraph)

#-----------
#fig, ax0 = plt.subplots(1)
# plt.plot(-122.27014, 37.873236, 'bo', markersize = 7) # the order matters

fig, ax0 = ox.plot_graph(MDGraph, bgcolor = '#fafafa', node_color='r', node_size=25, edge_color='#000000', edge_linewidth=2, show = False)
fig, ax1 = ox.plot_footprints(buildings, ax = ax0, show = False)


Node_list = []
edge_list = []
x_list = []
y_list = []
#print(Info_matrix)

for node_temp in MDGraph.nodes:  #todo fail in MDGraph.nodes[0] ?
    Node_list.append(node_temp)
    x_list.append(gdf_nodes.loc[node_temp].x)
    y_list.append(gdf_nodes.loc[node_temp].y)

for edge_temp in MDGraph.edges:
    edge_list.append(edge_temp)

print(Node_list)

# ax1.plot(gdf_nodes.loc[Node_list[0]].x, gdf_nodes.loc[Node_list[0]].y, 'bo', markersize = 16) # the order matters
# ax1.plot( (gdf_nodes.loc[Node_list[0]].x + gdf_nodes.loc[Node_list[1]].x)/2, (gdf_nodes.loc[Node_list[0]].y + gdf_nodes.loc[Node_list[1]].y)/2, 'go', markersize = 16) # the order matters


#ax1.plot(-122.268972, 37.872911, 'bo', markersize = 7) # the order matters

#ox.plot_footprints(buildings)

# ox.plot_footprints(buildings, ax = ax1)
# ox.plot_graph(MDGraph_proj, ax = ax1)

#plot.plot_figure_ground(point = (37.87327, -122.26982), dist = 175, network_type='drive')


# point_ani, = plt.plot(x_list[0], y_list[0], "r-", linewidth = 5)

# text_pt = plt.text(-122.268972, 37.872911, '', fontsize = 10)

# def update_rule(num):
#     xx = x_list[0:num]
#     yy = y_list[0:num]
#     point_ani.set_data(xx, yy)
#     text_pt.set_text("x=%.5f \ny =%.5f"%(x_list[num], x_list[num]))
#     return point_ani, text_pt,

# ani = animation.FuncAnimation(fig = fig, func = update_rule, frames = np.arange(np.size(Node_list)), interval = 800, blit = True)

# plt.show()




#--------------------------------
#1. find nearst node



#todo need to project first
#MDGraph = ox.distance.add_edge_lengths(MDGraph, precision=3)
re = ox.distance.nearest_edges(MDGraph, (gdf_nodes.loc[Node_list[0]].x + gdf_nodes.loc[Node_list[1]].x)/2, (gdf_nodes.loc[Node_list[0]].y + gdf_nodes.loc[Node_list[1]].y)/2, interpolate=None, return_dist=False)
print('re',re)

#MDGraph.remove_edges_from([re]) #? why I cannot delete
#route = ox.distance.shortest_path(MDGraph, re[0][0], re[0][1], weight="length")
route = ox.distance.shortest_path(MDGraph, re[0], re[1], weight="length")

print('short', MDGraph[re[0]][re[1]][0]['length'])

orig = ox.distance.nearest_nodes(MDGraph, X=-122.270734, Y=37.872681)



route = ox.distance.shortest_path(MDGraph, orig, re[1], weight="length")
edge_lengths = ox.utils_graph.get_route_edge_attributes(MDGraph, route, "length")
sumRoute = round(sum(edge_lengths))

print('long', sumRoute)

print("route", route)
#route = ox.distance.shortest_path(MDGraph, 53042661, 53042663, weight="length")


#print(MDGraph[53042661][53042663][0]['length']) # todo error (simplify=True)

fig, ax = ox.plot_graph_route(MDGraph, route, node_size=2)

ox.plot_graph(MDGraph)