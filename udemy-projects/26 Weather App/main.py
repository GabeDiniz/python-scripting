import requests   # pip install requests
from typing import Final
from weather_api import get_weather, get_weather_details, Weather

# Fetch Credentials from local .env variables 
from decouple import config

# Email Credentials
API_KEY = config('WEATHER_API_KEY')
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"

def main():
  # Get the current weather details
  while True:
    user_city: str = input("Enter a city: ")
    current_weather: dict = get_weather(user_city, mock=False)
    weather_details: list[Weather] = get_weather_details(current_weather)
    if weather_details:
      break
    print("[Error] City not found!\nPlease ensure you spelled the city correctly...")

  # Get the current days
  dfmt: str = "%d/%m/%y"
  days: list[str] = sorted(list({f"{date.date:{dfmt}}" for date in weather_details}))
  
  for day in days:
    print(day)
    print("-"*10)

    grouped: list[Weather] = [current for current in weather_details if f"{current.date:{dfmt}}" == day]
    for element in grouped: 
      print(element)

    print("")

if __name__ == "__main__":
  main()