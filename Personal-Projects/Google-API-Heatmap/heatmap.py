import pandas as pd
import folium
from folium.plugins import HeatMap
import os

print("Current Working Directory:", os.getcwd())
os.chdir('C:/Users/gabri/Desktop/Code/Misc/python-scripting/Personal Projects/Google API Heatmap')

# Load geocoded addresses
data = pd.read_csv('geocoded_addresses.csv')

# Prepare the data for the heatmap
# Ensure that your latitude and longitude are correctly indexed
print(data.iterrows())
# heat_data = [print(row["Latitude"]) for index, row in data.iterrows()]
heat_data = []
for _, row in data.iterrows():
  print(row)
  if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
        heat_data.append([row['Latitude'], row['Longitude']])

# Create a map centered around an average location
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
map = folium.Map(location=map_center, zoom_start=12)

# Add the heatmap
HeatMap(heat_data).add_to(map)

# Save it to an HTML file
map.save('C:/Users/gabri/Desktop/Code/Misc/python-scripting/Personal Projects/Google API Heatmap/heatmap.html')