"""
ANOVA & Group Comparison Engine (Session 3)
===========================================
Executes One-Way ANOVA, Levene's test of homogeneity of variances,
Welch's robust ANOVA, Kruskal-Wallis non-parametric test, effect sizes (Eta-squared),
and Games-Howell & Tukey HSD post-hoc pairwise comparisons across sectors.
"""

from typing import Any
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

from src.config import CLEANED_DATA_PATH


def compute_welch_anova(df: pd.DataFrame, continuous_var: str, group_var: str) -> dict[str, Any]:
    """
    Compute Welch's ANOVA for unequal variances across groups.
    Formula:
      w_i = n_i / s_i^2
      W = sum(w_i)
      x_bar_prime = sum(w_i * x_bar_i) / W
      F_welch = [ sum(w_i * (x_bar_i - x_bar_prime)^2) / (k - 1) ] / [ 1 + (2*(k-2)/(k^2-1)) * sum( (1/(n_i-1)) * (1 - w_i/W)^2 ) ]
    """
    sub = df[[continuous_var, group_var]].dropna()
    groups = [group[continuous_var].values for _, group in sub.groupby(group_var)]
    k = len(groups)

    n_i = np.array([len(g) for g in groups])
    x_bar_i = np.array([np.mean(g) for g in groups])
    s_i_sq = np.array([np.var(g, ddof=1) for g in groups])

    w_i = n_i / s_i_sq
    W = np.sum(w_i)
    x_bar_prime = np.sum(w_i * x_bar_i) / W

    numerator = np.sum(w_i * (x_bar_i - x_bar_prime) ** 2) / (k - 1)
    lambda_term = np.sum(((1 - w_i / W) ** 2) / (n_i - 1))
    denominator = 1 + (2 * (k - 2) / (k ** 2 - 1)) * lambda_term

    f_welch = numerator / denominator
    df1 = k - 1
    df2 = (k ** 2 - 1) / (3 * lambda_term)
    p_val = 1 - stats.f.cdf(f_welch, df1, df2)

    return {
        "f_welch": round(float(f_welch), 4),
        "df1": int(df1),
        "df2": round(float(df2), 2),
        "p_val": float(p_val),
        "p_val_apa": "< .001" if p_val < 0.001 else f"{p_val:.3f}",
    }


def compute_games_howell(df: pd.DataFrame, continuous_var: str, group_var: str) -> pd.DataFrame:
    """
    Compute Games-Howell post-hoc test for all pairwise group comparisons.
    Robust to unequal sample sizes and heterogeneous variances.
    """
    sub = df[[continuous_var, group_var]].dropna()
    grouped = sub.groupby(group_var)[continuous_var]

    group_names = list(grouped.groups.keys())
    k = len(group_names)

    means = grouped.mean().to_dict()
    vars_ = grouped.var().to_dict()
    ns = grouped.count().to_dict()

    results = []
    for i in range(k):
        for j in range(i + 1, k):
            g1, g2 = group_names[i], group_names[j]
            m1, m2 = means[g1], means[g2]
            v1, v2 = vars_[g1], vars_[g2]
            n1, n2 = ns[g1], ns[g2]

            diff = m1 - m2
            se_diff = np.sqrt((v1 / n1) + (v2 / n2))
            t_stat = diff / se_diff if se_diff != 0 else 0.0

            # Welch-Satterthwaite degrees of freedom
            dof_num = ((v1 / n1) + (v2 / n2)) ** 2
            dof_den = ((v1 / n1) ** 2 / (n1 - 1)) + ((v2 / n2) ** 2 / (n2 - 1))
            dof = dof_num / dof_den if dof_den != 0 else 1.0

            # Studentized range q statistic: q = t * sqrt(2)
            q_stat = np.abs(t_stat) * np.sqrt(2)
            # p-value approximation from studentized range distribution
            p_val = stats.studentized_range.sf(q_stat, k, dof)

            # 95% Confidence Interval for mean difference
            q_crit = stats.studentized_range.ppf(0.95, k, dof)
            margin = (q_crit / np.sqrt(2)) * se_diff
            ci_low = diff - margin
            ci_high = diff + margin

            p_apa = "< .001" if p_val < 0.001 else f"{p_val:.3f}"
            results.append({
                "Group_1": g1,
                "Group_2": g2,
                "Mean_Diff": round(float(diff), 4),
                "SE": round(float(se_diff), 4),
                "95%_CI": f"[{ci_low:.3f}, {ci_high:.3f}]",
                "t_stat": round(float(t_stat), 3),
                "p_val": p_apa,
                "Significant": p_val < 0.05,
            })

    return pd.DataFrame(results)


def run_full_anova_battery(df: pd.DataFrame, continuous_var: str, group_var: str = "Sector") -> dict[str, Any]:
    """
    Run complete ANOVA protocol on continuous_var grouped by group_var:
    1. Group descriptive summaries (N, Mean, SD, Median, IQR)
    2. Levene test of homogeneity of variances
    3. Standard One-Way ANOVA (Fisher's F) + Eta-squared effect size
    4. Welch's robust ANOVA
    5. Kruskal-Wallis non-parametric H-test
    6. Games-Howell post-hoc pairwise comparisons
    7. Tukey HSD post-hoc comparisons
    """
    sub = df[[continuous_var, group_var]].dropna()

    # 1. Group descriptives
    group_stats = sub.groupby(group_var)[continuous_var].agg(
        N="count",
        Mean="mean",
        Std="std",
        Median="median",
        IQR=lambda x: x.quantile(0.75) - x.quantile(0.25),
    ).reset_index()

    # 2. Levene's Test (center='median' is Brown-Forsythe robust test)
    groups = [group[continuous_var].values for _, group in sub.groupby(group_var)]
    levene_stat, levene_p = stats.levene(*groups, center="median")

    # 3. Standard One-Way ANOVA via OLS
    formula = f"{continuous_var} ~ C({group_var})"
    model = ols(formula, data=sub).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    ss_between = anova_table.loc[f"C({group_var})", "sum_sq"]
    ss_within = anova_table.loc["Residual", "sum_sq"]
    ss_total = ss_between + ss_within
    df_between = int(anova_table.loc[f"C({group_var})", "df"])
    df_within = int(anova_table.loc["Residual", "df"])
    f_stat = anova_table.loc[f"C({group_var})", "F"]
    p_fisher = anova_table.loc[f"C({group_var})", "PR(>F)"]

    # Eta-squared and Omega-squared
    eta_sq = ss_between / ss_total
    ms_within = ss_within / df_within
    omega_sq = (ss_between - df_between * ms_within) / (ss_total + ms_within)

    # 4. Welch's ANOVA
    welch_res = compute_welch_anova(df, continuous_var, group_var)

    # 5. Kruskal-Wallis Test
    kw_stat, kw_p = stats.kruskal(*groups)

    # 6. Games-Howell Post-Hoc
    gh_table = compute_games_howell(df, continuous_var, group_var)

    # 7. Tukey HSD
    tukey = pairwise_tukeyhsd(sub[continuous_var], sub[group_var], alpha=0.05)
    tukey_df = pd.DataFrame(
        data=tukey._results_table.data[1:],
        columns=tukey._results_table.data[0],
    )

    return {
        "variable": continuous_var,
        "group_stats": group_stats,
        "levene_stat": round(float(levene_stat), 4),
        "levene_p": float(levene_p),
        "levene_apa": "< .001" if levene_p < 0.001 else f"{levene_p:.3f}",
        "equal_variances": levene_p > 0.05,
        "f_stat": round(float(f_stat), 4),
        "df_between": df_between,
        "df_within": df_within,
        "p_fisher": float(p_fisher),
        "p_fisher_apa": "< .001" if p_fisher < 0.001 else f"{p_fisher:.3f}",
        "eta_squared": round(float(eta_sq), 4),
        "omega_squared": round(float(omega_sq), 4),
        "welch": welch_res,
        "kruskal_h": round(float(kw_stat), 4),
        "kruskal_p": float(kw_p),
        "kruskal_apa": "< .001" if kw_p < 0.001 else f"{kw_p:.3f}",
        "games_howell": gh_table,
        "tukey": tukey_df,
    }


if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)

    print("=== ANOVA: Profit Margin across Sectors ===")
    res_pm = run_full_anova_battery(df, "Profit_Margin", "Sector")
    print(f"Levene's Test: F = {res_pm['levene_stat']}, p = {res_pm['levene_apa']} (Equal variances: {res_pm['equal_variances']})")
    print(f"Standard ANOVA: F({res_pm['df_between']}, {res_pm['df_within']}) = {res_pm['f_stat']}, p = {res_pm['p_fisher_apa']}, Eta² = {res_pm['eta_squared']}")
    print(f"Welch's ANOVA: F({res_pm['welch']['df1']}, {res_pm['welch']['df2']}) = {res_pm['welch']['f_welch']}, p = {res_pm['welch']['p_val_apa']}")
    print(f"Kruskal-Wallis: H = {res_pm['kruskal_h']}, p = {res_pm['kruskal_apa']}")
    print("\nGroup Statistics:")
    print(res_pm["group_stats"].to_string(index=False))
    print("\nGames-Howell Post-Hoc Comparisons:")
    print(res_pm["games_howell"].to_string(index=False))

    print("\n\n=== ANOVA: Overall Governance Risk across Sectors ===")
    res_gov = run_full_anova_battery(df, "Overall_Governance_Risk", "Sector")
    print(f"Standard ANOVA: F({res_gov['df_between']}, {res_gov['df_within']}) = {res_gov['f_stat']}, p = {res_gov['p_fisher_apa']}, Eta² = {res_gov['eta_squared']}")
    print(f"Welch's ANOVA: F({res_gov['welch']['df1']}, {res_gov['welch']['df2']}) = {res_gov['welch']['f_welch']}, p = {res_gov['welch']['p_val_apa']}")
    print(res_gov["group_stats"].to_string(index=False))
