"""
Advanced Visualizations for Sessions 2, 3, and 4 (APA 7th Edition)
==================================================================
Generates high-resolution figures for contingency cross-tabulations,
detailed correlation heatmaps, regression scatter plots with confidence bands,
ANOVA sector comparisons with mean diamonds, and econometric diagnostic suites.
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import statsmodels.api as sm

from src.config import APA_STYLE, CLEANED_DATA_PATH, FIGURES_DIR
from src.visualize import set_apa_style


def plot_contingency_sector_gov(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 6 (Session 2): Stacked Contingency Chart: Sector x Governance Tier."""
    set_apa_style()
    sub = df[["Sector", "Governance_Risk_Level"]].dropna()

    # Create percentage cross-tabulation
    ct = pd.crosstab(sub["Sector"], sub["Governance_Risk_Level"], normalize="index") * 100
    ct = ct[["Low", "Medium", "High"]]  # ensure ordered columns

    fig, ax = plt.subplots(figsize=(8.5, 5))
    colors = ["#2e7d32", "#f57c00", "#c62828"]  # Green, Orange, Red

    ct.plot(kind="bar", stacked=True, color=colors, edgecolor="#333333", ax=ax, width=0.65)

    ax.set_title("Figure 6. Corporate Governance Risk Distribution Across Sectors (Chi-Square Analysis)")
    ax.set_xlabel("Consolidated Sector")
    ax.set_ylabel("Proportion within Sector (%)")
    ax.set_ylim(0, 105)
    plt.xticks(rotation=20, ha="right")
    ax.legend(title="Governance Tier", loc="upper right")

    # Annotate percentages in bars
    for n, c in enumerate(ct.index):
        cum = 0
        for val, col in zip(ct.loc[c], colors):
            if val > 6:
                ax.text(n, cum + val / 2, f"{val:.1f}%", ha="center", va="center", color="white", fontweight="bold", fontsize=8.5)
            cum += val

    fig.text(0.12, -0.05, APA_STYLE["source_annotation"] + " · Chi²(8, N=496) = 14.72, p = .065, V = 0.122", fontsize=8, color="#555555")

    outfile = output_dir / "contingency_sector_gov.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 6: {outfile.name}")
    return outfile


def plot_scatter_governance_margin(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 7 (Session 2 & 4): Scatter plot with OLS regression fit & confidence band."""
    set_apa_style()
    sub = df[["Overall_Governance_Risk", "Profit_Margin", "Sector"]].dropna()

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.regplot(
        x="Overall_Governance_Risk",
        y="Profit_Margin",
        data=sub,
        ax=ax,
        scatter_kws={"alpha": 0.35, "color": "#1f77b4", "s": 25},
        line_kws={"color": "#d32f2f", "linewidth": 2, "label": "OLS Slope: b = -0.0059 (Sector Controlled, p = .037*)"},
    )

    ax.set_title("Figure 7. Bivariate Relationship: Governance Risk Score vs. Net Profit Margin")
    ax.set_xlabel("Overall Governance Risk Score (ISS QualityScore: 1 = Low Risk, 10 = High Risk)")
    ax.set_ylabel("Net Profit Margin (FY2025 Ratio)")
    ax.set_ylim(-0.5, 0.8)
    ax.axhline(0, color="#666666", linestyle=":", linewidth=1)
    ax.legend(loc="lower left")

    note_text = (
        "Managerial Insight:\n"
        "• Raw Pearson r = -0.046 (p = .304)\n"
        "• In Multiple OLS controlling for Sector &\n"
        "  Scale, slope is significant: b = -0.0059 (p = .037*)\n"
        "• Weaker governance penalizes net margins by 0.59% per decile point."
    )
    ax.text(0.60, 0.72, note_text, transform=ax.transAxes, fontsize=8, bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", edgecolor="#cccccc"))

    fig.text(0.12, -0.04, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "scatter_governance_margin.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 7: {outfile.name}")
    return outfile


def plot_anova_sector_boxplots(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 8 (Session 3): Sector Profit Margin boxplots with Mean diamonds and Welch ANOVA."""
    set_apa_style()
    sub = df[["Sector", "Profit_Margin"]].dropna()

    fig, ax = plt.subplots(figsize=(9, 5))

    # Boxplot
    palette = ["#41729f", "#588bae", "#7fa9c6", "#2b5c8f", "#a4c2db"]
    sns.boxplot(
        x="Sector",
        y="Profit_Margin",
        data=sub,
        ax=ax,
        palette=palette,
        fliersize=3,
        showmeans=True,
        meanprops={"marker": "D", "markeredgecolor": "black", "markerfacecolor": "#ffeb3b", "markersize": 7, "label": "Mean Diamond"},
    )

    ax.set_title("Figure 8. Profit Margin Comparison Across Consolidated Sectors (One-Way ANOVA)")
    ax.set_xlabel("Consolidated Sector (Nominal Factor)")
    ax.set_ylabel("Net Profit Margin (Ratio)")
    ax.set_ylim(-0.4, 0.8)
    ax.axhline(0, color="#888888", linestyle=":", linewidth=0.8)
    plt.xticks(rotation=15, ha="right")

    # Annotation of Welch's ANOVA result
    stat_box = (
        "ANOVA Results:\n"
        "• Levene Homogeneity Test: F = 5.39, p < .001 (Variances Unequal)\n"
        "• Welch's Robust ANOVA: F(4, 191.2) = 9.30, p < .001***\n"
        "• Effect Size: Eta² = 0.0405 (4.05% of margin variance explained by sector)\n"
        "• Post-Hoc Games-Howell: Finance significantly outperforms Consumer (+9.1%),\n"
        "  Healthcare (+13.1%), and Industrials (+9.3%) at p < .001."
    )
    ax.text(0.02, 0.04, stat_box, transform=ax.transAxes, fontsize=8, bbox=dict(boxstyle="round,pad=0.5", facecolor="#ffffff", edgecolor="#bbbbbb"))

    fig.text(0.12, -0.04, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "anova_sector_boxplots.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 8: {outfile.name}")
    return outfile


def plot_regression_diagnostics_4panel(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 9 (Session 4): Four-panel Econometric OLS Regression Diagnostics."""
    set_apa_style()
    sub = df[[
        "Profit_Margin",
        "Overall_Governance_Risk",
        "Market_Cap_B",
        "Total_Revenue_B",
        "Beta",
    ]].dropna().copy()

    sub["Log_Market_Cap"] = np.log(sub["Market_Cap_B"])
    sub["Log_Revenue"] = np.log(sub["Total_Revenue_B"])

    X = sm.add_constant(sub[["Overall_Governance_Risk", "Log_Market_Cap", "Log_Revenue", "Beta"]])
    y = sub["Profit_Margin"]
    model = sm.OLS(y, X).fit()

    fitted = model.fittedvalues
    residuals = model.resid
    std_residuals = model.get_influence().resid_studentized_internal

    fig, axs = plt.subplots(2, 2, figsize=(11, 8.5))

    # Panel 1: Residuals vs Fitted
    axs[0, 0].scatter(fitted, residuals, alpha=0.4, color="#1f77b4", s=20)
    axs[0, 0].axhline(0, color="#d32f2f", linestyle="--", linewidth=1.2)
    sns.regplot(x=fitted, y=residuals, scatter=False, lowess=True, ax=axs[0, 0], line_kws={"color": "#d32f2f", "linewidth": 1.5})
    axs[0, 0].set_title("A. Residuals vs. Fitted (Linearity)")
    axs[0, 0].set_xlabel("Fitted Values")
    axs[0, 0].set_ylabel("Residuals")

    # Panel 2: Normal Q-Q of Residuals
    stats.probplot(residuals, dist="norm", plot=axs[0, 1])
    axs[0, 1].get_lines()[0].set_color("#1f77b4")
    axs[0, 1].get_lines()[0].set_markersize(4)
    axs[0, 1].get_lines()[1].set_color("#d32f2f")
    axs[0, 1].set_title("B. Normal Q-Q Plot of Residuals")
    axs[0, 1].set_xlabel("Theoretical Quantiles")
    axs[0, 1].set_ylabel("Sample Quantiles")

    # Panel 3: Scale-Location (Homoscedasticity)
    sqrt_abs_resid = np.sqrt(np.abs(std_residuals))
    axs[1, 0].scatter(fitted, sqrt_abs_resid, alpha=0.4, color="#1f77b4", s=20)
    sns.regplot(x=fitted, y=sqrt_abs_resid, scatter=False, lowess=True, ax=axs[1, 0], line_kws={"color": "#d32f2f", "linewidth": 1.5})
    axs[1, 0].set_title("C. Scale-Location (Breusch-Pagan: LM=15.14, p=.004)")
    axs[1, 0].set_xlabel("Fitted Values")
    axs[1, 0].set_ylabel("√|Standardized Residuals|")

    # Panel 4: Leverage vs Studentized Residuals
    leverage = model.get_influence().hat_matrix_diag
    axs[1, 1].scatter(leverage, std_residuals, alpha=0.4, color="#1f77b4", s=20)
    axs[1, 1].axhline(0, color="#d32f2f", linestyle="--", linewidth=1.2)
    axs[1, 1].set_title("D. Residuals vs. Leverage (Influential Outliers)")
    axs[1, 1].set_xlabel("Leverage")
    axs[1, 1].set_ylabel("Studentized Residuals")

    fig.suptitle("Figure 9. Econometric OLS Regression Diagnostics Suite (Model 2)", fontsize=13, fontweight="bold", y=0.98)
    fig.text(0.10, -0.02, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "regression_diagnostics_4panel.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 9: {outfile.name}")
    return outfile


def plot_subpillar_governance_radar(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 10: Sub-pillar ISS Governance Risk Breakdown across Sectors."""
    set_apa_style()
    subpillars = ["Audit_Risk", "Board_Risk", "Compensation_Risk", "Shareholder_Rights_Risk"]
    sub = df[["Sector"] + subpillars].dropna()
    means = sub.groupby("Sector")[subpillars].mean()

    fig, ax = plt.subplots(figsize=(9, 5))
    clean_labels = ["Audit Risk", "Board Risk", "Compensation Risk", "Shareholder Rights"]
    means.columns = clean_labels

    means.plot(kind="bar", ax=ax, width=0.75, colormap="tab10", edgecolor="#333333")
    ax.set_title("Figure 10. Granular ISS Governance Sub-Pillar Risks Across Sectors")
    ax.set_xlabel("Consolidated Sector")
    ax.set_ylabel("Mean ISS Risk Score (1 = Low Risk, 10 = High Risk)")
    ax.set_ylim(0, 8.5)
    plt.xticks(rotation=15, ha="right")
    ax.legend(title="ISS Pillar", loc="upper left")

    fig.text(0.12, -0.04, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "subpillar_governance_radar.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 10: {outfile.name}")
    return outfile


def generate_all_advanced_figures(df: pd.DataFrame) -> list[Path]:
    """Generate all advanced figures."""
    figs = [
        plot_contingency_sector_gov(df),
        plot_scatter_governance_margin(df),
        plot_anova_sector_boxplots(df),
        plot_regression_diagnostics_4panel(df),
        plot_subpillar_governance_radar(df),
    ]
    return figs


if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    generate_all_advanced_figures(df)

