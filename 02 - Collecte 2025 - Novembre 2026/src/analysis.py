"""Reference analyses for sessions 1-4 (label: REFERENCE, not Jamovi output).

Run: .venv/bin/python -m src.analysis   (needs requirements-analysis.txt)
Input : data/processed/sp500_2025_JAMOVI.csv   (SHA-256 recorded in results.json)
Output: outputs/analyses_reference/*.csv, results.json ; outputs/figures_reference/*.png
Conventions follow the course: alpha = 0.05, Shapiro-Wilk and Levene "opposite logic", Cramer's V, Pearson and
Spearman, Student/Welch, Fisher/Welch/Kruskal-Wallis with Tukey/Games-Howell/DSCF, eta squared, OLS with B and beta.
"""
import hashlib, json, math
from itertools import combinations
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.oneway import anova_oneway
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data/processed/sp500_2025_JAMOVI.csv"
OUT = ROOT / "outputs/analyses_reference"
FIG = ROOT / "outputs/figures_reference"
CONT = ["net_margin_pct", "roa_pct", "ln_assets", "debt_ratio_pct", "revenue_growth_pct", "asset_turnover"]
R = {}


def save(df, name, index=False):
    df.to_csv(OUT / name, index=index)


def describe(s):
    v = s.dropna()
    sw = stats.shapiro(v)
    return dict(N=len(v), missing=int(s.isna().sum()), mean=v.mean(), median=v.median(), mode=float(v.round(0).mode().iloc[0]), sd=v.std(), min=v.min(), q1=v.quantile(.25), q3=v.quantile(.75), max=v.max(),
                skewness=stats.skew(v, bias=False), excess_kurtosis=stats.kurtosis(v, bias=False), shapiro_W=sw.statistic, shapiro_p=sw.pvalue)


# ---------------------------------------------------------------- Session 1
def session1(d):
    rows = {c: describe(d[c]) for c in ["net_margin_pct", "roa_pct", "debt_ratio_pct", "revenue_growth_pct", "ln_assets", "asset_turnover"]}
    t = pd.DataFrame(rows).T
    save(t, "s1_descriptives_continuous.csv", index=True)
    for c in ("sector_group", "size_quartile", "finance_vs_other", "profitable"):
        f = d[c].value_counts(dropna=False).rename("n").to_frame()
        f["pct"] = 100 * f["n"] / f["n"].sum()
        save(f, f"s1_frequency_{c}.csv", index=True)
    R["s1"] = {c: {k: float(v) for k, v in rows[c].items()} for c in rows}
    for c, label in (("net_margin_pct", "Net margin (%)"), ("debt_ratio_pct", "Debt ratio (%)"), ("revenue_growth_pct", "Revenue growth (%)")):
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.4), gridspec_kw={"width_ratios": [3, 1]})
        v = d[c].dropna()
        ax[0].hist(v, bins=40, color="#4C72B0", edgecolor="white")
        ax[0].axvline(v.mean(), color="#C44E52", ls="--", label=f"mean {v.mean():.1f}")
        ax[0].axvline(v.median(), color="#55A868", ls="-", label=f"median {v.median():.1f}")
        ax[0].set_title(f"{label}: histogram (N = {len(v)})"); ax[0].legend(); ax[0].set_xlabel(label)
        ax[1].boxplot(v, vert=True); ax[1].set_title("Box plot")
        fig.tight_layout(); fig.savefig(FIG / f"s1_hist_box_{c}.png", dpi=150); plt.close(fig)
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    d["sector_group"].value_counts().sort_values().plot.barh(ax=ax, color="#4C72B0")
    ax.set_title("Companies by sector group (N = 500)"); fig.tight_layout(); fig.savefig(FIG / "s1_bar_sector_group.png", dpi=150); plt.close(fig)
    fig, ax = plt.subplots(figsize=(5, 3.2))
    d["size_quartile"].value_counts().sort_index().plot.bar(ax=ax, color="#4C72B0", rot=0)
    ax.set_title("Size quartile (total assets), N = 498"); fig.tight_layout(); fig.savefig(FIG / "s1_bar_size_quartile.png", dpi=150); plt.close(fig)


# ---------------------------------------------------------------- Session 2
def cramer_v(ct):
    chi2, p, dof, exp = stats.chi2_contingency(ct, correction=False)
    n = ct.values.sum()
    k = min(ct.shape) - 1
    return chi2, dof, p, math.sqrt(chi2 / (n * k)), exp


def session2(d):
    sub = d.dropna(subset=["size_quartile"])
    ct = pd.crosstab(sub["sector_group"], sub["size_quartile"])
    chi2, dof, p, v, exp = cramer_v(ct)
    save(ct, "s2_chi2_observed.csv", index=True)
    save(pd.DataFrame(exp, index=ct.index, columns=ct.columns), "s2_chi2_expected.csv", index=True)
    save((100 * ct.div(ct.sum(axis=1), axis=0)), "s2_chi2_row_pct.csv", index=True)
    R["s2_chi2"] = dict(N=int(ct.values.sum()), chi2=chi2, df=int(dof), p=p, cramers_v=v, min_expected=float(exp.min()), cells_below_5=int((exp < 5).sum()))
    fig, ax = plt.subplots(figsize=(7, 3.6))
    (100 * ct.div(ct.sum(axis=1), axis=0)).plot.bar(stacked=True, ax=ax, rot=15, colormap="Blues")
    ax.set_ylabel("% within sector group"); ax.set_title("Size quartile within each sector group (row %)"); ax.legend(title="Quartile", bbox_to_anchor=(1, 1))
    fig.tight_layout(); fig.savefig(FIG / "s2_chi2_row_pct.png", dpi=150); plt.close(fig)
    # correlations
    pear, spear, npair = {}, {}, {}
    rows = []
    for a, b in combinations(CONT, 2):
        s = d[[a, b]].dropna()
        pr, pp = stats.pearsonr(s[a], s[b]); sr, sp = stats.spearmanr(s[a], s[b])
        rows.append(dict(var1=a, var2=b, N=len(s), pearson_r=pr, pearson_p=pp, spearman_rho=sr, spearman_p=sp))
    cm = pd.DataFrame(rows)
    save(cm, "s2_correlations_pairs.csv")
    save(d[CONT].corr(method="pearson"), "s2_correlation_matrix_pearson.csv", index=True)
    save(d[CONT].corr(method="spearman"), "s2_correlation_matrix_spearman.csv", index=True)
    R["s2_corr"] = cm.set_index(["var1", "var2"]).to_dict("index") and {f"{a}|{b}": r for (a, b), r in cm.set_index(["var1", "var2"]).to_dict("index").items()}
    for a, b in (("net_margin_pct", "revenue_growth_pct"), ("net_margin_pct", "ln_assets")):
        s = d[[a, b]].dropna()
        fig, ax = plt.subplots(figsize=(5.4, 4))
        ax.scatter(s[b], s[a], s=10, alpha=.6, color="#4C72B0")
        m, c0 = np.polyfit(s[b], s[a], 1); xs = np.linspace(s[b].min(), s[b].max(), 50); ax.plot(xs, m * xs + c0, color="#C44E52")
        ax.set_xlabel(b); ax.set_ylabel(a); ax.set_title(f"{a} vs {b} (N = {len(s)}); line = OLS")
        fig.tight_layout(); fig.savefig(FIG / f"s2_scatter_{a}_{b}.png", dpi=150); plt.close(fig)
    # t-test Finance vs Non-finance on net margin
    g1 = d.loc[d.finance_vs_other == "Finance", "net_margin_pct"].dropna(); g2 = d.loc[d.finance_vs_other == "Non-finance", "net_margin_pct"].dropna()
    lev = stats.levene(g1, g2, center="mean"); levm = stats.levene(g1, g2, center="median")
    st = stats.ttest_ind(g1, g2, equal_var=True); we = stats.ttest_ind(g1, g2, equal_var=False); mw = stats.mannwhitneyu(g1, g2, alternative="two-sided")
    sp = math.sqrt(((len(g1) - 1) * g1.var() + (len(g2) - 1) * g2.var()) / (len(g1) + len(g2) - 2))
    dcoh = (g1.mean() - g2.mean()) / sp
    dfw = (g1.var() / len(g1) + g2.var() / len(g2)) ** 2 / ((g1.var() / len(g1)) ** 2 / (len(g1) - 1) + (g2.var() / len(g2)) ** 2 / (len(g2) - 1))
    se = math.sqrt(g1.var() / len(g1) + g2.var() / len(g2)); ci = (g1.mean() - g2.mean() + np.array([-1, 1]) * stats.t.ppf(.975, dfw) * se)
    R["s2_ttest"] = dict(n_finance=len(g1), n_other=len(g2), mean_finance=g1.mean(), mean_other=g2.mean(), sd_finance=g1.std(), sd_other=g2.std(), median_finance=g1.median(), median_other=g2.median(),
                         levene_mean_F=lev.statistic, levene_mean_p=lev.pvalue, levene_median_F=levm.statistic, levene_median_p=levm.pvalue,
                         student_t=st.statistic, student_df=len(g1) + len(g2) - 2, student_p=st.pvalue, welch_t=we.statistic, welch_df=dfw, welch_p=we.pvalue,
                         mean_diff=g1.mean() - g2.mean(), welch_ci_low=ci[0], welch_ci_high=ci[1], cohens_d=dcoh, mannwhitney_U=mw.statistic, mannwhitney_p=mw.pvalue,
                         shapiro_finance_p=stats.shapiro(g1).pvalue, shapiro_other_p=stats.shapiro(g2).pvalue)
    fig, ax = plt.subplots(figsize=(4.6, 3.8)); ax.boxplot([g1, g2], labels=["Finance", "Non-finance"]); ax.set_ylabel("Net margin (%)"); ax.set_title("Net margin: Finance vs Non-finance")
    fig.tight_layout(); fig.savefig(FIG / "s2_box_finance_vs_other.png", dpi=150); plt.close(fig)


# ---------------------------------------------------------------- Session 3
def games_howell(groups):
    names = list(groups)
    rows = []
    k = len(names)
    for a, b in combinations(names, 2):
        x, y = groups[a], groups[b]
        va, vb = x.var(ddof=1) / len(x), y.var(ddof=1) / len(y)
        se = math.sqrt(va + vb); t = (x.mean() - y.mean()) / se
        df = (va + vb) ** 2 / (va ** 2 / (len(x) - 1) + vb ** 2 / (len(y) - 1))
        p = stats.studentized_range.sf(abs(t) * math.sqrt(2), k, df)
        rows.append(dict(group1=a, group2=b, mean_diff=x.mean() - y.mean(), se=se, t=t, df=df, p_games_howell=p))
    return pd.DataFrame(rows)


def dscf(groups):
    names = list(groups); k = len(names); rows = []
    for a, b in combinations(names, 2):
        x, y = groups[a].to_numpy(), groups[b].to_numpy()
        n1, n2 = len(x), len(y); n = n1 + n2
        r = stats.rankdata(np.concatenate([x, y]))
        _, counts = np.unique(np.concatenate([x, y]), return_counts=True)
        ties = (counts ** 3 - counts).sum()
        mean = n1 * (n + 1) / 2
        var = n1 * n2 / 12 * ((n + 1) - ties / (n * (n - 1)))
        w = (r[:n1].sum() - mean) / math.sqrt(var)
        rows.append(dict(group1=a, group2=b, W=w, p_dscf=stats.studentized_range.sf(abs(w) * math.sqrt(2), k, np.inf)))
    return pd.DataFrame(rows)


def session3(d):
    s = d.dropna(subset=["net_margin_pct"])
    order = ["Consumer", "Finance", "Healthcare", "Industrials & Energy", "Tech & Comms"]
    groups = {g: s.loc[s.sector_group == g, "net_margin_pct"] for g in order}
    desc = pd.DataFrame({g: dict(N=len(v), mean=v.mean(), sd=v.std(), se=v.std() / math.sqrt(len(v)), median=v.median(), min=v.min(), max=v.max(), skew=stats.skew(v), shapiro_p=stats.shapiro(v).pvalue) for g, v in groups.items()}).T
    save(desc, "s3_group_descriptives.csv", index=True)
    lev_mean = stats.levene(*groups.values(), center="mean"); lev_med = stats.levene(*groups.values(), center="median")
    ols = smf.ols("net_margin_pct ~ C(sector_group)", s).fit(); aov = anova_lm(ols, typ=1)
    ss_b, ss_w = aov.loc["C(sector_group)", "sum_sq"], aov.loc["Residual", "sum_sq"]
    save(aov, "s3_anova_table.csv", index=True)
    welch = anova_oneway([v.to_numpy() for v in groups.values()], use_var="unequal", welch_correction=True)
    kw = stats.kruskal(*groups.values()); N = len(s)
    tuk = pd.DataFrame(sm.stats.multicomp.pairwise_tukeyhsd(s["net_margin_pct"], s["sector_group"]).summary().data[1:], columns=["group1", "group2", "mean_diff", "p_tukey", "lower", "upper", "reject"])
    gh = games_howell(groups); ds = dscf(groups)
    save(tuk, "s3_posthoc_tukey.csv"); save(gh, "s3_posthoc_games_howell.csv"); save(ds, "s3_posthoc_dscf.csv")
    R["s3"] = dict(N=N, k=len(groups), levene_mean_F=lev_mean.statistic, levene_mean_p=lev_mean.pvalue, levene_median_F=lev_med.statistic, levene_median_p=lev_med.pvalue,
                   fisher_F=aov.loc["C(sector_group)", "F"], fisher_df1=int(aov.loc["C(sector_group)", "df"]), fisher_df2=int(aov.loc["Residual", "df"]), fisher_p=aov.loc["C(sector_group)", "PR(>F)"],
                   eta2=ss_b / (ss_b + ss_w), welch_F=welch.statistic, welch_df1=welch.df_num, welch_df2=welch.df_denom, welch_p=welch.pvalue,
                   kruskal_H=kw.statistic, kruskal_p=kw.pvalue, epsilon2=kw.statistic / (N - 1))
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.boxplot([groups[g] for g in order], labels=[g.replace(" & ", "\n& ") for g in order], showmeans=True)
    ax.set_ylabel("Net margin (%)"); ax.set_title("Net margin by sector group"); fig.tight_layout(); fig.savefig(FIG / "s3_box_margin_by_sector.png", dpi=150); plt.close(fig)
    zoom = (-60, 80)
    fig, ax = plt.subplots(figsize=(7, 3.8)); ax.boxplot([groups[g] for g in order], labels=[g.replace(" & ", "\n& ") for g in order], showmeans=True); ax.set_ylim(*zoom)
    ax.set_title(f"Same plot, y-axis limited to {zoom[0]}..{zoom[1]} (outliers beyond are not shown)"); fig.tight_layout(); fig.savefig(FIG / "s3_box_margin_by_sector_zoom.png", dpi=150); plt.close(fig)


# ---------------------------------------------------------------- Session 4
def regression(df, formula, tag, ref="Industrials & Energy"):
    m = smf.ols(formula, df).fit()
    mh = smf.ols(formula, df).fit(cov_type="HC3")
    z = df.copy()
    for c in ("net_margin_pct", "roa_pct", "ln_assets", "debt_ratio_pct", "revenue_growth_pct", "asset_turnover"):
        if c in z: z[c] = (z[c] - z[c].mean()) / z[c].std()
    beta = smf.ols(formula, z).fit().params
    ci = m.conf_int()
    coef = pd.DataFrame(dict(B=m.params, SE=m.bse, t=m.tvalues, p=m.pvalues, ci_low=ci[0], ci_high=ci[1], beta_std=beta, SE_HC3=mh.bse, p_HC3=mh.pvalues))
    save(coef, f"s4_{tag}_coefficients.csv", index=True)
    X = m.model.exog; vif = {n: variance_inflation_factor(X, i) for i, n in enumerate(m.model.exog_names) if n != "Intercept"}
    infl = m.get_influence(); cook = infl.cooks_distance[0]
    top = pd.DataFrame(dict(company=df.loc[m.model.data.row_labels, "company"].values, cooks_d=cook)).sort_values("cooks_d", ascending=False).head(10)
    save(top, f"s4_{tag}_top_cooks_distance.csv")
    bp = het_breuschpagan(m.resid, X)
    res = dict(N=int(m.nobs), R2=m.rsquared, adj_R2=m.rsquared_adj, F=m.fvalue, df1=int(m.df_model), df2=int(m.df_resid), p_F=m.f_pvalue, durbin_watson=durbin_watson(m.resid),
               shapiro_resid_W=stats.shapiro(m.resid).statistic, shapiro_resid_p=stats.shapiro(m.resid).pvalue, breusch_pagan_LM=bp[0], breusch_pagan_p=bp[1], max_cooks_d=float(cook.max()),
               max_vif=max(vif.values()) if vif else None, vif=vif)
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
    ax[0].scatter(m.fittedvalues, m.resid, s=9, alpha=.6); ax[0].axhline(0, color="#C44E52"); ax[0].set_xlabel("Fitted values"); ax[0].set_ylabel("Residuals"); ax[0].set_title("Residuals vs fitted")
    sm.qqplot(m.resid, line="45", fit=True, ax=ax[1], markersize=3); ax[1].set_title("Q-Q plot of residuals")
    fig.tight_layout(); fig.savefig(FIG / f"s4_{tag}_diagnostics.png", dpi=150); plt.close(fig)
    return m, res


def session4(d):
    simple_df = d.dropna(subset=["net_margin_pct", "ln_assets"])
    _, R["s4_simple"] = regression(simple_df, "net_margin_pct ~ ln_assets", "simple")
    cc = d.dropna(subset=["net_margin_pct", "ln_assets", "debt_ratio_pct", "revenue_growth_pct"])
    f = "net_margin_pct ~ ln_assets + debt_ratio_pct + revenue_growth_pct + C(sector_group, Treatment('Industrials & Energy'))"
    m, R["s4_multiple"] = regression(cc, f, "multiple")
    m0 = smf.ols("net_margin_pct ~ ln_assets + debt_ratio_pct + revenue_growth_pct", cc).fit()
    R["s4_compare"] = dict(R2_continuous_only=m0.rsquared, adj_R2_continuous_only=m0.rsquared_adj, R2_with_sector=m.rsquared, adj_R2_with_sector=m.rsquared_adj,
                           F_change=float(((m.rsquared - m0.rsquared) / 4) / ((1 - m.rsquared) / m.df_resid)), p_change=float(stats.f.sf(((m.rsquared - m0.rsquared) / 4) / ((1 - m.rsquared) / m.df_resid), 4, m.df_resid)))
    # sensitivities
    _, R["s4_sens_roa"] = regression(cc, f.replace("net_margin_pct", "roa_pct"), "sens_roa")
    infl = m.get_influence().cooks_distance[0]; keep = cc.loc[m.model.data.row_labels][infl <= 4 / len(cc)]
    _, R["s4_sens_no_influential"] = regression(keep, f, "sens_no_influential")
    nf = cc[cc.sector_group != "Finance"]
    _, R["s4_sens_no_finance"] = regression(nf, "net_margin_pct ~ ln_assets + debt_ratio_pct + revenue_growth_pct + C(sector_group, Treatment('Industrials & Energy'))", "sens_no_finance")
    w = cc[(cc.net_margin_pct > cc.net_margin_pct.quantile(.01)) & (cc.net_margin_pct < cc.net_margin_pct.quantile(.99))]
    _, R["s4_sens_trim_1pct"] = regression(w, f, "sens_trim_1pct")
    # prediction example within the observed range
    ex = pd.DataFrame(dict(ln_assets=[cc.ln_assets.median()], debt_ratio_pct=[cc.debt_ratio_pct.median()], revenue_growth_pct=[cc.revenue_growth_pct.median()], sector_group=["Finance"]))
    R["s4_example_prediction_finance_median"] = float(m.predict(ex).iloc[0])


def main():
    OUT.mkdir(parents=True, exist_ok=True); FIG.mkdir(parents=True, exist_ok=True)
    d = pd.read_csv(CSV, dtype={"cik": str})
    R["input"] = dict(file=str(CSV.relative_to(ROOT)), sha256=hashlib.sha256(CSV.read_bytes()).hexdigest(), rows=len(d),
                      versions=dict(pandas=pd.__version__, numpy=np.__version__, scipy=__import__("scipy").__version__, statsmodels=sm.__version__, matplotlib=matplotlib.__version__))
    session1(d); session2(d); session3(d); session4(d)
    def clean(o):
        if isinstance(o, dict): return {str(k): clean(v) for k, v in o.items()}
        if isinstance(o, (np.floating, np.integer)): return o.item()
        return o
    (OUT / "results.json").write_text(json.dumps(clean(R), indent=2, default=float))
    print("done:", len(list(OUT.glob('*'))), "tables,", len(list(FIG.glob('*.png'))), "figures")


if __name__ == "__main__":
    main()
