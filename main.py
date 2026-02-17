import argparse
import csv
import os
import time
from dataclasses import dataclass

import yaml
from dotenv import load_dotenv

from notifier import send_telegram_message
from scraper import fetch_current_price, parse_price_text

TRUTHY_VALUES = {"1", "true", "yes", "y", "on"}


@dataclass(slots=True)
class Product:
    name: str
    url: str
    target_price: float
    currency: str = "USD"
    selector: str = "span.price"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Track product prices and notify when targets are reached."
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to YAML config file (default: config.yaml).",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run only one check cycle and exit.",
    )
    return parser.parse_args()


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}
    if not isinstance(config, dict):
        raise ValueError(f"Invalid config format in {path}: expected a YAML object.")
    return config


def parse_bool(value: str | bool | None, *, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    return str(value).strip().lower() in TRUTHY_VALUES


def load_products(csv_path: str, default_currency: str = "USD") -> list[Product]:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    products: list[Product] = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for line_number, row in enumerate(reader, start=2):
            if not parse_bool(row.get("enabled", "true"), default=True):
                continue

            name = (row.get("name") or "").strip()
            url = (row.get("url") or "").strip()
            target_raw = (row.get("target_price") or "").strip()
            currency = (row.get("currency") or default_currency).strip() or default_currency
            selector = (row.get("selector") or "span.price").strip() or "span.price"

            if not name or not url or not target_raw:
                print(
                    f"[WARN] Skipping CSV line {line_number}: "
                    "missing name/url/target_price."
                )
                continue

            target_price = parse_price_text(target_raw)
            if target_price is None:
                print(
                    f"[WARN] Skipping CSV line {line_number}: "
                    f"invalid target price '{target_raw}'."
                )
                continue

            products.append(
                Product(
                    name=name,
                    url=url,
                    target_price=target_price,
                    currency=currency.upper(),
                    selector=selector,
                )
            )
    return products


def build_alert_message(product: Product, current_price: float) -> str:
    return (
        "Price target reached.\n\n"
        f"Product: {product.name}\n"
        f"URL: {product.url}\n"
        f"Current price: {current_price:.2f} {product.currency}\n"
        f"Target price: {product.target_price:.2f} {product.currency}\n\n"
        "Suggestion: validate shipping and seller reputation before purchase."
    )


def check_prices_once(config: dict) -> None:
    data_source = config.get("data_source", {})
    csv_path = data_source.get("path", "urls.example.csv")
    default_currency = str(config.get("currency", "USD")).upper()
    products = load_products(csv_path, default_currency=default_currency)

    notifications = config.get("notifications", {})
    telegram_enabled = parse_bool(
        notifications.get("telegram", {}).get("enabled", True),
        default=True,
    )

    if not products:
        print("[WARN] No active products found in the CSV list.")
        return

    for product in products:
        current_price = fetch_current_price(product.url, selector=product.selector)
        if current_price is None:
            print(f"[WARN] Could not get price for: {product.name}")
            continue

        print(
            f"[INFO] {product.name}: "
            f"current={current_price:.2f} {product.currency} | "
            f"target={product.target_price:.2f} {product.currency}"
        )

        if current_price <= product.target_price:
            message = build_alert_message(product, current_price)
            if telegram_enabled:
                delivered = send_telegram_message(message)
                status = "sent" if delivered else "failed"
                print(f"[INFO] Alert {status} for: {product.name}")
            else:
                print(f"[INFO] Alert matched (Telegram disabled): {product.name}")


def main() -> None:
    load_dotenv()
    args = parse_args()
    config_path = args.config

    if not os.path.exists(config_path):
        if config_path == "config.yaml" and os.path.exists("config.example.yaml"):
            print("[WARN] config.yaml not found. Falling back to config.example.yaml.")
            config_path = "config.example.yaml"
        else:
            raise FileNotFoundError(f"Config file not found: {config_path}")

    config = load_config(config_path)
    interval_minutes = int(config.get("check_interval_minutes", 60))
    if interval_minutes <= 0:
        print("[WARN] Invalid interval in config. Using 60 minutes.")
        interval_minutes = 60

    print("[INFO] Starting price tracker bot...")
    print(f"[INFO] Config file: {config_path}")

    if args.once:
        check_prices_once(config)
        return

    print(f"[INFO] Check interval: {interval_minutes} minutes")
    try:
        while True:
            check_prices_once(config)
            print(f"[INFO] Sleeping for {interval_minutes} minutes...")
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\n[INFO] Shutdown requested by user.")


if __name__ == "__main__":
    main()
