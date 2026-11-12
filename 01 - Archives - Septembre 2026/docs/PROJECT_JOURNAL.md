# Project Master Journal & Audit Trail (Journal de Bord)

> **Project**: S&P 500 Corporate Governance & Financial Performance Analysis
> **Course**: Quantitative Data Analysis (M1 – S7, Course code: 2627_ECO_2_EN_009)
> **Institution**: EM Normandie Business School
> **Lecturer**: Dr. NGUYEN Anh-Tuan
> **Lead Researcher**: David & Consulting Project Team
> **Academic Year**: 2026–2027
> **Language**: English (Academic & Executive Standard)

---

## 1. Executive Summary & Research Framework

### 1.1 The Managerial Problematic (Research Question)

Corporate executives, board directors, and ESG fund managers face an ongoing debate: _Does dedicating significant capital and operational focus to institutional corporate governance and social responsibility enhance shareholder value, or does it impose costly bureaucratic frictions that compromise financial profitability?_

To resolve this question empirically, this project establishes a 4-week analytical trajectory centered on:

> **"Does corporate governance risk (ISS QualityScore) compromise financial profitability and market valuation among S&P 500 firms, or does strong governance provide a resilience and performance premium?"**

### 1.2 The 4-Step Answering Protocol

In accordance with course guidelines (Slide 9 & Slide 41), every hypothesis and statistical result follows a strict four-step protocol:

1. **IDENTIFY**: Justify the statistical test exclusively from the measurement scale of the variables (Nominal, Ordinal, Continuous).
2. **HYPOTHESISE**: Formulate the Null ($H_0$) and Alternative ($H_1$) hypotheses in plain business language.
3. **DECIDE**: Evaluate the significance level ($\alpha = 0.05$, report exact $p$-value or $p < .001$) and assess the magnitude/effect size ($r$, $\eta^2$, Cramér's $V$, $R^2$).
4. **RECOMMEND**: Provide concrete operational directives answering: _"What does the manager do on Monday morning?"_

---

## 2. Chronological Log of Project Milestones

| Date & Time          | Phase                      | Actions Performed                                                                                                 | Status    |
| -------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------- |
| **2026-09-21 11:38** | Project Inception          | Initial virtual environment `.venv` and preliminary requirements established.                                     | Completed |
| **2026-09-21 11:48** | Data Scrape (Initial)      | Initial execution of `extract_sp500_esg.py` pulling 503 S&P 500 tickers via `yfinance`.                           | Completed |
| **2026-09-21 18:07** | Diagnostic Review          | Full audit of course brief `AQD_Session1 copie.pdf` and existing repository files.                                | Completed |
| **2026-09-21 18:37** | Repository Re-architecture | Git initialized (`main` branch), directory tree restructured into `data/`, `src/`, `docs/`, `figures/`, `tests/`. | Completed |
| **2026-09-21 18:41** | Dependency Hardening       | Installed verified scientific stack: `scipy`, `statsmodels`, `matplotlib`, `seaborn`, `openpyxl`, `pytest`.       | Completed |
| **2026-09-21 18:42** | Data Cleaning Pipeline     | Automated `src/cleaning.py` executed: remediated Fiserv (`FISV` $\rightarrow$ `FI`), built Jamovi CSV & Excel.    | Completed |
| **2026-09-21 18:42** | Automated Testing          | Built and executed `tests/test_dataset_integrity.py` with `pytest` (6/6 tests passed).                            | Completed |
| **2026-09-21 18:43** | Univariate Engine          | Ran `src/stats_univariate.py` generating 3-centre statistics, dispersion, skewness, kurtosis, Shapiro-Wilk tests. | Completed |
| **2026-09-21 18:43** | APA Visualizations         | Ran `src/visualize.py` generating publication-grade figures in `figures/`.                                        | Completed |
| **2026-09-21 18:45** | Deliverable Authoring      | Authored `Approval_Slip.md`, `Data_Cleaning_Log.md`, `Artefact_1_Session_1.md`, and Jamovi guide.                 | Completed |

---

## 3. Data Provenance, Acquisition & Temporal Grounding

### 3.1 Data Sources

1. **Constituent Universe**: The list of 503 constituent companies of the S&P 500 index was scraped dynamically from the official Wikipedia directory of S&P 500 companies (maintained from S&P Dow Jones Indices releases).
2. **Corporate Governance Scores**: Sourced from **Institutional Shareholder Services (ISS)** Governance QualityScore ratings accessed via the Yahoo Finance query infrastructure.
   - Scale: Decile scores from 1 (lowest risk, highest governance quality) to 10 (highest risk, poorest governance quality).
   - Core sub-pillars: _Audit Risk_, _Board Structure Risk_, _Compensation Risk_, _Shareholder Rights Risk_, and composite _Overall Governance Risk_.
3. **Financial Fundamentals**: Extracted via Yahoo Finance API (`yfinance`), retrieving audited 10-K SEC regulatory filings.
   - Core variables: _Total Revenue ($B)_, _Market Capitalization ($B)_, _Net Profit Margin_, _Return on Equity (ROE)_, _Market Beta (5Y monthly)_, and _Headcount_.

### 3.2 Why Full Fiscal Year 2025 (FY2025)?

In empirical quantitative finance, using partial current-year figures (e.g. Q1/Q2 2026) creates severe seasonal distortion, annualized extrapolation errors, and interim accounting noise.

- **Audited Completeness**: FY2025 provides complete, 12-month audited financial statements filed with the U.S. Securities and Exchange Commission (SEC).
- **Macroeconomic Stability**: Captures the full annual economic cycle, ensuring valid comparability across sectors with contrasting seasonality (e.g., Retail peak in Q4 vs. Energy fluctuations).
- **Synchronicity**: Financial ratios for FY2025 align with Q3/Q4 2025 ISS governance evaluations, ensuring cross-sectional validity.

---

## 4. Comprehensive Data Cleaning & Remediation Audit

### 4.1 Remediation of Ticker Anomalies: Fiserv (`FISV` $\rightarrow$ `FI`)

- **Diagnosis**: In the raw extract, row 199 (`FISV`) exhibited missing values across sector, revenue, profit margin, beta, headcount, and governance risk.
- **Root Cause Analysis**: In 2023, Fiserv, Inc. transferred its listing from NASDAQ to the New York Stock Exchange (NYSE) and rebranded its ticker symbol from `FISV` to `FI`. The raw extraction script relied on the legacy ticker symbol, causing Yahoo Finance API calls to return null objects.
- **Remediation**: The pipeline programmatically maps `FISV` to `FI`, populating its proper sector (_Financial Services_ $\rightarrow$ _Finance_), FY2025 revenue (\$19.09B), profit margin (16.0%), beta (0.88), headcount (42,000), and ISS governance risk scores.

### 4.2 The Case of Negative Book Equity & Undefined ROE ($N = 32$)

- **Diagnosis**: 32 major blue-chip corporations exhibited missing values (`NaN`) in the `ROE` column.
  - Affected firms include: AbbVie (`ABBV`), Altria Group (`MO`), AutoZone (`AZO`), Booking Holdings (`BKNG`), Cardinal Health (`CAH`), Domino's Pizza (`DPZ`), Fair Isaac (`FICO`), HCA Healthcare (`HCA`), Hilton Worldwide (`HLT`), HP Inc. (`HPQ`), and Philip Morris.
- **Root Cause (Corporate Finance Theory)**:
  $$\text{ROE} = \frac{\text{Net Income}}{\text{Shareholders' Equity}}$$
  Over the past decade, these mature corporations executed aggressive, debt-financed share repurchase programs (_treasury stock buybacks_). Cumulative buybacks subtracted from retained earnings have driven total book value of equity into negative territory. When book equity is negative, computing a standard ROE yields either a mathematically positive number for loss-making firms or a negative ratio for highly profitable firms—rendering ROE economically meaningless. Consequently, standard financial databases (including Yahoo Finance and Bloomberg) suppress ROE for negative-equity firms.
- **Remediation & Pedagogical Strategy**:
  1. We do **not** arbitrarily impute or drop these corporations; doing so would delete 32 of America's most prominent firms and introduce severe selection bias.
  2. We retain `ROE` for the 471 firms where equity is positive ($N = 471$), while reporting missingness transparently.
  3. We introduce **Net Profit Margin** ($\frac{\text{Net Income}}{\text{Revenue}}$) as our co-primary profitability metric. Because revenue is always positive for operating firms, `Profit_Margin` is 100% defined for all $N = 503$ firms.

### 4.3 Extreme Outlier Treatment: Masco Corporation (`MAS`)

- **Diagnosis**: Masco Corp displayed an extreme ROE of $58.625$ ($5,862.5\%$).
- **Root Cause**: Masco held a tiny positive equity balance ($\approx \$80\text{M}$) against nearly \$1B in net profits, causing the ratio denominator to approach zero.
- **Remediation**: In accordance with course guidelines (Slide 21: _"The mean is destroyed by outliers. The median is robust to outliers and skew"_), we preserve the authentic observation without artificial truncation or winsorization. We explicitly report both the mean ($\bar{x} = 39.5\%$) and median ($\text{Mdn} = 16.8\%$) and use the median as the true managerial measure of central tendency.

### 4.4 Sector Consolidation (Course Constraint: 2 to 5 Categories)

The Global Industry Classification Standard (GICS) specifies 11 raw sectors. To satisfy the mandatory course rule (_Nominal grouping variable MUST have between 2 and 5 categories_), sectors were mapped into 5 homogeneous business groups:

1. **Industrials & Energy** ($n = 148$, $29.4\%$, **Mode**)
2. **Consumer** ($n = 116$, $23.1\%$)
3. **Tech & Comms** ($n = 108$, $21.5\%$)
4. **Finance** ($n = 71$, $14.1\%$)
5. **Healthcare** ($n = 60$, $11.9\%$)

---

## 5. Summary of Cleaned Dataset Files

1. **`data/raw/sp500_esg_dataset_raw.csv`**: Pristine original scrape preserved for replication audits.
2. **`data/processed/sp500_esg_cleaned.csv`**: Cleaned, imputed, and validated dataset for Python and R pipelines.
3. **`data/processed/sp500_esg_jamovi.csv`**: Formatted specifically for Jamovi with standardized short headers (`Ticker`, `Company`, `Sector`, `Revenue_B`, etc.).
4. **`data/processed/sp500_esg_jamovi.xlsx`**: Excel workbook featuring sheet 1 (`Data`) and sheet 2 (`Codebook_Jamovi`) with explicit variable definitions, measure types, and measurement levels.

---

## 6. Git Version Control Log

The project repository is under strict local Git version control:

- **Repository**: `Group Work S&P 500`
- **Active Branch**: `main`
- **Initial Commit**: Project baseline structure and raw data assets.
- **Pipeline Commit**: Modular data cleaning, univariate engine, APA visualizations, automated test suite, and submission documentation.
