import time
import yaml
from dotenv import load_dotenv

from scraper import fetch_current_price
from notifier import send_telegram_message
import csv
import os
import shutil


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_products(csv_path: str):
    products = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert CSV "enabled" field from string to bool
            enabled = str(row.get("enabled", "true")).lower() == "true"
            if not enabled:
                continue
            products.append(
                {
                    "name": row["name"],
                    "url": row["url"],
                    "target_price": float(row["target_price"]),
                    "currency": row.get("currency", "USD"),
                }
            )
    return products


def check_prices_once(config: dict):
    products = load_products(config["data_source"]["path"])

    for product in products:
        current_price = fetch_current_price(product["url"])
        if current_price is None:
            print(f"[WARN] Could not get price for: {product['name']}")
            continue

        print(
            f"[INFO] {product['name']}: current={current_price} "
            f"target={product['target_price']}"
        )

        if current_price <= product["target_price"]:
            message = (
                f"Price alert!\n\n"
                f"Product: {product['name']}\n"
                f"URL: {product['url']}\n"
                f"Current price: {current_price} {product['currency']}\n"
                f"Target price: {product['target_price']} {product['currency']}"
            )
            send_telegram_message(message)


def main():
    load_dotenv()

    config = load_config("config.yaml")
    interval = config.get("check_interval_minutes", 60)

    print("[INFO] Starting price tracker bot...")
    print(f"[INFO] Check interval: {interval} minutes")

    while True:
        check_prices_once(config)
        print(f"[INFO] Sleeping for {interval} minutes...")
        time.sleep(interval * 60)


if __name__ == "__main__":
    if not os.path.exists("config.yaml"):
        if os.path.exists("config.example.yaml"):
            shutil.copyfile("config.example.yaml", "config.yaml")
            print("[INFO] config.yaml created from config.example.yaml.")
        else:
            raise FileNotFoundError(
                "config.yaml not found and config.example.yaml is missing."
            )
    main()
