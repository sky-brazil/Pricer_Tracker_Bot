import requests
from bs4 import BeautifulSoup
import os


def fetch_current_price(url: str) -> float | None:
    """
    Price extraction for demo purposes.

    - If `url` starts with http, tries HTTP request.
    - Otherwise, treats `url` as a local HTML file path.
    - Looks for <span class="price">$199.99</span>.
    """

    html = None

    if url.startswith("http"):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            html = resp.text
        except Exception as e:
            print(f"[ERROR] Request failed for {url}: {e}")
            return None
    else:
        # Local file mode
        if not os.path.exists(url):
            print(f"[ERROR] Local file not found: {url}")
            return None
        try:
            with open(url, "r", encoding="utf-8") as f:
                html = f.read()
        except Exception as e:
            print(f"[ERROR] Failed to read local file {url}: {e}")
            return None

    soup = BeautifulSoup(html, "html.parser")

    price_element = soup.find("span", class_="price")
    if not price_element:
        print(f"[WARN] Could not find <span class='price'> element for: {url}")
        return None

    raw_text = price_element.get_text(strip=True)

    cleaned = (
        raw_text.replace("US$", "")
        .replace("$", "")
        .replace("€", "")
        .replace("£", "")
        .replace(",", "")
    )

    try:
        return float(cleaned)
    except ValueError:
        print(f"[WARN] Could not parse price from text '{raw_text}' on {url}")
        return None
