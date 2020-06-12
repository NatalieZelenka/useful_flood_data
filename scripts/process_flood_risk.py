import geopandas as gpd
import os


# '#81c803;#fcf803;#fc9403;#fc6703;fc0303'  # 5,4,3,2,1

dir_path = '../data/flood_hazard/flood_risk/'
file_path = os.path.join(dir_path, 'Mozambique_1in100yearfloodMERIT_MERITHYDRO_georef_clipped_reclassified.gpkg')
gp_df = gpd.read_file(file_path)

polygons = []

for risk_level in range(5, 0, -1):
    gp_df_risk_level = gp_df[gp_df.DN == risk_level]
    new_file_name = f"mozambique_flood_risk_level_{risk_level}.gpkg"
    new_file_path = os.path.join(dir_path, new_file_name)
    gp_df_risk_level.to_file(new_file_path, layer='countries', driver="GPKG")

