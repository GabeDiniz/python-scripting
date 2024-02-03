from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates:
  latitude: float
  longitude: float
  
  def coordinates(self):
    return self.latitude, self.longitude
  

def get_coordinates(address: str) -> Coordinates | None:
  geolocator = Nominatim(user_agent = "distance_calculator")
  location = geolocator.geocode(address)

  if location:
    return Coordinates(latitude = location.latitude, longitude = location.longitude)
  

def main():
  home_address: str = input("Enter Home Address >> ")
  destination_address: str = input("Enter Destination Address >> ")

  print(get_coordinates(home_address))

if __name__ == "__main__":
  main()