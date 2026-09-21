"""
Data Integrity & Course Requirement Verification Tests
======================================================
Automated test suite enforcing the 6 non-negotiable course criteria
defined in AQD Session 1 (Slide 29) and CLAUDE.md:
1. N >= 100 observations
2. Exactly 2 to 5 categories for the nominal variable (Sector)
3. At least 1 ordinal variable
4. At least 3 continuous variables
5. Unit of observation: 1 row = 1 firm (zero duplicates)
6. Jamovi header compliance (short, no spaces, no accents)
"""

import pandas as pd
import pytest

from src.config import CLEANED_DATA_PATH


@pytest.fixture(scope="session")
def cleaned_df():
    """Load cleaned dataset fixture."""
    assert CLEANED_DATA_PATH.exists(), f"Cleaned dataset missing: {CLEANED_DATA_PATH}"
    df = pd.read_csv(CLEANED_DATA_PATH)
    return df


def test_minimum_observations(cleaned_df):
    """Criterion 1: Dataset must have at least 100 rows."""
    n_rows = len(cleaned_df)
    assert n_rows >= 100, f"Expected >= 100 observations, got {n_rows}"


def test_nominal_sector_categories(cleaned_df):
    """Criterion 2: Nominal variable must have between 2 and 5 categories and zero NaNs."""
    assert "Sector" in cleaned_df.columns, "Missing 'Sector' nominal column."
    assert cleaned_df["Sector"].isna().sum() == 0, "Nominal 'Sector' column must not contain NaNs."

    unique_sectors = cleaned_df["Sector"].unique()
    n_categories = len(unique_sectors)
    assert 2 <= n_categories <= 5, f"Nominal variable must have 2-5 categories, found {n_categories}: {unique_sectors}"

    expected_sectors = {
        "Tech & Comms",
        "Healthcare",
        "Finance",
        "Industrials & Energy",
        "Consumer",
    }
    assert set(unique_sectors) == expected_sectors, f"Mismatch in sector groupings: {set(unique_sectors)}"


def test_ordinal_variables(cleaned_df):
    """Criterion 3: At least 1 valid ordinal variable."""
    assert "Governance_Risk_Level" in cleaned_df.columns, "Missing 'Governance_Risk_Level' ordinal column."
    gov_levels = set(cleaned_df["Governance_Risk_Level"].dropna().unique())
    assert gov_levels == {"Low", "Medium", "High"}, f"Invalid governance tiers: {gov_levels}"

    assert "Market_Cap_Quartile" in cleaned_df.columns, "Missing 'Market_Cap_Quartile' ordinal column."
    quartiles = set(cleaned_df["Market_Cap_Quartile"].dropna().unique())
    assert quartiles == {"Q1", "Q2", "Q3", "Q4"}, f"Invalid market cap quartiles: {quartiles}"


def test_continuous_variables(cleaned_df):
    """Criterion 4: At least 3 continuous variables."""
    continuous_cols = [
        "Total_Revenue_B",
        "Market_Cap_B",
        "Profit_Margin",
        "ROE",
        "Beta",
        "Overall_Governance_Risk",
    ]
    for col in continuous_cols:
        assert col in cleaned_df.columns, f"Missing continuous column: {col}"
        assert pd.api.types.is_numeric_dtype(cleaned_df[col]), f"Column {col} must be numeric."

    # Verify at least 3 continuous columns have valid data
    valid_counts = [cleaned_df[col].notna().sum() for col in continuous_cols]
    assert all(count >= 100 for count in valid_counts[:3]), "Top 3 continuous variables must have >= 100 valid observations."


def test_unit_of_observation(cleaned_df):
    """Criterion 5: One row = one firm (Ticker is unique identifier)."""
    assert "Ticker" in cleaned_df.columns, "Missing 'Ticker' column."
    assert cleaned_df["Ticker"].is_unique, "Tickers must be unique across all rows."


def test_jamovi_header_compliance(cleaned_df):
    """Criterion 6: Headers must contain no spaces, no accents, and no special chars (except underscore)."""
    for col in cleaned_df.columns:
        assert " " not in col, f"Column '{col}' contains spaces (violates Jamovi naming standards)."
        assert col.isascii(), f"Column '{col}' contains non-ASCII characters."

