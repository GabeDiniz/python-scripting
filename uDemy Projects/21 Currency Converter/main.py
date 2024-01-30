import requests   # pip install requests
import json
from typing import Final

# Fetch API key from local .env variables 
from decouple import config

# Google Maps API key
API_KEY: Final[str] = config('CURRENT_API_KEY')
BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'


def get_rates(mock: bool = False) -> dict:
  # If mock data exists
  if mock: 
    with open("rates.json", "r") as file:
      return json.load(file)
    
  payload: dict = {"access_key": API_KEY}
  request = requests.get(url=BASE_URL, params=payload)
  data: dict = request.json()

  with open("rates.json", "w") as file:
    return json.dump(data, file)
  
  return data

get_rates()