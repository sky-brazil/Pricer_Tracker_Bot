import requests
from bs4 import BeautifulSoup
import os
import re


def parse_price_text(raw_text: str) -> float | None:
    """
    Parse price text in common formats:
    - "$1,299.99"
    - "US$ 1.299,99"
    - "1299.99"
    """
    text = (
        raw_text.replace("US$", "")
        .replace("$", "")
        .replace("€", "")
        .replace("£", "")
        .replace("R$", "")
    )
    text = re.sub(r"\s+", "", text)
    text = re.sub(r"[^0-9,.\-]", "", text)

    if not text:
        return None

    # If both separators exist, assume the last one is decimal.
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        if text.count(",") > 1:
            text = text.replace(",", "")
        else:
            integer_part, fractional_part = text.split(",", maxsplit=1)
            if len(fractional_part) == 3:
                text = integer_part + fractional_part
            else:
                text = integer_part + "." + fractional_part
    elif "." in text:
        if text.count(".") > 1:
            text = text.replace(".", "")
        else:
            integer_part, fractional_part = text.split(".", maxsplit=1)
            if len(fractional_part) == 3:
                text = integer_part + fractional_part

    try:
        return float(text)
    except ValueError:
        return None


def fetch_current_price(url: str, selector: str = "span.price") -> float | None:
    """
    Price extraction for demo purposes.

    - If `url` starts with http, tries HTTP request.
    - Otherwise, treats `url` as a local HTML file path.
    - Looks for a price element using a CSS selector.
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

    price_element = soup.select_one(selector)
    if not price_element and selector != "span.price":
        # Keeps backward compatibility for legacy samples.
        price_element = soup.select_one("span.price")
    if not price_element:
        print(f"[WARN] Could not find selector '{selector}' for: {url}")
        return None

    raw_text = price_element.get_text(strip=True)

    parsed = parse_price_text(raw_text)
    if parsed is None:
        print(f"[WARN] Could not parse price from text '{raw_text}' on {url}")
        return None
    return parsed
