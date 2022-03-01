#!/usr/bin/python3
'''
Author: Tao SHU, at Berkeley
Reference: todo
Stamp: 11:24AM, 11/08/2021 
Description: generate route, then interpolate and fitting it
'''
import networkx as nx
import osmnx as ox
import numpy as np
from scipy.interpolate import CubicSpline, splprep, splev, splrep
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------
#Adjustable parameter
origPoint = [42.3828246, -121.0180924] # the coordinates of start point in [latitude, longitude]
destPoint  = [42.3796160, -121.0231100] # the coordinates of goal point in [latitude, longitude]
#destPoint  = [42.3823027, -121.0179955] # test short route
degreeInterpolate = 15*np.pi/180 # 
flag = degreeInterpolate/10
smoothingCondition = 25 # the s parameter in scipy.interpolate.splprep
sampleNumber = 10000 # only for plot 
origin = [662583, 4693164]
np.set_printoptions(threshold=np.inf)
#-------------------------------------------------------------------------


def route_angle(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    dot = x1*x2 + y1*y2
    det = x1*y2 - y1*x2
    theta = np.arctan2(det, dot)
    return theta

print(route_angle([1,0],[0,-1]))

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421

MDGraph_pre = ox.graph_from_bbox(north, south, east, west, simplify = True)
#ox.plot_graph(MDGraph_pre)
#ox.osm_xml.save_graph_xml(MDGraph_pre, filepath='./OSM and GeoJSON/Bly_pre_Tao.osm')

MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = False)
MDGraph_proj = ox.projection.project_graph(MDGraph)
#ox.osm_xml.save_graph_xml(MDGraph, filepath='./OSM and GeoJSON/Bly_Tao.osm')
#ox.osm_xml.save_graph_xml(MDGraph_proj, filepath='./OSM and GeoJSON/Bly_projected_Tao.osm')
#print("Is the graph projected? ---- ", ox.projection.is_projected('crs'))
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
sum_count = 0
for i in range(count):
    Route_x.append(gdf_nodes.loc[Route_NodeList[i]].x)
    Route_y.append(gdf_nodes.loc[Route_NodeList[i]].y)
    if (i != 0 and i != (count - 1)):
        v1 = [gdf_nodes.loc[Route_NodeList[i]].x - gdf_nodes.loc[Route_NodeList[i-1]].x, gdf_nodes.loc[Route_NodeList[i]].y - gdf_nodes.loc[Route_NodeList[i-1]].y]
        v2 = [gdf_nodes.loc[Route_NodeList[i+1]].x - gdf_nodes.loc[Route_NodeList[i]].x, gdf_nodes.loc[Route_NodeList[i+1]].y - gdf_nodes.loc[Route_NodeList[i]].y]
        RouteAngle_temp = route_angle(v1, v2)
        if(np.absolute(RouteAngle_temp) > degreeInterpolate):
            #Linear interpolation
            interpolation_count = int(np.absolute(RouteAngle_temp)/degreeInterpolate) 
            for j in range(interpolation_count):
                if (j == 0):
                    Route_x.insert(i + j + sum_count, (gdf_nodes.loc[Route_NodeList[i - 1]].x + gdf_nodes.loc[Route_NodeList[i]].x)/2)
                    Route_x.insert(i + j + 2 + sum_count, (gdf_nodes.loc[Route_NodeList[i]].x + gdf_nodes.loc[Route_NodeList[i + 1]].x)/2)
                    Route_y.insert(i + j + sum_count, (gdf_nodes.loc[Route_NodeList[i - 1]].y + gdf_nodes.loc[Route_NodeList[i]].y)/2)
                    Route_y.insert(i + j + 2 + sum_count, (gdf_nodes.loc[Route_NodeList[i]].y + gdf_nodes.loc[Route_NodeList[i + 1]].y)/2)
                else:
                    Route_x.insert(i + j + sum_count, (Route_x[i + j - 1 + sum_count] + Route_x[i + j + sum_count])/2)
                    Route_x.insert(i + j + 2 + sum_count, (Route_x[i + j + 1 + sum_count] + Route_x[i + j + 2 + sum_count])/2)
                    Route_y.insert(i + j + sum_count, (Route_y[i + j - 1 + sum_count] + Route_y[i + j + sum_count])/2)
                    Route_y.insert(i + j + 2 + sum_count, (Route_y[i + j + 1 + sum_count] + Route_y[i + j + 2 + sum_count])/2)
            sum_count += 2*interpolation_count

Route_orig_x = []
Route_orig_y = []
count = np.size(route)
for i in range(count):
    Route_orig_x.append(gdf_nodes.loc[Route_NodeList[i]].x)
    Route_orig_y.append(gdf_nodes.loc[Route_NodeList[i]].y)

print("Route_orig_x:", Route_orig_x)
print("Route_orig_y:", Route_orig_y)
print("route_x: ", Route_x)
print("route_y: ", Route_y)

tck0, u0 = splprep([Route_orig_x, Route_orig_y], k = 1, s = 0)
pre_points = splev(np.linspace(0.,1.,sampleNumber), tck0)

tck1, u1 = splprep([Route_orig_x, Route_orig_y], s = smoothingCondition)
new_points1 = splev(np.linspace(0.,1.,sampleNumber), tck1)

X2_unique = []
Y2_unique = []
_, idx = np.unique(Route_x, return_index=True) #todo: Tao
idx_sort = np.sort(idx)
for i in idx_sort:
    X2_unique.append(Route_x[i])
    Y2_unique.append(Route_y[i])

tck2, u2 = splprep([X2_unique, Y2_unique], s = smoothingCondition) # must set s, because exist duplicate x
new_points2 = splev(np.linspace(0.,1.,sampleNumber), tck2)

fig, (ax0, ax1, ax2) = plt.subplots(3)
ax0.plot(Route_orig_x, Route_orig_y, 'ro', pre_points[0], pre_points[1], 'b-')
ax0.set_aspect('equal', adjustable='datalim')
ax1.plot(Route_orig_x, Route_orig_y, 'ro', new_points1[0], new_points1[1], 'b-')
ax1.set_aspect('equal', adjustable='datalim')
ax2.plot(Route_x, Route_y, 'ro', new_points2[0], new_points2[1], 'b-')
ax2.set_aspect('equal', adjustable='datalim')
plt.show()

Turn_flag = np.zeros(sampleNumber)

for i in range(sampleNumber):
    if (i != 0 and i != (sampleNumber - 1)):
        v1 = [pre_points[0][i] - pre_points[0][i - 1], pre_points[1][i] - pre_points[1][i - 1]]
        v2 = [pre_points[0][i + 1] - pre_points[0][i], pre_points[1][i + 1] - pre_points[1][i]]
        RouteAngle_temp = route_angle(v1, v2)
        if(np.absolute(RouteAngle_temp) > flag): 
            Turn_flag[i] = 1

#print(Turn_flag)

Heading_angle = []
Heading_angle_pre = []
v1 = [1, 0]
for i in range(sampleNumber):
    if (i != (sampleNumber - 1)):
        v2 = [new_points2[0][i + 1] - new_points2[0][i], new_points2[1][i + 1] - new_points2[1][i]]
        angle_temp = route_angle(v1, v2)
        Heading_angle.append(angle_temp)

Heading_angle.append(Heading_angle[-1])

for i in range(sampleNumber):
    if (i != (sampleNumber - 1)):
        v2 = [pre_points[0][i + 1] - pre_points[0][i], pre_points[1][i + 1] - pre_points[1][i]]
        angle_temp = route_angle(v1, v2)
        Heading_angle_pre.append(angle_temp)

Heading_angle_pre.append(Heading_angle_pre[-1])
print('-----------------------------',Heading_angle)
print('-----------------------------',Heading_angle_pre)

WayPoints_smoothing = np.array(new_points2).copy()
WayPoints_pre = np.array(pre_points).copy()

for i in range(sampleNumber):
    WayPoints_smoothing[0][i] = WayPoints_smoothing[0][i] - origin[0]
    WayPoints_smoothing[1][i] = WayPoints_smoothing[1][i] - origin[1]
    WayPoints_pre[0][i] = WayPoints_pre[0][i] - origin[0]
    WayPoints_pre[1][i] = WayPoints_pre[1][i] - origin[1]

print(np.shape(Heading_angle))

np.save('route_data_pre.npy', np.array([new_points2, Heading_angle, pre_points, Turn_flag]))
np.save('route_data_relative.npy', np.array([WayPoints_smoothing, Heading_angle, WayPoints_pre, Heading_angle_pre, Turn_flag]))
