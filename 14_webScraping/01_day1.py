"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    headers = { #define the headers to avoid forbidden warning
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/130.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10) #using the request, get all response
        response.raise_for_status() #to check html status
    except requests.RequestException as e:
        print(f"failed to fetch the page \n {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser") #use response.text, and html.parser not html-parser
    h2_tags = soup.find_all("h2") #method to find_all ocurrences of something

    headers_list = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True).replace("[edit]", "")
        if header_text.lower() != "contents":
            headers_list.append(header_text)

    print(f"Total headers found: {len(headers_list)}\n")
    print("First 10 headers:\n", headers_list[:10])
    print(f"all headers : \n{headers_list}")

get_h2_headers(URL)
