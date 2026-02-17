# Lead Enrichment Automation (Python)

Portuguese version: [README.pt-BR.md](./README.pt-BR.md)

## Business problem

Sales teams often work with raw CSV lead lists that are inconsistent and hard to prioritize.

## Solution

This project enriches and scores leads from a simple CSV file:

- normalizes company names;
- extracts email domains;
- adds a lead score;
- exports a clean file ready for outreach.

## Why this is attractive on Upwork

- Immediate business value (faster prospecting).
- Clear before/after output.
- Easy to adapt for agencies and SMB sales teams.

## Tech stack

- Python 3
- pandas

## Project structure

```text
01-lead-enrichment-automation/
├── data/
│   └── leads.csv
├── src/
│   └── enrich_leads.py
└── requirements.txt
```

## Run

```bash
cd portfolio-projects/01-lead-enrichment-automation
pip install -r requirements.txt
python src/enrich_leads.py
```

Generated output:

- `data/leads_enriched.csv`

## Suggested fixed-price packages

- Basic: clean and normalize CSV lead list.
- Standard: enrichment + scoring + filtered exports.
- Premium: enrichment pipeline + scheduled delivery + Telegram/email alert.
