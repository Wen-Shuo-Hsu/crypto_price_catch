# Enhanced USDT Price Analysis Script

This Python script retrieves historical price data of Tether (USDT) against USD from the CoinGecko API, computes descriptive statistics, and visualizes the price trend over the past year along with a 7-day rolling mean and standard deviation using matplotlib.

## Purpose

The purpose of this script is to:

- Fetch the historical price data of Tether (USDT) from the CoinGecko API and process it into a pandas DataFrame.
- Compute descriptive statistics (e.g., mean, standard deviation) of the USDT price.
- Calculate and plot a 7-day rolling mean and standard deviation to illustrate the trend and volatility of the USDT price over time.

## How it Works

1. **API Integration**: The script makes an API request to CoinGecko to obtain historical market data for Tether (USDT) against USD.
2. **Data Processing**: It extracts price data and timestamps from the API response and constructs a pandas DataFrame with timestamps as the index.
3. **Descriptive Statistics**: The script computes descriptive statistics (e.g., mean, standard deviation) of the USDT price.
4. **Rolling Metrics**: It calculates a 7-day rolling mean and standard deviation of the USDT price for trend analysis.
5. **Visualization**: Using matplotlib, the script plots the original USDT price along with the 7-day rolling mean and standard deviation to visualize the price trend and volatility over the past year.

## Dependencies

- `requests`: For making HTTP requests to the CoinGecko API.
- `pandas`: For data manipulation and DataFrame operations.
- `matplotlib`: For creating data visualizations, including line plots and time series representations.

## Usage

1. Ensure that the required libraries (`requests`, `pandas`, `matplotlib`) are installed.
2. Run the script to fetch and analyze the USDT price data.
3. View the descriptive statistics printed in the console and the plotted graph illustrating the USDT price trend, rolling mean, and standard deviation over the past year.
