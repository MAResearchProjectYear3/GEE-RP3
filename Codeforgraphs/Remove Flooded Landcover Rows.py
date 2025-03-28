# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 21:51:08 2025

@author: Almeh
"""

import pandas as pd

# Load the CSV file
df = pd.read_csv('Merged_Bangladesh_Event2a_Combined.csv')

# Remove rows where Landcover is 80
df_filtered = df[df['Landcover'] != 80]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv('Bangladesh_Event2a_Complete_N80LC.csv', index=False)
