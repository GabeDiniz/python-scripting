import requests
import json
import matplotlib.pyplot as plt
import datetime

# Fetch API key from local .env variables 
from decouple import config

api_key = config('api_key')
api_url = f"https://api.stlouisfed.org/fred/series/observations?series_id=GNPCA&{api_key}"

response = requests.get(api_url)

if response.status_code == 200:
  data = json.loads(response.text)
  observations = data["observations"]

  dates = []
  values = []
  x = 0
  
  for observation in observations:
    date = observation["date"]
    value = observation["value"]

    print(datetime.datetime.strptime(date, "%Y-%m-%d"))
    dates.append(datetime.datetime.strptime(date, "%Y-%m-%d"))
    values.append(float(value))
    x += 1
    print(x)

print("test")
print(values)

plt.plot(dates, values)
plt.show()