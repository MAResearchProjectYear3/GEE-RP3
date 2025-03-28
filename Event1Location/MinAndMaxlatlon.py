# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 04:04:44 2025

@author: Almeh
"""

import math

def bounding_box(center_lat, center_lon, area_km2=100):
    # Side length of the square in km
    side_km = math.sqrt(area_km2)
    half_side_km = side_km / 2

    # Approx conversion from km to degrees
    lat_per_km = 1 / 111.32  # degrees latitude per km
    lon_per_km = 1 / (111.32 * math.cos(math.radians(center_lat)))  # degrees longitude per km at given lat

    # Latitude bounds
    delta_lat = half_side_km * lat_per_km
    min_lat = center_lat - delta_lat
    max_lat = center_lat + delta_lat

    # Longitude bounds
    delta_lon = half_side_km * lon_per_km
    min_lon = center_lon - delta_lon
    max_lon = center_lon + delta_lon

    return {
        "min_lat": min_lat,
        "max_lat": max_lat,
        "min_lon": min_lon,
        "max_lon": max_lon
    }

#Event 1
#1st: 91.9444, 24.7038
#2nd: 92.0447024671648, 24.545699216951935
#3rd: 92.07634063577363, 24.76681186444096

# Example usage:
center_lat = 24.76681186444096
center_lon = 92.07634063577363
bbox = bounding_box(center_lat, center_lon)
print(bbox)
