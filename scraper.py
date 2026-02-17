import requests
from bs4 import BeautifulSoup
import os
import re


def _parse_price(raw_text: str) -> float | None:
    """
    Parse common international price formats.

    Examples:
    - "$1,299.99" -> 1299.99
    - "EUR 1.299,99" -> 1299.99
    - "199,99" -> 199.99
    """
    cleaned = re.sub(r"[^\d,.\-]", "", raw_text)
    if not cleaned:
        return None

    has_comma = "," in cleaned
    has_dot = "." in cleaned

    if has_comma and has_dot:
        # Use the last separator as decimal marker and remove the other.
        if cleaned.rfind(",") > cleaned.rfind("."):
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
    elif has_comma and not has_dot:
        # If there is a single comma and exactly 2 digits after it, treat it as decimal.
        parts = cleaned.split(",")
        if len(parts) == 2 and len(parts[1]) in {2, 3}:
            cleaned = ".".join(parts)
        else:
            cleaned = cleaned.replace(",", "")

    try:
        return float(cleaned)
    except ValueError:
        return None


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
    parsed_price = _parse_price(raw_text)
    if parsed_price is None:
        print(f"[WARN] Could not parse price from text '{raw_text}' on {url}")
        return None
    return parsed_price
