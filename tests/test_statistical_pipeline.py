"""
Automated Test Suite for Statistical Modeling Pipeline (Sessions 2, 3, 4)
========================================================================
Validates that Chi-Square tests, Welch's ANOVA, Games-Howell post-hoc tests,
and OLS multiple regression models execute cleanly and adhere to mathematical bounds.
"""

import pandas as pd
import pytest
from src.config import CLEANED_DATA_PATH
from src.stats_bivariate import compute_chi2_contingency, compute_bivariate_correlations
from src.stats_anova import run_full_anova_battery
from src.stats_regression import run_full_regression_suite


@pytest.fixture(scope="session")
def df_clean():
    """Load verified clean dataset fixture."""
    return pd.read_csv(CLEANED_DATA_PATH)


def test_session2_chi2_contingency(df_clean):
    """Verify Chi-Square test of independence executes with valid bounds."""
    res = compute_chi2_contingency(df_clean, "Sector", "Governance_Risk_Level")
    assert res["chi2_stat"] > 0, "Chi-square statistic must be strictly positive."
    assert res["dof"] == 8, f"Expected 8 degrees of freedom, got {res['dof']}"
    assert 0.0 <= res["p_val"] <= 1.0, "p-value must reside in [0, 1]."
    assert 0.0 <= res["cramers_v"] <= 1.0, "Cramer's V must reside in [0, 1]."
    assert res["observed"].shape == (5, 3), "Contingency table must be 5x3."


def test_session2_bivariate_correlations(df_clean):
    """Verify Pearson and Spearman correlation calculations."""
    vars_list = ["Overall_Governance_Risk", "Profit_Margin", "Beta"]
    corr_df, _ = compute_bivariate_correlations(df_clean, vars_list)
    assert len(corr_df) == 3, "Expected 3 pairwise correlations."
    for _, row in corr_df.iterrows():
        assert -1.0 <= row["Pearson_r"] <= 1.0, "Pearson r must reside in [-1, 1]."
        assert -1.0 <= row["Spearman_rho"] <= 1.0, "Spearman rho must reside in [-1, 1]."


def test_session3_anova_welch_and_games_howell(df_clean):
    """Verify Welch's ANOVA and Games-Howell post-hoc tests."""
    res = run_full_anova_battery(df_clean, "Profit_Margin", "Sector")
    assert res["levene_stat"] > 0, "Levene statistic must be positive."
    assert res["welch"]["f_welch"] > 0, "Welch F statistic must be positive."
    assert res["df_between"] == 4, "Between-group df must equal k - 1 = 4."
    assert len(res["games_howell"]) == 10, "5 sectors must generate exactly 10 pairwise comparisons (5*4/2)."


def test_session4_regression_suite():
    """Verify Multiple Regression OLS Models and VIF values."""
    suite = run_full_regression_suite()
    _, res1 = suite["m1"]
    _, res2, vif2 = suite["m2"]
    _, res3, vif3 = suite["m3"]

    # Model 1 bounds
    assert 0.0 <= res1["r_squared"] <= 1.0, "R² must reside in [0, 1]."

    # Model 2 & 3 checks
    assert res2["r_squared"] > res1["r_squared"], "Model 2 must explain more variance than Model 1."
    assert res3["r_squared"] > res2["r_squared"], "Model 3 must explain more variance than Model 2."

    # Multicollinearity check
    for _, row in vif3.iterrows():
        assert row["VIF"] < 5.0, f"VIF for {row['Predictor']} exceeds conservative threshold of 5.0."

    # Verify governance coefficient in Model 3 is negative
    gov_coef = res3["coefficients"].loc[res3["coefficients"]["Predictor"] == "Overall_Governance_Risk", "Coef_B"].values[0]
    assert gov_coef < 0, "Governance risk coefficient in Model 3 must be negative (penalizing margins)."
