import schedule
from datetime import datetime
import os
import requests
import csv
import matplotlib.pyplot as plt
import time

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


def job():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching current crypto data...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)
    print("Data saved successfully.\n")


if __name__ == "__main__":
    # Run main once to show data and allow user interaction
    main()

    # Schedule the job every hour on the hour
    schedule.every().hour.at(":00").do(job)

    print("\n✅ Auto data collection enabled! Fetching every hour...\n(Press Ctrl+C to stop.)\n")
    while True:
        schedule.run_pending()
        time.sleep(1)





















"""
-------------------------------
📘 DAY 7 (SCHEDULED VERSION)
-------------------------------

🔹 ADDITIONS YOU MADE:
1️ Imported the `schedule` library.
   → Allows automatic execution of tasks at specific time intervals.

2️ Added a new function `job()`.
   → Fetches latest crypto data using `fetch_crypto_data()`
     and appends it to CSV automatically.
   → Runs without user input.

3️ Added scheduling logic:
   ```python
   schedule.every().hour.at(":00").do(job)
"""