"""Robustness checks that consolidate the weak points of the main regression (REFERENCE, not Jamovi).

Run: .venv/bin/python -m src.robustness  -> outputs/analyses_reference/s5_robustness.csv, s5_sector11_*.csv, results_robustness.json
Checks: bootstrap CI, Huber robust regression, median (quantile) regression, winsorised growth, 11 GICS sectors.
"""
import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from src.analysis import CSV, OUT

d = pd.read_csv(CSV, dtype={"cik": str})
cc = d.dropna(subset=["net_margin_pct", "ln_assets", "debt_ratio_pct", "revenue_growth_pct"]).copy()
F = "net_margin_pct ~ ln_assets + debt_ratio_pct + revenue_growth_pct + C(sector_group, Treatment('Industrials & Energy'))"
KEEP = {"revenue_growth_pct": "growth", "C(sector_group, Treatment('Industrials & Energy'))[T.Finance]": "finance", "ln_assets": "size", "debt_ratio_pct": "debt"}
rows = []


def add(name, params, se=None, p=None, lo=None, hi=None, n=None):
    for k, label in KEEP.items():
        rows.append(dict(method=name, term=label, B=params[k], SE=None if se is None else se[k], p=None if p is None else p[k],
                         ci_low=None if lo is None else lo[k], ci_high=None if hi is None else hi[k], N=n))


ols = smf.ols(F, cc).fit(); add("OLS (classic errors)", ols.params, ols.bse, ols.pvalues, ols.conf_int()[0], ols.conf_int()[1], len(cc))
h3 = smf.ols(F, cc).fit(cov_type="HC3"); add("OLS (HC3 robust errors)", h3.params, h3.bse, h3.pvalues, h3.conf_int()[0], h3.conf_int()[1], len(cc))
# bootstrap (2000 resamples of companies)
rng = np.random.default_rng(2026); y, X = ols.model.endog, ols.model.exog; names = ols.model.exog_names
bs = np.empty((2000, X.shape[1]))
for i in range(2000):
    idx = rng.integers(0, len(y), len(y)); bs[i] = np.linalg.lstsq(X[idx], y[idx], rcond=None)[0]
bsp = pd.Series(bs.mean(0), index=names); lo = pd.Series(np.percentile(bs, 2.5, axis=0), index=names); hi = pd.Series(np.percentile(bs, 97.5, axis=0), index=names)
pb = pd.Series({n: 2 * min((bs[:, i] <= 0).mean(), (bs[:, i] >= 0).mean()) for i, n in enumerate(names)})
add("OLS, bootstrap percentile CI (2000)", ols.params, pd.Series(bs.std(0, ddof=1), index=names), pb, lo, hi, len(cc))
rlm = sm.RLM(y, X, M=sm.robust.norms.HuberT()).fit(); rp = pd.Series(rlm.params, index=names); add("Huber robust regression", rp, pd.Series(rlm.bse, index=names), pd.Series(rlm.pvalues, index=names), None, None, len(cc))
q = sm.QuantReg(y, X).fit(q=.5); qp = pd.Series(q.params, index=names); add("Median (quantile 0.5) regression", qp, pd.Series(q.bse, index=names), pd.Series(q.pvalues, index=names), None, None, len(cc))
w = cc.copy(); lo_, hi_ = w.revenue_growth_pct.quantile([.01, .99]); w["revenue_growth_pct"] = w.revenue_growth_pct.clip(lo_, hi_)
wf = smf.ols(F, w).fit(); wh = smf.ols(F, w).fit(cov_type="HC3"); add("OLS, growth winsorised 1%-99% (classic)", wf.params, wf.bse, wf.pvalues, wf.conf_int()[0], wf.conf_int()[1], len(w)); add("OLS, growth winsorised 1%-99% (HC3)", wh.params, wh.bse, wh.pvalues, wh.conf_int()[0], wh.conf_int()[1], len(w))
lowg = cc[cc.revenue_growth_pct <= 50]; lg = smf.ols(F, lowg).fit(cov_type="HC3"); add("OLS HC3, growth <= 50% (no large acquisitions)", lg.params, lg.bse, lg.pvalues, lg.conf_int()[0], lg.conf_int()[1], len(lowg))
t = pd.DataFrame(rows); t.to_csv(OUT / "s5_robustness.csv", index=False)
# 11 GICS sectors
s11 = d.dropna(subset=["net_margin_pct"]); g = [x.to_numpy() for _, x in s11.groupby("sector")["net_margin_pct"]]
lev = stats.levene(*g, center="mean"); kw = stats.kruskal(*g); import statsmodels.stats.oneway as so
wel = so.anova_oneway(g, use_var="unequal", welch_correction=True); fi = stats.f_oneway(*g)
grand = np.concatenate(g).mean(); ssb = sum(len(x) * (x.mean() - grand) ** 2 for x in g); sst = ((np.concatenate(g) - grand) ** 2).sum()
m11 = smf.ols("net_margin_pct ~ ln_assets + debt_ratio_pct + revenue_growth_pct + C(sector, Treatment('Industrials'))", cc).fit()
r = dict(n_sectors=len(g), levene_p=lev.pvalue, fisher_F=fi.statistic, fisher_p=fi.pvalue, welch_F=wel.statistic, welch_p=wel.pvalue, eta2=ssb / sst, kruskal_H=kw.statistic, kruskal_p=kw.pvalue,
         reg11_R2=m11.rsquared, reg11_growth_B=m11.params["revenue_growth_pct"], reg11_growth_p=m11.pvalues["revenue_growth_pct"], reg11_size_p=m11.pvalues["ln_assets"], reg11_debt_p=m11.pvalues["debt_ratio_pct"],
         reg11_financials_B=m11.params["C(sector, Treatment('Industrials'))[T.Financials]"], reg11_financials_p=m11.pvalues["C(sector, Treatment('Industrials'))[T.Financials]"])
pd.DataFrame(smf.ols("net_margin_pct ~ ln_assets + debt_ratio_pct + revenue_growth_pct + C(sector, Treatment('Industrials'))", cc).fit().summary2().tables[1]).to_csv(OUT / "s5_sector11_regression.csv")
(OUT / "results_robustness.json").write_text(json.dumps({k: float(v) for k, v in r.items()}, indent=2))
pd.set_option("display.width", 200)
print(t[t.term.isin(["growth", "finance"])].round(3).to_string(index=False))
print(json.dumps({k: round(float(v), 4) for k, v in r.items()}, indent=1))
