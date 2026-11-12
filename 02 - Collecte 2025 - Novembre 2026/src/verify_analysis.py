"""P07: recompute the key results with independent code (hand formulas, numpy) and compare with results.json."""
import json, math
import numpy as np
import pandas as pd
from scipy import stats
from src.analysis import CSV, OUT

R = json.loads((OUT / "results.json").read_text())
d = pd.read_csv(CSV, dtype={"cik": str})
checks = []


def check(name, mine, ref, tol=1e-6):
    ok = math.isclose(mine, ref, rel_tol=tol, abs_tol=1e-9)
    checks.append((name, mine, ref, ok))


# chi-square by hand
sub = d.dropna(subset=["size_quartile"])
ct = pd.crosstab(sub.sector_group, sub.size_quartile).to_numpy().astype(float)
E = ct.sum(1, keepdims=True) * ct.sum(0, keepdims=True) / ct.sum()
chi2 = ((ct - E) ** 2 / E).sum()
check("chi2", chi2, R["s2_chi2"]["chi2"]); check("cramers_v", math.sqrt(chi2 / (ct.sum() * (min(ct.shape) - 1))), R["s2_chi2"]["cramers_v"])
# Welch t by hand
a = d.loc[d.finance_vs_other == "Finance", "net_margin_pct"].dropna().to_numpy(); b = d.loc[d.finance_vs_other == "Non-finance", "net_margin_pct"].dropna().to_numpy()
se = math.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
check("welch_t", (a.mean() - b.mean()) / se, R["s2_ttest"]["welch_t"])
sp = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
check("cohens_d", (a.mean() - b.mean()) / sp, R["s2_ttest"]["cohens_d"])
# one-way ANOVA by hand and with scipy
s = d.dropna(subset=["net_margin_pct"]); g = [x.to_numpy() for _, x in s.groupby("sector_group")["net_margin_pct"]]
grand = np.concatenate(g).mean(); ssb = sum(len(x) * (x.mean() - grand) ** 2 for x in g); ssw = sum(((x - x.mean()) ** 2).sum() for x in g)
F = (ssb / (len(g) - 1)) / (ssw / (len(s) - len(g)))
check("fisher_F", F, R["s3"]["fisher_F"]); check("fisher_F_scipy", stats.f_oneway(*g).statistic, R["s3"]["fisher_F"]); check("eta2", ssb / (ssb + ssw), R["s3"]["eta2"])
# Welch ANOVA by hand
n = np.array([len(x) for x in g]); m = np.array([x.mean() for x in g]); v = np.array([x.var(ddof=1) for x in g]); w = n / v
mw = (w * m).sum() / w.sum(); k = len(g)
A = (w * (m - mw) ** 2).sum() / (k - 1); Bc = 1 + 2 * (k - 2) / (k ** 2 - 1) * ((1 - w / w.sum()) ** 2 / (n - 1)).sum()
check("welch_F", A / Bc, R["s3"]["welch_F"])
check("kruskal_H", stats.kruskal(*g).statistic, R["s3"]["kruskal_H"])
# multiple regression by numpy
cc = d.dropna(subset=["net_margin_pct", "ln_assets", "debt_ratio_pct", "revenue_growth_pct"])
X = pd.get_dummies(cc.sector_group).drop(columns="Industrials & Energy").astype(float)
X["ln_assets"], X["debt_ratio_pct"], X["revenue_growth_pct"] = cc.ln_assets, cc.debt_ratio_pct, cc.revenue_growth_pct
X.insert(0, "const", 1.0); y = cc.net_margin_pct.to_numpy(); Xm = X.to_numpy()
beta = np.linalg.lstsq(Xm, y, rcond=None)[0]; res = y - Xm @ beta
r2 = 1 - (res ** 2).sum() / ((y - y.mean()) ** 2).sum()
check("R2", r2, R["s4_multiple"]["R2"]); check("adj_R2", 1 - (1 - r2) * (len(y) - 1) / (len(y) - Xm.shape[1]), R["s4_multiple"]["adj_R2"])
check("B_growth", beta[list(X.columns).index("revenue_growth_pct")], pd.read_csv(OUT / "s4_multiple_coefficients.csv", index_col=0).loc["revenue_growth_pct", "B"])
for nme, mine, ref, ok in checks:
    print(f"{'OK ' if ok else 'DIFF'} {nme:16s} {mine:.8g} vs {ref:.8g}")
print("ALL OK" if all(c[3] for c in checks) else "DIFFERENCES FOUND")
