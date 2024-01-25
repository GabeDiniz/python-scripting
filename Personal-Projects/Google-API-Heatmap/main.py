
import pandas as pd
import googlemaps
import csv

# Fetch API key from local .env variables 
from decouple import config

# Google Maps API key
api_key = config('GOOGLE_API_KEY')

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=api_key)

# Get latitude and longitude
def get_lat_lng(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    return None, None

# Read addresses from CSV
addresses = pd.read_csv('addresses.csv', header=None)[0]  # Adjust column name if necessary
print(addresses)

# Create a list to store geocoding results
results = []

# Geocode each address
for address in addresses:
    lat, lng = get_lat_lng(address)
    results.append([address, lat, lng])

# Save results to a new CSV file
with open('geocoded_addresses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Address', 'Latitude', 'Longitude'])
    writer.writerows(results)

print("Geocoding complete. Results saved to 'geocoded_addresses.csv'")
