import os
import csv
from datetime import datetime
import requests
import schedule
import time
import sqlite3

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

DB_NAME = 'crypto.db'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   coin TEXT,
                   price REAL
                   )
''')
    conn.commit()
    conn.close()

def save_to_database(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data:
        cursor.execute('''
            INSERT INTO crypto_prices (timestamp, coin, price)
                       VALUES (?, ?, ?)
''', (timestamp, coin['id'], coin['current_price']))
        
    conn.commit()
    conn.close()
    print("Price saved to database")

def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, price FROM crypto_prices
                   WHERE coin = ?
                   ORDER BY timestamp DESC
                   LIMIT 1
''', (coin_name, ))
    result = cursor.fetchone()
    conn.close()
    # print("RESULT RAW", result)
    if result:
        print(f"${result[1]} - {result[0]}")
    

def main():
    create_table()
    print("1. Fetch and store crypto data")
    print("2. Search latest price for a coin")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        data = fetch_crypto_data()
        save_to_database(data)
    elif choice == "2":
        coin_name = input("Enter coin name: ").strip().lower()
        search_coin(coin_name)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()









"""
-------------------------------
📘 DAY 8 - SQLITE INTEGRATION (Built on Day 7)
-------------------------------

WHAT CHANGED FROM DAY 7:
1) Storage Layer: Moved from CSV to SQLite.
   - Day 7 wrote rows to 'crypto_prices.csv'.
   - Day 8 writes rows into a local database 'crypto.db' (table: crypto_prices).
   - Benefit: Faster queries, structured data, easy filtering/aggregation, and no CSV parsing.

2) Data Access Pattern: Introduced SQL queries with sqlite3 cursor.
   - INSERT rows for each coin on every fetch.
   - SELECT the latest price for a given coin using ORDER BY + LIMIT 1.
   - Benefit: O(1) latest lookup without scanning entire files.

3) Time Format: Using ISO-like "%Y-%m-%d %H:%M:%S".
   - Benefit: Timestamps sort correctly as TEXT in SQLite (lexicographical order matches chronological).

-------------------------------------------------
HOW sqlite3 / CURSOR IS USED (Step by Step)
-------------------------------------------------
• sqlite3.connect(DB_NAME)
  - Opens (or creates) the SQLite database file 'crypto.db' and returns a connection object.

• conn.cursor()
  - Creates a cursor object used to execute SQL statements and fetch results.

• cursor.execute(SQL, params)
  - Runs a parameterized SQL statement. Using placeholders (?) prevents SQL injection and handles typing.

• conn.commit()
  - Persists changes (INSERT/UPDATE/DELETE) to disk. Required after write operations.

• cursor.fetchone() / cursor.fetchall()
  - Retrieves one or all rows from the result set after a SELECT.

• conn.close()
  - Closes the connection and releases file locks/resources.

---------------------------------
EVERY QUERY EXPLAINED IN PLAIN ENGLISH
---------------------------------
1) Table creation (run once per app start):
   '''
   CREATE TABLE IF NOT EXISTS crypto_prices (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       timestamp TEXT,
       coin TEXT,
       price REAL
   )
   '''
   - Creates a table to store historical prices.
   - id: unique row id, auto-incremented by SQLite.
   - timestamp: human-readable time WHEN the price was recorded.
   - coin: coin identifier from API (e.g., 'bitcoin', 'ethereum').
   - price: numeric USD price at that timestamp.
   - IF NOT EXISTS ensures re-running does not error if table already exists.

2) Insert price rows (called for each fetch):
   '''
   INSERT INTO crypto_prices (timestamp, coin, price)
   VALUES (?, ?, ?)
   '''
   - Adds a new row per coin with the current timestamp and price.
   - (?, ?, ?) are placeholders bound to actual Python values (timestamp, coin['id'], coin['current_price']).

3) Fetch latest price for a given coin:
   '''
   SELECT timestamp, price
   FROM crypto_prices
   WHERE coin = ?
   ORDER BY timestamp DESC
   LIMIT 1
   '''
   - Filters rows to the selected coin.
   - Orders by timestamp descending so the newest record is first.
   - LIMIT 1 returns only the latest row.
   - Works because timestamps are stored in a sortable ISO-like format.

---------------------------------
PROGRAM FLOW (WHAT HAPPENS WHEN YOU RUN IT)
---------------------------------
1) create_table() ensures the database and table exist.
2) You choose:
   - Option 1: Fetches live prices from CoinGecko and INSERTs all 10 coins into the DB.
   - Option 2: Prompts for a coin name and SELECTs the latest price for that coin.
3) The app prints either "Prices saved to database" or the latest price for that coin.

---------------------------------
EXTENDING WITH SCHEDULING (FROM DAY 7 IDEA)
---------------------------------
• To log prices automatically (e.g., every 10 minutes), add:
   schedule.every(10).minutes.do(lambda: save_to_database(fetch_crypto_data()))
   while True:
       schedule.run_pending()
       time.sleep(1)

• Benefit: Builds a time series automatically; later you can graph or analyze directly from SQL.

---------------------------------
TIPS / BEST PRACTICES
---------------------------------
• Keep timestamps in "%Y-%m-%d %H:%M:%S" so TEXT sorting matches chronological order.
• Always use parameterized queries (VALUES (?, ?, ?)) to avoid SQL injection and typing issues.
• Add indexes for faster queries if the table grows large:
   CREATE INDEX IF NOT EXISTS idx_coin_time ON crypto_prices (coin, timestamp);

• Common query patterns you can add:
   - Last N points for a coin:
     SELECT timestamp, price FROM crypto_prices
     WHERE coin = ? ORDER BY timestamp DESC LIMIT 100;

   - Daily average price:
     SELECT substr(timestamp, 1, 10) AS day, AVG(price)
     FROM crypto_prices
     WHERE coin = ?
     GROUP BY day ORDER BY day;

---------------------------------
WHAT YOU GAINED
---------------------------------
• Durable, queryable storage (SQLite) instead of flat files.
• Instant latest-price lookups and powerful analytics via SQL.
• Easy path to dashboards and scheduled collectors.
"""