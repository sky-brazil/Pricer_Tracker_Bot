# Price Tracker Bot | Client-Ready Price Intelligence Automation

This repository presents a production-oriented automation baseline designed for
international clients who care about business outcomes, speed, and operational
reliability.

The delivery is positioned as a **commercial service**, not a generic script.
It combines implementation, portfolio framing, and communication artifacts that
support Upwork-style discovery calls and business-focused proposals.

---

## Executive business summary

Companies buy this type of solution to:

- reduce repetitive manual price checks;
- react faster to discount windows and margin opportunities;
- build reliable procurement intelligence;
- create an automation layer that can evolve into a broader decision platform.

---

## What clients receive

- Config-driven monitoring (`config.yaml`) with clear defaults;
- CSV onboarding with per-product CSS selector support;
- resilient parsing for common US/EU currency formats;
- single-run mode (`--once`) for demos, QA, and scheduled execution;
- Telegram notifications with safe runtime fallback behavior;
- practical logs for monitoring and troubleshooting.

---

## Portfolio offers (commercially differentiated)

See `portfolio/README.md` for the full index.

1. `portfolio/01_marketplace_guardian.md`
2. `portfolio/02_flash_deals_scout.md`
3. `portfolio/03_map_compliance_monitor.md`
4. `portfolio/04_procurement_negotiation_radar.md`

Each profile includes:

- specific business context;
- measurable KPI goals;
- scoped implementation path;
- realistic pricing ranges for freelance discovery conversations.

---

## Typical engagement models

| Package | Focus | Typical range |
| --- | --- | --- |
| Starter Validation | Fast setup for critical SKUs and alert proof-of-value | USD 150-350 |
| Growth Automation | Broader catalog coverage and monitoring workflow hardening | USD 400-1,000 |
| Ongoing Optimization | Continuous iteration, tuning, and stakeholder-ready reporting | USD 100-500/week |

---

## Repository structure

- `main.py` - CLI entry point, config handling, CSV loading, scheduling loop.
- `scraper.py` - HTML retrieval, selector extraction, and price parsing logic.
- `notifier.py` - Telegram transport with graceful runtime error handling.
- `tests/test_price_parser.py` - parser and product-loading regression tests.
- `config.yaml` - production-leaning baseline config.
- `config.example.yaml` - safe starter template.
- `urls.example.csv` - sample product registry.
- `portfolio/` - client-facing project positioning.
- `docs/` - profile-ready communication assets for international clients.

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

### 3) Review configuration

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

### 5) Validate with a single cycle

```bash
python main.py --once
```

### 6) Run continuously

```bash
python main.py
```

### 7) Run test suite

```bash
python -m unittest discover -s tests -p "test_*.py"
```

---

## Quality and professionalism signals

- English-only documentation curated for international audiences;
- business narrative aligned with buyer priorities;
- test coverage for core parsing and CSV ingestion flows;
- CI-ready workflow for baseline validation;
- explicit portfolio segmentation to avoid "one-size-fits-all" positioning.

---

## Recommended premium upgrades

- alert de-duplication memory;
- scheduled stakeholder reports;
- dashboard exports (Google Sheets / BI);
- anti-block strategy for larger crawling scale.
