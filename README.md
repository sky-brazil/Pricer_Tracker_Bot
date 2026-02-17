# E-commerce Price Tracker Bot (Upwork-Ready)

Production-style Python bot to monitor product prices and send alerts when a target value is reached.

This repository is positioned as a **client-ready automation project** for international freelance work (Upwork, direct contracts, agency projects).

## Business use cases

- Competitor price monitoring
- MAP policy checks
- Promo campaign tracking
- High-value product watchlists
- Internal procurement alerts

## Core features

- Reads products from CSV (`name`, `url`, `target_price`, `currency`, `enabled`)
- Supports both HTTP URLs and local HTML files (for testing/demo)
- Parses common international price formats (`1,299.99`, `1.299,99`, etc.)
- Sends Telegram alerts when `current_price <= target_price`
- Includes `--run-once` mode for cron jobs, QA, and demos
- Uses environment variables for secrets

## Tech stack

- Python 3
- `requests`
- `beautifulsoup4`
- `PyYAML`
- `python-dotenv`

## Project structure

- `main.py` - orchestration, configuration loading, CSV processing, alert logic
- `scraper.py` - page fetch + price extraction/parsing
- `notifier.py` - Telegram sender
- `config.yaml` - active runtime configuration
- `config.example.yaml` - starter configuration template
- `urls.example.csv` - sample product list
- `.env.example` - starter environment variable template

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
cp config.example.yaml config.yaml
```

Update `.env`:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

Update `urls.example.csv` (or point to your own file in `config.yaml`):

```csv
name,url,target_price,currency,enabled
"Local Test Product","test_product.html",250.00,"USD",true
```

Run once (recommended for testing):

```bash
python main.py --run-once
```

Run continuously:

```bash
python main.py
```

## Configuration

`config.yaml`:

```yaml
check_interval_minutes: 60
currency: "USD"
data_source:
  type: "csv"
  path: "urls.example.csv"
notifications:
  telegram:
    enabled: true
```

## Notes for real client deployments

- The current selector expects `<span class="price">...</span>`.
- For live client projects, selectors and anti-bot strategy should be customized per target site.
- Add retry logic, structured logging, proxy rotation, and persistence if needed.
- Always follow each website's Terms of Service and legal requirements.

## Why this is portfolio-friendly for Upwork

- Clean modular structure
- Environment-based secret handling
- Easy to demo locally
- Ready to extend for real-world e-commerce monitoring contracts
