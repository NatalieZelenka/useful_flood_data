# -------
# IMPORTS
# -------
import geopandas as gpd  # for loading/manipulating vector data
from shapely.geometry import Point
from shapely.geometry import Polygon
import rasterio  # for loading/manipulating raster data


import folium  # for creating the interactive map

import numpy as np
import pandas as pd
import sys
import os

from PIL import Image, ImageChops

import warnings

warnings.filterwarnings('ignore', 'GeoSeries.notna', UserWarning)

# ---------
# FUNCTIONS
# ---------

def set_crs(df, crs):
    """

    :param df:
    :param crs:
    :return:
    """
    if type(df.crs).__name__ in ['CRS']:
        if str(df.crs).upper() != crs:
            df = df.to_crs(crs)
    else:
        df.crs = crs
    return df


def add_choropleth(feature_group_name, paths, colours, map_obj, crs, bounding_box):
    """

    :param feature_group_name:
    :param path:
    :param colours:
    :param map_obj:
    :param crs:
    :param bounding_box:
    :return:
    """

    feature_group = folium.FeatureGroup(feature_group_name, show=False)
    for i, path in enumerate(paths):
        gp_df = gpd.read_file(path)
        # TODO: Figure out why clipping doesn't work for these created geometries. Or just maybe add an extra data_dict key.
        try:
            assert(str(gp_df.crs).lower() == crs.lower())
        except AssertionError:
            continue  # TODO: logging
        gp_df = set_crs(gp_df, crs)
        colour = colours[i]

        for _, gp_row in gp_df.iterrows():
            polygon_obj = gp_row.geometry
            coords = list(zip(polygon_obj.exterior.coords.xy[1], polygon_obj.exterior.coords.xy[0]))
            polygon = folium.vector_layers.Polygon(coords,
                                                   fill_color=colour,
                                                   fill_opacity=0.7,
                                                   stroke=False)
            feature_group.add_child(polygon)
    map_obj.add_child(feature_group)

    return map_obj


def add_polygon(polygon_name, polygon_path, outline_colour, outline_thickness, map_obj, crs, bounding_box):
    """

    :param polygon_name:
    :param polygon_path:
    :param outline_colour:
    :param outline_thickness:
    :param map_obj:
    :param crs:
    :param bounding_box:
    :return:
    """

    gp_df = gpd.read_file(polygon_path)
    gp_df = gpd.clip(gp_df, bounding_box)
    gp_df = set_crs(gp_df, crs)

    feature_group = folium.FeatureGroup(
        name=polygon_name,
        show=False,
    )

    for i, gp_row in gp_df.iterrows():
        if not type(gp_row.geometry).__name__ == 'MultiPolygon':
            continue

        for polygon_obj in gp_row.geometry:
            coords = list(zip(polygon_obj.exterior.coords.xy[1], polygon_obj.exterior.coords.xy[0]))
            polygon = folium.vector_layers.Polygon(coords, color=outline_colour, line_thickness=outline_thickness)

        feature_group.add_child(polygon)

    map_obj.add_child(feature_group)

    return map_obj


def add_line(line_name, line_path, line_colour, line_thickness, map_obj, crs, bounding_box):
    """

    :param line_name:
    :param line_path:
    :param line_colour:
    :param line_thickness:
    :param map_obj:
    :param crs:
    :param bounding_box:
    :return:
    """
    gp_df = gpd.read_file(line_path)
    gp_df = set_crs(gp_df, crs)
    gp_df = gpd.clip(gp_df, bounding_box)

    feature_group = folium.FeatureGroup(
        name=line_name,
        show=False,
    )

    for _, gp_row in gp_df.iterrows():
        if not type(gp_row.geometry).__name__ == 'LineString':
            # TODO: deal with multiline strings
            continue
        coords = list(zip(gp_row.geometry.xy[1], gp_row.geometry.xy[0]))

        line = folium.vector_layers.PolyLine(coords, color=line_colour, weight=line_thickness, opacity=1)
        feature_group.add_child(line)

    map_obj.add_child(feature_group)

    return map_obj


def add_markers(feature_group_name, marker_path, icon_url, map_obj, crs, bounding_box):
    """

    :param feature_group_name:
    :param marker_path:
    :param icon_url:
    :param map_obj:
    :param crs:
    :param bounding_box:
    :return:
    """
    gp_df = gpd.read_file(marker_path)
    gp_df = set_crs(gp_df, crs)
    gp_df = gpd.clip(gp_df, mask=bounding_box)

    try:
        assert (file_suffix in ['shp', 'gpkg'])
    except AssertionError:
        raise
        # TODO: logging

    feature_group = folium.FeatureGroup(
        name=feature_group_name,
        show=False,
    )

    icon_url = os.path.join(website, icon_url)
    for _, gp_row in gp_df.iterrows():
        if gp_row.geometry.type == 'Point':
            lat = gp_row.geometry.y
            lon = gp_row.geometry.x
        elif gp_row.geometry.type == 'MultiPolygon':  # TODO: Could draw polygon with marker, ask Laurence
            lat = gp_row.geometry.centroid.y
            lon = gp_row.geometry.centroid.x
        icon = folium.features.CustomIcon(icon_url, icon_size=[14, 14])
        marker = folium.Marker(
            [lat, lon],
            icon=icon,
            icon_size=[8, 8],  # TODO: Ask about preferred icon size? 20?
        )
        feature_group.add_child(marker)

    feature_group.add_to(map_obj)

    return map_obj


def icon_colourmap(data_dict, out_dir, colour_col='marker_colour'):
    """

    :param data_dict:
    :param colour_col:
    :return:
    """
    data_dict['new_icon'] = pd.Series(index=data_dict.index, dtype=object)
    for name, row in data_dict.iterrows():
        colour = row[colour_col]
        if not pd.isna(colour) and row.info_type == 'marker':
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
    # TODO: If there is no colour, add path fill = the new colour.
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
    """

    :param tif_file:
    :return:
    """
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
    """

    :param tif:
    :param dest_png:
    :return:
    """
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

    img.save(dest_png)

    return None


def display_tif(src_tif, dest_png, dest_crs):
    """

    :param src_tif:
    :param dest_png:
    :param dest_crs:
    :return:
    """

    # TODO: Put into a function, where you can specify the colourmap/gradient.
    with rasterio.open(src_tif, 'r', driver='GTiff') as tif:
        bounds = tif.bounds

        if not os.path.exists(dest_png):
            png_to_tif(tif, dest_png)

    png_file = os.path.join(website, 'pngs', src_tif.replace('.tif', '.png'))
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

    assert(tif.crs == dest_crs)
    return None


def trim(img):
    border = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, border)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


class Vars:
    """
    Hard-coded variables
    """
    # bounding box:
    n = 35  # lon_max
    e = -19  # lat_max
    s = 34  # lon_min
    w = -20  #lat_min

    crs = 'EPSG:4326'  # This is the version that is


vars_ = Vars()
center = [np.mean([vars_.w, vars_.e]), np.mean([vars_.s, vars_.n])]

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
    # prevent map from panning out of the bounding box:
    min_lat=vars_.w,
    max_lat=vars_.e,
    min_lon=vars_.s,
    max_lon=vars_.n,
)

sw = [vars_.w, vars_.s]
ne = [vars_.e, vars_.n]
m.fit_bounds(bounds=[sw, ne])  # creates the ideal initial zoom level

for map_name in base_maps.keys():
    folium.TileLayer(base_maps[map_name][0],
                     name=map_name,
                     attr=base_maps[map_name][1],
                     min_zoom=9,   # done by trial and error currently
                     ).add_to(m)

# ------------
# ICON COLOURS
# ------------
data_dict_df = pd.read_csv(data_dict_file,
                           header=0,  # Row index 0 is the header row.
                           skiprows=[1],  # Row index 1 is the example row.
                           index_col='data_name',
                           skip_blank_lines=True)
data_dict_df = data_dict_df[data_dict_df.index.notnull()]
data_dict_df = icon_colourmap(data_dict_df, out_dir, colour_col='colour')


# ------------
# LOAD IN DATA
# ------------

bounding_box_coords = [(vars_.n, vars_.w), (vars_.n, vars_.e), (vars_.s, vars_.e), (vars_.s, vars_.w)]
# polygon = gpd.GeoSeries([Point(x[0], x[1]) for x in bounding_box_coords])
polygon = Polygon([x[0], x[1]] for x in bounding_box_coords)


for index, row in data_dict_df.iterrows():
    file_path = row.file_path
    file_suffix = file_path.split('.')[-1]
    relative_path_to_data = '../'

    if row.info_type == 'image_overlay':
        continue
        # if file_suffix == 'tif':
        #     file_name = os.path.basename(file_path)
        #     png_file = os.path.join(out_dir, 'pngs', file_name.replace('.tif', '.png'))
        #     # img = display_tif(src_tif=file_path, dest_png = png_file, dest_crs=crs)
        #     continue  # TODO: Hopefully convert to geojson/geopackage because the pixels look bad.

    elif row.info_type == 'choropleth':
        multiple_paths = file_path.split(';')
        multiple_paths = [os.path.join(relative_path_to_data, path) for path in multiple_paths]
        m = add_choropleth(feature_group_name=index,
                           paths=multiple_paths,
                           colours=row.colour.split(';'),
                           map_obj=m,
                           crs=vars_.crs,
                           bounding_box=polygon)

    elif row.info_type == 'marker':
        m = add_markers(feature_group_name=index,
                        marker_path=os.path.join(relative_path_to_data, file_path),
                        icon_url=row.new_icon,
                        map_obj=m,
                        crs=vars_.crs,
                        bounding_box=polygon)

    elif row.info_type == 'line':
        m = add_line(line_name=index,
                     line_path=os.path.join(relative_path_to_data, file_path),
                     line_colour=row.colour,
                     line_thickness=row.thickness,
                     map_obj=m,
                     crs=vars_.crs,
                     bounding_box=polygon)

    elif row.info_type == 'polygon':
        m = add_polygon(polygon_name=index,
                        polygon_path=os.path.join(relative_path_to_data, file_path),
                        outline_colour=row.colour,
                        outline_thickness=row.thickness,
                        map_obj=m,
                        crs=vars_.crs,
                        bounding_box=polygon)
    else:
        print(f"Info type detected not known: {row.info_type}")  # TODO logging

# draw bounding box:
bounding_box_coords = [(vars_.w, vars_.n), (vars_.e, vars_.n), (vars_.e, vars_.s), (vars_.w, vars_.s)]
bounding_box_poly = folium.vector_layers.Polygon(bounding_box_coords, color='#7a7a7a')
m.add_child(bounding_box_poly)

folium.LayerControl(collapsed=False).add_to(m)

# -------
# OUTPUT
# ------
html_file = os.path.join(out_dir, 'index.html')
m.save(html_file)
