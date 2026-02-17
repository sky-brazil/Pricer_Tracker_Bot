# Guide: Split Portfolio Projects into Independent GitHub Repositories

Goal: publish each project in `portfolio-projects/` as a standalone repository.

## Prerequisites

- Git installed
- GitHub CLI authenticated (`gh auth status`)

## Option 1 (automatic)

Run:

```bash
bash scripts/split_portfolio_projects.sh sky-brazil
```

The script will:

- copy each curated project to a temporary folder;
- initialize git in each project folder;
- create a GitHub repo (if it does not exist);
- push an initial commit.

## Option 2 (manual)

For each project:

1. Create repository on GitHub
2. Copy project folder contents
3. Create initial commit
4. Push to `main`

## Suggested repository names

- `lead-enrichment-automation`
- `price-monitoring-api`
- `job-intelligence-dashboard`

## Post-publication checklist

1. Add topics
2. Improve short description
3. Enable GitHub Actions
4. Pin the 3 repositories in your profile
5. Link them in Upwork with visual proof
