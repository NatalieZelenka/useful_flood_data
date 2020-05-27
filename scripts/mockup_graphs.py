# -------
# IMPORTS
# -------
import geopandas as gpd  # for loading/manipulating vector data
import rasterio  # for loading/manipulating raster data

import folium  # for creating the interactive map

import numpy as np
import pandas as pd
import os

from PIL import Image, ImageChops


# ---------
# FUNCTIONS
# ---------

def icon_colourmap(data_dict, out_dir, colour_col='marker_colour'):
    """

    :param data_dict:
    :param colour_col:
    :return:
    """
    data_dict['new_icon'] = pd.Series(index=data_dict.index, dtype=object)
    for name, row in data_dict.iterrows():
        colour = row[colour_col]
        if not pd.isna(colour):
            icon_file = row.icon
            new_icon_file = recolour_icon(icon_file, colour, out_dir)
            data_dict.loc[name, 'new_icon'] = new_icon_file
    return data_dict


def recolour_icon(old_icon_file, new_colour_hex, out_dir, new_subdir='recoloured', old_color_hex='#418fde'):
    """

    :param old_icon_file:
    :param new_colour_hex:
    :param out_dir:
    :param new_subdir:
    :param old_color_hex:
    :return:
    """
    old_icon_file = os.path.join(out_dir, old_icon_file)
    directory_path, file_name = os.path.split(old_icon_file)
    directory_path = os.path.join(directory_path, new_subdir)
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)
    file_name, file_extension = os.path.splitext(file_name)
    new_colour_name = new_colour_hex[1:]
    new_icon_file = os.path.join(directory_path, f"{file_name}_{new_colour_name}.svg")
    try:
        assert(file_extension == '.svg')
    except AssertionError:
        # TODO: warnings/logging
        raise

    if not os.path.isfile(new_icon_file):
        with open(old_icon_file, 'r') as f:
            text = f.read()
            occurrence_count = text.count(old_color_hex)
            text = text.replace(old_color_hex, new_colour_hex, occurrence_count)
        with open(new_icon_file, 'w') as f:
            f.write(text)
    return new_icon_file.strip(out_dir)


def tif_to_geojson(tif_file):
    with rasterio.open(tif_file) as dataset:
        # Read the dataset's valid data mask as a ndarray.
        mask = dataset.dataset_mask()

        # Extract feature shapes and values from the array.
        for geom, val in rasterio.features.shapes(
                mask, transform=dataset.transform):
            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geom = rasterio.warp.transform_geom(
                dataset.crs, 'EPSG:4326', geom, precision=6)

            # Print GeoJSON shapes to stdout.
            return geom

def png_to_tif(tif, dest_png):

        # tif files are crazy so they can have negative numbers and floats convert to 8 bit:
        # TODO: add colourmap option
        raster = tif.read()

        alpha = np.array(raster)
        raster[raster < 0] = 0
        raster = (255 * (raster - raster.min())) / (raster.max() - raster.min())
        raster = raster.astype(int).squeeze()
        shape = raster.shape

        zeroes = np.zeros(shape)

        image = np.zeros([shape[0], shape[1], 4], dtype=np.uint8)
        image[:, :, 2] = raster
        image[:, :, 3] = raster

        img = Image.fromarray(image)
        downsize_by = 0.2  # 20%
        new_size = [int(i * downsize_by) for i in shape]
        img.thumbnail(new_size, Image.ANTIALIAS)

        # img = trim(img)

        img.save(png_file)

        return None

def display_tif(src_tif, dest_png, dest_crs):

    # TODO: Put into a function, where you can specify the colourmap/gradient.
    with rasterio.open(src_tif, 'r', driver='GTiff') as tif:
        bounds = tif.bounds

        if not os.path.exists(dest_png):
            png_to_tif(tif, dest_png)


    png_file = os.path.join(website, 'pngs', file_name.replace('.tif', '.png'))
    image_overlay = folium.raster_layers.ImageOverlay(
                image=png_file,
                name=index,
                interactive=False,
                z_index=100,
                opacity=1,
                bounds=[[bounds.bottom, bounds.left], [bounds.top, bounds.right]],
                cross_origin=False,
                )
    m.add_child(image_overlay)

# if tif.crs != crs:  # TODO: maybe put this in?
# shape = raster.shape
#     dest = np.zeroes(shape)
#     reproject(
#         raster,
#         dest,
#         src_crs=tif.crs,
#         dst_crs=crs,
#         resampling=Resampling.nearest)

def trim(img):
    border = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, border)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img

# ---------
# VARIABLES
# ---------
sw = [-25.0, 30.0]
ne = [-8.5, 43.0]
crs = 'EPSG:4326'  # This is the version that is

lat_min, long_min = sw
lat_max, long_max = ne
center = [np.mean([lat_min, lat_max]), np.mean([long_min, long_max])]

out_dir = '../docs/'
data_dict_file = '../data/data_dict_demo_map.csv'  # data dict file tells us which files to read in
website = 'https://nataliethurlby.github.io/useful_flood_data/'

# --------
# BASEMAPS
# --------

base_maps = {
    'OSM Humanitarian':
        ('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
         '<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>).'),
    'OSM Standard':
        ('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 'Data by &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'),
    'ESRI Satellite':
        ('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 'ESRI'),  # TODO: add attributions for basemaps
    'ESRI World Topo':
        ('https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', 'ESRI'),  # TODO: add attributions for basemaps
}
default_base_map = base_maps['OSM Humanitarian']

# ----------
# MAP SETUP
# ---------

m = folium.Map(
    location=center,
    tiles=None,
    max_bounds=True,
    # prevent map from zooming/panning out of the bounding box:
    min_lat=lat_min,
    max_lat=lat_max,
    min_lon=long_min,
    max_lon=long_max,
)

m.fit_bounds(bounds=[sw, ne])  # creates the ideal initial zoom level

for map_name in base_maps.keys():
    folium.TileLayer(base_maps[map_name][0],
                     name=map_name,
                     attr=base_maps[map_name][1],
                     min_zoom=5,
                     ).add_to(m)

# ------------
# ICON COLOURS
# ------------
data_dict_df = pd.read_csv(data_dict_file,
                           header=0,  # Row index 0 is the header row.
                           skiprows=[1],  # Row index 1 is the example row.
                           index_col='data_name',)

marker_colours = {
    'Airports': '#34b1eb',
    'Health Facilities': '#34ebb4',
    'City': '#000000',
}

data_dict_df['marker_colour'] = data_dict_df.index.map(marker_colours)
data_dict_df = icon_colourmap(data_dict_df, out_dir)

# ------------
# LOAD IN DATA
# ------------

for index, row in data_dict_df.iterrows():
    file_path = row.file_path
    file_suffix = file_path.split('.')[-1]
    if file_path[0] == 'D':
        continue
        # TODO: remove this line, it's just for convenience (which rows I haven't filled in on the data dict yet).

    file_path = os.path.join('../', file_path)

    if row.info_type == 'image_overlay':

        if file_suffix == 'tif':
            file_name = os.path.basename(file_path)
            png_file = os.path.join(out_dir, 'pngs', file_name.replace('.tif', '.png'))
            # img = display_tif(src_tif=file_path, dest_png = png_file, dest_crs=crs)
            continue  # TODO: Hopefully convert to geojson/geopackage because the pixels look bad.

    elif row.info_type == 'marker':
        gp_df = gpd.read_file(file_path)
        if type(gp_df.crs).__name__ in ['CRS']:
            assert(str(gp_df.crs).upper() == crs)
        # else:  # TODO: tidy
        #     print(type(gp_df.crs).__name__)
        assert(file_suffix in ['shp', 'gpkg'])

        feature_group = folium.FeatureGroup(
            name=index,
        )

        for _, gp_row in gp_df.iterrows():
            if gp_row.geometry.type == 'Point':
                lat = gp_row.geometry.y
                lon = gp_row.geometry.x
            elif gp_row.geometry.type == 'MultiPolygon':  # TODO: Could draw polygon with marker, ask Laurence
                lat = gp_row.geometry.centroid.y
                lon = gp_row.geometry.centroid.x

            icon_url = os.path.join(website, row.new_icon)
            icon = folium.features.CustomIcon(icon_url, icon_size=[14,14])
            marker = folium.Marker(
                [lat, lon],
                icon=icon,
                icon_size=[8, 8],  # TODO: Ask about preferred icon size? 20?
            )
            feature_group.add_child(marker)

        feature_group.add_to(m)
    else:
        gp_df = gpd.read_file(file_path)
        print(index, gp_df)

folium.LayerControl().add_to(m)

# -------
# OUTPUT
# ------
html_file = os.path.join(out_dir, 'index.html')
m.save(html_file)
