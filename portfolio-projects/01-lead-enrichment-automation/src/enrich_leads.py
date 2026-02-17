from pathlib import Path

import pandas as pd


def normalize_company_name(value: str) -> str:
    return " ".join(word.capitalize() for word in value.strip().split())


def extract_domain(email: str) -> str:
    if "@" not in email:
        return ""
    return email.split("@", maxsplit=1)[1].lower()


def calculate_lead_score(domain: str, country: str) -> int:
    score = 50
    if domain.endswith(".com"):
        score += 20
    if country.lower() in {"spain", "portugal", "uk"}:
        score += 15
    return min(score, 100)


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "leads.csv"
    output_path = base_dir / "data" / "leads_enriched.csv"

    df = pd.read_csv(input_path)
    df["company"] = df["company"].fillna("").map(normalize_company_name)
    df["email"] = df["email"].fillna("")
    df["domain"] = df["email"].map(extract_domain)
    df["lead_score"] = [
        calculate_lead_score(domain=domain, country=country)
        for domain, country in zip(df["domain"], df["country"].fillna(""))
    ]

    df.sort_values(by="lead_score", ascending=False, inplace=True)
    df.to_csv(output_path, index=False)
    print(f"[OK] Enriched leads saved to: {output_path}")


if __name__ == "__main__":
    main()
