# tech-graph-recommendation
SMA-based analysis and recommendations for the selected cryptocurrency

# Crypto Market Analysis with Simple Moving Average (SMA)

This Python script performs crypto market analysis for a selected cryptocurrency based on Simple Moving Average (SMA). It fetches price data from the CoinGecko API, calculates the SMA, and generates a chart displaying the price data along with the SMA line. It also provides a recommendation (Buy, Sell, or Hold) based on the comparison of the current price with the SMA.

## Prerequisites

- Python 3.x
- `requests` library
- `matplotlib` library

## Installation

1. Clone this repository or download the `crypto_analysis.py` file.

2. Install the required libraries using pip:

   ```
   pip install requests matplotlib
   ```

## Usage

1. Open a terminal or command prompt and navigate to the directory where the `crypto_analysis.py` file is located.

2. Run the script using the following command:

   ```
   python crypto_analysis.py
   ```

3. The script will fetch the price data, plot the chart with SMA, and display the recommendation in the terminal.

4. The chart will be displayed on the screen. You can interact with the chart (zoom in/out, save as an image, etc.) based on your platform and the capabilities of your matplotlib backend.

## Customization

- To analyze a different cryptocurrency or currency pair, modify the `cryptocurrency` and `currency` variables in the script.

- You can adjust the window size for the SMA calculation by changing the `window_size` variable in the script.

## Disclaimer

- The analysis and recommendation provided by this script are based on Simple Moving Average (SMA) and should not be considered as financial advice. Always do your own research and consider multiple factors before making any investment decisions.

- The script uses the CoinGecko API to fetch price data. Please refer to CoinGecko's terms of service and API documentation for usage guidelines and any potential limitations.

---
