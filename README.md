# Price Tracker Bot for E-commerce (USD)

Python automation to monitor e-commerce prices and send alerts when products hit a target value.

This repository is built as a practical portfolio project for freelance opportunities involving:

- web scraping;
- monitoring automations;
- alerts and notifications;
- lightweight client-ready Python tooling.

## Features

- Reads products from CSV (`name`, `url`, `target_price`, `currency`, `enabled`).
- Supports local HTML files and real HTTP URLs.
- Extracts prices from `span.price` elements.
- Compares current price against target price.
- Sends Telegram alert messages when target is reached.
- Runs continuously on a configurable interval.

## Tech stack

- Python 3
- requests
- beautifulsoup4
- pyyaml
- python-dotenv

## Project structure

```text
.
├── main.py
├── scraper.py
├── notifier.py
├── config.yaml
├── urls.example.csv
├── test_product.html
└── requirements.txt
```

## Quick start

1. Clone and enter the project:

   ```bash
   git clone https://github.com/sky-brazil/Pricer_Tracker_Bot.git
   cd Pricer_Tracker_Bot
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create local config file:

   ```bash
   cp config.example.yaml config.yaml
   ```

5. Configure environment variables:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` with:

   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`

6. Run:

   ```bash
   python main.py
   ```

## CSV format

`urls.example.csv`:

```csv
name,url,target_price,currency,enabled
"Local Test Product","test_product.html",250.00,"USD",true
```

## Configuration

`config.yaml` controls:

- check interval in minutes;
- data source path;
- default currency;
- notification channels.

## Notes for client work

For production projects, this base can be extended with:

- per-site selectors;
- retry/backoff strategy;
- proxy rotation;
- anti-bot handling;
- Docker deployment;
- persistent storage (SQLite/PostgreSQL);
- email/Slack/webhook notifications.

## License

No license file is included yet. For commercial use, add a license before distribution.
