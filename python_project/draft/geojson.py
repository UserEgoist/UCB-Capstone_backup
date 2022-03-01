#!/usr/bin/python3

import geopandas as gp

loadData = gp.read_file("./OSM and GeoJSON/bly_piers.geojson")
print(loadData)

loadType = loadData['geometry'][0].geom_type
print(loadType)

