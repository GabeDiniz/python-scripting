from crypto_data import get_coins, Coin

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
  for coin in coins_list:
    if coin.symbol == symbol:
      if coin.current_price > top:
        print(coin, "!!! Price is HIGH !!!")
      elif coin.current_price < bottom:
        print(coin, "!!! Price is LOW !!!")
      else: 
        print(coin)

if __name__ == "__main__":
  coins: list[Coin] = get_coins()

  alert("btc", bottom=30000, top=49955.78, coins_list=coins)
  alert("eth", bottom=3000, top=3405.34, coins_list=coins)

