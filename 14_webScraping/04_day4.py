import os
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-._ ]', '', title).replace(" ", "_")
# generate the regex eqn from regex site or chatgpt. sub(find, replace_with, the_string)
# we often come along titles which have complex namings, so to sanitize means to simplify/clear the title


def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Error\n{e}")
# filename is the name of image you want to give


def scrape_and_download_image():
    url = BASE_URL
    response = requests.get(url)  # ✅ FIXED: corrected from response.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']  # extract the title from <a> tag inside <h3>
        relative_img_url = book.find("img")["src"]  # get the relative image link
        img_url = urljoin(BASE_URL, relative_img_url)  # join base + relative path
        filename = sanitize_filename(title) + '.jpg'  # clean title for file naming
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"downloading file - {filename}...")
        download_image(img_url, filepath)
    print("Downloaded successfully.")


if __name__ == "__main__":
    scrape_and_download_image()



"""
========================= 📘 SCRIPT DOCUMENTATION GUIDE =========================

▶ OVERVIEW:
This Python script scrapes book titles and cover images from the website:
    https://books.toscrape.com/
It downloads the first 10 book cover images and saves them locally in an
"images" directory.

-------------------------------------------------------------------------------

▶ MODULES USED:
- os → For creating folders and handling file paths.
- re → For sanitizing filenames using regular expressions.
- bs4 (BeautifulSoup) → For parsing and extracting data from HTML.
- requests → For making HTTP GET requests.
- urllib.parse.urljoin → For combining base URLs and relative URLs.

-------------------------------------------------------------------------------

▶ FUNCTION 1: sanitize_filename(title)
Purpose:
    - Cleans up a book title so it can safely be used as a filename.
Process:
    - Removes special characters (anything except letters, digits, '_', '-', '.', and spaces).
    - Replaces spaces with underscores "_".
Example:
    Input:  "Harry Potter: The Philosopher’s Stone"
    Output: "Harry_Potter_The_Philosophers_Stone"

-------------------------------------------------------------------------------

▶ FUNCTION 2: download_image(img_url, filename)
Purpose:
    - Downloads an image from the given URL and saves it locally.
Steps:
    1. Sends a GET request to the image URL.
    2. Uses `stream=True` to download data in chunks (useful for large files).
    3. Checks for HTTP errors using `raise_for_status()`.
    4. Opens a file in binary write mode ('wb') and writes the downloaded data.
    5. Handles and prints any errors (like connection timeout or permission errors).

-------------------------------------------------------------------------------

▶ FUNCTION 3: scrape_and_download_image()
Purpose:
    - Scrapes the website, extracts book titles and images, and downloads them.
Steps:
    1. Sends an HTTP GET request to the base URL.
    2. Parses HTML content using BeautifulSoup.
    3. Selects all book containers using the CSS selector "article.product_pod".
    4. Takes the first 10 books for simplicity.
    5. Creates the "images" folder if it doesn’t already exist.
    6. For each book:
         - Extracts title text.
         - Finds the relative image path.
         - Joins it with the base URL using `urljoin()`.
         - Sanitizes the title to create a clean filename.
         - Downloads the image using `download_image()`.

-------------------------------------------------------------------------------

▶ MAIN EXECUTION BLOCK:
if __name__ == "__main__":
    scrape_and_download_image()

Purpose:
    - Ensures the script runs only when executed directly (not when imported).

-------------------------------------------------------------------------------

▶ OUTPUT:
- Creates a folder named "images" in the current working directory.
- Saves the first 10 book cover images as sanitized JPG filenames.
- Prints progress messages for each download.

-------------------------------------------------------------------------------

▶ COMMON ISSUES / NOTES:
- If connection fails → check your internet connection or site availability.
- If filenames look strange → check the regex pattern in `sanitize_filename`.
- `stream=True` ensures memory-efficient downloading.
- `'wb'` mode is necessary for writing binary image data.

===============================================================================
"""
