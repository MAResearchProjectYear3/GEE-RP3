# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:25:58 2025

@author: Almeh
"""
import random
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

def generate_random_points(num_points, min_lat, max_lat, min_lon, max_lon, csv_filename=None):
    """Generates random points within the given latitude and longitude range and saves them to a CSV file."""
    np.random.seed(6)  # For reproducibility
    random_points = [
        [np.random.uniform(min_lat, max_lat), np.random.uniform(min_lon, max_lon)]
        for _ in range(num_points)
    ]
    
    # Ensure the file is saved in the current working directory
    file_path = os.path.join(os.getcwd(), csv_filename)
    
    # Save to CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Latitude", "Longitude"])  # Header
        writer.writerows(random_points)
    
    print(f"Generated {num_points} random points and saved to {file_path}")
    return random_points

def plot_random_points(random_points):
    """Plots the generated random points on a scatter plot."""
    latitudes, longitudes = zip(*random_points)
    plt.figure(figsize=(8, 6))
    plt.scatter(longitudes, latitudes, c='blue', marker='o', alpha=0.6, s=1, label='Random Points')
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Randomly Generated Points")
    plt.grid(True)
    plt.show()

 
    
# Define the bounding box
min_lon, min_lat = 91.89527837619349,24.65882295497023
max_lon, max_lat = 91.99368159724968,24.748794329757427

# Number of random points to generate
num_points = 100000

# User-defined filename (set to None to use default)
csv_filename = "GEE_Event_01c_Bangladesh_3.csv"

# Generate and plot points
random_points = generate_random_points(num_points, min_lat, max_lat, min_lon, max_lon, csv_filename)
plot_random_points(random_points)