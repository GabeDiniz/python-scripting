import json
import requests   # pip install requests
from typing import Final

# Fetch Credentials from local .env variables 
from decouple import config

# Email Credentials
API_KEY = config('WEATHER_API_KEY')
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city_name: str, mock: bool = True) -> dict:
  if mock:
    with open("dummy_data.json") as file:
      return json.load(file)
    
  # Request live data
  payload: dict = {"q": city_name, "appid": API_KEY, "units": "metric"}
  request = requests.get(url=BASE_URL, params=payload)
  data: dict = request.json()

  # Puts API data into JSON file
  with open("dummy_data.json", "w") as file:
    json.dump(data, file)

  return data

if __name__ == "__main__":
  print(get_weather("Toronto", mock=True))
