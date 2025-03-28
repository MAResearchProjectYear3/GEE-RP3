# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 05:15:02 2025

@author: Almeh
"""

import pandas as pd

# Load CSV files
vv_vh_df = pd.read_csv('Bangladesh_VVVH_Ending_3.csv')
elevation_df = pd.read_csv('Bangladesh_Event1a_Elevation_3.csv')
flooded_df = pd.read_csv('Bangladesh_Event1a_Flooded_3.csv')
landcover_df = pd.read_csv('Bangladesh_Event1a_Landcover_3.csv')  # Corrected file name
slope_df = pd.read_csv('Bangladesh_Event1a_Slope_3.csv')

# Rename columns to ensure consistency
elevation_df = elevation_df.rename(columns={'dem': 'Elevation'})
flooded_df = flooded_df.rename(columns={'flooded': 'Flooded'})
slope_df = slope_df.rename(columns={'AVE': 'Slope'})
landcover_df = landcover_df.rename(columns={'Map': 'Landcover'})  # Ensure landcover column exists

# Merge all datasets on Latitude & Longitude
merged_df = vv_vh_df.merge(flooded_df, on=['Latitude', 'Longitude'], how='left')
merged_df = merged_df.merge(landcover_df, on=['Latitude', 'Longitude'], how='left')
merged_df = merged_df.merge(elevation_df, on=['Latitude', 'Longitude'], how='left')
merged_df = merged_df.merge(slope_df, on=['Latitude', 'Longitude'], how='left')

# Ensure all expected columns exist
print("Final Merged Columns:", merged_df.columns)

# Reorder columns to match the required schema
final_columns = ['date', 'Latitude', 'Longitude', 'VV', 'VH', 'Flooded', 'Landcover', 'Elevation', 'Slope']
merged_df = merged_df[final_columns]

# Drop rows with any missing values
merged_df = merged_df.dropna()

# Save the merged dataframe
output_path = "Merged_Bangladesh_Event1a_3.csv"
merged_df.to_csv(output_path, index=False)

# Print dataset preview
print("Merged Data Preview:")
print(merged_df.head())

# Notify user
print(f"Merged dataset saved to: {output_path}")



