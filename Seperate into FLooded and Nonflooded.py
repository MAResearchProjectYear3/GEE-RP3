# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 21:57:15 2025

@author: Almeh
"""

import pandas as pd

# Load the CSV file
df = pd.read_csv('Merged_Bangladesh_Event2a_Combined.csv')

# Separate into flooded and non-flooded
flooded_df = df[df['Flooded'] == 1]
non_flooded_df = df[df['Flooded'] == 0]

# Save to new CSV files
flooded_df.to_csv('Bangladesh_Event2a_Complete_N80LC_flooded.csv', index=False)
non_flooded_df.to_csv('Bangladesh_Event2a_Complete_N80LC_nflooded.csv', index=False)
