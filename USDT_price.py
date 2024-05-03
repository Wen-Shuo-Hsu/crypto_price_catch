import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_usdt_price():
    # CoinGecko API for USDT price
    url = "https://api.coingecko.com/api/v3/coins/tether/market_chart?vs_currency=usd&days=365"

    # Get data from API
    response = requests.get(url)
    data = response.json()

    # Convert to DataFrame
    prices = [item[1] for item in data['prices']]
    timestamps = [item[0] for item in data['prices']]
    df = pd.DataFrame(prices, columns=['price'], index=pd.to_datetime(timestamps, unit='ms'))

    return df

# Get USDT price data
df = get_usdt_price()

# Descriptive statistics
print(df['price'].describe())

# Calculate rolling mean and standard deviation
df['rolling_mean'] = df['price'].rolling(window=7).mean()
df['rolling_std'] = df['price'].rolling(window=7).std()

# Plot original price, rolling mean and standard deviation
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(df.index, df['price'], label='USDT price')
ax.plot(df.index, df['rolling_mean'], label='7-day rolling mean')
ax.plot(df.index, df['rolling_std'], label='7-day rolling standard deviation')

# Set x-axis to show months
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))

plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.title('USDT Price Over the Past Year')
plt.legend()

# Show plot
plt.show()