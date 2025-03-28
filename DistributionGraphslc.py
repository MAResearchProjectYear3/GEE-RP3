# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 07:37:03 2025

@author: Almeh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Load the CSV file
file_path = "Bangladesh_Event1_Complete_N80LC.csv"
df = pd.read_csv(file_path)

# Clean and prepare the data
df_clean = df.dropna(subset=["VV", "VH", "Elevation", "Landcover", "Flooded"])
df_clean["Flooded"] = df_clean["Flooded"].astype(int)

# Features and labels
features = ["Landcover"]
titles = ["Landcover"] 

# Define custom legend handles to ensure correct color-label match
legend_handles = [
    mpatches.Patch(color='blue', label='Non-Flooded (0)'),
    mpatches.Patch(color='red', label='Flooded (1)')
]

# Plotting
plt.figure(figsize=(15, 5))
for i, (feature, title) in enumerate(zip(features, titles), 1):
    plt.subplot(1, 3, i)
    sns.histplot(
        data=df_clean,
        x=feature,
        hue="Flooded",
        hue_order=[0, 1],  # Ensures 0 = blue, 1 = red
        kde=True,
        stat="density",
        common_norm=False,
        palette={0: "blue", 1: "red"},
        legend=False  # Disable auto-legend
    )
    plt.xlabel(title)
    plt.ylabel("Density")
    plt.legend(handles=legend_handles, title="Flood Status")

plt.tight_layout()
plt.show()
