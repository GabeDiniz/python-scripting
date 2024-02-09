import json
import requests   # pip install requests
from typing import Final
from model import Weather, dt

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

def get_weather_details(weather: dict) -> list[Weather]:
  days: list[dict] = weather.get("list")

  # If no data -> raise exception
  if not days:
    raise Exception(f"[Error] Problem with json: {weather}")
  
  list_of_weather: list[Weather] = []
  for day in days:
    w: Weather = Weather(date = dt.fromtimestamp(day.get('dt')),
                         details = (details := day.get("main")),
                         temp = details.get("temp"),
                         weather = (weather := day.get("weather")),
                         description = weather[0].get("description"))
    list_of_weather.append(w)

  return list_of_weather


if __name__ == "__main__":
  current_weather: dict = get_weather("Toronto", mock=True)
  weather: list[Weather] = get_weather_details(current_weather)

  for w in weather:
    print(w)
    print(w.temp, w.details)