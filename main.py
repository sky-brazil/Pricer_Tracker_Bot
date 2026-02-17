import argparse
import csv
import os
import time
from typing import Any

import yaml
from dotenv import load_dotenv

from notifier import send_telegram_message
from scraper import fetch_current_price


def load_config(path: str = "config.yaml") -> dict[str, Any]:
    config_path = path

    if not os.path.exists(config_path):
        fallback_path = "config.example.yaml"
        if os.path.exists(fallback_path):
            print(f"[WARN] '{config_path}' not found. Using '{fallback_path}'.")
            config_path = fallback_path
        else:
            raise FileNotFoundError(
                f"Configuration file '{config_path}' was not found. "
                "Create it from 'config.example.yaml'."
            )

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def parse_bool(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def load_products(csv_path: str, default_currency: str = "USD") -> list[dict[str, Any]]:
    products: list[dict[str, Any]] = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required_columns = {"name", "url", "target_price"}
        missing_columns = required_columns - set(reader.fieldnames or [])
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(
                f"CSV file '{csv_path}' is missing required columns: {missing}"
            )

        for line_number, row in enumerate(reader, start=2):
            if not parse_bool(row.get("enabled", "true")):
                continue

            name = (row.get("name") or "").strip()
            url = (row.get("url") or "").strip()
            target_price_raw = (row.get("target_price") or "").strip()

            if not name or not url or not target_price_raw:
                print(
                    f"[WARN] Skipping row {line_number}: missing name, url, or target_price."
                )
                continue

            try:
                target_price = float(target_price_raw)
            except ValueError:
                print(
                    f"[WARN] Skipping row {line_number}: invalid target_price "
                    f"'{target_price_raw}'."
                )
                continue

            currency = (row.get("currency") or default_currency).strip().upper()
            products.append(
                {
                    "name": name,
                    "url": url,
                    "target_price": target_price,
                    "currency": currency,
                }
            )

    return products


def check_prices_once(config: dict[str, Any]) -> None:
    data_source = config.get("data_source", {})
    csv_path = data_source.get("path", "urls.example.csv")
    default_currency = str(config.get("currency", "USD")).upper()
    telegram_enabled = bool(
        config.get("notifications", {}).get("telegram", {}).get("enabled", False)
    )

    products = load_products(csv_path, default_currency=default_currency)
    if not products:
        print("[WARN] No enabled products found in the CSV file.")
        return

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
                "Price alert!\n\n"
                f"Product: {product['name']}\n"
                f"URL: {product['url']}\n"
                f"Current price: {current_price} {product['currency']}\n"
                f"Target price: {product['target_price']} {product['currency']}"
            )
            if telegram_enabled:
                delivered = send_telegram_message(message)
                if delivered:
                    print(f"[INFO] Alert sent for: {product['name']}")
            else:
                print(f"[INFO] Alert triggered for {product['name']} (Telegram disabled).")


def main(run_once: bool = False) -> None:
    load_dotenv()
    config = load_config("config.yaml")
    interval = int(config.get("check_interval_minutes", 60))
    if interval <= 0:
        raise ValueError("check_interval_minutes must be a positive number.")

    print("[INFO] Starting price tracker bot...")
    print(f"[INFO] Check interval: {interval} minutes")

    try:
        while True:
            check_prices_once(config)
            if run_once:
                print("[INFO] Run completed (run-once mode).")
                break
            print(f"[INFO] Sleeping for {interval} minutes...")
            time.sleep(interval * 60)
    except KeyboardInterrupt:
        print("\n[INFO] Price tracker interrupted by user.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Price tracker bot for e-commerce.")
    parser.add_argument(
        "--run-once",
        action="store_true",
        help="Run a single price check cycle and exit.",
    )
    args = parser.parse_args()
    main(run_once=args.run_once)
