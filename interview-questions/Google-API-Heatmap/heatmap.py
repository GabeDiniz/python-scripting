import pandas as pd
import folium
from folium.plugins import HeatMap
import os

print("Current Working Directory:", os.getcwd())

# Load geocoded addresses
data = pd.read_csv('geocoded_addresses.csv')

# Prepare the data for the heatmap
heat_data = []
for _, row in data.iterrows():
  if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
    heat_data.append([row['Latitude'], row['Longitude']])

# Create a map centered around an average location
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
map = folium.Map(location=map_center, zoom_start=12)

# Add the heatmap
HeatMap(heat_data).add_to(map)

# Save it to an HTML file
print("Heatmap generated successfully...")
map.save('heatmap.html')