# Price Tracker Bot for E-commerce (USD)

Python bot to **monitor product prices in USD** and trigger alerts when the price drops below a target value. Designed for remote / international clients who need automated price tracking and competitor monitoring.

## What this bot does

- Reads a list of products from a CSV file (`urls.example.csv`).
- For each product, fetches the current price (from a web page or local HTML).
- Compares the current price with the configured `target_price`.
- Triggers an alert (Telegram) when the price is **below or equal** to the target.
- Allows enabling/disabling products individually via the CSV file.

In a real client project, the scraping logic can be adapted to any specific e-commerce site (Amazon, Walmart, etc.), using proper selectors, headers, and, if needed, proxy/scraping services.[web:88][web:89]

## Tech stack

- Python  
- Requests (HTTP client)[web:62]  
- BeautifulSoup (HTML parsing)[web:88]  
- PyYAML (configuration file)  
- python-dotenv (environment variables)  

## Project structure

- `main.py` – entry point; loads config, reads CSV, runs the price checks, triggers alerts.  
- `scraper.py` – contains `fetch_current_price`, responsible for extracting the price from HTML.  
- `notifier.py` – handles Telegram notifications.  
- `urls.example.csv` – example list of products to monitor (name, url, target_price, currency, enabled).  
- `config.yaml` – main configuration (interval, data source, notification settings).  
- `.env` – environment variables (Telegram bot token, chat id, email credentials if used).  
- `requirements.txt` – Python dependencies.

## How it works (short version)

1. **Configuration**  
   - `config.yaml` defines:
     - check interval in minutes,  
     - default currency (`USD`),  
     - where to read products from (CSV file),  
     - whether Telegram/email notifications are enabled.

2. **Product list (CSV)**  
   The CSV file follows this format:

   ```csv
   name,url,target_price,currency,enabled
   "Local Test Product","test_product.html",250.00,"USD",true
