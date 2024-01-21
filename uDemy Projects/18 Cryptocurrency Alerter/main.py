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