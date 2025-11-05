"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""

import csv
import requests
import os
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"


def fetch_top_posts():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Network error!\n{e}")
        return []  # ✅ prevent further code from running if failed

    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")  # select all anchor tags inside span.titleline

    posts = []
    for link in post_links[:20]:  # top 20 posts
        title = link.text.strip()
        url = link.get("href").strip()
        posts.append({"title": title, "url": url})
    return posts


def save_to_csv(posts):
    if not posts:
        print("Nothing to save...")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)

    print(f"✅ Saved Hacker News to {CSV_FILE}")


def main():
    print("Scraping the HN portal....")
    posts = fetch_top_posts()
    print(f"Collected all data...now saving it in {CSV_FILE}")
    save_to_csv(posts)
    print(f"Saved to {CSV_FILE}")


if __name__ == "__main__":
    main()


"""
===========================
💡 CODE SUMMARY & REASONS
===========================

1. **Imports**
   - `requests`: Sends an HTTP request to fetch Hacker News HTML.
   - `BeautifulSoup`: Parses the HTML and extracts specific elements.
   - `csv`: Writes structured data (title, URL) into a CSV file.
   - `os`: Not directly used here, but can help in managing file paths (optional).

2. **Global Constants**
   - `HN_URL`: Base URL of Hacker News homepage.
   - `CSV_FILE`: Name of the output file where data will be stored.

3. **fetch_top_posts()**
   - Sends a GET request to Hacker News and raises an exception if the request fails.
   - Wrapped in a `try-except` block to handle network errors gracefully and prevent crashes.
   - Uses `BeautifulSoup` to parse HTML with the `"html.parser"` engine.
   - The CSS selector `"span.titleline > a"` targets the main news post links.
   - Extracts:
       • **title** – the text inside the link  
       • **url** – the hyperlink from the `href` attribute
   - Collects the first 20 posts (top stories only) into a list of dictionaries:
     ```python
     [{"title": "Post 1", "url": "https://..."}, ...]
     ```
   - Returns the list for saving.

4. **save_to_csv(posts)**
   - Verifies the list isn’t empty to avoid writing blank files.
   - Opens a CSV file with UTF-8 encoding and newline control.
   - Uses `csv.DictWriter` for clean column-based writing.
   - Writes:
       • A header row → `["title", "url"]`  
       • Each dictionary as one CSV row.
   - Prints a confirmation when saved successfully.

5. **main()**
   - Acts as the driver function.
   - Calls `fetch_top_posts()` to scrape data.
   - Passes the collected list to `save_to_csv()`.
   - Prints progress updates for better user feedback.

6. **Error Handling**
   - `try-except` prevents runtime errors due to bad responses or connection timeouts.
   - Returns an empty list if a network issue occurs → keeps the program stable.

7. **Why CSV Format?**
   - Easy to open in Excel, Google Sheets, or pandas.
   - Each row represents one post, ensuring a clear, tabular structure.

8. **Program Flow Summary**
"""