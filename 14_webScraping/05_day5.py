#using the wget tool.
import os
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import wget


BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-._ ]', '', title).replace(" ", "_")


'''we dont need this custom image downloading function anymore'''
# def download_image(img_url, filename):
#     try:
#         response = requests.get(img_url, stream=True, timeout=10)
#         response.raise_for_status()
#         with open(filename, 'wb') as f:
#             for chunk in response.iter_content(1024):
#                 f.write(chunk)
#     except Exception as e:
#         print(f"Error\n{e}")
# # filename is the name of image you want to give


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
        # download_image(img_url, filepath) '''
        wget.download(img_url,filepath)
    print("Downloaded successfully.")


if __name__ == "__main__":
    scrape_and_download_image()


"""
========================= 📘 DAY 5 GUIDE — USING wget TOOL =========================

▶ OVERVIEW:
In Day 5, we replaced the custom `download_image()` function (which used
the `requests` module and manual byte writing) with the built-in
`wget` library’s simpler method: `wget.download(url, filepath)`.

This allows automatic file downloading with less code, while still saving
the image into the desired directory with a custom filename.

-------------------------------------------------------------------------------

▶ WHY SWITCH TO wget?
1. **Less boilerplate** — No need to handle streams, timeouts, or binary writes.
2. **Automatic file saving** — It saves directly to a file path you provide.
3. **Built-in progress output** — Shows a download progress bar by default.
4. **Reliable and lightweight** — Designed exactly for downloading files via HTTP/HTTPS.

-------------------------------------------------------------------------------

▶ HOW wget IS USED IN THIS SCRIPT:

    import wget

    # inside the scrape_and_download_image() loop:
    wget.download(img_url, filepath)

Explanation:
- `img_url`: The full, absolute URL of the book’s cover image.
- `filepath`: The complete destination path (including filename and extension)
              where the image will be saved, e.g.:
              "images/A_Light_in_the_Attic.jpg"

When this line executes:
1. wget sends a GET request to `img_url`.
2. It retrieves the binary image data.
3. Writes the data directly into `filepath`.
4. Displays a progress bar in the terminal while downloading.

-------------------------------------------------------------------------------

▶ COMPARISON: CUSTOM METHOD vs wget.download()

| Feature | Custom Function (requests) | wget.download() |
|----------|----------------------------|-----------------|
| Manual stream handling | Yes | No |
| Manual binary write | Yes | No |
| Timeout control | Yes | Limited |
| Progress indicator | No | Yes (built-in) |
| Simplicity | Medium | Very high |

→ Summary: `wget` is perfect for small to medium scraping tasks where you just need quick downloads without full control over stream handling.

-------------------------------------------------------------------------------

▶ EXAMPLE FLOW IN THIS SCRIPT:

1. The scraper extracts:
      - book title → used to create a safe filename
      - image src → converted to a full URL
2. `filepath` is built using the sanitized title.
3. `wget.download(img_url, filepath)` downloads and saves the image.
4. Repeat for all selected books.
5. At the end, the script prints “Downloaded successfully.”

-------------------------------------------------------------------------------

▶ NOTES:
- `wget` automatically overwrites existing files with the same name.
- You can suppress its progress bar by passing `bar=None`:
      wget.download(img_url, filepath, bar=None)
- Unlike the custom method, wget doesn’t need `stream=True` or `iter_content()`.

-------------------------------------------------------------------------------

▶ OUTPUT EXAMPLE:

downloading file - A_Light_in_the_Attic.jpg...
100% [............................................]  20.3K / 20.3K
downloading file - Tipping_the_Velvet.jpg...
100% [............................................]  18.7K / 18.7K
Downloaded successfully.

===============================================================================
"""


