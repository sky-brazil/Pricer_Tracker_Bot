from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "jobs.csv"
OUTPUT_XLSX = BASE_DIR / "data" / "job_intelligence_report.xlsx"
OUTPUT_SUMMARY = BASE_DIR / "data" / "executive_summary.md"


def load_jobs() -> pd.DataFrame:
    df = pd.read_csv(INPUT_PATH)
    df["remote"] = df["remote"].astype(str).str.lower().eq("true")
    df["salary_usd"] = pd.to_numeric(df["salary_usd"], errors="coerce")
    return df


def build_summary_tables(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    by_company = (
        df.groupby("company", as_index=False)
        .agg(
            jobs_count=("job_id", "count"),
            avg_salary_usd=("salary_usd", "mean"),
            remote_jobs=("remote", "sum"),
        )
        .sort_values(by="jobs_count", ascending=False)
    )

    by_location = (
        df.groupby("location", as_index=False)
        .agg(
            jobs_count=("job_id", "count"),
            avg_salary_usd=("salary_usd", "mean"),
        )
        .sort_values(by="jobs_count", ascending=False)
    )

    return by_company, by_location


def write_excel(df: pd.DataFrame, by_company: pd.DataFrame, by_location: pd.DataFrame) -> None:
    with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="raw_jobs", index=False)
        by_company.to_excel(writer, sheet_name="by_company", index=False)
        by_location.to_excel(writer, sheet_name="by_location", index=False)


def write_summary(df: pd.DataFrame, by_company: pd.DataFrame, by_location: pd.DataFrame) -> None:
    top_company = by_company.iloc[0]["company"] if not by_company.empty else "N/A"
    top_location = by_location.iloc[0]["location"] if not by_location.empty else "N/A"
    remote_share = round(100 * df["remote"].mean(), 2) if not df.empty else 0.0
    avg_salary = round(df["salary_usd"].mean(), 2) if not df.empty else 0.0

    generated_at = datetime.now(timezone.utc).isoformat()
    content = (
        "# Executive Summary\n\n"
        f"- Generated at (UTC): {generated_at}\n"
        f"- Total jobs: {len(df)}\n"
        f"- Remote share: {remote_share}%\n"
        f"- Average salary (USD): {avg_salary}\n"
        f"- Top hiring company: {top_company}\n"
        f"- Top location by volume: {top_location}\n"
    )
    OUTPUT_SUMMARY.write_text(content, encoding="utf-8")


def main() -> None:
    jobs = load_jobs()
    by_company, by_location = build_summary_tables(jobs)
    write_excel(jobs, by_company, by_location)
    write_summary(jobs, by_company, by_location)

    print(f"[OK] Excel report: {OUTPUT_XLSX}")
    print(f"[OK] Summary file: {OUTPUT_SUMMARY}")


if __name__ == "__main__":
    main()
