# Price Tracker Bot - Professional Upwork-Style Delivery

This repository is structured as a client-ready automation project, focused on
real business outcomes: faster buying decisions, competitor visibility, and
less manual monitoring.

It is not a generic "script dump". The code, documentation, and portfolio
positioning are organized so each project can be sold as a differentiated
commercial service.

---

## Why companies pay for this

Clients on Upwork usually pay for measurable results, not code lines.
This bot helps with:

- reducing manual price checks;
- reacting faster to discounts and margin opportunities;
- protecting procurement decisions with repeatable monitoring;
- creating a baseline automation that can be expanded into full intelligence.

---

## Portfolio projects (each one has a different commercial angle)

See `portfolio/README.md` for the full index.

1. `portfolio/01_marketplace_guardian.md`
2. `portfolio/02_flash_deals_scout.md`
3. `portfolio/03_map_compliance_monitor.md`
4. `portfolio/04_procurement_negotiation_radar.md`

Each project has:
- specific business pain;
- different KPI goals;
- unique implementation scope;
- realistic budget framing for Upwork conversations.

---

## Core technical features

- Config-driven monitoring (`config.yaml`);
- CSV-based product onboarding with per-item CSS selector;
- robust price parser for multiple currency/locale formats;
- one-shot mode (`--once`) for demos, cron jobs, and QA;
- Telegram notifications with production-safe error handling;
- clear logs for operational visibility.

---

## Project structure

- `main.py`: entry point, config loading, CSV validation, run loop.
- `scraper.py`: HTML fetch + selector extraction + resilient price parsing.
- `notifier.py`: Telegram delivery with runtime safeguards.
- `config.yaml`: local production baseline.
- `config.example.yaml`: safe starter config.
- `urls.example.csv`: example product list with selector field.
- `test_product.html`: local HTML sample for quick validation.
- `portfolio/`: differentiated project proposals for client-facing use.

---

## Quick start

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Configure environment variables

Create `.env`:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### 3) Review `config.yaml`

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

### 4) Prepare product CSV

```csv
name,url,target_price,currency,selector,enabled
"Local Test Product - Electronics","test_product.html",250.00,"USD","span.price",true
"Weekend Deals - Fashion","https://example.com/fashion-item",79.90,"USD","span.price",false
```

### 5) Run once (recommended for validation)

```bash
python main.py --once
```

### 6) Run continuously

```bash
python main.py
```

---

## Human touch and differentiation (important)

To avoid "assembly line" delivery:

- each portfolio project has a different business narrative;
- alert messages include decision-oriented guidance;
- implementation can be tuned by niche (electronics, fashion, B2B procurement);
- scope is defined by business priority first, tooling second.

This keeps the work credible, client-specific, and commercially relevant.

---

## Suggested next upgrades for premium clients

- anti-duplication alert memory (avoid repeated notifications);
- dashboard export (Google Sheets / BI);
- scheduled reports for non-technical stakeholders;
- rotating proxies / anti-block strategy for large-scale crawling.
