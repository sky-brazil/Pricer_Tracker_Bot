# Price Monitoring API (Python + Flask)

Portuguese version: [README.pt-BR.md](./README.pt-BR.md)

## Business problem

E-commerce operators and resellers need fast visibility of competitor prices, but manual checks are slow and unreliable.

## Solution

This project exposes a simple API to monitor product prices against target thresholds.

### Endpoints

- `GET /health` -> service status
- `POST /check-once` -> runs one monitoring cycle and returns matched alerts

## Why this is attractive on Upwork

- API-first delivery is easy to integrate with existing client systems.
- Clear path from MVP to production (DB, scheduler, auth, webhooks).
- Directly relevant for competitor monitoring and repricing workflows.

## Tech stack

- Python 3
- Flask
- requests
- beautifulsoup4

## Run

```bash
cd portfolio-projects/02-price-monitoring-api
pip install -r requirements.txt
python src/app.py
```

Then test:

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/check-once
```

## Suggested fixed-price packages

- Basic: one-site scraper + single alert channel.
- Standard: multi-site monitoring + API endpoint.
- Premium: API + dashboard + scheduled checks + deployment.
