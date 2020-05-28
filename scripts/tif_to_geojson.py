import geopandas as gpd  # for loading/manipulating vector data
import rasterio
import rasterio.features
import rasterio.warp

tif_file = '../data/flood_hazard/Mozambique_1in100yearfloodMERIT_MERITHYDRO.tif'
crs = 'EPSG:3857'

def tif_to_geojson(tif):
    with rasterio.open(tif) as dataset:

        # Read the dataset's valid data mask as a ndarray.
        mask = dataset.dataset_mask()

        # Extract feature shapes and values from the array.
        for geom, val in rasterio.features.shapes(
                mask, transform=dataset.transform):
            print(geom,val)
            # Transform shapes from the dataset's own coordinate
            # reference system to CRS84 (EPSG:4326).
            geom = rasterio.warp.transform_geom(
                dataset.crs, crs, geom, precision=6)

            # Print GeoJSON shapes to stdout.
            print(geom)

tif_to_geojson(tif_file)