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

  # with open("rates.json", "w") as file:
  #   return json.dump(data, file)
  
  return data

def get_currency(currency: str, rates: dict) -> float:
  currency: str = currency.upper()
  if currency in rates.keys():
    return rates.get(currency)
  else:
    raise ValueError(f'"{currency}" is not a valid currency')

def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
  base_rate: float = get_currency(base, rates)
  vs_rate: float = get_currency(vs, rates)

  conversion: float = round((vs_rate / base_rate) * amount, 2)
  print(f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})') # if number is greater than 10000 it will place a decimal -> 10,000
  return conversion


# print(get_rates(mock=True))

def main():
  data: dict = get_rates(mock=True)
  rates: dict = data.get("rates")
  print("Converting from ____ to CAD.")
  fr = input("Which currency would you like to convert from: ")
  convert_currency(1, fr, "CAD", rates=rates)

if __name__ == "__main__":
  main()