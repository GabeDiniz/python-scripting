import requests   # pip install requests
from dataclasses import dataclass
from typing import Final

BASE_URL: Final[str] = "https://api.coingecko.com/api/v3/coins/markets"

# Keeps track of Crypto currencies. This script tells you when a crypto currency 
#   has reached your specified price point. 

@dataclass
class Coin:
  name: str
  symbol: str
  current_price: float
  high_24h: float
  low_24h: float
  price_change_24h: float
  price_change_percentage_24h: float

  def __str__(self):
    return f"{self.name} ({self.symbol}): ${self.current_price:,}"
  
def get_coins() -> list[Coin]:
  payload: dict = {"vs_currency": "cad", "order": "market_cap_desc"}
  data = requests.get(BASE_URL, params=payload)
  json: dict = data.json()

  coin_list: list[Coin] = []
  for item in json:
    current_coin: Coin = Coin(name=item.get("name"),
                              symbol=item.get("symbol"),
                              current_price=item.get("current_price"),
                              high_24h=item.get("high_24h"),
                              low_24h=item.get("low_24h"),
                              price_change_24h=item.get("price_change_24h"),
                              price_change_percentage_24h=item.get("price_change_percentage_24h"))
    coin_list.append(current_coin)
  return coin_list

if __name__ == "__main__":
  coins = get_coins()
  for coin in coins:
    print(coin)