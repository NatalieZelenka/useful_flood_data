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

out_dir = '../docs/'
data_dict = '../data/data_dict_demo_map.csv'  # data dict file tells us which files to read in
website = 'https://nataliethurlby.github.io/useful_flood_data/'

# --------
# BASEMAPS
# --------

base_maps = {
    'OSM Humanitarian':
        ('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
         '<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>).'),
    'OSM Standard':
        ('https://{s}.tile.openstreetmap.org/${z}/${x}/${y}.png', ' '),  # TODO: add attributions for basemaps
    'Google Satellite':
        ('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', ' '),  # TODO: add attributions for basemaps
    'ESRI World Topo':
        ('https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', ' '),  # TODO: add attributions for basemaps
}
default_base_map = base_maps['OSM Humanitarian']

# ----------
# MAP SETUP
# ---------

m = folium.Map(
    location=center,
    tiles=default_base_map[0],
    attr=default_base_map[1],
    max_bounds=True,
    # prevent map from zooming/panning out of the bounding box:
    min_lat=lat_min,
    max_lat=lat_max,
    min_lon=long_min,
    max_lon=long_max,
    min_zoom=5,
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
    if file_path[0] == 'D':
        continue
        # TODO: remove this line, it's just for convenience (which rows I haven't filled in on the data dict yet).

    file_path = os.path.join('../', file_path)

    if row.info_type == 'marker':
        gp_df = gpd.read_file(file_path)
        assert(file_suffix in ['shp', 'gpkg'])
        for _, gp_row in gp_df.iterrows():
            if gp_row.geometry.type == 'Point':
                lat = gp_row.geometry.y
                lon = gp_row.geometry.x
            elif gp_row.geometry.type == 'MultiPolygon':  # TODO: Could draw polygon with marker
                lat = gp_row.geometry.centroid.y
                lon = gp_row.geometry.centroid.x
            # name = gp_row.name_en
            icon_url = os.path.join(website, row.icon)
            icon = folium.features.CustomIcon(icon_url, icon_size=(14, 14))
            marker = folium.Marker(
                [lat, lon],
                icon=icon,
                # popup=name,  # TODO: Ask Laurence about popups.
                # tooltip='Test',
            #    icon_size=(, 1000),
            )  # TODO: Ask about icon size
            m.add_child(marker)

        # points = folium.features.GeoJson(geo_json)
        # m.add_child(points)

# -------
# OUTPUT
# ------
m.save(os.path.join(out_dir, 'index.md'))
m.save(os.path.join(out_dir, 'index.html'))
