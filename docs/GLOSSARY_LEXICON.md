# S&P 500 Quantitative Data Analysis — Master Glossary & Lexicon (Lexique Complet)

> **Course**: Quantitative Data Analysis (M1 – S7, Course code: `2627_ECO_2_EN_009`)  
> **Institution**: EM Normandie Business School · Programme Grande École  
> **Lecturer**: Dr. NGUYEN Anh-Tuan  
> **Purpose**: A comprehensive, beginner-friendly bilingual guide (English concepts with detailed French explanations) covering all Financial, Data, Statistical, ESG, and Jamovi terminology used across all 4 sessions of the project.

---

## Table of Contents
1. [Data Fundamentals & Variable Typology](#1-data-fundamentals--variable-typology)
2. [Financial & Corporate Accounting Terminology](#2-financial--corporate-accounting-terminology)
3. [ESG & Corporate Governance (ISS Framework)](#3-esg--corporate-governance-iss-framework)
4. [Univariate Statistics & Shape Parameters (Session 1)](#4-univariate-statistics--shape-parameters-session-1)
5. [Bivariate Analysis & Hypothesis Testing (Session 2)](#5-bivariate-analysis--hypothesis-testing-session-2)
6. [Group Comparisons & ANOVA (Session 3)](#6-group-comparisons--anova-session-3)
7. [Regression Modeling & Econometrics (Session 4)](#7-regression-modeling--econometrics-session-4)
8. [Jamovi Software Operations & Common Pitfalls](#8-jamovi-software-operations--common-pitfalls)

---

## 1. Data Fundamentals & Variable Typology

### Unit of Observation (Unité d'observation)
* **Definition**: Exactly what a single row represents in your database.
* **In our project**: **1 row = 1 publicly traded S&P 500 company**.
* **Why it matters (Slide 11)**: If you cannot finish the sentence *"One row = one..."*, you do not understand your dataset. Having 1 row = 1 firm ensures independence of observations for ANOVA and regression.

### Sample Size ($N$ / Observation count)
* **Definition**: The total number of valid entities observed in the study.
* **In our project**: $N = 503$ companies (exceeds the course minimum requirement of $N \ge 100$).

### Qualitative / Categorical Variable (Variable qualitative)
Variables that express names, categories, or labels rather than numeric quantities. You can count their frequency, but you **cannot** compute a mathematical average.
* **Nominal Variable (Variable nominale)**:
  * Categories with **no natural order or ranking**.
  * *Examples*: Industry sector (`Sector`), country of listing, legal status.
  * *Course rule (Slide 29)*: Must have between **2 and 5 categories**. Our project has exactly 5: *Tech & Comms, Healthcare, Finance, Industrials & Energy, Consumer*.
  * *Golden Rule (Slide 19)*: **Never compute a mean for a nominal variable!** Saying *"Average sector = 2.4"* is completely meaningless and results in lost marks.
* **Ordinal Variable (Variable ordinale)**:
  * Categories that possess a **clear, natural ranking or order**, but where the distance (gap) between categories is **not equal** or mathematically measurable.
  * *Examples*: Credit rating (AAA > AA > A), Customer satisfaction (1 star to 5 stars), Governance tier (*Low < Medium < High*), Size quartile (*Q1 < Q2 < Q3 < Q4*).
  * *Golden Rule (Slide 13)*: The distance between A and B is not the same as between B and C. Central tendency is captured by the **mode** or the **median category**.

### Quantitative / Numerical Variable (Variable quantitative)
Variables that represent measurable or countable numerical values where arithmetic operations (addition, subtraction, averaging) are valid.
* **Discrete Variable (Variable discrète)**: Countable integer values with no decimals (e.g., Number of employees `Headcount`, number of factories, number of board members).
* **Continuous Variable (Variable continue)**: Measured on an unbroken numerical continuum, allowing decimals (e.g., `Profit_Margin`, `Total_Revenue_B`, `Market_Cap_B`, `Beta`).
* **Scale Types: Interval vs. Ratio (Échelle d'intervalle vs. Échelle de rapport)**:
  * *Interval scale*: Has an arbitrary zero point (e.g., Temperature in °C: 0°C does not mean "absence of temperature", so 20°C is not "twice as hot" as 10°C).
  * *Ratio scale*: Has a **true, absolute zero** indicating complete absence of the quantity (e.g., Turnover = \$0 means zero sales; \$20M is truly twice as much as \$10M).
  * *In our project*: `Total_Revenue_B`, `Market_Cap_B`, and `Profit_Margin` are ratio-scale continuous variables, enabling full correlation and regression modeling.

### Dataset Structure: Cross-Sectional vs. Time-Series vs. Panel
* **Cross-Sectional Dataset (Coupe transversale)**: Multiple entities (503 firms) observed at a **single point in time** (e.g., FY2025). This is our project structure.
* **Time-Series (Série temporelle)**: A single entity observed over multiple consecutive periods (e.g., Apple's stock price daily from 2020 to 2026).
* **Panel Data (Données de panel)**: Multiple entities observed across multiple time periods ($1\text{ row} = 1\text{ firm-year}$). *Caution*: Panel data introduces autocorrelation, which violates standard ANOVA and OLS regression assumptions taught in this course.

---

## 2. Financial & Corporate Accounting Terminology

### S&P 500 Index (Standard & Poor's 500)
A market-capitalization-weighted equity index tracking the 500 largest public companies listed on stock exchanges in the United States (NYSE and NASDAQ), representing approximately 80% of total U.S. equity market capitalization.

### Ticker Symbol (Symbole boursier)
A unique arrangement of 1 to 5 letters identifying a specific publicly traded security on an exchange (e.g., `AAPL` for Apple, `MSFT` for Microsoft, `NVDA` for Nvidia, `FI` for Fiserv). Serves as the primary `ID` variable in our dataset.

### Market Capitalization (`Market_Cap_B` — Capitalisation boursière)
$$\text{Market Cap} = \text{Current Share Price} \times \text{Total Shares Outstanding}$$
The total equity market value of a public company, expressed in **Billions of USD (\$B)** in our dataset.
* *Market Cap Quartiles (`Market_Cap_Quartile`)*: The S&P 500 divided into 4 equal tiers of firm size:
  * **Q1**: Smallest quartile in the index (\$6.5B to \$22.2B)
  * **Q2**: Mid-sized large-cap (\$22.2B to \$44.5B)
  * **Q3**: Upper large-cap (\$44.5B to \$94.0B)
  * **Q4**: Mega-cap giants (\$94.0B to \$5,367.1B, including Apple, Microsoft, Nvidia)

### Total Revenue (`Total_Revenue_B` — Chiffre d'affaires / Turnover)
The total gross amount of income generated by the sale of goods or services related to the company's primary operations before deducting any expenses, taxes, or depreciation. Reported in **Billions of USD (\$B)**.

### Fiscal Year (FY — Exercice fiscal) vs. Calendar Year (Année calendaire)
* *Calendar Year*: Strictly January 1 to December 31.
* *Fiscal Year (FY2025)*: The official 12-month accounting period used by a corporation to prepare audited financial reports (SEC Form 10-K).
* *Why it matters*: Many US companies do not close their books on December 31. Apple closes in September; Nvidia and Walmart close in January; Microsoft closes in June. Using **FY2025** ensures we analyze 12 full months of audited operating figures for every single corporation.

### Trailing Twelve Months (TTM — Douze derniers mois glissants)
A financial reporting measurement window that calculates performance over the most recent 12-month period (the last 4 quarters) regardless of the fiscal year-end date.

### Net Profit Margin (`Profit_Margin` — Marge bénéficiaire nette)
$$\text{Profit Margin} = \frac{\text{Net Income}}{\text{Total Revenue}}$$
The percentage of revenue that remains as bottom-line profit after paying all operating expenses, interest, and taxes. Expressed as a decimal in our dataset (e.g., $0.15 = 15\%$).
* *Advantage in Data Analysis*: Revenue is positive for all operating firms, meaning `Profit_Margin` is 100% defined and available for all 503 firms without accounting distortion.

### Return on Equity (`ROE` — Rentabilité des capitaux propres)
$$\text{ROE} = \frac{\text{Net Income}}{\text{Shareholders' Equity}}$$
Measures how efficiently a company's management uses shareholders' capital to generate net profits. Expressed as a decimal (e.g., $0.20 = 20\%$).

### Negative Shareholders' Equity & Missing ROE (Capitaux propres négatifs)
* *The Phenomenon*: In our dataset, 32 prominent corporations (AbbVie, Altria, AutoZone, Booking Holdings, Domino's Pizza, etc.) show missing/NaN values for ROE.
* *The Financial Reason*: These mature, highly cash-generative firms engaged in aggressive, debt-funded **share buybacks (rachats d'actions)** over 10+ years. Buying back stock reduces the accounting book equity on the balance sheet. When cumulative buybacks exceed retained earnings, book equity becomes negative.
* *Econometric Implication*: Net income divided by negative equity produces a mathematically meaningless or negative number. Financial databases (Yahoo Finance, Bloomberg) set ROE to `NaN`. Rather than deleting these premier companies (which would introduce survival and industry bias), we document this in the *Data Cleaning Log* and utilize `Profit_Margin` as our universal profitability indicator.

### Market Beta (`Beta` — Volatilité systématique)
A quantitative measure of a stock's volatility (systematic market risk) in comparison to the overall market (S&P 500 index), calculated from a **5-year window of monthly returns**:
* $\beta = 1.0$: Stock moves in tandem with the market.
* $\beta > 1.0$: Aggressive / high-volatility stock (e.g., high-growth tech).
* $\beta < 1.0$: Defensive / low-volatility stock (e.g., consumer staples, utilities).
* $\beta < 0$: Inverted movement (extremely rare in equities).

### Form 10-K (Rapport annuel SEC)
The comprehensive annual regulatory filing required by the U.S. Securities and Exchange Commission (SEC) providing a detailed, audited breakdown of a public company's financial performance.

---

## 3. ESG & Corporate Governance (ISS Framework)

### ESG (Environmental, Social, and Governance)
A tri-pillar framework used by institutional investors to evaluate corporate sustainability, societal impact, and ethical leadership alongside traditional financial statements.

### ISS (Institutional Shareholder Services)
The global leader in proxy voting advisory and corporate governance research. ISS evaluates publicly listed firms and assigns quantitative risk ratings based on regulatory disclosures.

### ISS Governance QualityScore (`Overall_Governance_Risk`)
A composite decile score measuring corporate governance risk across 4 core pillars on a **1 to 10 scale**:
* **Audit Risk (`Audit_Risk`)**: Financial integrity, accounting oversight, auditor independence, and financial restatements.
* **Board Structure Risk (`Board_Risk`)**: Independence of directors, board diversity, committee structures, and separation of CEO and Chairman roles.
* **Compensation Risk (`Compensation_Risk`)**: Alignment between executive pay and shareholder returns, clawback policies, and golden parachutes.
* **Shareholder Rights Risk (`Shareholder_Rights_Risk`)**: Voting rights, poison pills, classified boards, and takeover defense mechanisms.

> [!CAUTION]
> **Crucial Inversion**: In the ISS methodology, **1 represents the lowest risk (best governance practices)**, while **10 represents the highest risk (poorest governance practices)**!
> A negative correlation between Governance Risk and Profit Margin therefore implies that *better governance (lower risk score) is associated with higher profitability*!

### Governance Risk Tier (`Governance_Risk_Level` — Variable ordinale)
To enable categorical contingency tables (Chi-Square) and group tests, the 1–10 continuous score is classified into three ordered tiers:
* **Low Risk** (Scores 1 to 3): Premier governance compliance ($n = 150$, $30.2\%$).
* **Medium Risk** (Scores 4 to 6): Standard market governance ($n = 149$, $30.0\%$).
* **High Risk** (Scores 7 to 10): Elevated governance friction ($n = 197$, $39.7\%$, Modal tier).

---

## 4. Univariate Statistics & Shape Parameters (Session 1)

### Univariate Analysis (Analyse univariée)
The statistical examination of **one single variable in isolation**, without analyzing causes, relationships, or predictive influences (Slide 19).

### Central Tendency: The Three Centres (Tendance centrale)
1. **Arithmetic Mean ($\bar{x}$ — Moyenne)**:
   $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$
   The mathematical average. Takes every data point into account. **Weakness (Slide 21)**: Completely distorted and destroyed by extreme outliers and skewness.
2. **Median ($\text{Mdn}$ — Médiane)**:
   The exact middle value (50th percentile) dividing the ordered dataset into two equal halves. **Strength**: Robust and immune to extreme outliers.
3. **Mode (Mode)**:
   The most frequently occurring value or category in a distribution. **The only valid measure of central tendency for nominal data** (Slide 20).

### Dispersion & Variability (Mesures de dispersion)
* **Standard Deviation ($s$ — Écart-type)**:
  $$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}$$
  The average distance of an observation from the mean. Tells you whether the mean accurately represents the typical case (Slide 22).
* **Variance ($s^2$)**: The square of the standard deviation.
* **Range (Étendue)**: The absolute distance between maximum and minimum ($\text{Max} - \text{Min}$).
* **Interquartile Range ($IQR$ — Écart interquartile)**:
  $$IQR = Q_3 - Q_1$$
  The range covering the central 50% of observations. Highly robust against outliers.

### Distribution Shape: Skewness & Kurtosis (Forme de distribution)
* **Skewness ($g_1$ — Asymétrie)**:
  Measures the lack of symmetry in a distribution.
  * $g_1 \approx 0$: Symmetric distribution ($\text{Mean} \approx \text{Median} \approx \text{Mode}$).
  * $g_1 > 0$ (**Positive / Right Skew**): Mean > Median > Mode. A long tail extending to the right (typical of income, revenue, market cap).
  * $g_1 < 0$ (**Negative / Left Skew**): Mean < Median < Mode. A long tail extending to the left (typical of profit margins with distressed outliers).
* **Kurtosis ($g_2$ — Aplatissement / Acuité)**:
  Measures the "tailedness" and peakedness of the distribution relative to a normal curve.
  * $g_2 = 0$ (Mesokurtic): Standard bell-shaped normal curve.
  * $g_2 > 0$ (Leptokurtic): Sharply peaked with heavy, fat tails (higher probability of extreme outliers).
  * $g_2 < 0$ (Platykurtic): Flatter peak with thin tails.
* **The Normality Rule of Thumb (Slide 23)**: Both skewness and kurtosis falling within **$[-1.0, +1.0]$** is consistent with normality.

### Normality Testing: The Three Converging Pieces of Evidence (Slide 24)
Never rely on a single metric; evaluate all three simultaneously:
1. **Compare the Three Centres**: If $\text{Mean} \approx \text{Median} \approx \text{Mode}$, the distribution is roughly symmetric.
2. **Evaluate Skewness and Kurtosis**: Verify whether both reside inside the $[-1.0, +1.0]$ window.
3. **Visual Inspection & Formal Shapiro-Wilk Test**:
   * *Visual Inspection*: Inspect Histogram, Density curve, and Q-Q Plot.
   * *Shapiro-Wilk Test*: Formal statistical test with null hypothesis $H_0$: *"The data are normally distributed"*.
   * **The Inverted Logic (Slide 24)**: Unlike almost every other test in the course, **$p > 0.05$ means you KEEP normality**. If $p < 0.05$, you **REJECT normality**.

---

## 5. Bivariate Analysis & Hypothesis Testing (Session 2)

### Bivariate Analysis (Analyse bivariée)
The statistical examination of the relationship or association between **two variables simultaneously** (Slide 17 & Session 2).

### The Four-Step Protocol (Slide 9 & 41)
The mandatory answer template for every analytical question:
1. **IDENTIFY**: Which statistical test to execute? Fully justified by the variable scales.
2. **HYPOTHESISE**: Formulate $H_0$ and $H_1$ in clear, non-technical business language.
3. **DECIDE**: Is $p < 0.05$? If yes, what is the magnitude/strength of the effect?
4. **RECOMMEND**: Actionable executive guidance answering: *"What does the manager do on Monday morning?"*

### Hypotheses: Null ($H_0$) vs. Alternative ($H_1$)
* **Null Hypothesis ($H_0$)**: The hypothesis of "no difference", "no relationship", or "status quo" (e.g., *"Governance risk has no relationship with sector"*).
* **Alternative Hypothesis ($H_1$)**: The research hypothesis proposing an active relationship or group difference (e.g., *"Governance risk varies significantly across sectors"*).

### Statistical Significance ($p$-value) vs. Effect Size (Slide 42)
* **$p$-value (Significance)**: The probability of observing results at least as extreme as the sample data assuming $H_0$ is true. If $p < 0.05$, we reject $H_0$ and conclude that an effect exists.
* **Reporting Standard (Slide 42)**: Never write $p = 0.000$! Software printing `.000` means the value is below three decimal places. Report strictly as **$p < .001$**.
* **Effect Size (Strength)**: While $p$-value tells you *whether* an effect exists, effect size tells you *how strong* it is (whether it practically matters to a manager).

### Chi-Square Test of Independence ($\chi^2$ — Nominal $\times$ Ordinal)
Tests whether two qualitative categorical variables are independent or statistically associated (e.g., `Sector` $\times$ `Governance_Risk_Level`).
* **Cramér's $V$ (Effect Size)**:
  Measures the strength of association between categorical variables, ranging from $0$ (no association) to $1$ (perfect association).
  * $V < 0.10$: Negligible
  * $0.10 \le V < 0.30$: Weak to moderate association
  * $V \ge 0.30$: Strong association

### Pearson Correlation Coefficient ($r$ — Continuous $\times$ Continuous)
Measures the linear strength and direction of the association between two continuous variables (e.g., `Overall_Governance_Risk` vs. `Profit_Margin`).
* Ranges from $-1.0$ (perfect negative correlation) to $+1.0$ (perfect positive correlation), with $0.0$ indicating no linear relationship.
* Requires continuous interval or ratio scale data.
* **Confidence Interval (95% CI)**: The estimated range within which the true population correlation coefficient lies with 95% certainty.

---

## 6. Group Comparisons & ANOVA (Session 3)

### One-Way ANOVA (Analysis of Variance — Qualitative 3+ groups $\times$ Quantitative)
Tests whether the mean of a continuous outcome variable (e.g., `Profit_Margin`) differs significantly across three or more categorical groups (e.g., the 5 `Sector` categories).
* *Null Hypothesis ($H_0$)*: $\mu_1 = \mu_2 = \mu_3 = \mu_4 = \mu_5$ (All sector population means are equal).
* *Alternative Hypothesis ($H_1$)*: At least one sector mean is significantly different.

### ANOVA Parametric Assumptions
1. **Normality of Residuals**: Verified via Shapiro-Wilk per group or residual Q-Q plot.
2. **Homogeneity of Variances (Homoscedasticity)**: Tested using **Levene's Test** ($H_0$: variances are equal across groups).

### What if Assumptions are Violated? (Slide 118)
* If variances are unequal ($p < 0.05$ on Levene's test): Run **Welch's ANOVA** instead of standard Fisher's ANOVA.
* If normality is severely breached: Run the non-parametric **Kruskal-Wallis Test**.

### Post-Hoc Pairwise Comparisons (Comparisons post-hoc)
If the overall ANOVA is significant ($p < 0.05$), post-hoc tests determine *which specific pairs of groups* differ:
* **Tukey's HSD (Honestly Significant Difference)**: Used when variances are equal.
* **Games-Howell Post-Hoc**: Used when variances are unequal (adjusts p-values to control for family-wise error rate without assuming equal variances).

---

## 7. Regression Modeling & Econometrics (Session 4)

### Linear Regression (Régression linéaire)
Models the mathematical relationship between one continuous dependent variable ($Y$, e.g., `Profit_Margin`) and one or more independent explanatory variables ($X$, e.g., `Overall_Governance_Risk`, `Market_Cap_B`, `Beta`).

### Model Equation (Multiple OLS Regression)
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$
* $\beta_0$ (Intercept): Expected value of $Y$ when all $X = 0$.
* $\beta_k$ (Regression slope coefficient): The expected change in $Y$ for a one-unit change in $X_k$, holding all other variables constant (*ceteris paribus*).
* $SE$ (Standard Error): The precision of the coefficient estimate.
* $t$-statistic & $p$-value: Tests whether $\beta_k$ is significantly different from zero.

### Coefficient of Determination ($R^2$ and Adjusted $R^2$)
* **$R^2$**: The proportion of variance in the dependent variable explained by the regression model (ranges from 0 to 1).
* **Adjusted $R^2$**: Penalizes the model for adding useless explanatory variables; used to compare models with different numbers of predictors.

### Regression Diagnostic Assumptions
1. **Linearity**: The true relationship between predictors and outcome is linear (inspected via Residuals vs. Fitted plot).
2. **Normality of Residuals**: The model errors ($\epsilon$) are normally distributed (Q-Q plot of residuals).
3. **Homoscedasticity**: The variance of the residuals is constant across all predicted values (tested via **Breusch-Pagan test**).
4. **No Multicollinearity**: Explanatory variables are not overly correlated with one another. Evaluated using the **Variance Inflation Factor (VIF)**:
   * $\text{VIF} < 5$: Acceptable / low collinearity.
   * $\text{VIF} > 10$: Severe multicollinearity (distorts coefficient estimates).

---

## 8. Jamovi Software Operations & Common Pitfalls

### What is Jamovi?
A free, open-source, point-and-click statistical software package built on top of the R statistical programming language, providing SPSS-style output tables and real-time reactive calculations (Slide 37).

### Jamovi Measure Types (Slide 38)
* **ID**: Column used solely to identify entities (e.g., `Ticker`). Jamovi never computes statistics on ID columns.
* **Nominal**: Unordered qualitative categories (icon: three colored circles).
* **Ordinal**: Ranked qualitative categories (icon: small step chart).
* **Continuous**: Numeric measurements with decimals (icon: small ruler).

### The `.omv` File Format
The proprietary Jamovi file format that bundles the spreadsheet dataset, variable configurations, and all statistical output tables and graphs together into a single file. **This is the primary file submitted for lab coursework** (Slide 37).

### Top 6 Errors That Cost Marks Every Year (Slide 42)
1. **Reporting a mean for a nominal variable**: e.g., writing *"average sector = 2.4"*.
2. **Setting the wrong measure type in Jamovi**: e.g., setting `Sector` as Continuous or `Profit_Margin` as Nominal, causing Jamovi to hide the required statistical tests.
3. **Reading "Sig. = 0.000" as $p = 0$**: Always format as **$p < .001$**.
4. **Confusing significance with strength**: A test can be statistically significant ($p < 0.05$) because sample size $N$ is large, but have a tiny, negligible effect size ($r = 0.08$).
5. **Pasting output tables without interpretation**: Half the marks are awarded for explaining what the numbers mean in plain English.
6. **Stopping at the statistic without recommending action**: Always conclude with what the executive or portfolio manager does on Monday morning.
