# Coursework Approval Slip — Dataset Provenance & Specification

> **Course**: Quantitative Data Analysis (M1 – S7)
> **Course Code**: `2627_ECO_2_EN_009` — Academic Year 2026–2027
> **Institution**: EM Normandie Business School
> **Lecturer**: Dr. NGUYEN Anh-Tuan
> **Grade Weight**: **10 Marks (Provenance & Dataset Quality)**
> **Submission Milestone**: Session 1 Approval Gate (Slide 35)

---

## 1. Administrative Identification

| Field                              | Description / Value                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Team Members**                   | David & Group Consulting Team (M1 S7 PGE)                                                                                     |
| **Programme & Campus**             | Programme Grande École — EM Normandie                                                                                         |
| **Dataset Title**                  | **S&P 500 Corporate Governance & Financial Performance Dataset (FY2025)**                                                     |
| **Source URL 1 (Constituents)**    | [Wikipedia S&P 500 Directory](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) (sourced from S&P Dow Jones Indices) |
| **Source URL 2 (Fundamentals)**    | [Yahoo Finance](https://finance.yahoo.com) (sourced from SEC 10-K audited annual filings)                                     |
| **Source URL 3 (Governance Risk)** | [Institutional Shareholder Services (ISS)](https://www.issgovernance.com) via Yahoo Finance API                               |
| **Producer & Year**                | Standard & Poor's, ISS Governance, and Yahoo Finance / SEC filings (Audited FY2025, ratings Q3/Q4 2025)                       |
| **Downloadable File Format**       | `.csv` (`sp500_esg_cleaned.csv` / `sp500_esg_jamovi.csv`) and `.xlsx` (`sp500_esg_jamovi.xlsx`)                               |

---

## 2. Dataset Structural Compliance (All Boxes Ticked)

| Requirement (Slide 29)                | Project Specification                                                                                                                                                                                                                                                                                                                                                  | Compliance |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------: |
| **One row = one...**                  | **One row = one publicly traded S&P 500 corporation**                                                                                                                                                                                                                                                                                                                  | ✅ **YES** |
| **$N$ (Observations)**                | **$N = 503$ firms** (exceeds the $\ge 100$ minimum threshold)                                                                                                                                                                                                                                                                                                          | ✅ **YES** |
| **Nominal Variable (2–5 categories)** | `Sector` — exactly **5 consolidated categories**:<br>1. _Industrials & Energy_ ($n=148$, $29.4\%$, Mode)<br>2. _Consumer_ ($n=116$, $23.1\%$)<br>3. _Tech & Comms_ ($n=108$, $21.5\%$)<br>4. _Finance_ ($n=71$, $14.1\%$)<br>5. _Healthcare_ ($n=60$, $11.9\%$)                                                                                                        | ✅ **YES** |
| **Ordinal Variable ($\ge 1$)**        | 1. `Governance_Risk_Level` (3 ordered tiers: Low, Medium, High)<br>2. `Market_Cap_Quartile` (4 ordered tiers: Q1, Q2, Q3, Q4)                                                                                                                                                                                                                                          | ✅ **YES** |
| **Continuous Variables ($\ge 3$)**    | 6 continuous variables available:<br>1. `Profit_Margin` (Net profit margin, FY2025)<br>2. `ROE` (Return on Equity, FY2025)<br>3. `Market_Cap_B` (Market capitalization in \$ Billion)<br>4. `Total_Revenue_B` (Annual turnover in \$ Billion)<br>5. `Beta` (Systematic risk coefficient, 5Y monthly)<br>6. `Overall_Governance_Risk` (ISS QualityScore, 1 to 10 scale) | ✅ **YES** |
| **Raw & Authentic Data**              | Live extracted from financial APIs; zero pre-processed, synthetic, or beginner datasets (Iris, Titanic, Boston Housing strictly excluded).                                                                                                                                                                                                                             | ✅ **YES** |

---

## 3. Managerial Research Question (Problematic)

> **"Does corporate governance risk (ISS QualityScore) compromise financial profitability and market valuation among S&P 500 firms, or does strong governance provide a resilience and performance premium?"**

### Alignment with the 4 Course Sessions:

- **Session 1 (Univariate)**: What are the distribution profiles, central tendencies, and dispersions of profitability and governance risk? (Skewness, kurtosis, normality checks).
- **Session 2 (Bivariate)**: Are high-risk governance firms disproportionately concentrated in certain sectors or size quartiles (Chi-Square)? Is governance risk correlated with profit margins (Pearson $r$)?
- **Session 3 (ANOVA)**: Does profitability or governance risk differ significantly across the 5 economic sectors (One-Way ANOVA & Games-Howell/Tukey HSD)?
- **Session 4 (Regression)**: Does governance risk predict profit margins when controlling for firm size (`Market_Cap_B`) and market volatility (`Beta`)?

---

## 4. Lecturer Validation Gate

```
Lecturer Name:      Dr. NGUYEN Anh-Tuan
Approval Decision:  [   ] APPROVED (10 / 10 marks awarded)
                    [   ] REVISION REQUIRED

Signature:          __________________________________________

Date:               ____ / ____ / 2026
```
