"""
Univariate Statistical Engine
=============================
Computes descriptive statistics, central tendency, dispersion, shape metrics,
and formal normality tests (Shapiro-Wilk) adhering to APA 7th edition standards
and the course analytical protocol (Slides 19-25 & 40-41).
"""

from typing import Any
import numpy as np
import pandas as pd
from scipy import stats

from src.config import CLEANED_DATA_PATH, VARIABLE_METADATA


def compute_continuous_univariate(series: pd.Series, var_name: str) -> dict[str, Any]:
    """
    Compute full univariate descriptive statistics for a continuous variable.
    Includes the 3 centres (Mean, Median, Mode), dispersion metrics,
    shape parameters (Skewness, Kurtosis), and Shapiro-Wilk normality test.
    """
    valid = series.dropna()
    n_valid = len(valid)
    n_missing = series.isna().sum()

    if n_valid < 3:
        raise ValueError(f"Not enough valid observations for variable: {var_name}")

    # Central Tendency
    mean_val = float(valid.mean())
    median_val = float(valid.median())

    # Mode: For continuous data, compute on rounded values or KDE peak
    # Here rounded to 2 decimal places to capture frequency clusters
    rounded_series = valid.round(2)
    mode_counts = rounded_series.value_counts()
    mode_val = float(mode_counts.index[0]) if not mode_counts.empty else np.nan

    # Dispersion
    std_val = float(valid.std(ddof=1))
    var_val = float(valid.var(ddof=1))
    min_val = float(valid.min())
    max_val = float(valid.max())
    q25 = float(valid.quantile(0.25))
    q75 = float(valid.quantile(0.75))
    iqr_val = q75 - q25

    # Shape
    skew_val = float(stats.skew(valid, bias=False))
    kurt_val = float(stats.kurtosis(valid, bias=False))  # Fisher excess kurtosis (normal = 0)

    # Normality Test: Shapiro-Wilk (H0 = normal distribution)
    # Note: SciPy handles up to N=5000
    shapiro_w, shapiro_p = stats.shapiro(valid)

    # Three-evidence normality assessment:
    # 1. Centres alignment
    diff_mean_median_pct = abs(mean_val - median_val) / (std_val if std_val != 0 else 1.0)
    centres_aligned = diff_mean_median_pct < 0.2

    # 2. Skewness and Kurtosis rule of thumb (-1 to +1)
    shape_normal = (-1.0 <= skew_val <= 1.0) and (-1.0 <= kurt_val <= 1.0)

    # 3. Shapiro-Wilk decision
    shapiro_normal = shapiro_p > 0.05

    is_normal = centres_aligned and shape_normal and shapiro_normal

    return {
        "variable": var_name,
        "n_valid": n_valid,
        "n_missing": n_missing,
        "pct_missing": round((n_missing / len(series)) * 100, 2),
        "mean": round(mean_val, 4),
        "median": round(median_val, 4),
        "mode_rounded": round(mode_val, 4),
        "std": round(std_val, 4),
        "var": round(var_val, 4),
        "min": round(min_val, 4),
        "max": round(max_val, 4),
        "q25": round(q25, 4),
        "q75": round(q75, 4),
        "iqr": round(iqr_val, 4),
        "skewness": round(skew_val, 4),
        "kurtosis": round(kurt_val, 4),
        "shapiro_w": round(float(shapiro_w), 4),
        "shapiro_p": float(shapiro_p),
        "centres_aligned": centres_aligned,
        "shape_normal": shape_normal,
        "shapiro_normal": shapiro_normal,
        "overall_normal": is_normal,
    }


def compute_categorical_univariate(series: pd.Series, var_name: str) -> dict[str, Any]:
    """
    Compute frequency distribution, percentages, and mode for nominal/ordinal variables.
    """
    valid = series.dropna()
    n_valid = len(valid)
    n_missing = series.isna().sum()

    freq = valid.value_counts(sort=True)
    pct = (freq / n_valid) * 100

    mode_cat = freq.index[0]
    mode_freq = int(freq.iloc[0])
    mode_pct = round(float(pct.iloc[0]), 2)

    table = pd.DataFrame({
        "Category": freq.index,
        "Frequency": freq.values,
        "Percent": pct.values.round(2),
    })

    return {
        "variable": var_name,
        "n_valid": n_valid,
        "n_missing": n_missing,
        "pct_missing": round((n_missing / len(series)) * 100, 2),
        "mode": mode_cat,
        "mode_frequency": mode_freq,
        "mode_percent": mode_pct,
        "table": table.to_dict(orient="records"),
    }


def run_full_univariate_suite(df: pd.DataFrame) -> dict[str, Any]:
    """
    Run the univariate battery across key variables required for Artefact 1:
    1. Sector (Nominal)
    2. Governance_Risk_Level (Ordinal)
    3. Market_Cap_Quartile (Ordinal)
    4. Profit_Margin (Continuous)
    5. ROE (Continuous)
    6. Market_Cap_B (Continuous)
    7. Total_Revenue_B (Continuous)
    8. Overall_Governance_Risk (Continuous)
    """
    results = {
        "categorical": {},
        "continuous": {},
    }

    categorical_cols = ["Sector", "Governance_Risk_Level", "Market_Cap_Quartile"]
    for col in categorical_cols:
        if col in df.columns:
            results["categorical"][col] = compute_categorical_univariate(df[col], col)

    continuous_cols = [
        "Profit_Margin",
        "ROE",
        "Market_Cap_B",
        "Total_Revenue_B",
        "Overall_Governance_Risk",
        "Beta",
    ]
    for col in continuous_cols:
        if col in df.columns:
            results["continuous"][col] = compute_continuous_univariate(df[col], col)

    return results


def format_apa_continuous_table(continuous_results: dict[str, dict]) -> pd.DataFrame:
    """Format continuous statistics into an APA 7-compliant summary table."""
    rows = []
    for var, stats_dict in continuous_results.items():
        p_str = "< .001" if stats_dict["shapiro_p"] < 0.001 else f"{stats_dict['shapiro_p']:.3f}"
        rows.append({
            "Variable": var,
            "N": stats_dict["n_valid"],
            "Mean": stats_dict["mean"],
            "Median": stats_dict["median"],
            "SD": stats_dict["std"],
            "Min": stats_dict["min"],
            "Max": stats_dict["max"],
            "IQR": stats_dict["iqr"],
            "Skewness": stats_dict["skewness"],
            "Kurtosis": stats_dict["kurtosis"],
            "Shapiro-Wilk W": stats_dict["shapiro_w"],
            "p-value": p_str,
            "Normal?": "Yes" if stats_dict["overall_normal"] else "No",
        })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    suite = run_full_univariate_suite(df)
    apa_table = format_apa_continuous_table(suite["continuous"])
    print("\n=== Continuous Variables Summary (APA Format) ===")
    print(apa_table.to_string(index=False))

    print("\n=== Categorical Variables Summary ===")
    for var, cat_stats in suite["categorical"].items():
        print(f"\n--- {var} (Mode: {cat_stats['mode']} - {cat_stats['mode_percent']}%) ---")
        print(pd.DataFrame(cat_stats["table"]).to_string(index=False))
