import requests
import matplotlib.pyplot as plt
import numpy as np

# Define the cryptocurrency and currency pair
cryptocurrency = 'cardano'
currency = 'usd'

# Fetch data from CoinGecko API
api_url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency}/market_chart'
params = {
    'vs_currency': currency,
    'days': '90',  # Data for the last 90 days
}
response = requests.get(api_url, params=params)
data = response.json()

# Extract the prices and timestamps
prices = data['prices']
timestamps = [price[0] / 1000 for price in prices]  # Convert milliseconds to seconds
price_values = [price[1] for price in prices]

# Calculate the Simple Moving Average (SMA)
window_size = 20
sma_values = np.convolve(price_values, np.ones(window_size), 'valid') / window_size
sma_timestamps = timestamps[window_size - 1:]

# Plot the chart with prices and SMA
fig, ax = plt.subplots()
ax.plot(timestamps, price_values, label='Price')
ax.plot(sma_timestamps, sma_values, label=f'{window_size}-day SMA')
ax.set_xlabel('Timestamp')
ax.set_ylabel(f'{cryptocurrency.upper()} Price ({currency.upper()})')
ax.set_title(f'{cryptocurrency.upper()} Price Chart with {window_size}-day SMA')
ax.legend()
ax.grid(True)

# Add recommendation text to the chart
current_price = price_values[-1]
current_sma = sma_values[-1]
recommendation = ''

if current_price > current_sma:
    recommendation = 'Sell'
    recommendation_color = 'red'
elif current_price < current_sma:
    recommendation = 'Buy'
    recommendation_color = 'green'
else:
    recommendation = 'Hold'
    recommendation_color = 'orange'

ax.text(
    0.5, 0.95, f'Recommendation: {recommendation} ({current_price})',
    horizontalalignment='center', verticalalignment='top',
    transform=ax.transAxes, color=recommendation_color, fontsize=12, weight='bold'
)

plt.show()