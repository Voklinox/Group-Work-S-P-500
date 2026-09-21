"""
Configuration & Metadata Specifications
========================================
Centralized project configuration, directory paths, variable taxonomy,
Jamovi settings, and APA 7th edition visualization aesthetics.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# 1. DIRECTORY PATHS
# ---------------------------------------------------------------------------
SRC_DIR = Path(__file__).resolve().parent
BASE_DIR = SRC_DIR.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FIGURES_DIR = BASE_DIR / "figures"
DOCS_DIR = BASE_DIR / "docs"

RAW_DATA_PATH = RAW_DATA_DIR / "sp500_esg_dataset_raw.csv"
CLEANED_DATA_PATH = PROCESSED_DATA_DIR / "sp500_esg_cleaned.csv"
JAMOVI_CSV_PATH = PROCESSED_DATA_DIR / "sp500_esg_jamovi.csv"
JAMOVI_XLSX_PATH = PROCESSED_DATA_DIR / "sp500_esg_jamovi.xlsx"

# Ensure runtime directories exist
for folder in [RAW_DATA_DIR, PROCESSED_DATA_DIR, FIGURES_DIR, DOCS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 2. SECTOR MAPPING (11 GICS SECTORS -> 5 NOMINAL GROUPS)
# Coursework Requirement: Nominal variable MUST have 2 to 5 categories.
# ---------------------------------------------------------------------------
SECTOR_MAP = {
    # Tech & Comms
    "Technology": "Tech & Comms",
    "Information Technology": "Tech & Comms",
    "Communication Services": "Tech & Comms",
    # Healthcare
    "Healthcare": "Healthcare",
    "Health Care": "Healthcare",
    # Finance
    "Financial Services": "Finance",
    "Financials": "Finance",
    # Industrials & Energy
    "Industrials": "Industrials & Energy",
    "Energy": "Industrials & Energy",
    "Utilities": "Industrials & Energy",
    "Basic Materials": "Industrials & Energy",
    "Materials": "Industrials & Energy",
    # Consumer
    "Consumer Cyclical": "Consumer",
    "Consumer Defensive": "Consumer",
    "Consumer Discretionary": "Consumer",
    "Consumer Staples": "Consumer",
    "Real Estate": "Consumer",
}

# ---------------------------------------------------------------------------
# 3. VARIABLE TAXONOMY & JAMOVI SPECIFICATIONS
# Format adheres to Slide 38 ("short, no spaces, no accents")
# ---------------------------------------------------------------------------
VARIABLE_METADATA = {
    "Ticker": {
        "label": "Stock Ticker Symbol",
        "type": "ID",
        "jamovi_type": "ID",
        "description": "Unique equity ticker symbol",
        "unit": "string",
    },
    "Company": {
        "label": "Company Name",
        "type": "Nominal",
        "jamovi_type": "Nominal",
        "description": "Legal operating corporate identity",
        "unit": "string",
    },
    "Sector": {
        "label": "Sector (5 Consolidated Groups)",
        "type": "Nominal",
        "jamovi_type": "Nominal",
        "description": "Consolidated business sector (5 groups for ANOVA/Chi-Square)",
        "unit": "categories",
        "levels": [
            "Tech & Comms",
            "Healthcare",
            "Finance",
            "Industrials & Energy",
            "Consumer",
        ],
    },
    "Sector_Raw": {
        "label": "GICS Raw Sector",
        "type": "Nominal",
        "jamovi_type": "Nominal",
        "description": "Original 11-category GICS sector classification",
        "unit": "categories",
    },
    "Total_Revenue_B": {
        "label": "Total Revenue ($B)",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "Annual total revenue for FY2025 in billions USD",
        "unit": "$ Billion",
    },
    "Market_Cap_B": {
        "label": "Market Capitalization ($B)",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "Total market capitalization in billions USD",
        "unit": "$ Billion",
    },
    "Market_Cap_Quartile": {
        "label": "Market Cap Quartile",
        "type": "Ordinal",
        "jamovi_type": "Ordinal",
        "description": "Firm size quartile from Q1 (smallest) to Q4 (mega-cap)",
        "unit": "quartiles",
        "levels": ["Q1", "Q2", "Q3", "Q4"],
    },
    "ROE": {
        "label": "Return on Equity (ROE)",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "Net income divided by shareholders equity (FY2025)",
        "unit": "decimal",
    },
    "Profit_Margin": {
        "label": "Net Profit Margin",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "Net income divided by total revenue (FY2025)",
        "unit": "decimal",
    },
    "Beta": {
        "label": "Market Beta (5Y Monthly)",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "Systematic market risk coefficient against S&P 500",
        "unit": "ratio",
    },
    "Headcount": {
        "label": "Full-Time Employees",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "Total full-time headcount globally",
        "unit": "employees",
    },
    "Audit_Risk": {
        "label": "Audit Risk Score",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "ISS Governance QualityScore for audit practices (1-10, lower=better)",
        "unit": "score (1-10)",
    },
    "Board_Risk": {
        "label": "Board Structure Risk Score",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "ISS Governance QualityScore for board independence (1-10, lower=better)",
        "unit": "score (1-10)",
    },
    "Compensation_Risk": {
        "label": "Compensation Risk Score",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "ISS Governance QualityScore for executive pay alignment (1-10, lower=better)",
        "unit": "score (1-10)",
    },
    "Shareholder_Rights_Risk": {
        "label": "Shareholder Rights Risk Score",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "ISS Governance QualityScore for shareholder rights protection (1-10, lower=better)",
        "unit": "score (1-10)",
    },
    "Overall_Governance_Risk": {
        "label": "Overall Governance Risk Score",
        "type": "Continuous",
        "jamovi_type": "Continuous",
        "description": "ISS composite governance quality score (1-10, lower=better)",
        "unit": "score (1-10)",
    },
    "Governance_Risk_Level": {
        "label": "Governance Risk Category",
        "type": "Ordinal",
        "jamovi_type": "Ordinal",
        "description": "Categorized governance risk: Low (1-3), Medium (4-6), High (7-10)",
        "unit": "tier",
        "levels": ["Low", "Medium", "High"],
    },
}

# ---------------------------------------------------------------------------
# 4. APA 7TH EDITION VISUALIZATION STYLE
# ---------------------------------------------------------------------------
APA_STYLE = {
    "font_family": "sans-serif",
    "title_size": 14,
    "axis_title_size": 12,
    "tick_size": 10,
    "legend_size": 10,
    "source_size": 9,
    "palette": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
    "source_annotation": "Source: S&P 500 Corporate Governance & Financial Performance Dataset (ISS & Yahoo Finance, FY2025/2026)",
}
