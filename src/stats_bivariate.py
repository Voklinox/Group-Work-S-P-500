"""
Bivariate Statistical Engine (Session 2)
========================================
Executes Chi-Square tests of independence with Cramér's V for nominal x ordinal variables,
and computes Pearson and Spearman correlation matrices with 95% Confidence Intervals
and exact two-tailed p-values for continuous variables.
"""

from typing import Any
import numpy as np
import pandas as pd
from scipy import stats

from src.config import CLEANED_DATA_PATH


def compute_chi2_contingency(
    df: pd.DataFrame, var1: str, var2: str
) -> dict[str, Any]:
    """
    Perform a full Chi-Square test of independence between two categorical variables.
    Computes observed contingency table, expected frequencies, standardized residuals,
    Chi-Square statistic, degrees of freedom, p-value, and Cramér's V effect size.
    """
    sub = df[[var1, var2]].dropna()
    n_total = len(sub)

    contingency_observed = pd.crosstab(sub[var1], sub[var2])
    chi2_stat, p_val, dof, expected_arr = stats.chi2_contingency(contingency_observed)

    contingency_expected = pd.DataFrame(
        expected_arr,
        index=contingency_observed.index,
        columns=contingency_observed.columns,
    )

    # Standardized Residuals: (Observed - Expected) / sqrt(Expected)
    std_residuals = (contingency_observed - contingency_expected) / np.sqrt(contingency_expected)

    # Cramér's V effect size
    r, k = contingency_observed.shape
    min_dim = min(r - 1, k - 1)
    cramers_v = np.sqrt(chi2_stat / (n_total * min_dim)) if min_dim > 0 else 0.0

    return {
        "var1": var1,
        "var2": var2,
        "n_total": n_total,
        "chi2_stat": round(float(chi2_stat), 4),
        "dof": int(dof),
        "p_val": float(p_val),
        "p_val_apa": "< .001" if p_val < 0.001 else f"{p_val:.3f}",
        "cramers_v": round(float(cramers_v), 4),
        "observed": contingency_observed,
        "expected": contingency_expected.round(2),
        "std_residuals": std_residuals.round(2),
    }


def pearson_ci(r: float, n: int, confidence: float = 0.95) -> tuple[float, float]:
    """Calculate 95% confidence interval for Pearson r via Fisher z-transformation."""
    if abs(r) >= 1.0 or n <= 3:
        return (r, r)
    z = np.arctanh(r)
    se = 1.0 / np.sqrt(n - 3)
    alpha = 1 - confidence
    z_crit = stats.norm.ppf(1 - alpha / 2)
    ci_lower = np.tanh(z - z_crit * se)
    ci_upper = np.tanh(z + z_crit * se)
    return float(ci_lower), float(ci_upper)


def compute_bivariate_correlations(
    df: pd.DataFrame, vars_list: list[str]
) -> tuple[pd.DataFrame, list[dict]]:
    """
    Compute pairwise Pearson and Spearman correlation matrices with 95% CIs and p-values.
    """
    records = []
    n_vars = len(vars_list)

    for i in range(n_vars):
        for j in range(i + 1, n_vars):
            v1 = vars_list[i]
            v2 = vars_list[j]

            valid = df[[v1, v2]].dropna()
            n_pair = len(valid)
            if n_pair < 5:
                continue

            r_val, p_pearson = stats.pearsonr(valid[v1], valid[v2])
            ci_low, ci_high = pearson_ci(r_val, n_pair, confidence=0.95)
            rho_val, p_spearman = stats.spearmanr(valid[v1], valid[v2])

            p_p_str = "< .001" if p_pearson < 0.001 else f"{p_pearson:.3f}"
            p_s_str = "< .001" if p_spearman < 0.001 else f"{p_spearman:.3f}"

            records.append({
                "Variable_1": v1,
                "Variable_2": v2,
                "N": n_pair,
                "Pearson_r": round(float(r_val), 4),
                "Pearson_p": p_p_str,
                "95%_CI": f"[{ci_low:.3f}, {ci_high:.3f}]",
                "Spearman_rho": round(float(rho_val), 4),
                "Spearman_p": p_s_str,
                "Significant_05": p_pearson < 0.05,
            })

    summary_table = pd.DataFrame(records)
    return summary_table, records


def run_full_session2_pipeline():
    """Execute complete Session 2 bivariate battery."""
    df = pd.read_csv(CLEANED_DATA_PATH)

    # 1. Chi-Square: Sector x Governance_Risk_Level
    chi_sector = compute_chi2_contingency(df, "Sector", "Governance_Risk_Level")

    # 2. Chi-Square: Market_Cap_Quartile x Governance_Risk_Level
    chi_size = compute_chi2_contingency(df, "Market_Cap_Quartile", "Governance_Risk_Level")

    # 3. Continuous Correlations
    core_vars = [
        "Overall_Governance_Risk",
        "Profit_Margin",
        "ROE",
        "Market_Cap_B",
        "Total_Revenue_B",
        "Beta",
        "Audit_Risk",
        "Board_Risk",
        "Compensation_Risk",
        "Shareholder_Rights_Risk",
    ]
    corr_table, corr_records = compute_bivariate_correlations(df, core_vars)

    return {
        "chi_sector": chi_sector,
        "chi_size": chi_size,
        "correlations": corr_table,
    }


if __name__ == "__main__":
    results = run_full_session2_pipeline()

    print("=== Chi-Square Test: Sector x Governance_Risk_Level ===")
    print(f"Chi2({results['chi_sector']['dof']}, N = {results['chi_sector']['n_total']}) = {results['chi_sector']['chi2_stat']}, p = {results['chi_sector']['p_val_apa']}, Cramér's V = {results['chi_sector']['cramers_v']}")
    print("\nObserved Contingency Table:")
    print(results["chi_sector"]["observed"])
    print("\nStandardized Residuals:")
    print(results["chi_sector"]["std_residuals"])

    print("\n=== Chi-Square Test: Market_Cap_Quartile x Governance_Risk_Level ===")
    print(f"Chi2({results['chi_size']['dof']}, N = {results['chi_size']['n_total']}) = {results['chi_size']['chi2_stat']}, p = {results['chi_size']['p_val_apa']}, Cramér's V = {results['chi_size']['cramers_v']}")

    print("\n=== Key Pearson Correlations with Overall Governance Risk ===")
    gov_corrs = results["correlations"][
        (results["correlations"]["Variable_1"] == "Overall_Governance_Risk") |
        (results["correlations"]["Variable_2"] == "Overall_Governance_Risk")
    ]
    print(gov_corrs[["Variable_1", "Variable_2", "N", "Pearson_r", "Pearson_p", "95%_CI", "Spearman_rho"]].to_string(index=False))
