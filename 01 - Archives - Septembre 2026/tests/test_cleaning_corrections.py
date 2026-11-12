"""Preserve archived evidence while preparing one observation per issuer."""

import pandas as pd
import pytest

from src.cleaning import load_raw_dataset, remediate_ticker_anomalies


def test_fiserv_keeps_its_current_ticker_and_unobserved_values_missing():
    raw = load_raw_dataset()
    result = remediate_ticker_anomalies(raw)
    row = result.loc[result["Company"] == "Fiserv, Inc."].iloc[0]
    assert row["Ticker"] == "FISV"
    assert row["Sector"] == "Finance"
    assert pd.isna(row["Sector_Raw"])
    for column in ["Total_Revenue_B", "Profit_Margin", "Beta", "Headcount", "Overall_Governance_Risk"]:
        assert pd.isna(row[column]), f"Unobserved {column} must not be invented"


def test_duplicate_share_classes_are_resolved_independently_of_row_order():
    from src.cleaning import retain_one_share_class_per_company

    raw = load_raw_dataset().sample(frac=1, random_state=42)
    result = retain_one_share_class_per_company(raw)
    assert len(result) == 500
    assert result["Company"].is_unique
    assert set(raw["Ticker"]) - set(result["Ticker"]) == {"GOOG", "FOX", "NWS"}
    for ticker in ["GOOGL", "FOXA", "NWSA"]:
        pd.testing.assert_series_equal(
            result.set_index("Ticker").loc[ticker], raw.set_index("Ticker").loc[ticker]
        )


def test_unknown_duplicate_companies_are_reported_instead_of_silently_dropped():
    from src.cleaning import retain_one_share_class_per_company

    raw = load_raw_dataset()
    extra = raw.iloc[[0]].copy()
    extra["Ticker"] = "UNREVIEWED"
    with pytest.raises(ValueError, match="Unresolved duplicate"):
        retain_one_share_class_per_company(pd.concat([raw, extra], ignore_index=True))
