import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
TARGETS_PATH = BASE_DIR / "data" / "targets.csv"


def parse_enabled(value: str) -> bool:
    return str(value).strip().lower() == "true"


def load_targets() -> list[dict]:
    targets = []
    with TARGETS_PATH.open("r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if not parse_enabled(row.get("enabled", "true")):
                continue
            targets.append(
                {
                    "name": row["name"],
                    "url": row["url"],
                    "target_price": float(row["target_price"]),
                    "currency": row.get("currency", "USD"),
                }
            )
    return targets


def fetch_price(url: str) -> float | None:
    html = ""
    if url.startswith("http"):
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            html = response.text
        except Exception:
            return None
    else:
        local_path = Path(url)
        if not local_path.is_absolute():
            local_path = BASE_DIR / "data" / local_path
        if not local_path.exists():
            return None
        html = local_path.read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "html.parser")
    price_node = soup.find("span", class_="price")
    if not price_node:
        return None

    cleaned = (
        price_node.get_text(strip=True)
        .replace("US$", "")
        .replace("$", "")
        .replace("€", "")
        .replace("£", "")
        .replace(",", "")
    )
    try:
        return float(cleaned)
    except ValueError:
        return None


def run_check_once() -> list[dict]:
    alerts = []
    for target in load_targets():
        current_price = fetch_price(target["url"])
        if current_price is None:
            continue
        if current_price <= target["target_price"]:
            alerts.append(
                {
                    "name": target["name"],
                    "url": target["url"],
                    "current_price": current_price,
                    "target_price": target["target_price"],
                    "currency": target["currency"],
                }
            )
    return alerts


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/check-once")
def check_once():
    alerts = run_check_once()
    return jsonify({"alerts_count": len(alerts), "alerts": alerts})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
