# Portfolio Projects for Upwork Positioning

These three projects are designed to attract freelance work in the same line as your current GitHub portfolio: automation, scraping, and business reporting.

Portuguese curation: [`../docs/CURADORIA_PROJETOS_PTBR.md`](../docs/CURADORIA_PROJETOS_PTBR.md)

## Included projects

1. [`01-lead-enrichment-automation`](./01-lead-enrichment-automation)
   - Turns raw leads into scored, enriched outreach-ready data.

2. [`02-price-monitoring-api`](./02-price-monitoring-api)
   - API-first version of price monitoring for e-commerce and competitor tracking.

3. [`03-job-intelligence-dashboard`](./03-job-intelligence-dashboard)
   - Data pipeline that converts raw job listings into business reports.

## How to use commercially

- Publish each folder as a separate repository.
- Add screenshots/GIFs of input -> output.
- Record a 60-90 second walkthrough video.
- Link each project in your Upwork portfolio.
- Offer fixed-price MVP packages based on each project.

## Repository separation (GitHub)

Each project folder is prepared to be copied to an independent repository.
Each one includes:

- `README.md` (EN) and `README.pt-BR.md` (PT-BR)
- `LICENSE`
- `.gitignore`
- `.github/workflows/ci.yml`

Suggested repository names:

- `lead-enrichment-automation`
- `price-monitoring-api`
- `job-intelligence-dashboard`

You can use the helper script:

```bash
bash scripts/split_portfolio_projects.sh sky-brazil
```
