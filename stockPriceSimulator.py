import numpy as np
import matplotlib.pyplot as plt

# Parameters
current_price = 100  # current stock price in dollars
volatility = 0.1     # stock volatility (10%)
timeframe = 252      # number of trading days in a year
simulations = 10   # number of simulations

# Simulating stock prices
np.random.seed(0)  # for reproducible results
price_paths = np.zeros((timeframe, simulations))
price_paths[0] = current_price

for t in range(1, timeframe):
    random_shocks = np.random.normal(loc=0, scale=volatility, size=simulations)
    price_paths[t] = price_paths[t - 1] * np.exp(random_shocks)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(price_paths)
plt.title("Simulated Stock Price Paths")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.show()
