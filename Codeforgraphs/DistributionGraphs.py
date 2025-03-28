# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 07:37:03 2025

@author: Almeh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.ticker import ScalarFormatter, FuncFormatter

# Bangladesh_Event1_Complete_N80LC
#"Merged_Bangladesh_Event2a_Combined_N80LC.csv"
# Load the CSV file
file_path = "Merged_Bangladesh_Event2a_Combined_N80LC.csv"
df = pd.read_csv(file_path)

# Clean and prepare the data
df_clean = df.dropna(subset=["VV", "VH", "Elevation", "Landcover", "Flooded"])

# Features and labels
features = ["VV", "VH", "Elevation"]
titles = ["VV (dB)", "VH (dB)", "Elevation (m)"]
#xlims = [(-27.5, 0), (-37.5, -7.5), (7.5, 22.5)] #Event 1
xlims = [(-25, 0), (-37.5, -7.5), (0 ,12.5)] #Event 2

# Control number of ticks per subplot (can be different)
x_tick_counts = [6, 5, 6]  # <- Set how many ticks you want for each subplot Event 1
#x_tick_counts = [6, 5, 6]  # <- Set how many ticks you want for each subplot Event 2

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

for i, (ax, feature, title, xlim, tick_count) in enumerate(zip(axes, features, titles, xlims, x_tick_counts)):
    # Extract values
    data0 = df_clean[df_clean["Flooded"] == 0][feature].values
    data1 = df_clean[df_clean["Flooded"] == 1][feature].values

    # Plot histograms
    sns.histplot(data0, stat="density", bins=200, color="red", element="step", fill=True, alpha=0.3, ax=ax)
    sns.histplot(data1, stat="density", bins=200, color="blue", element="step", fill=True, alpha=0.3, ax=ax)

    # KDEs
    kde0 = gaussian_kde(data0)
    kde1 = gaussian_kde(data1)

    x = np.linspace(xlim[0], xlim[1], 1000)
    y0 = kde0(x)
    y1 = kde1(x)

    # Plot KDE curves
    ax.fill_between(x, y0, color="red", alpha=0.5)
    ax.fill_between(x, y1, color="blue", alpha=0.5)

    # Find intersection point
    diff = np.abs(y0 - y1)
    idx = np.argmin(diff)
    intersection_x = x[idx]

    # Draw vertical line at intersection
    ax.axvline(intersection_x, color="black", linestyle="--", linewidth=2)
    ax.text(intersection_x + 0.5, max(max(y0), max(y1)) * 0.95, f"{intersection_x:.2f}", 
            color="black", fontsize=16, rotation=0, va='top', ha='left')

    # Axes settings
    ax.set_xlabel(title, fontsize=16)
    if i == 0:
        ax.set_ylabel("Density", fontsize=16)
    else:
        ax.set_ylabel("")

    ax.set_xlim(xlim)

    # Custom number of ticks for this subplot
    xticks = np.linspace(xlim[0], xlim[1], tick_count)
    ax.set_xticks(xticks)

    # Custom formatter for x-axis: show "0" instead of "0.00"
    def custom_formatter(x, _):
        return "0" if abs(x) < 1e-8 else f"{x:.2f}"
    ax.xaxis.set_major_formatter(FuncFormatter(custom_formatter))

    ax.tick_params(axis='both', labelsize=14)
    ax.tick_params(axis='x', pad=10)

    # Format y-axis ticks to remove ".00"
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.get_major_formatter().set_useOffset(False)
    ax.yaxis.get_major_formatter().set_scientific(False)

    # Set ylim with extra headroom for first two plots
    y_max = max(max(y0), max(y1))
    if i < 2:
        ax.set_ylim(0, y_max + 0.02)

    # Legend on first plot
    if i == 0:
        ax.legend(
            handles=[
                mpatches.Patch(color='red', label='Non-Flooded', alpha=0.5),
                mpatches.Patch(color='blue', label='Flooded', alpha=0.5),
                mpatches.Patch(color='purple', label='Intersection')
            ],
            title="Flood Status",
            loc='upper left',
            fontsize=12,
            title_fontsize=13
        )

# Save and show
plt.savefig("Event2aDistributionLC.png", dpi=400, bbox_inches='tight')
plt.show()





