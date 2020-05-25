# -------
# IMPORTS
# -------
import geopandas as gpd  # for loading/manipulating vector data
import rasterio  # for loading/manipulating raster data
import folium  # for creating the interactive map

import numpy as np
import pandas as pd
import os
import sys

# ---------
# VARIABLES
# ---------
sw = [-25.0, 30.0]
ne = [-8.5, 43.0]
lat_min, long_min = sw
lat_max, long_max = ne
center = [np.mean([lat_min, lat_max]), np.mean([long_min, long_max])]

out_dir = '../output/'
data_dict = '../data/data_dict_demo_map.csv'  # data dict file tells us which files to read in


# ----------
# MAP SETUP
# ---------

m = folium.Map(
    location=center,
    # max_bounds=True,
    # # prevent map from zooming/panning out of the bounding box:
    # min_lat=lat_min,
    # max_lat=lat_max,
    # min_lon=long_min,
    # max_lon=long_max,
    # min_zoom=5
)

m.fit_bounds(bounds=[sw, ne])  # creates the ideal initial zoom level


# ------------
# LOAD IN DATA
# ------------

data_dict_df = pd.read_csv(data_dict,
                           header=0,  # Row index 0 is the header row.
                           skiprows=[1],  # Row index 1 is the example row.
                           index_col='data_name',)


for index, row in data_dict_df.iterrows():
    file_path = row.file_path
    file_suffix = file_path.split('.')[-1]
    print(file_path, file_path[0], file_suffix)
    if file_path[0] == 'D':
        continue
        # TODO: remove this line, it's just for convenience (which rows I haven't filled in on the data dict yet).

    file_path = os.path.join('../', file_path)
    if file_suffix == 'shp':
        gp_df = gpd.read_file(file_path)
        geo_json = gp_df.to_json()

        for _, gp_row in gp_df.iterrows():
            lat = gp_row.geometry.y
            lon = gp_row.geometry.x
            name = gp_row.name_en
            icon = folium.features.CustomIcon(row.icon2, icon_size=(14, 14))
            marker = folium.Marker(
                [lat, lon],
                icon=icon,
                icon_size=(14, 14))
            m.add_child(marker)

        # points = folium.features.GeoJson(geo_json)
        # m.add_child(points)



### BASEMAPS ###
base_maps = {
    'OSM Humanitarian':
        'http://a.tile.openstreetmap.fr/hot/${z}/${x}/${y}.png',
    'OSM Standard':
        'https://a.tile.openstreetmap.org/${z}/${x}/${y}.png',
    'Google Satellite':
        'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    'ESRI World Topo':
        'https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
}
default_base_map = base_maps['OSM Humanitarian']


# -------
# OUTPUT
# ------
m.save(os.path.join(out_dir, 'map.html'))
