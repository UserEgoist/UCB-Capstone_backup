#!/usr/bin/python3
import networkx as nx
import osmnx as ox
import numpy as np
from scipy.interpolate import CubicSpline, splprep, splev, splrep
import matplotlib.pyplot as plt
from sympy import lambdify, bspline_basis_set
from sympy.abc import u

def route_angle(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    dot = x1*x2 + y1*y2
    det = x1*y2 - y1*x2
    theta = np.arctan2(det, dot)
    return theta*180/np.pi

# download/model a street network for some city then visualize it
#G = ox.graph_from_xml(filepath='./OSM and GeoJSON/bly_01.osm')
#fig, ax = ox.plot_graph(G)

north, south, east, west = 42.3873318, 42.370086, -121.0101128, -121.0317421
MDGraph = ox.graph_from_bbox(north, south, east, west, simplify = False)
MDGraph_proj = ox.projection.project_graph(MDGraph)
#ox.osm_xml.save_graph_xml(G, filepath='./OSM and GeoJSON/Tao.osm')
#print("Is the graph projected? ---- ", ox.projection.is_projected('crs'))
#ox.plot_graph(MDGraph)

# get the nearest network nodes to two lat/lng points with the distance module
orig = ox.distance.nearest_nodes(MDGraph, X=-121.0180924, Y=42.3828246)
#dest = ox.distance.nearest_nodes(MDGraph, X=-121.023110,  Y=42.379616)
dest = ox.distance.nearest_nodes(MDGraph, X=-121.0179955, Y=42.3823027)

print(orig, dest)
# find the shortest path between nodes, minimizing travel time, then plot it
route = ox.distance.shortest_path(MDGraph, orig, dest, weight="length") #todo travel_time
#fig, ax = ox.plot_graph_route(MDGraph, route, node_size=0)

gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph)
print("1Str------------------------------")
print(gdf_nodes.loc[route])
print("1End------------------------------")

gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(MDGraph_proj)
print("2Str------------------------------")
print(gdf_nodes.loc[route])
print("2End------------------------------")

print(gdf_nodes.loc[route[0]].y)
print(gdf_nodes.loc[route[1]].y)
#ox.plot_graph(MDGraph_proj)
#fig, ax = ox.plot_graph_route(MDGraph, route, node_size=0)
# how long is our route in meters?
edge_lengths = ox.utils_graph.get_route_edge_attributes(MDGraph, route, "length")
sumRoute = round(sum(edge_lengths))
print("size of route", len(route))
print(route)
print("sumRoute = ", sumRoute)
#fig, ax = ox.plot_graph_route(MDGraph, route, node_size=0)

# how far is it between these two nodes as the crow flies?
# use OSMnx's vectorized great-circle distance (haversine) function
# orig_x = MDGraph.nodes[orig]["x"]
# orig_y = MDGraph.nodes[orig]["y"]
# dest_x = MDGraph.nodes[dest]["x"]
# dest_y = MDGraph.nodes[dest]["y"]
# sumCircle = round(ox.distance.great_circle_vec(orig_y, orig_x, dest_y, dest_x))
# print("sumCircle = ", sumCircle)

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
        print(RouteAngle_temp)
        if(np.absolute(RouteAngle_temp) > 20): # assume 10 degree is smooth enough
            #Linear interpolation
            interpolation_count = int(np.absolute(RouteAngle_temp)/20) # assume 10 degree is smooth enough
            print(interpolation_count)
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

print(np.size(Route_NodeList))
print(np.size(Route_x))

Route_orig_x = []
Route_orig_y = []
count = np.size(route)
for i in range(count):
    Route_orig_x.append(gdf_nodes.loc[Route_NodeList[i]].x)
    Route_orig_y.append(gdf_nodes.loc[Route_NodeList[i]].y)

print("route_Ox:", Route_orig_x)
print("route_Oy:", Route_orig_y)
print("route_x: ", Route_x)
print("route_y: ", Route_y)

tck1, u1 = splprep([Route_orig_x, Route_orig_y], s = 20)
new_points1 = splev(np.linspace(0.,1.,10000), tck1)

X2_unique = []
Y2_unique = []
_, idx1 = np.unique(Route_x, return_index=True)
idx1_sort = np.sort(idx1)
for i in idx1_sort:
    X2_unique.append(Route_x[i])
    Y2_unique.append(Route_y[i])

tck2, u2 = splprep([X2_unique, Y2_unique], s = 20) # must set s, because exist duplicate x
new_points2 = splev(np.linspace(0.,1.,10000), tck2)

print("tck2", tck2)
print("u2", u2)

basis = bspline_basis_set(tck2[2], tck2[0],  u)
for i, b in enumerate(basis):
    print(f"Basis {i} :", b)

# convert the basis functions to numpy so they can be evaluated quicker
np_basis = [lambdify(u, b, modules=['numpy']) for b in basis]
print(np_basis)





# spl11 = splrep(Route_orig_x[-5:-10:-1], Route_orig_y[-5:-10:-1])
# X1_splrep1 = np.linspace(Route_orig_x[4], Route_orig_x[0], 100)
# Y1_splrep1 = splev(X1_splrep1, spl11)
# spl12 = splrep(Route_orig_x[4:], Route_orig_y[4:], k = 3)
# X1_splrep2 = np.linspace(Route_orig_x[4], Route_orig_x[-1], 100)
# Y1_splrep2 = splev(X1_splrep2, spl12)

# spl21 = splrep(Route_x[-19:-36:-1], Route_y[-19:-36:-1], s = 1) # must set s, because exist duplicate x
# X2_splrep1 = np.linspace(Route_x[16], Route_x[0], 100)
# Y2_splrep1 = splev(X2_splrep1, spl21)
# spl22 = splrep(Route_x[16:], Route_y[16:], s = 1)
# X2_splrep2 = np.linspace(Route_x[16], Route_x[-1], 100)
# Y2_splrep2 = splev(X2_splrep2, spl22)

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(Route_orig_x, Route_orig_y, 'ro', new_points1[0], new_points1[1], 'b-')
ax1.set_aspect('equal', adjustable='datalim')
ax2.plot(Route_x, Route_y, 'ro', new_points2[0], new_points2[1], 'b-')
ax2.set_aspect('equal', adjustable='datalim')
# ax3.plot(Route_orig_x, Route_orig_y, 'ro', X1_splrep1, Y1_splrep1, 'b-', X1_splrep2, Y1_splrep2, 'y-')
# ax3.set_aspect('equal', adjustable='datalim')
# ax4.plot(Route_x, Route_y, 'ro', X2_splrep1, Y2_splrep1, 'b-', X2_splrep2, Y2_splrep2, 'y-')
# ax4.set_aspect('equal', adjustable='datalim')
plt.show()


