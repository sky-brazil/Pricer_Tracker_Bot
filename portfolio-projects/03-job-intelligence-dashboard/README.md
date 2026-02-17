# Job Intelligence Dashboard (Python + Pandas)

Portuguese version: [README.pt-BR.md](./README.pt-BR.md)

## Business problem

Recruitment and talent teams collect job market data from multiple sources but struggle to transform raw CSV files into decision-ready insights.

## Solution

This project converts a raw jobs dataset into:

- a multi-sheet Excel report;
- company and location aggregates;
- an executive summary in Markdown.

## Why this is attractive on Upwork

- Strong fit for reporting and operations automation jobs.
- Demonstrates full pipeline mindset: ingest -> transform -> deliverable.
- Easy to adapt to HR analytics, competitor hiring signals, and market intelligence.

## Tech stack

- Python 3
- pandas
- openpyxl

## Run

```bash
cd portfolio-projects/03-job-intelligence-dashboard
pip install -r requirements.txt
python src/build_report.py
```

Generated files:

- `data/job_intelligence_report.xlsx`
- `data/executive_summary.md`

## Suggested fixed-price packages

- Basic: clean and aggregate one dataset.
- Standard: recurring report generation with multiple sheets.
- Premium: report pipeline + dashboard + delivery automation.
