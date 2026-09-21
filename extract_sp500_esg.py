"""
S&P 500 Governance & Financial Data Extraction Script
=====================================================
Extracts financial metrics and ISS governance risk scores for all
S&P 500 companies and exports a clean CSV dataset for quantitative
data analysis.

Note: Yahoo Finance deprecated free Sustainalytics ESG scores.
      This script uses ISS (Institutional Shareholder Services)
      governance quality scores instead, which are still available
      via the yfinance API.

Requirements:
    pip install yfinance pandas tqdm lxml html5lib requests

Usage:
    source .venv/bin/activate
    python extract_sp500_esg.py
"""

import time
import numpy as np
import pandas as pd
import requests as _requests
import yfinance as yf
from tqdm import tqdm

# ---------------------------------------------------------------------------
# 1. CONFIGURATION
# ---------------------------------------------------------------------------

OUTPUT_FILE = "sp500_esg_dataset.csv"
SLEEP_SECONDS = 0.25  # Pause between API calls to avoid rate-limiting

# Mapping of the 11 GICS sectors → 5 grouped categories
SECTOR_MAP = {
    # Tech & Comms
    "Technology":                "Tech & Comms",
    "Information Technology":    "Tech & Comms",
    "Communication Services":    "Tech & Comms",
    # Healthcare
    "Healthcare":                "Healthcare",
    "Health Care":               "Healthcare",
    # Finance
    "Financial Services":        "Finance",
    "Financials":                "Finance",
    # Industrials & Energy
    "Industrials":               "Industrials & Energy",
    "Energy":                    "Industrials & Energy",
    "Utilities":                 "Industrials & Energy",
    "Basic Materials":           "Industrials & Energy",
    "Materials":                 "Industrials & Energy",
    # Consumer
    "Consumer Cyclical":         "Consumer",
    "Consumer Defensive":        "Consumer",
    "Consumer Discretionary":    "Consumer",
    "Consumer Staples":          "Consumer",
    "Real Estate":               "Consumer",
}

# ---------------------------------------------------------------------------
# 2. FETCH S&P 500 TICKER LIST FROM WIKIPEDIA
# ---------------------------------------------------------------------------

def get_sp500_tickers() -> list[str]:
    """Scrape the current S&P 500 constituents table from Wikipedia."""
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    resp = _requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    tables = pd.read_html(resp.text)
    df = tables[0]
    # The ticker column is typically named 'Symbol'
    tickers = df["Symbol"].str.replace(".", "-", regex=False).tolist()
    print(f"✓ Fetched {len(tickers)} S&P 500 tickers from Wikipedia.\n")
    return tickers

# ---------------------------------------------------------------------------
# 3. EXTRACT DATA FOR A SINGLE TICKER
# ---------------------------------------------------------------------------

def extract_ticker_data(ticker_symbol: str) -> dict:
    """
    Pull financial info and governance risk scores for one ticker via yfinance.
    Returns a dict of values; missing fields default to np.nan.

    ISS Governance Risk Scores (1-10 scale):
        1 = low risk (good governance), 10 = high risk (poor governance)
        - auditRisk: Risk related to audit practices
        - boardRisk: Risk related to board composition/independence
        - compensationRisk: Risk related to executive compensation
        - shareHolderRightsRisk: Risk related to shareholder rights protections
        - overallRisk: Composite governance risk score
    """
    record = {
        "Ticker":                 ticker_symbol,
        "Company":                np.nan,
        "Sector_Raw":             np.nan,
        "Sector":                 np.nan,           # Grouped (5 categories) — NOMINAL
        "Total_Revenue_B":        np.nan,           # In billions USD
        "Market_Cap_B":           np.nan,           # In billions USD
        "ROE":                    np.nan,           # Return on Equity
        "Profit_Margin":          np.nan,           # Net profit margin
        "Beta":                   np.nan,           # Market risk (volatility)
        "Headcount":              np.nan,           # Full-time employees
        "Audit_Risk":             np.nan,           # ISS (1-10)
        "Board_Risk":             np.nan,           # ISS (1-10)
        "Compensation_Risk":      np.nan,           # ISS (1-10)
        "Shareholder_Rights_Risk": np.nan,          # ISS (1-10)
        "Overall_Governance_Risk": np.nan,          # ISS (1-10)
    }

    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info  # dict of ~150 fields

        # --- Company identity ---
        record["Company"] = info.get("shortName", info.get("longName", np.nan))

        # --- Sector (raw + grouped) ---
        raw_sector = info.get("sector", np.nan)
        record["Sector_Raw"] = raw_sector
        record["Sector"] = SECTOR_MAP.get(raw_sector, np.nan)

        # --- Financials (continuous) ---
        revenue = info.get("totalRevenue")
        if revenue is not None:
            record["Total_Revenue_B"] = round(revenue / 1e9, 3)

        market_cap = info.get("marketCap")
        if market_cap is not None:
            record["Market_Cap_B"] = round(market_cap / 1e9, 3)

        roe = info.get("returnOnEquity")
        if roe is not None:
            record["ROE"] = round(roe, 4)

        profit_margin = info.get("profitMargins")
        if profit_margin is not None:
            record["Profit_Margin"] = round(profit_margin, 4)

        beta = info.get("beta")
        if beta is not None:
            record["Beta"] = round(beta, 3)

        headcount = info.get("fullTimeEmployees")
        if headcount is not None:
            record["Headcount"] = headcount

        # --- ISS Governance Risk Scores (1-10, lower = better) ---
        record["Audit_Risk"]              = info.get("auditRisk", np.nan)
        record["Board_Risk"]              = info.get("boardRisk", np.nan)
        record["Compensation_Risk"]       = info.get("compensationRisk", np.nan)
        record["Shareholder_Rights_Risk"] = info.get("shareHolderRightsRisk", np.nan)
        record["Overall_Governance_Risk"] = info.get("overallRisk", np.nan)

    except Exception as e:
        # If the entire ticker fetch fails, the record stays all NaN
        print(f"  ⚠ Error fetching {ticker_symbol}: {e}")

    return record

# ---------------------------------------------------------------------------
# 4. MAIN PIPELINE
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  S&P 500 Governance & Financial Data Extraction")
    print("=" * 60)
    print()

    # Step 1 — Get ticker list
    tickers = get_sp500_tickers()

    # Step 2 — Loop through tickers and collect data
    records = []
    for ticker in tqdm(tickers, desc="Extracting data", unit="ticker"):
        row = extract_ticker_data(ticker)
        records.append(row)
        time.sleep(SLEEP_SECONDS)

    # Step 3 — Build DataFrame
    df = pd.DataFrame(records)

    # Step 4 — Post-processing: create ordinal variables
    # 4a. Market Cap Quartile (ordinal: Q1=smallest → Q4=largest)
    df["Market_Cap_Quartile"] = pd.qcut(
        df["Market_Cap_B"],
        q=4,
        labels=["Q1", "Q2", "Q3", "Q4"],
    )

    # 4b. Governance Risk Level (ordinal: derived from Overall_Governance_Risk)
    #     1-3 → Low, 4-6 → Medium, 7-10 → High
    def classify_gov_risk(score):
        if pd.isna(score):
            return np.nan
        score = int(score)
        if score <= 3:
            return "Low"
        elif score <= 6:
            return "Medium"
        else:
            return "High"

    df["Governance_Risk_Level"] = df["Overall_Governance_Risk"].apply(classify_gov_risk)

    # Step 5 — Summary statistics
    print("\n" + "=" * 60)
    print("  EXTRACTION SUMMARY")
    print("=" * 60)
    print(f"  Total tickers attempted     : {len(df)}")
    print(f"  Non-null Revenue            : {df['Total_Revenue_B'].notna().sum()}")
    print(f"  Non-null Market Cap         : {df['Market_Cap_B'].notna().sum()}")
    print(f"  Non-null ROE                : {df['ROE'].notna().sum()}")
    print(f"  Non-null Profit Margin      : {df['Profit_Margin'].notna().sum()}")
    print(f"  Non-null Beta               : {df['Beta'].notna().sum()}")
    print(f"  Non-null Governance Risk     : {df['Overall_Governance_Risk'].notna().sum()}")
    print(f"  Sector distribution         :")
    print(df["Sector"].value_counts().to_string(header=False))
    print(f"\n  Governance Risk Level       :")
    print(df["Governance_Risk_Level"].value_counts().to_string(header=False))
    print("=" * 60)

    # Step 6 — Export
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✓ Dataset exported to '{OUTPUT_FILE}' ({len(df)} rows).\n")


if __name__ == "__main__":
    main()
