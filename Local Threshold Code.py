# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:14:40 2025

@author: Almeh
"""

import pandas as pd

# === Load your CSV file ===
input_file = "Bangladesh_Event2_Complete.csv"
df = pd.read_csv(input_file)

# === Localized thresholds from Event 1 ===
#VV_threshold = -14.09      # dB
#VH_threshold = -20.38      # dB
#elevation_threshold = 13.24  # meters

# === Localized thresholds from Event 2 ===
VV_threshold = -12.66     # dB
VH_threshold = -19.48      # dB
elevation_threshold = 5.58  # meters


# === Classification Function ===
def classify_flood_status(row):
    if (
        row['VV'] < VV_threshold and
        row['VH'] < VH_threshold and
        row['Elevation'] < elevation_threshold
    ):
        return 'FGT' # Flodded
    else:
        return 'NFT'

# === Apply the classification to each row ===
df['Flood_Status'] = df.apply(classify_flood_status, axis=1)

# === Save the output ===
output_file = "ThresholdEvent2.csv"
df.to_csv(output_file, index=False)

print(f"Flood status classification complete. Output saved to {output_file}")



