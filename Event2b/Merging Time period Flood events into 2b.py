# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 10:57:49 2025

@author: Almeh
"""

import pandas as pd

# File paths
file_paths = [
    "Merged_Bangladesh_Event2b_1.csv",
    "Merged_Bangladesh_Event2b_2.csv",
    "Merged_Bangladesh_Event2b_3.csv"
]

# Read all files into dataframes
dfs = [pd.read_csv(file) for file in file_paths]

# Remove unnecessary unnamed columns if present
dfs = [df.loc[:, ~df.columns.str.contains('Unnamed')] for df in dfs]

# Remove the 'date' column if present
dfs = [df.drop(columns=['date'], errors='ignore') for df in dfs]

# Concatenate all dataframes while keeping only one header row
merged_df_corrected = pd.concat(dfs, ignore_index=True)

# Save the corrected merged file
corrected_file_path = "Merged_Bangladesh_Event2b_Combined.csv"
merged_df_corrected.to_csv(corrected_file_path, index=False)

print(f"Merged file saved as {corrected_file_path}")

