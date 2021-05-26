"""
Run this once to pre-processes flood risk data to store each risk level (1-5) as different file,
so each can be a different layer.
"""

import geopandas as gpd
import os

dir_path = '../data/flood_hazard/flood_risk/'
file_path = os.path.join(dir_path, 'Mozambique_1in100yearfloodMERIT_MERITHYDRO_georef_clipped_reclassified.gpkg')
gp_df = gpd.read_file(file_path)

polygons = []

for risk_level in range(5, 0, -1):
    gp_df_risk_level = gp_df[gp_df.DN == risk_level]
    new_file_name = f"mozambique_flood_risk_level_{risk_level}.gpkg"
    new_file_path = os.path.join(dir_path, new_file_name)
    gp_df_risk_level.to_file(new_file_path, layer='countries', driver="GPKG")

