import requests

# Fetch API key from local .env variables 
from decouple import config

# Google Maps API key
API_KEY = config('SPORT_ODDS_API_KEY')
HOST = 'https://api.the-odds-api.com'

sport = "upcoming"
request = requests.get(f"{HOST}/v4/sports/{sport}/odds/?apiKey={API_KEY}&regions=us")
data = request.json()

print(data)