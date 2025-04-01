import pandas as pd
import requests
import time

def fetch_binance_data(symbol="BTCUSDT", interval="15m", days=30):
    base_url = "https://api.binance.com/api/v3/klines"
    end_time = int(time.time() * 1000)  # Adjust parameters to get data accoording to your need.
    start_time = end_time - (days * 24 * 60 * 60 * 1000)  # 1 year back

    all_data = []
    limit = 1000  # Binance API max limit per request is 1000 so using loop 

    while start_time < end_time:
        url = f"{base_url}?symbol={symbol}&interval={interval}&limit={limit}&startTime={start_time}"
        response = requests.get(url)
        data = response.json()

        if not data:
            break  # If No more data available

        all_data.extend(data)
        start_time = data[-1][0] + 1  # Move to the next batch

        print(f"Fetched {len(all_data)} records so far...")

    df = pd.DataFrame(all_data, columns=[
        "timestamp", "open", "high", "low", "close", "volume", "close_time",
        "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume", "ignore"
    ])

    df = df[["timestamp", "open", "high", "low", "close", "volume"]]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df[["open", "high", "low", "close","volume"]] = df[["open", "high", "low", "close","volume"]].astype(float)

    filename = f"{symbol}_{interval}_{days}.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved as {filename}")

    return df

# Fetch any ticker data at your desired time-frame and duration.
df = fetch_binance_data(symbol="BTCUSDT", interval="1h", days=365)
