# CLAUDE.md — AI Context & System Guidelines

> **Project**: S&P 500 ESG & Financial Performance Analysis
> **Course**: Quantitative Data Analysis (M1 – S7)
> **Team**: Group Consulting Report
> **Last Updated**: September 2026

---

## 1. Project Overview & Problematic

### Research Question (Problematic)

> **"Does environmental and social performance (ESG) compromise financial profitability among S&P 500 companies?"**

### Goal

Produce a **professional consulting report** that uses rigorous quantitative methods to answer the research question above. The report must follow academic standards (APA formatting) while maintaining a consulting-oriented tone with actionable recommendations.

### Dataset

- **Source**: Real-time extraction from Yahoo Finance via `yfinance` API.
- **Unit of observation**: 1 row = 1 S&P 500 company.
- **File**: `sp500_esg_dataset.csv`

### Variables Summary

| Variable | Name in Dataset | Type | Details |
|---|---|---|---|
| Sector (5 groups) | `Sector` | **Nominal** | Tech & Comms, Healthcare, Finance, Industrials & Energy, Consumer |
| Market Cap Quartile | `Market_Cap_Quartile` | **Ordinal** | Q1 (smallest) → Q4 (largest) |
| Governance Risk Level | `Governance_Risk_Level` | **Ordinal** | Low (1–3), Medium (4–6), High (7–10) — derived from ISS Overall Risk |
| Total Revenue (B$) | `Total_Revenue_B` | Continuous | In billions USD |
| Market Capitalization (B$) | `Market_Cap_B` | Continuous | In billions USD |
| Return on Equity | `ROE` | Continuous | Decimal (e.g., 0.15 = 15%) |
| Profit Margin | `Profit_Margin` | Continuous | Net profit margin (decimal) |
| Beta | `Beta` | Continuous | Market risk / volatility measure |
| Headcount | `Headcount` | Continuous | Full-time employees |
| Audit Risk | `Audit_Risk` | Continuous | ISS score (1–10, lower = better) |
| Board Risk | `Board_Risk` | Continuous | ISS score (1–10, lower = better) |
| Compensation Risk | `Compensation_Risk` | Continuous | ISS score (1–10, lower = better) |
| Shareholder Rights Risk | `Shareholder_Rights_Risk` | Continuous | ISS score (1–10, lower = better) |
| Overall Governance Risk | `Overall_Governance_Risk` | Continuous | ISS composite score (1–10, lower = better) |

> [!NOTE]
> **Why ISS governance scores instead of ESG?** Yahoo Finance deprecated its free Sustainalytics ESG endpoint. ISS (Institutional Shareholder Services) governance quality scores remain available and serve as a strong proxy for corporate governance quality — a core pillar of ESG. The research question can be adapted to: *"Does governance quality (ISS risk scores) relate to financial profitability among S&P 500 companies?"*

---

## 2. Strict Course Requirements (The "Must-Haves")

These are **non-negotiable** constraints imposed by the course. Every analysis and deliverable **must** satisfy them.

> [!CAUTION]
> Failing to meet any of these requirements will make the lab sessions impossible and jeopardize the grade.

| Requirement | Constraint | Status |
|---|---|---|
| **Unit of observation** | 1 row = 1 firm | ✅ |
| **Minimum observations** | ≥ 100 rows | ✅ (~500 firms) |
| **Nominal variable** | Exactly **2 to 5** categories | ✅ `Sector` has 5 groups |
| **Ordinal variable** | At least 1 | ✅ `Market_Cap_Quartile` + `Governance_Risk_Level` |
| **Continuous variables** | At least 3 | ✅ 9 continuous variables available |
| **Raw data** | No pre-processed / "cleaned for beginners" datasets | ✅ Extracted live from Yahoo Finance |

### Why the Nominal Variable Matters

The nominal variable (`Sector`) is the **grouping factor** used in:
- **Session 2**: Cross-tabulation and Chi-square tests (nominal × ordinal).
- **Session 3**: ANOVA and post-hoc tests (continuous variable grouped by nominal).

If the nominal variable has more than 5 categories, post-hoc comparisons become unmanageable and statistically underpowered. If it has fewer than 2, no grouping is possible.

---

## 3. The 4-Week Analytical Roadmap

### Session 1 — Data Cleaning & Univariate Description
**Focus**: Get the dataset ready and understand each variable in isolation.

- [ ] Import dataset and verify structure (types, dimensions).
- [ ] Handle missing values (report % missing per variable, decide strategy: drop/impute).
- [ ] Detect and treat outliers (box plots, z-scores, IQR method).
- [ ] **Univariate statistics**:
  - Continuous: mean, median, SD, skewness, kurtosis, histograms, box plots.
  - Nominal: frequency tables, bar charts.
  - Ordinal: frequency tables, bar charts (ordered).
- [ ] **Deliverable**: Clean dataset + descriptive statistics summary table.

---

### Session 2 — Bivariate Analysis: Associations
**Focus**: Test relationships between pairs of variables.

#### Nominal × Ordinal → Chi-Square Test
- [ ] Cross-tabulation: `Sector` × `Highest_Controversy_Level`.
- [ ] Cross-tabulation: `Sector` × `Market_Cap_Quartile`.
- [ ] Perform Chi-square (χ²) test of independence.
- [ ] Report: χ² statistic, degrees of freedom, p-value, Cramér's V.

#### Continuous × Continuous → Correlation
- [ ] Compute Pearson correlation matrix for all continuous variables.
- [ ] Generate a correlation heatmap.
- [ ] Test significance of key correlations (e.g., `Total_ESG_Score` vs `ROE`).
- [ ] Report: r, p-value, 95% CI.

---

### Session 3 — ANOVA & Post-Hoc Tests
**Focus**: Test whether group means differ significantly.

#### Continuous × Nominal → One-Way ANOVA
- [ ] Test: Does `ROE` differ significantly across `Sector` groups?
- [ ] Test: Does `Total_ESG_Score` differ significantly across `Sector` groups?
- [ ] Check ANOVA assumptions:
  - Normality (Shapiro-Wilk per group).
  - Homogeneity of variances (Levene's test).
- [ ] If assumptions violated → use Welch's ANOVA or Kruskal-Wallis.

#### Post-Hoc Comparisons
- [ ] Tukey HSD or Games-Howell (depending on variance homogeneity).
- [ ] Report: mean difference, 95% CI, adjusted p-value for each pair.
- [ ] Visualize with grouped box plots + significance brackets.

---

### Session 4 — Regression & Final Recommendations
**Focus**: Model predictive relationships and synthesize findings.

#### Simple & Multiple Linear Regression
- [ ] Simple regression: `ROE` ~ `Total_ESG_Score`.
- [ ] Multiple regression: `ROE` ~ `Total_ESG_Score` + `Market_Cap_B` + `Headcount`.
- [ ] Check regression assumptions:
  - Linearity (scatter plots, residual plots).
  - Normality of residuals (Q-Q plot, Shapiro-Wilk).
  - Homoscedasticity (residuals vs fitted plot, Breusch-Pagan test).
  - Multicollinearity (VIF).
- [ ] Report: R², adjusted R², F-statistic, β coefficients, SE, t, p-value.

#### Consolidated Recommendations
- [ ] Synthesize findings across all 4 sessions.
- [ ] Answer the research question with evidence.
- [ ] Provide actionable consulting recommendations.
- [ ] Discuss limitations and future research directions.

---

## 4. AI Assistant Directives

> [!IMPORTANT]
> **Any AI assistant helping with this project MUST follow these rules.**

1. **Always refer to the 4-session roadmap above.** Before generating any analysis, identify which session it belongs to and confirm that prerequisites from prior sessions are completed.

2. **Statistical output format**: All test results must be reported in **APA 7th edition** style. Examples:
   - Chi-square: *χ²*(df, *N* = n) = value, *p* = .xxx, Cramér's *V* = .xx
   - Correlation: *r*(df) = .xx, *p* = .xxx, 95% CI [.xx, .xx]
   - ANOVA: *F*(df₁, df₂) = value, *p* = .xxx, η² = .xx
   - Regression: *β* = .xx, *SE* = .xx, *t*(df) = value, *p* = .xxx

3. **Jamovi compatibility**: Suggest workflows that are compatible with the **Jamovi** statistical software (open-source, GUI-based). When the user asks for a procedure, provide:
   - The Jamovi menu path (e.g., `Analyses → ANOVA → One-Way ANOVA`).
   - Which options/checkboxes to enable.
   - How to interpret the output tables.

4. **Variable types awareness**: Always respect the variable classification table in Section 2. Do not treat ordinal variables as continuous, or nominal variables as ordinal, unless the user explicitly requests it with justification.

5. **Missing data transparency**: When running analyses, always report how many observations were excluded due to missing data and whether this could introduce bias.

6. **Visualization standards**: All charts should include:
   - Descriptive title.
   - Labeled axes with units.
   - Legend (if applicable).
   - Source annotation: "Source: S&P 500 ESG Dataset (Yahoo Finance, Sept. 2026)".

7. **Consulting tone**: The final report should balance academic rigor with a business-consulting delivery style. Avoid jargon when possible; explain statistical concepts to a non-technical stakeholder audience.

---

*This file is the single source of truth for all AI-assisted work on this project.*
