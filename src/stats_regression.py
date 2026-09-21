"""
Multiple Regression & Econometric Modeling Engine (Session 4)
============================================================
Executes Simple & Multiple Linear Regression (OLS), calculates standardized betas,
computes Variance Inflation Factors (VIF) for multicollinearity,
and runs Breusch-Pagan homoscedasticity and residual normality diagnostics.
"""

from typing import Any
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

from src.config import CLEANED_DATA_PATH


def prepare_regression_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare regression variables, apply logarithmic transformations to skewed size variables,
    and drop incomplete records.
    """
    sub = df[[
        "Profit_Margin",
        "Overall_Governance_Risk",
        "Market_Cap_B",
        "Total_Revenue_B",
        "Beta",
        "Sector",
    ]].dropna().copy()

    # Log transformations for highly skewed financial size metrics
    sub["Log_Market_Cap"] = np.log(sub["Market_Cap_B"])
    sub["Log_Revenue"] = np.log(sub["Total_Revenue_B"])

    return sub


def extract_model_summary(model, df_used: pd.DataFrame, feature_names: list[str]) -> dict[str, Any]:
    """Extract comprehensive coefficients, standardized betas, and model diagnostics."""
    n_obs = int(model.nobs)
    r_squared = float(model.rsquared)
    adj_r_squared = float(model.rsquared_adj)
    f_stat = float(model.fvalue)
    f_pvalue = float(model.f_pvalue)
    aic = float(model.aic)
    bic = float(model.bic)

    # Standardized coefficients (Beta*)
    y = df_used["Profit_Margin"]
    sy = np.std(y, ddof=1)

    coef_table = []
    for name in model.params.index:
        b = float(model.params[name])
        se = float(model.bse[name])
        t_val = float(model.tvalues[name])
        p_val = float(model.pvalues[name])

        if name == "const":
            beta_star = np.nan
        else:
            clean_name = name.replace("C(Sector)[T.", "Sector_").replace("]", "")
            if clean_name in df_used.columns:
                sx = np.std(df_used[clean_name], ddof=1)
                beta_star = b * (sx / sy) if sy != 0 else np.nan
            else:
                beta_star = np.nan

        p_str = "< .001" if p_val < 0.001 else f"{p_val:.3f}"
        coef_table.append({
            "Predictor": name,
            "Coef_B": round(b, 4),
            "Std_Error": round(se, 4),
            "Std_Beta": round(beta_star, 4) if not np.isnan(beta_star) else "-",
            "t_statistic": round(t_val, 3),
            "p_value": p_str,
            "Significant_05": p_val < 0.05,
        })

    # Residual diagnostics
    residuals = model.resid
    shapiro_w, shapiro_p = stats.shapiro(residuals)

    # Breusch-Pagan test for heteroscedasticity
    bp_test = het_breuschpagan(residuals, model.model.exog)
    bp_lm = float(bp_test[0])
    bp_p = float(bp_test[1])

    return {
        "n_obs": n_obs,
        "r_squared": round(r_squared, 4),
        "adj_r_squared": round(adj_r_squared, 4),
        "f_stat": round(f_stat, 3),
        "f_pvalue": f_pvalue,
        "f_pvalue_apa": "< .001" if f_pvalue < 0.001 else f"{f_pvalue:.3f}",
        "aic": round(aic, 2),
        "bic": round(bic, 2),
        "coefficients": pd.DataFrame(coef_table),
        "residuals": residuals,
        "shapiro_w": round(float(shapiro_w), 4),
        "shapiro_p": float(shapiro_p),
        "shapiro_apa": "< .001" if shapiro_p < 0.001 else f"{shapiro_p:.3f}",
        "bp_lm": round(bp_lm, 3),
        "bp_p": float(bp_p),
        "bp_apa": "< .001" if bp_p < 0.001 else f"{bp_p:.3f}",
        "homoscedastic": bp_p > 0.05,
    }


def compute_vif(df_features: pd.DataFrame) -> pd.DataFrame:
    """Compute Variance Inflation Factor (VIF) to assess multicollinearity."""
    x = sm.add_constant(df_features)
    vif_data = []
    for i in range(1, x.shape[1]):
        col = x.columns[i]
        val = variance_inflation_factor(x.values, i)
        vif_data.append({
            "Predictor": col,
            "VIF": round(float(val), 3),
            "Tolerance": round(1.0 / float(val), 3) if val != 0 else 0.0,
            "Multicollinearity_Risk": "High (VIF > 5)" if val > 5 else "Low",
        })
    return pd.DataFrame(vif_data)


def run_full_regression_suite():
    """Execute Models 1, 2, and 3 with full diagnostic reports."""
    df = pd.read_csv(CLEANED_DATA_PATH)
    reg_data = prepare_regression_data(df)

    # -------------------------------------------------------------
    # Model 1: Simple OLS (Profit_Margin ~ Overall_Governance_Risk)
    # -------------------------------------------------------------
    x1 = sm.add_constant(reg_data[["Overall_Governance_Risk"]])
    y = reg_data["Profit_Margin"]
    m1 = sm.OLS(y, x1).fit()
    res1 = extract_model_summary(m1, reg_data, ["Overall_Governance_Risk"])

    # -------------------------------------------------------------
    # Model 2: Multiple OLS (Adding Size & Beta Controls)
    # -------------------------------------------------------------
    feat2 = ["Overall_Governance_Risk", "Log_Market_Cap", "Log_Revenue", "Beta"]
    x2 = sm.add_constant(reg_data[feat2])
    m2 = sm.OLS(y, x2).fit()
    res2 = extract_model_summary(m2, reg_data, feat2)
    vif2 = compute_vif(reg_data[feat2])

    # -------------------------------------------------------------
    # Model 3: Sector Fixed Effects Model
    # -------------------------------------------------------------
    sector_dummies = pd.get_dummies(reg_data["Sector"], prefix="Sector", drop_first=True, dtype=float)
    x3_data = pd.concat([reg_data[feat2], sector_dummies], axis=1)
    x3 = sm.add_constant(x3_data)
    m3 = sm.OLS(y, x3).fit()
    res3 = extract_model_summary(m3, pd.concat([reg_data, sector_dummies], axis=1), list(x3_data.columns))
    vif3 = compute_vif(x3_data)

    return {
        "m1": (m1, res1),
        "m2": (m2, res2, vif2),
        "m3": (m3, res3, vif3),
        "data": reg_data,
    }


if __name__ == "__main__":
    suite = run_full_regression_suite()
    m1, res1 = suite["m1"]
    m2, res2, vif2 = suite["m2"]
    m3, res3, vif3 = suite["m3"]

    print("=== Model 1: Simple OLS (Profit_Margin ~ Governance Risk) ===")
    print(f"R² = {res1['r_squared']}, F = {res1['f_stat']}, p = {res1['f_pvalue_apa']}")
    print(res1["coefficients"].to_string(index=False))

    print("\n=== Model 2: Multiple OLS (with Size & Market Risk Controls) ===")
    print(f"R² = {res2['r_squared']}, Adj R² = {res2['adj_r_squared']}, F = {res2['f_stat']}, p = {res2['f_pvalue_apa']}")
    print(res2["coefficients"].to_string(index=False))
    print("\nVariance Inflation Factors (VIF):")
    print(vif2.to_string(index=False))
    print(f"Breusch-Pagan Test: LM = {res2['bp_lm']}, p = {res2['bp_apa']} (Homoscedastic: {res2['homoscedastic']})")

    print("\n=== Model 3: Multiple OLS with Sector Dummies ===")
    print(f"R² = {res3['r_squared']}, Adj R² = {res3['adj_r_squared']}, F = {res3['f_stat']}, p = {res3['f_pvalue_apa']}")
    print(res3["coefficients"].to_string(index=False))
