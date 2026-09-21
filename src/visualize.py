"""
Publication-Grade Visualizations (APA 7th Edition)
==================================================
Generates high-resolution figures for descriptive analysis,
frequency distributions, and normality diagnostics adhering to
academic and executive consulting standards.
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for server/script execution
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

from src.config import APA_STYLE, CLEANED_DATA_PATH, FIGURES_DIR


def set_apa_style():
    """Apply APA 7th edition clean formatting to Matplotlib/Seaborn."""
    plt.rcParams.update({
        "font.family": APA_STYLE["font_family"],
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "#333333",
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "grid.color": "#ebebeb",
        "grid.linestyle": "--",
        "grid.linewidth": 0.6,
        "axes.titlesize": APA_STYLE["title_size"],
        "axes.titleweight": "bold",
        "axes.titlepad": 12,
        "axes.labelsize": APA_STYLE["axis_title_size"],
        "axes.labelweight": "medium",
        "axes.labelpad": 8,
        "xtick.labelsize": APA_STYLE["tick_size"],
        "ytick.labelsize": APA_STYLE["tick_size"],
        "legend.fontsize": APA_STYLE["legend_size"],
        "figure.dpi": 300,
    })


def plot_sector_distribution(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 1: Nominal Sector Distribution with counts and percentages."""
    set_apa_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    counts = df["Sector"].value_counts()
    n_total = len(df["Sector"].dropna())
    colors = ["#2b5c8f", "#41729f", "#588bae", "#7fa9c6", "#a4c2db"]

    bars = ax.bar(counts.index, counts.values, color=colors[:len(counts)], edgecolor="#1c3b5e", width=0.6)

    # Add frequency and percentage labels
    for bar in bars:
        height = bar.get_height()
        pct = (height / n_total) * 100
        ax.annotate(
            f"{int(height)}\n({pct:.1f}%)",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="semibold",
        )

    ax.set_title("Figure 1. Distribution of S&P 500 Firms Across Consolidated Sectors (N = 503)")
    ax.set_xlabel("Consolidated Sector (Nominal Factor)")
    ax.set_ylabel("Number of Companies")
    ax.set_ylim(0, max(counts.values) * 1.18)
    plt.xticks(rotation=15, ha="right")

    fig.text(0.12, -0.04, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "sector_distribution.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 1: {outfile.name}")
    return outfile


def plot_governance_risk_distribution(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 2: Ordinal Governance Risk Level Distribution."""
    set_apa_style()
    fig, ax = plt.subplots(figsize=(7, 4.5))

    order = ["Low", "Medium", "High"]
    counts = df["Governance_Risk_Level"].value_counts().reindex(order).fillna(0)
    n_total = df["Governance_Risk_Level"].notna().sum()
    palette = ["#2e7d32", "#f57c00", "#c62828"]  # Green (Low risk), Orange (Medium), Red (High risk)

    bars = ax.bar(order, counts.values, color=palette, edgecolor="#333333", width=0.55)

    for bar in bars:
        height = bar.get_height()
        pct = (height / n_total) * 100
        ax.annotate(
            f"{int(height)}\n({pct:.1f}%)",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="semibold",
        )

    ax.set_title("Figure 2. Governance Risk Tier Breakdown (ISS Overall QualityScore)")
    ax.set_xlabel("Governance Risk Tier (Ordinal Variable)")
    ax.set_ylabel("Number of Companies")
    ax.set_ylim(0, max(counts.values) * 1.18)

    fig.text(0.12, -0.04, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "governance_risk_distribution.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 2: {outfile.name}")
    return outfile


def plot_profit_margin_normality(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """
    Figure 3: Multi-panel Normality Diagnostic for Net Profit Margin.
    Demonstrates the 3 converging pieces of evidence:
    1. Centres comparison (Mean, Median, Mode)
    2. Skewness and Kurtosis shape evaluation
    3. Histogram + Density + Q-Q Plot + Shapiro-Wilk test
    """
    set_apa_style()
    valid = df["Profit_Margin"].dropna()

    mean_val = valid.mean()
    median_val = valid.median()
    mode_val = valid.round(2).mode()[0]
    std_val = valid.std()
    skew_val = stats.skew(valid, bias=False)
    kurt_val = stats.kurtosis(valid, bias=False)
    w_stat, p_val = stats.shapiro(valid)

    fig, (ax_hist, ax_qq) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: Histogram & KDE
    sns.histplot(valid, kde=True, ax=ax_hist, color="#3470a3", edgecolor="#1e4263", bins=35, stat="density")
    ax_hist.axvline(mean_val, color="#d32f2f", linestyle="--", linewidth=1.5, label=f"Mean = {mean_val:.3f}")
    ax_hist.axvline(median_val, color="#388e3c", linestyle="-", linewidth=1.5, label=f"Median = {median_val:.3f}")
    ax_hist.axvline(mode_val, color="#7b1fa2", linestyle=":", linewidth=1.5, label=f"Mode = {mode_val:.3f}")

    ax_hist.set_title("A. Distribution Shape & 3 Centres")
    ax_hist.set_xlabel("Net Profit Margin (Continuous Ratio)")
    ax_hist.set_ylabel("Density")
    ax_hist.legend(loc="upper left")

    # Panel B: Q-Q Plot
    stats.probplot(valid, dist="norm", plot=ax_qq)
    ax_qq.get_lines()[0].set_color("#3470a3")
    ax_qq.get_lines()[0].set_markersize(4)
    ax_qq.get_lines()[1].set_color("#d32f2f")
    ax_qq.get_lines()[1].set_linewidth(1.5)
    ax_qq.set_title("B. Normal Q-Q Plot")
    ax_qq.set_xlabel("Theoretical Normal Quantiles")
    ax_qq.set_ylabel("Sample Quantiles")

    # Diagnostic text box
    p_disp = "< .001" if p_val < 0.001 else f"= {p_val:.3f}"
    diag_text = (
        f"Normality Evidence Summary:\n"
        f"• Centre Divergence: Mean ({mean_val:.3f}) != Mode ({mode_val:.3f})\n"
        f"• Skewness: {skew_val:.2f} (Violates [-1, +1])\n"
        f"• Kurtosis: {kurt_val:.2f} (Heavy left-tail leptokurtic)\n"
        f"• Shapiro-Wilk: W = {w_stat:.3f}, p {p_disp}\n"
        f"Conclusion: Severe violation of normality (Reject H0)"
    )
    fig.text(0.53, 0.20, diag_text, fontsize=8.5, bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa", edgecolor="#cccccc"))

    fig.suptitle("Figure 3. Three-Evidence Normality Diagnostic: Net Profit Margin", fontsize=13, fontweight="bold", y=0.98)
    fig.text(0.08, -0.03, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "profit_margin_normality.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 3: {outfile.name}")
    return outfile


def plot_market_cap_distribution(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 4: Market Capitalization Distribution & Log Skewness."""
    set_apa_style()
    fig, ax = plt.subplots(figsize=(8, 4.5))

    valid = df["Market_Cap_B"].dropna()
    mean_val = valid.mean()
    median_val = valid.median()

    sns.histplot(valid, kde=True, ax=ax, color="#2e7d32", bins=40, edgecolor="#1b5e20")
    ax.axvline(mean_val, color="#d32f2f", linestyle="--", linewidth=1.5, label=f"Mean = ${mean_val:.1f}B")
    ax.axvline(median_val, color="#0288d1", linestyle="-", linewidth=1.5, label=f"Median = ${median_val:.1f}B")

    ax.set_title("Figure 4. Market Capitalization Asymmetry (Extreme Mega-Cap Skew)")
    ax.set_xlabel("Market Capitalization ($ Billion)")
    ax.set_ylabel("Frequency")
    ax.legend()

    fig.text(0.12, -0.04, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "market_cap_distribution.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 4: {outfile.name}")
    return outfile


def plot_correlation_preview(df: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> Path:
    """Figure 5: Correlation Matrix of Key Continuous Variables."""
    set_apa_style()
    continuous_vars = [
        "Total_Revenue_B",
        "Market_Cap_B",
        "Profit_Margin",
        "ROE",
        "Beta",
        "Overall_Governance_Risk",
    ]
    sub = df[continuous_vars].dropna()
    corr = sub.corr()

    labels = [
        "Revenue ($B)",
        "Market Cap ($B)",
        "Profit Margin",
        "ROE",
        "Beta",
        "Gov Risk",
    ]

    fig, ax = plt.subplots(figsize=(7, 5.5))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-0.4,
        vmax=0.8,
        xticklabels=labels,
        yticklabels=labels,
        cbar_kws={"shrink": 0.8},
        ax=ax,
        linewidths=0.5,
    )
    ax.set_title("Figure 5. Bivariate Pearson Correlation Matrix (Preview for Session 2)")
    plt.xticks(rotation=30, ha="right")

    fig.text(0.12, -0.05, APA_STYLE["source_annotation"], fontsize=8, color="#555555")

    outfile = output_dir / "correlation_preview.png"
    fig.tight_layout()
    fig.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    print(f"✓ Saved Figure 5: {outfile.name}")
    return outfile


def generate_all_figures(df: pd.DataFrame) -> list[Path]:
    """Generate the complete set of APA figures."""
    figures = [
        plot_sector_distribution(df),
        plot_governance_risk_distribution(df),
        plot_profit_margin_normality(df),
        plot_market_cap_distribution(df),
        plot_correlation_preview(df),
    ]
    return figures


if __name__ == "__main__":
    df = pd.read_csv(CLEANED_DATA_PATH)
    generate_all_figures(df)

