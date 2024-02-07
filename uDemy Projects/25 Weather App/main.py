import requests   # pip install requests
from typing import Final

# Fetch Credentials from local .env variables 
from decouple import config

# Email Credentials
API_KEY = config('WEATHER_API_KEY')
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}"
