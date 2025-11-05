"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""

import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin  # to safely join base and relative URLs

BASE_URL = "https://books.toscrape.com/"  
START_URL = "catalogue/page-1.html"  
OUTPUT_FILE = "books_data.json"
TARGET_COUNT = 100


def scrape_current_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Could'nt fetch url\n{e}")
        return [], None

    response.encoding = "utf-8"  # ensure £ symbol and text decode correctly
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3>a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()
        books.append({"title": title, "price": price})

    next_page_link = soup.select_one("li.next>a")
    next_link = next_page_link.get("href") if next_page_link else None
    next_url = urljoin(url, next_link) if next_link else None
    return next_url, books


def main():
    collected = []
    current_url = urljoin(BASE_URL, START_URL)

    while len(collected) < TARGET_COUNT and current_url:
        print(f"Scraping {current_url}")
        next_url, books = scrape_current_page(current_url)
        collected.extend(books)
        current_url = next_url

    collected = collected[:TARGET_COUNT]
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2)

if __name__ == "__main__":
    main()


"""
===========================
💡 CODE SUMMARY & REASONS
===========================

1. **Imports**  
   - `requests`: To send HTTP GET requests and fetch HTML pages.  
   - `BeautifulSoup`: To parse and extract data (title, price) from HTML easily.  
   - `json`: To save the scraped book data in a structured format.  
   - `urljoin`: Ensures correct URL formation when joining relative paths (like "page-2.html") with the base site URL.

2. **Constants**  
   - `BASE_URL`: Common prefix for all pages of the site.  
   - `START_URL`: The entry page to begin scraping.  
   - `TARGET_COUNT`: Total number of books to collect (acts as a stopping condition).  
   - `OUTPUT_FILE`: Destination JSON file for saving scraped data.

3. **scrape_current_page(url)**  
   - Sends a GET request to the page with a timeout to avoid hanging.  
   - Handles errors using `try-except` → prevents crashes if a page fails.  
   - Parses the HTML with BeautifulSoup to find all `article.product_pod` blocks (each representing one book).  
   - Extracts:
       • `title` from the `<h3><a title="">` attribute.  
       • `price` from `<p class="price_color">`.  
   - Looks for the "Next" page link using `li.next > a`.  
   - Builds an absolute URL for the next page with `urljoin()` for safe navigation.  
   - Returns a tuple: `(next_page_url, books_list)`.

4. **main() loop**  
   - Starts scraping from the first page (`START_URL`).  
   - While fewer than `TARGET_COUNT` books are collected and a next page exists:  
       • Scrape the current page.  
       • Append its books to the global list.  
       • Move to the next page (`current_url = next_url`).  
   - Truncates extra entries to ensure exactly 100 books.  
   - Saves the results as a prettified JSON file using `json.dump()`.

5. **Why JSON?**  
   - JSON is structured, human-readable, and easily reusable for data analysis or import into pandas later.

6. **Why urljoin()?**  
   - The site provides relative URLs like `"page-2.html"`.  
   - `urljoin()` merges it safely with the base domain so no broken URLs occur.

7. **Why UTF-8 Encoding?**  
   - Ensures special symbols like "£" display correctly instead of "Â£".

8. **Error Handling & Progress Tracking**  
   - Gracefully skips pages on failure without terminating.  
   - Prints progress for user visibility (“Scraping page …”).

Result → A robust, paginated web scraper that collects up to 100 books with title & price 
and saves them neatly into `books_data.json`.
"""
