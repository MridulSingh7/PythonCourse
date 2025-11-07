from datetime import datetime
import os
import requests
import csv
import matplotlib.pyplot as plt


API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False
}

CSV_FILE = "crypto_prices.csv"


def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    response.raise_for_status()
    return response.json()


def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin["current_price"]])


def plot_graph(coin_id):
    times = []
    prices = []
    with open(CSV_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row["timestamp"])
                prices.append(float(row["price"]))
    if not times:
        print(f"No data found for this coin - {coin_id}")
        return
    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o', linestyle='-', linewidth=2)
    plt.title(f"{coin_id.upper()} Price History")
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def main():
    print("Fetching live crypto data....")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)
    print("-" * 40)
    print("Top 10 Cryptocurrency Prices (USD):")
    print("-" * 40)
    for coin in crypto_data:
        print(f"{coin['id']}: ${coin['current_price']}")
    print("-" * 40)
    choice = input("Enter the coin name to plot graph (e.g. bitcoin): ").strip().lower()
    if choice:
        plot_graph(choice)


if __name__ == "__main__":
    main()












"""
-------------------------------
📘 DAY 7 - CRYPTO PRICE TRACKER
-------------------------------

🔹 Objective:
Fetch live cryptocurrency prices from CoinGecko API, store them in a CSV file,
and visualize the price history of any selected coin.

🔹 Key Concepts Covered:
1. API requests using the `requests` library
2. CSV file handling and appending new data
3. Basic data visualization using `matplotlib`
4. Timestamping and logging fetched data
5. Simple user interaction for plotting selected coin data

🔹 Function Overview:
- fetch_crypto_data():
    Fetches top 10 coins by market cap from CoinGecko API in USD.
- save_to_csv(data):
    Appends fetched coin prices to a CSV file with a timestamp.
- plot_graph(coin_id):
    Reads the CSV and plots the price history for the chosen coin.
- main():
    Orchestrates fetching, saving, displaying, and plotting.

🔹 Example Usage:
$ python 07_day_7.py  
Fetching live crypto data....  
Top 10 Cryptocurrency Prices (USD):  
bitcoin: $71345  
ethereum: $3645  
Enter the coin name to plot graph (e.g. bitcoin): bitcoin  
→ Displays a line chart of Bitcoin price history

"""
