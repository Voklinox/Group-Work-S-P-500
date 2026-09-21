# Systematic Data Cleaning & Audit Log (Cleaning Log)

> **Course**: Quantitative Data Analysis (M1 – S7)  
> **Coursework Deliverable**: Artefact 1 — Audit Component (Slide 39 & 41)  
> **Dataset**: S&P 500 Corporate Governance & Financial Performance (FY2025)  
> **Total Records Audited**: $N = 503$ observations, 17 raw features

---

## 1. Executive Cleaning Summary

In professional consulting and econometric modeling, an unexamined dataset produces indefensible conclusions. As established in the course doctrine (*"Garbage in, garbage out. Software never refuses to print a number. Sanity-checking output is your job"* — Slides 25 & 34), this log systematically documents all anomalies identified, the corrective actions taken, and the methodological justifications.

```
Total Raw Rows Extracted:        503
Total Cleaned Analytical Rows:   503
Duplicate Tickers / Rows:        0 (100% Unique)
Remediated Ticker Entities:      1 (Fiserv, Inc.)
Categorical Formatting Fixes:    503 (Standardized to 5 GICS groups)
Decimal / Type Harmonization:    100% Validated (Period decimal separators, numeric floats)
```

---

## 2. Granular Audit Matrix: What Was Wrong, What Was Done, Why

| # | Inspection Category (Slide 39) | Anomaly Detected in Raw Data | Corrective Action Taken | Methodological & Business Justification |
|---|---|---|---|---|
| **1** | **Missing Values in Disguise** | Row 199 (`FISV`) returned `NaN` across sector, turnover, margin, and governance scores. | Identified corporate ticker transition from `FISV` to `FI` on NYSE. Programmatically re-mapped to `FI` and populated audited FY2025 financials and ISS risk scores. | Prevents silent data attrition. Fiserv is an S&P 500 fintech market leader (\$19.09B revenue); retaining it eliminates sample truncation bias. |
| **2** | **Duplicate Rows** | Evaluated ticker column uniqueness (`df['Ticker'].is_unique`). | Zero duplicate rows detected ($503$ unique equity symbols). | Guarantees that each observation represents exactly one independent firm. |
| **3** | **Impossible / Extreme Values: ROE** | Masco Corp (`MAS`) exhibited an ROE of $58.625$ ($5,862.5\%$). | Retained raw observation without arbitrary deletion or trimming. Documented in statistical tables that $\text{Mean} = 39.5\%$ is distorted and declared the **Median ($16.8\%$)** as the official reporting metric. | Preserves empirical authenticity. Trimming eliminates real accounting phenomena (Masco had \$80M equity vs \$1B net income). Using median protects against outlier distortion (Slide 21). |
| **4** | **Structural Missingness: Negative Equity ROE** | 32 blue-chip corporations (e.g., AbbVie, Altria, AutoZone, Booking, Domino's, HP Inc.) had `NaN` for `ROE`. | Evaluated balance sheets; confirmed negative book equity driven by cumulative share repurchases (*treasury stock buybacks*). Retained `ROE` for $N = 471$ positive-equity firms, and established **Net Profit Margin** ($N = 503$ valid) as the primary cross-firm profitability benchmark. | Deleting 32 premier firms would cause severe survivorship and industry bias (Retail, Tobacco, Pharma). Profit Margin is unaffected by capital structure and valid across all 503 firms. |
| **5** | **Inconsistent Categories** | Raw data contained 11 distinct GICS sectors, exceeding the mandatory course limit of 2 to 5 nominal categories. | Mapped all 11 sectors into 5 homogeneous business groups (`Tech & Comms`, `Healthcare`, `Finance`, `Industrials & Energy`, `Consumer`). | Mandatory requirement for ANOVA (Session 3) and Chi-Square (Session 2). Prevents statistical fragmentation and ensures adequate cell frequencies ($n \ge 60$ per sector). |
| **6** | **Number Stored as Text & Formatting** | Risk of string-type formatting, thousand separators, or French comma decimals (`56,7` vs `56.7`). | Enforced standard float casting on all financial metrics, removed commas, stripped whitespace, and formatted for Jamovi import. | Prevents Jamovi from mistakenly misclassifying continuous numeric variables as Nominal factors (Slide 38 & 39). |
| **7** | **Variable Naming for Jamovi** | Column headers with spaces or special characters can disrupt statistical scripts in Jamovi/R. | Standardized all column names to strict ASCII alphanumeric format (`Ticker`, `Total_Revenue_B`, `Market_Cap_B`, `ROE`, `Profit_Margin`, `Governance_Risk_Level`). | Conforms strictly to Slide 38 requirement: *"Name — short, no spaces, no accents"*. |

---

## 3. Data Completeness Profile (Before vs. After Cleaning)

| Variable Name | Jamovi Type | Valid Observations (Raw) | Valid Observations (Cleaned) | Completeness Rate | Treatment Rationale |
|---|---|:---:|:---:|:---:|---|
| `Ticker` | ID | 503 | 503 | 100.0% | Primary key, unique |
| `Company` | Nominal | 503 | 503 | 100.0% | Complete |
| `Sector` | Nominal (5 groups) | 502 | 503 | 100.0% | Fiserv mapped to *Finance* |
| `Total_Revenue_B` | Continuous | 502 | 503 | 100.0% | Fiserv updated (\$19.09B) |
| `Market_Cap_B` | Continuous | 503 | 503 | 100.0% | Complete |
| `Market_Cap_Quartile` | Ordinal (4 tiers) | 503 | 503 | 100.0% | Perfect quartile distribution ($n \approx 126$) |
| `Profit_Margin` | Continuous | 502 | 503 | 100.0% | Primary uncorrupted profitability metric |
| `ROE` | Continuous | 471 | 471 | 93.6% | 32 firms negative equity (transparently reported) |
| `Beta` | Continuous | 498 | 499 | 99.2% | Standard 5Y monthly volatility |
| `Headcount` | Continuous | 499 | 500 | 99.4% | Full-time employees |
| `Overall_Governance_Risk` | Continuous | 495 | 496 | 98.6% | ISS composite score (1–10) |
| `Governance_Risk_Level` | Ordinal (3 tiers) | 495 | 496 | 98.6% | Low ($n=150$), Med ($n=149$), High ($n=197$) |

---

## 4. Verification Check against Costly Student Traps (Slide 42)

- [x] **Trap 1: Reporting a mean for a nominal variable**: Avoided. `Sector` is analyzed strictly via frequency distributions and mode.
- [x] **Trap 2: Setting the measure type wrong in Jamovi**: Avoided. Every variable has a documented Jamovi Measure Type in `Codebook_Jamovi`.
- [x] **Trap 3: Reading "Sig. = 0.000" as $p = 0$**: Avoided. Formatted rigorously in APA style as $p < .001$.
- [x] **Trap 4: Confusing statistical significance with strength**: Addressed. We report effect sizes ($IQR$, $SD$, Skewness, Kurtosis) alongside hypothesis tests.
- [x] **Trap 5: Copying output with no interpretation**: Addressed. Full narrative interpretations written for all variables.
- [x] **Trap 6: Stopping at the statistic**: Addressed. Formulated executive Monday-morning recommendations.
