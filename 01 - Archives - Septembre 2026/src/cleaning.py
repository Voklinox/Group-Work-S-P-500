"""
Data Cleaning & Harmonization Pipeline
======================================
Prepares one observation per S&P 500 issuer from the archived extract,
preserves unobserved values, and exports a Jamovi CSV with a codebook.
"""

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from src.config import (
    CLEANED_DATA_PATH,
    DOCS_DIR,
    JAMOVI_CODEBOOK_PATH,
    RAW_DATA_PATH,
    SECTOR_MAP,
    VARIABLE_METADATA,
)


def load_raw_dataset(filepath: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw scraped S&P 500 dataset."""
    if not filepath.exists():
        raise FileNotFoundError(f"Raw data file not found at: {filepath}")
    df = pd.read_csv(filepath)
    print(f"✓ Loaded raw dataset from {filepath.name}: {df.shape[0]} rows, {df.shape[1]} columns.")
    return df


def remediate_ticker_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """Code Fiserv's analytical sector without inventing unobserved values."""
    df = df.copy()
    # Fiserv returned to FISV in November 2025; preserve its raw source fields.
    fiserv = (df["Ticker"] == "FISV") & df["Sector"].isna()
    df.loc[fiserv, "Sector"] = "Finance"
    return df


def retain_one_share_class_per_company(df: pd.DataFrame) -> pd.DataFrame:
    """Resolve the three reviewed issuer duplicates; reject unreviewed cases."""
    df = df.copy()
    for extra, retained in {"GOOG": "GOOGL", "FOX": "FOXA", "NWS": "NWSA"}.items():
        redundant = df["Ticker"] == extra
        if not redundant.any():
            continue
        canonical = df.loc[df["Ticker"] == retained]
        if len(canonical) != 1 or not df.loc[redundant, "Company"].eq(canonical.iloc[0]["Company"]).all():
            raise ValueError(f"Unresolved duplicate share classes: {extra}/{retained}")
        df = df.loc[~redundant].copy()
    if df["Company"].isna().any() or df["Company"].duplicated().any():
        raise ValueError("Unresolved duplicate or missing company identity")
    return df.reset_index(drop=True)


def standardize_sectors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure all sectors map into the 5 required course groups:
    Tech & Comms, Healthcare, Finance, Industrials & Energy, Consumer.
    """
    df = df.copy()
    # Map raw sector if Sector column is missing or NaN
    missing_sector = df["Sector"].isna()
    if missing_sector.any():
        df.loc[missing_sector, "Sector"] = df.loc[missing_sector, "Sector_Raw"].map(SECTOR_MAP)

    # Validate that exactly 5 categories exist
    unique_sectors = set(df["Sector"].dropna().unique())
    expected_sectors = {
        "Tech & Comms",
        "Healthcare",
        "Finance",
        "Industrials & Energy",
        "Consumer",
    }
    diff = unique_sectors - expected_sectors
    if diff:
        raise ValueError(f"Unexpected sectors detected: {diff}")

    print(f"✓ Sectors verified: {len(unique_sectors)} nominal categories matching course requirements.")
    return df


def engineer_ordinal_variables(df: pd.DataFrame) -> pd.DataFrame:
    """
    Construct validated ordinal variables:
    1. Market_Cap_Quartile: Q1 (smallest) -> Q4 (mega-cap)
    2. Governance_Risk_Level: Low (1-3), Medium (4-6), High (7-10)
    """
    df = df.copy()

    # 1. Market Cap Quartile
    df["Market_Cap_Quartile"] = pd.qcut(
        df["Market_Cap_B"],
        q=4,
        labels=["Q1", "Q2", "Q3", "Q4"],
    )

    # 2. Governance Risk Level
    def classify_risk(val):
        if pd.isna(val):
            return np.nan
        val = int(val)
        if val <= 3:
            return "Low"
        elif val <= 6:
            return "Medium"
        else:
            return "High"

    df["Governance_Risk_Level"] = df["Overall_Governance_Risk"].apply(classify_risk)

    print("✓ Ordinal classifications constructed: Market_Cap_Quartile & Governance_Risk_Level.")
    return df


def audit_and_clean_pipeline() -> tuple[pd.DataFrame, dict]:
    """
    Execute the end-to-end cleaning pipeline and return cleaned DataFrame + audit log.
    """
    df_raw = load_raw_dataset()

    initial_audit = {
        "initial_rows": len(df_raw),
        "initial_columns": len(df_raw.columns),
        "initial_nan_counts": df_raw.isna().sum().to_dict(),
    }

    # Preserve one reviewed equity record per issuer, never sum share-class values.
    df_clean = retain_one_share_class_per_company(df_raw)
    df_clean = remediate_ticker_anomalies(df_clean)

    # Step 2: Standardize sectors
    df_clean = standardize_sectors(df_clean)

    # Step 3: Recompute ordinals
    df_clean = engineer_ordinal_variables(df_clean)

    # Step 4: Validate column order & naming for Jamovi
    ordered_cols = [
        "Ticker",
        "Company",
        "Sector",
        "Sector_Raw",
        "Total_Revenue_B",
        "Market_Cap_B",
        "Market_Cap_Quartile",
        "ROE",
        "Profit_Margin",
        "Beta",
        "Headcount",
        "Audit_Risk",
        "Board_Risk",
        "Compensation_Risk",
        "Shareholder_Rights_Risk",
        "Overall_Governance_Risk",
        "Governance_Risk_Level",
    ]
    df_clean = df_clean[ordered_cols]

    final_audit = {
        "cleaned_rows": len(df_clean),
        "cleaned_columns": len(df_clean.columns),
        "cleaned_nan_counts": df_clean.isna().sum().to_dict(),
    }

    # Export to processed CSV
    df_clean.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"✓ Cleaned dataset saved to: {CLEANED_DATA_PATH}")

    codebook = []
    for col in ordered_cols:
        meta = VARIABLE_METADATA.get(col, {})
        codebook.append({
            "Variable": col,
            "Label": meta.get("label", col),
            "Jamovi Measure Type": meta.get("jamovi_type", "Continuous"),
            "Description": meta.get("description", ""),
            "Unit": meta.get("unit", ""),
            "Levels / Range": ", ".join(meta.get("levels", [])) or meta.get("unit", ""),
        })
    pd.DataFrame(codebook).to_csv(JAMOVI_CODEBOOK_PATH, index=False)

    audit_report = {
        "initial": initial_audit,
        "final": final_audit,
        "removed_share_classes": ["GOOG", "FOX", "NWS"],
        "retained_share_classes": ["GOOGL", "FOXA", "NWSA"],
        "fiserv_sector": "Finance: analyst classification; original Sector_Raw remains missing",
        "imputed_financial_or_governance_values": 0,
        "temporal_scope": "Archived Yahoo Finance snapshot; fiscal periods not harmonised or verified",
        "raw_sha256": hashlib.sha256(RAW_DATA_PATH.read_bytes()).hexdigest(),
        "prepared_sha256": hashlib.sha256(CLEANED_DATA_PATH.read_bytes()).hexdigest(),
    }
    (DOCS_DIR / "Data_Preparation_v2.json").write_text(json.dumps(audit_report, indent=2))
    return df_clean, audit_report


if __name__ == "__main__":
    df_clean, audit = audit_and_clean_pipeline()
    print("\n--- Summary Audit ---")
    print(f"Observations: {audit['final']['cleaned_rows']}")
    print("Sectors:", df_clean["Sector"].value_counts().to_dict())
    print("Gov Risk:", df_clean["Governance_Risk_Level"].value_counts().to_dict())

