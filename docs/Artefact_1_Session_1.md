# Artefact 1 — Clean Database & Univariate Description Report

> **Course**: Quantitative Data Analysis (M1 – S7)  
> **Course Code**: `2627_ECO_2_EN_009` — Academic Year 2026–2027  
> **Institution**: EM Normandie Business School  
> **Lecturer**: Dr. NGUYEN Anh-Tuan  
> **Deliverable**: **Artefact 1 (20 Marks)**  
> **Accompanying Files**: `sp500_esg_jamovi.csv`, `sp500_esg_jamovi.xlsx`, `Approval_Slip.md`, `Data_Cleaning_Log.md`

---

## 1. Submission Overview & Dataset Access

This report constitutes the official submission for **Artefact 1**, fulfilling all requirements specified in Slide 41 of the course syllabus. The underlying dataset comprises $N = 503$ publicly traded corporations from the S&P 500 index for Fiscal Year 2025 (FY2025).

### Available Data Files
1. **Jamovi Ready CSV**: [`data/processed/sp500_esg_jamovi.csv`](file:///Users/david/Library/Mobile%20Documents/com~apple~CloudDocs/Etudes%20Supp/EMN%20M1%20/M1%20-%20S7/Data%20Analysis%20Quantitative/Group%20Work%20S&P%20500/data/processed/sp500_esg_jamovi.csv)
   - Formatted with standardized short headers, no spaces, no accents, and period decimals. Ready for instant import via Jamovi (`≡ menu → Open → Browse`).
2. **Jamovi / Excel Master Workbook**: [`data/processed/sp500_esg_jamovi.xlsx`](file:///Users/david/Library/Mobile%20Documents/com~apple~CloudDocs/Etudes%20Supp/EMN%20M1%20/M1%20-%20S7/Data%20Analysis%20Quantitative/Group%20Work%20S&P%20500/data/processed/sp500_esg_jamovi.xlsx)
   - Includes two dedicated sheets: `Data` (the full analytical matrix) and `Codebook_Jamovi` (detailed metadata with variable definitions and measurement types).

---

## 2. Summary of Provenance & Approval Slip (Slide 35)

- **Dataset Title**: S&P 500 Corporate Governance & Financial Performance Dataset (FY2025).
- **Producers**: Standard & Poor's, Institutional Shareholder Services (ISS), and Yahoo Finance (SEC 10-K audited filings).
- **Unit of Observation**: 1 row = 1 publicly traded S&P 500 firm ($N = 503$).
- **Research Question**: *"Does corporate governance risk (ISS QualityScore) compromise financial profitability and market valuation among S&P 500 firms, or does strong governance provide a resilience and performance premium?"*
- **Complete Details**: Refer to [`docs/Approval_Slip.md`](file:///Users/david/Library/Mobile%20Documents/com~apple~CloudDocs/Etudes%20Supp/EMN%20M1%20/M1%20-%20S7/Data%20Analysis%20Quantitative/Group%20Work%20S&P%20500/docs/Approval_Slip.md).

---

## 3. Data Cleaning Summary (Slide 39)

Prior to statistical computation, the raw extract underwent systematic verification against the 6 student traps (Slide 39):
1. **Fiserv Remediation**: Ticker updated from `FISV` to `FI` to resolve a missing observation caused by its 2023 NYSE transfer, restoring full financial and governance coverage.
2. **Zero Duplicates**: Verified 100% uniqueness across all 503 equity tickers.
3. **Negative Equity Treatment**: Identified 32 firms with undefined `ROE` due to multi-year share buybacks driving book equity below zero (e.g. AbbVie, Altria, Domino's). Documented transparently without dropping observations, using `Profit_Margin` as the universal profitability metric.
4. **Outlier Documentation**: Retained Masco Corp's authentic $58.625$ ROE while establishing the Median ($16.8\%$) as the true managerial benchmark to avoid mean distortion (Slide 21).
5. **Sector Consolidation**: Grouped 11 GICS sectors into exactly 5 nominal categories ($n = 60$ to $148$).
6. **Full Audit**: Refer to [`docs/Data_Cleaning_Log.md`](file:///Users/david/Library/Mobile%20Documents/com~apple~CloudDocs/Etudes%20Supp/EMN%20M1%20/M1%20-%20S7/Data%20Analysis%20Quantitative/Group%20Work%20S&P%20500/docs/Data_Cleaning_Log.md).

---

## 4. Univariate Description of Five Variables (Slide 41)

In accordance with course directives (*"Half the marks are for points 4–6 — the interpretation. Producing output is not analysis. Explaining it is"*), the following five variables are profiled in complete sentences adhering to statistical protocol.

### 4.1 Variable 1: `Sector` (Nominal Variable — 5 Categories)
- **Nature**: Qualitative nominal factor representing the primary industry classification of the firm. Because categories possess no mathematical rank or numerical magnitude, computing a mean or median is strictly invalid (Slide 19); the distribution must be described exclusively through frequency tables and the **mode** (Slide 20).
- **Distribution & Mode**:
  Across the $N = 503$ firms, the modal category is **Industrials & Energy**, representing $148$ firms ($29.42\%$), followed by **Consumer** with $116$ firms ($23.06\%$), **Tech & Comms** with $108$ firms ($21.47\%$), **Finance** with $71$ firms ($14.12\%$), and **Healthcare** with $60$ firms ($11.93\%$).
- **Managerial Interpretation**: The S&P 500 is structurally anchored in industrial, cyclical, and technological infrastructure rather than consumer staples or pure healthcare. Every sector retains at least 60 observations, satisfying statistical power requirements for the upcoming One-Way ANOVA in Session 3.

```
Sector Frequency Breakdown:
1. Industrials & Energy : 148 (29.4%) [MODE]
2. Consumer             : 116 (23.1%)
3. Tech & Comms         : 108 (21.5%)
4. Finance              :  71 (14.1%)
5. Healthcare           :  60 (11.9%)
Total Valid Observations: 503 (100.0%)
```

---

### 4.2 Variable 2: `Governance_Risk_Level` (Ordinal Variable — 3 Tiers)
- **Nature**: Qualitative ordinal factor classifying firms into three ordered governance risk tiers derived from the ISS Overall QualityScore: *Low* (scores 1–3, best governance), *Medium* (scores 4–6), and *High* (scores 7–10, poorest governance). While categories follow a natural sequence, intervals between tiers are not mathematically identical (Slide 13); central tendency is captured by the mode and median rank.
- **Distribution & Central Tendency**:
  Among the $496$ reporting corporations ($7$ firms unrated by ISS), the modal tier is **High Governance Risk**, encompassing $197$ firms ($39.72\%$), while **Low Governance Risk** accounts for $150$ firms ($30.24\%$) and **Medium Governance Risk** accounts for $149$ firms ($30.04\%$). The median firm falls exactly in the **Medium** tier.
- **Managerial Interpretation**: Contrary to common assumptions, nearly $40\%$ of S&P 500 corporations exhibit high institutional governance risk scores, predominantly driven by contentious executive compensation packages and shareholder rights restrictions. This substantial variance provides an ideal foundation for testing risk differentials in Session 2 (Chi-Square) and Session 4 (Regression).

---

### 4.3 Variable 3: `Profit_Margin` (Continuous Variable — Ratio Scale)
- **Nature**: Quantitative continuous ratio variable measuring net income as a proportion of total revenue for FY2025. Because zero represents a true economic threshold (break-even), ratios and parametric moments are mathematically defined (Slide 14).
- **Statistical Profile ($N = 503$)**:
  - *Central Tendency*: Mean $\bar{x} = 0.1479$ ($14.79\%$), Median $\text{Mdn} = 0.1315$ ($13.15\%$), Rounded Mode $= 0.1100$ ($11.00\%$).
  - *Dispersion*: Standard Deviation $s = 0.1856$ ($18.56\%$), Variance $s^2 = 0.0345$, Interquartile Range $IQR = 0.1446$ ($14.46\%$, spanning $Q_1 = 7.50\%$ to $Q_3 = 21.97\%$). Full range spans from $-2.3010$ (Lumentum Holdings) to $+0.7295$ (Western Digital).
  - *Shape*: Fisher-Pearson Skewness $g_1 = -5.4205$ (severe negative/left skewness), Excess Kurtosis $g_2 = 69.9129$ (extreme leptokurtosis with heavy loss-making tails).
- **Managerial Interpretation**: The median S&P 500 company generates $13.15$ cents of bottom-line profit for every dollar of turnover. However, the substantial standard deviation ($18.56\%$) relative to the mean confirms pronounced profit dispersion across business models, with a small cluster of tech/semiconductor companies posting massive margins while distressed or restructuring firms pull down the arithmetic average.

---

### 4.4 Variable 4: `ROE` (Continuous Variable — Ratio Scale)
- **Nature**: Quantitative continuous variable measuring annual net earnings generated per dollar of book equity.
- **Statistical Profile ($N = 471$ valid, $32$ negative-equity firms)**:
  - *Central Tendency*: Mean $\bar{x} = 0.3952$ ($39.52\%$), Median $\text{Mdn} = 0.1676$ ($16.76\%$), Rounded Mode $= 0.1200$ ($12.00\%$).
  - *Dispersion*: Standard Deviation $s = 2.7231$ ($272.31\%$), Interquartile Range $IQR = 0.2195$ ($21.95\%$, $Q_1 = 9.32\%$ to $Q_3 = 31.27\%$). Range spans from $-2.4003$ to $+58.6250$ (Masco Corp).
  - *Shape*: Skewness $g_1 = 20.9053$, Kurtosis $g_2 = 447.6009$.
- **Managerial Interpretation**: The massive divergence between the arithmetic mean ($39.52\%$) and the median ($16.76\%$) illustrates the textbook danger highlighted in Slide 21 (*"The mean is destroyed by outliers. The median is robust"*). Masco Corp's near-zero equity balance inflates its ROE to $5,862.5\%$, heavily distorting the mean. A manager analyzing corporate performance must rely on the median ROE of $16.76\%$ as the true representative baseline.

---

### 4.5 Variable 5: `Market_Cap_B` (Continuous Variable — Ratio Scale)
- **Nature**: Quantitative continuous ratio variable measuring the total equity market valuation in billions of USD.
- **Statistical Profile ($N = 503$)**:
  - *Central Tendency*: Mean $\bar{x} = \$147.60\text{B}$, Median $\text{Mdn} = \$44.47\text{B}$, Mode Cluster $\approx \$20.00\text{B}$.
  - *Dispersion*: Standard Deviation $s = \$490.01\text{B}$, Interquartile Range $IQR = \$71.79\text{B}$ ($Q_1 = \$22.21\text{B}$ to $Q_3 = \$94.00\text{B}$). Range spans from $\$6.48\text{B}$ to $\$5,367.15\text{B}$.
  - *Shape*: Skewness $g_1 = 7.8532$, Kurtosis $g_2 = 68.1146$.
- **Managerial Interpretation**: S&P 500 capitalization exhibits acute right-skewness (*Pareto distribution*): while half the index is valued below $\$44.5\text{B}$, a handful of multi-trillion mega-cap tech conglomerates (NVIDIA, Apple, Microsoft, Alphabet, Amazon) inflate the average valuation to $\$147.6\text{B}$. Size must therefore be modeled via quartiles (`Market_Cap_Quartile`) or logarithmic transformations in subsequent regression modeling.

---

## 5. Normality Evaluation of a Continuous Variable (`Profit_Margin`)

In strict accordance with Slide 24 (*"Three converging pieces of evidence — use all three, never just one"*), we evaluate whether `Profit_Margin` satisfies the assumption of normality:

```
========================================================================================
NORMALITY DIAGNOSTIC MATRIX: Net Profit Margin (N = 503)
========================================================================================
Test Component        Empirical Value            Normality Criterion           Verdict
----------------------------------------------------------------------------------------
1. Three Centres      Mean   = 0.1479            Mean ≈ Median ≈ Mode          VIOLATED
                      Median = 0.1315            (Centres diverge by > 0.035)
                      Mode   = 0.1100

2. Shape Parameters   Skewness = -5.42           Both strictly in [-1, +1]     VIOLATED
                      Kurtosis = 69.91           (Severe left skew & leptokurtic)

3. Formal Test        Shapiro-Wilk W = 0.6530    p > 0.05 (Fail to reject H0)  REJECTED
                      p-value < .001                                            (p < .001)
========================================================================================
FINAL VERDICT: Severe violation of normality. Parametric normality assumption REJECTED.
========================================================================================
```

### The Three Converging Pieces of Evidence Explained:
1. **Evidence 1: Comparison of the Three Centres (Slide 24)**  
   In a normal distribution, the curve is perfectly symmetric and $\text{Mean} \approx \text{Median} \approx \text{Mode}$. Here, the arithmetic mean ($0.1479$) noticeably exceeds the median ($0.1315$), which in turn exceeds the modal cluster ($0.1100$). This clear divergence indicates positive asymmetry across typical operating firms, countered by severe negative tail outliers.
2. **Evidence 2: Skewness and Kurtosis Rule of Thumb (Slide 23 & 24)**  
   The course rule of thumb dictates that both skewness and kurtosis must fall within $[-1.0, +1.0]$ for a distribution to be considered normal. `Profit_Margin` yields a skewness of $-5.42$ and an excess kurtosis of $+69.91$, violently breaching the normative boundaries due to extreme loss-making firms in cyclical sectors.
3. **Evidence 3: Graphical Inspection & Formal Shapiro-Wilk Test (Slide 24)**  
   - *Graphical Inspection*: The density plot demonstrates a sharp, narrow peak with long heavy tails, while the Normal Q-Q plot reveals severe departures from the 45-degree theoretical reference line at both extremities.
   - *Formal Test*: The Shapiro-Wilk test tests the null hypothesis $H_0$: *"The population is normally distributed"*. The test statistic is $W = 0.6530$ with a significance level of $p < .001$. Because $p < 0.05$, we decisively **reject $H_0$**.

**Methodological Implication for Sessions 2, 3, and 4**:  
Because normality is violated, Session 3 group comparisons must employ **Welch's ANOVA** or **Kruskal-Wallis** tests, with post-hoc comparisons using **Games-Howell** rather than standard Tukey HSD whenever variance homogeneity is also breached.

---

## 6. Two-Sentence Managerial Takeaways (Slide 41)

> **"Because profit margins and market valuations deviate sharply from normal distributions with high positive and negative tail skewness, managers and corporate analysts must evaluate operating performance against sector medians ($13.15\%$) rather than distorted index averages ($14.79\%$). On Monday morning, leadership should benchmark corporate governance policies not to arbitrary peer averages, but against the $39.7\%$ high-risk corporate governance cohort to preempt investor pushback on executive compensation and board independence."**

---

## 7. Jamovi Navigation Guide for Session 1

To replicate these findings directly in the Jamovi desktop environment (Slides 36–40):
1. **Import Data**: Launch Jamovi $\rightarrow$ Click `≡ menu` $\rightarrow$ `Open` $\rightarrow$ `Browse` $\rightarrow$ Select `sp500_esg_jamovi.csv`.
2. **Verify Measure Types (Slide 38)**:
   - `Ticker`: Set to `ID`.
   - `Sector`: Set to `Nominal`.
   - `Market_Cap_Quartile` & `Governance_Risk_Level`: Set to `Ordinal`.
   - `Total_Revenue_B`, `Market_Cap_B`, `Profit_Margin`, `ROE`, `Beta`, `Overall_Governance_Risk`: Set to `Continuous`.
3. **Run Descriptive Statistics (Slide 40)**:
   - Navigate to `Analyses` $\rightarrow$ `Exploration` $\rightarrow$ `Descriptives`.
   - For continuous variables: Check `Mean`, `Median`, `Mode`, `Std. deviation`, `Min`, `Max`, `IQR`, `Skewness`, `Kurtosis`, `Shapiro-Wilk`, and select `Histogram`, `Density`, and `Box plot`.
   - For categorical variables: Move `Sector` and `Governance_Risk_Level` to Variables $\rightarrow$ Check `Frequency tables` and select `Bar plot`.
4. **Save Session**: Click `≡ menu` $\rightarrow$ `Save As` $\rightarrow$ Save as `sp500_esg_session1.omv`.
