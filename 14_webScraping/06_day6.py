import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import ImageDraw, ImageFont, Image

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"


def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quotes_data = []
    for q in quotes[:5]:
        text = q.find("span", class_="text").text.strip("“”")
        author = q.find("small", class_="author").text.strip()
        quotes_data.append((text, author))
    return quotes_data


def create_image(text, author, index):
    width, height = 1200, 800
    background_color = "#fff8e1"
    text_color = "#1f1f1f"

    
    try:
        quote_font = ImageFont.truetype("arial.ttf", 56)
        author_font = ImageFont.truetype("ariali.ttf", 40)
    except:
        quote_font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    wrapped = textwrap.fill(text, width=30)

    text_bbox = draw.multiline_textbbox((0, 0), wrapped, font=quote_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_x = width // 2
    text_y = (height - text_height) // 2 - 40

    draw.multiline_text(
        (text_x, text_y),
        wrapped,
        font=quote_font,
        fill=text_color,
        anchor="mm",
        align="center",
    )

    author_text = f"— {author}"
    draw.text(
        (text_x, text_y + text_height // 2 + 60),
        author_text,
        font=author_font,
        fill="#444444",
        anchor="mm",
    )

    border_color = "#e0c95f"
    draw.rectangle([(15, 15), (width - 15, height - 15)], outline=border_color, width=6)


    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    filename = os.path.join(OUTPUT_DIR, f"quote_{index + 1}.png")
    print("creating image...")
    image.save(filename)
    print(f"✅ Saved image — {filename}")


def main():
    quotes = fetch_quotes()
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)


if __name__ == "__main__":
    main()






"""
🗓️ DAY 6 — QUOTE IMAGE GENERATOR (Web Scraping + PIL)

📘 GOAL:
Fetch inspiring quotes from a website and turn them into beautiful, styled image posters automatically using Python.

---

🧩 CONCEPTS COVERED:
1. Web scraping using `requests` + `BeautifulSoup`
2. Data extraction and text formatting
3. Image generation using `Pillow (PIL)`
4. Text wrapping, alignment & font styling
5. File system automation

---

⚙️ SETUP INSTRUCTIONS:

1️⃣ Create a new folder:
    mkdir quote_image_generator
    cd quote_image_generator

2️⃣ (Optional) Create a virtual environment:
    python3 -m venv venv
    source venv/bin/activate      # macOS/Linux
    venv\Scripts\activate         # Windows

3️⃣ Install required packages:
    pip install requests beautifulsoup4 pillow

4️⃣ Create a new Python file:
    touch main.py

---

💻 FULL CODE:

import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import ImageDraw, ImageFont, Image

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"


def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quotes_data = []
    for q in quotes[:5]:
        text = q.find("span", class_="text").text.strip("“”")
        author = q.find("small", class_="author").text.strip()
        quotes_data.append((text, author))
    return quotes_data


def create_image(text, author, index):
    width, height = 1200, 800
    background_color = "#fff8e1"
    text_color = "#1f1f1f"

    # Load fonts (fallback to default if not found)
    try:
        quote_font = ImageFont.truetype("arial.ttf", 56)
        author_font = ImageFont.truetype("ariali.ttf", 40)
    except:
        quote_font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    # Create blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Wrap text neatly
    wrapped = textwrap.fill(text, width=30)

    # Measure text box for centering
    text_bbox = draw.multiline_textbbox((0, 0), wrapped, font=quote_font)
    text_height = text_bbox[3] - text_bbox[1]

    text_x = width // 2
    text_y = (height - text_height) // 2 - 40

    # Draw main quote text
    draw.multiline_text(
        (text_x, text_y),
        wrapped,
        font=quote_font,
        fill=text_color,
        anchor="mm",
        align="center",
    )

    # Draw author name below
    author_text = f"— {author}"
    draw.text(
        (text_x, text_y + text_height // 2 + 60),
        author_text,
        font=author_font,
        fill="#444444",
        anchor="mm",
    )

    # Add soft border
    border_color = "#e0c95f"
    draw.rectangle([(15, 15), (width - 15, height - 15)], outline=border_color, width=6)

    # Save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    filename = os.path.join(OUTPUT_DIR, f"quote_{index + 1}.png")
    image.save(filename)
    print(f"✅ Saved image — {filename}")


def main():
    quotes = fetch_quotes()
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)


if __name__ == "__main__":
    main()

---

▶️ RUNNING THE SCRIPT:

Run the file:
    python main.py

It will:
- Scrape quotes from https://quotes.toscrape.com/
- Generate styled poster images
- Save them inside the `quotes/` folder

Output Example:
    ✅ Saved image — quotes/quote_1.png
    ✅ Saved image — quotes/quote_2.png

---

🎨 CUSTOMIZATION GUIDE:

| What you want to change | How to do it |
|--------------------------|--------------|
| Increase number of quotes | Change `quotes[:5]` to `quotes[:10]` |
| Change background color | Edit `background_color = "#fff8e1"` |
| Bigger text | Increase `quote_font` size (e.g., `64`) |
| Different fonts | Replace `"arial.ttf"` with any `.ttf` file in folder |
| Instagram-style size | Change image size → `(1080, 1080)` |
| Gradient background | Use `Image.linear_gradient("L")` or custom fill |

---

💡 EXTENSIONS:
- Add pagination to scrape all quotes from all pages.
- Add random gradient backgrounds.
- Use stylish fonts (Playfair Display, Montserrat).
- Automatically generate social media posts.

---

🏁 SUMMARY:
This project combines **web scraping** and **image generation** — a creative blend of automation and design.  
It fetches live quotes and transforms them into elegant posters — perfect for social feeds or content automation.

"""
