# S&P 500 Quantitative Data Analysis — Master Glossary & Lexicon (Grand Lexique Bilingue)

> **Course**: Quantitative Data Analysis (M1 – S7, Course code: `2627_ECO_2_EN_009`)
> **Institution**: EM Normandie Business School · Programme Grande École
> **Lecturer**: Dr. NGUYEN Anh-Tuan
> **Purpose**: A comprehensive, beginner-friendly bilingual guide (English concepts with detailed French explanations) covering all Financial, Data, Statistical, Econometric, ESG, and Jamovi terminology across all 4 sessions of the project.

---

## Table of Contents

1. [Data Fundamentals & Variable Typology](#1-data-fundamentals--variable-typology)
2. [Financial & Corporate Accounting Terminology](#2-financial--corporate-accounting-terminology)
3. [ESG & Corporate Governance (ISS Framework)](#3-esg--corporate-governance-iss-framework)
4. [Session 1: Univariate Statistics & Shape Parameters](#4-session-1-univariate-statistics--shape-parameters)
5. [Session 2: Bivariate Associations, Chi-Square & Correlations](#5-session-2-bivariate-associations-chi-square--correlations)
6. [Session 3: Group Comparisons, Welch's ANOVA & Games-Howell](#6-session-3-group-comparisons-welchs-anova--games-howell)
7. [Session 4: Multiple Linear Regression & Econometric Diagnostics](#7-session-4-multiple-linear-regression--econometric-diagnostics)
8. [Jamovi Software Operations & Costly Student Traps](#8-jamovi-software-operations--costly-student-traps)

---

## 1. Data Fundamentals & Variable Typology

### Unit of Observation (Unité d'observation)

- **Definition**: Exactly what a single row represents in your database.
- **In our project**: **1 row = 1 publicly traded S&P 500 company**.
- **Why it matters (Slide 11)**: If you cannot finish the sentence _"One row = one..."_, you do not understand your dataset. Having 1 row = 1 firm ensures independence of observations for ANOVA and regression.

### Sample Size ($N$ / Observation count)

- **Definition**: The total number of valid entities observed in the study.
- **In our project**: $N = 503$ companies (exceeds the course minimum requirement of $N \ge 100$).

### Qualitative / Categorical Variable (Variable qualitative)

Variables that express names, categories, or labels rather than numeric quantities. You can count their frequency, but you **cannot** compute a mathematical average.

- **Nominal Variable (Variable nominale)**:
  - Categories with **no natural order or ranking**.
  - _Examples_: Industry sector (`Sector`), country of listing, legal status.
  - _Course rule (Slide 29)_: Must have between **2 and 5 categories**. Our project has exactly 5: _Tech & Comms, Healthcare, Finance, Industrials & Energy, Consumer_.
  - _Golden Rule (Slide 19)_: **Never compute a mean for a nominal variable!** Saying _"Average sector = 2.4"_ is completely meaningless and results in lost marks.
- **Ordinal Variable (Variable ordinale)**:
  - Categories that possess a **clear, natural ranking or order**, but where the distance (gap) between categories is **not equal** or mathematically measurable.
  - _Examples_: Credit rating (AAA > AA > A), Customer satisfaction (1 star to 5 stars), Governance tier (_Low < Medium < High_), Size quartile (_Q1 < Q2 < Q3 < Q4_).
  - _Golden Rule (Slide 13)_: The distance between A and B is not the same as between B and C. Central tendency is captured by the **mode** or the **median category**.

### Quantitative / Numerical Variable (Variable quantitative)

Variables that represent measurable or countable numerical values where arithmetic operations (addition, subtraction, averaging) are valid.

- **Discrete Variable (Variable discrète)**: Countable integer values with no decimals (e.g., Number of employees `Headcount`, number of factories, number of board members).
- **Continuous Variable (Variable continue)**: Measured on an unbroken numerical continuum, allowing decimals (e.g., `Profit_Margin`, `Total_Revenue_B`, `Market_Cap_B`, `Beta`).
- **Scale Types: Interval vs. Ratio (Échelle d'intervalle vs. Échelle de rapport)**:
  - _Interval scale_: Has an arbitrary zero point (e.g., Temperature in °C: 0°C does not mean "absence of temperature", so 20°C is not "twice as hot" as 10°C).
  - _Ratio scale_: Has a **true, absolute zero** indicating complete absence of the quantity (e.g., Turnover = \$0 means zero sales; \$20M is truly twice as much as \$10M).
  - _In our project_: `Total_Revenue_B`, `Market_Cap_B`, and `Profit_Margin` are ratio-scale continuous variables, enabling full correlation and regression modeling.

### Dataset Structure: Cross-Sectional vs. Time-Series vs. Panel

- **Cross-Sectional Dataset (Coupe transversale)**: Multiple entities (503 firms) observed at a **single point in time** (e.g., FY2025). This is our project structure.
- **Time-Series (Série temporelle)**: A single entity observed over multiple consecutive periods (e.g., Apple's stock price daily from 2020 to 2026).
- **Panel Data (Données de panel)**: Multiple entities observed across multiple time periods ($1\text{ row} = 1\text{ firm-year}$). _Caution_: Panel data introduces autocorrelation, which violates standard ANOVA and OLS regression assumptions taught in this course.

---

## 2. Financial & Corporate Accounting Terminology

### S&P 500 Index (Standard & Poor's 500)

A market-capitalization-weighted equity index tracking the 500 largest public companies listed on stock exchanges in the United States (NYSE and NASDAQ), representing approximately 80% of total U.S. equity market capitalization.

### Ticker Symbol (Symbole boursier)

A unique arrangement of 1 to 5 letters identifying a specific publicly traded security on an exchange (e.g., `AAPL` for Apple, `MSFT` for Microsoft, `NVDA` for Nvidia, `FI` for Fiserv). Serves as the primary `ID` variable in our dataset.

### Market Capitalization (`Market_Cap_B` — Capitalisation boursière)

$$\text{Market Cap} = \text{Current Share Price} \times \text{Total Shares Outstanding}$$
The total equity market value of a public company, expressed in **Billions of USD (\$B)** in our dataset.

- _Market Cap Quartiles (`Market_Cap_Quartile`)_: The S&P 500 divided into 4 equal tiers of firm size:
  - **Q1**: Smallest quartile in the index (\$6.5B to \$22.2B)
  - **Q2**: Mid-sized large-cap (\$22.2B to \$44.5B)
  - **Q3**: Upper large-cap (\$44.5B to \$94.0B)
  - **Q4**: Mega-cap giants (\$94.0B to \$5,367.1B, including Apple, Microsoft, Nvidia)

### Total Revenue (`Total_Revenue_B` — Chiffre d'affaires / Turnover)

The total gross amount of income generated by the sale of goods or services related to the company's primary operations before deducting any expenses, taxes, or depreciation. Reported in **Billions of USD (\$B)**.

### Fiscal Year (FY — Exercice fiscal) vs. Calendar Year (Année calendaire)

- _Calendar Year_: Strictly January 1 to December 31.
- _Fiscal Year (FY2025)_: The official 12-month accounting period used by a corporation to prepare audited financial reports (SEC Form 10-K).
- _Why it matters_: Many US companies do not close their books on December 31. Apple closes in September; Nvidia and Walmart close in January; Microsoft closes in June. Using **FY2025** ensures we analyze 12 full months of audited operating figures for every single corporation.

### Trailing Twelve Months (TTM — Douze derniers mois glissants)

A financial reporting measurement window that calculates performance over the most recent 12-month period (the last 4 quarters) regardless of the fiscal year-end date.

### Net Profit Margin (`Profit_Margin` — Marge bénéficiaire nette)

$$\text{Profit Margin} = \frac{\text{Net Income}}{\text{Total Revenue}}$$
The percentage of revenue that remains as bottom-line profit after paying all operating expenses, interest, and taxes. Expressed as a decimal in our dataset (e.g., $0.15 = 15\%$).

- _Advantage in Data Analysis_: Revenue is positive for all operating firms, meaning `Profit_Margin` is 100% defined and available for all 503 firms without accounting distortion.

### Return on Equity (`ROE` — Rentabilité des capitaux propres)

$$\text{ROE} = \frac{\text{Net Income}}{\text{Shareholders' Equity}}$$
Measures how efficiently a company's management uses shareholders' capital to generate net profits. Expressed as a decimal (e.g., $0.20 = 20\%$).

### Negative Shareholders' Equity & Missing ROE (Capitaux propres négatifs)

- _The Phenomenon_: In our dataset, 32 prominent corporations (AbbVie, Altria, AutoZone, Booking Holdings, Domino's Pizza, etc.) show missing/NaN values for ROE.
- _The Financial Reason_: These mature, highly cash-generative firms engaged in aggressive, debt-funded **share buybacks (rachats d'actions)** over 10+ years. Buying back stock reduces the accounting book equity on the balance sheet. When cumulative buybacks exceed retained earnings, book equity becomes negative.
- _Econometric Implication_: Net income divided by negative equity produces a mathematically meaningless or negative number. Financial databases (Yahoo Finance, Bloomberg) set ROE to `NaN`. Rather than deleting these premier companies (which would introduce survival and industry bias), we document this in the _Data Cleaning Log_ and utilize `Profit_Margin` as our universal profitability indicator.

### Market Beta (`Beta` — Volatilité systématique)

A quantitative measure of a stock's volatility (systematic market risk) in comparison to the overall market (S&P 500 index), calculated from a **5-year window of monthly returns**:

- $\beta = 1.0$: Stock moves in tandem with the market.
- $\beta > 1.0$: Aggressive / high-volatility stock (e.g., high-growth tech).
- $\beta < 1.0$: Defensive / low-volatility stock (e.g., consumer staples, utilities).
- $\beta < 0$: Inverted movement (extremely rare in equities).

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

- **Audit Risk (`Audit_Risk`)**: Financial integrity, accounting oversight, auditor independence, and financial restatements.
- **Board Structure Risk (`Board_Risk`)**: Independence of directors, board diversity, committee structures, and separation of CEO and Chairman roles.
- **Compensation Risk (`Compensation_Risk`)**: Alignment between executive pay and shareholder returns, clawback policies, and golden parachutes.
- **Shareholder Rights Risk (`Shareholder_Rights_Risk`)**: Voting rights, poison pills, classified boards, and takeover defense mechanisms.

> [!CAUTION]
> **Crucial Inversion**: In the ISS methodology, **1 represents the lowest risk (best governance practices)**, while **10 represents the highest risk (poorest governance practices)**!
> A negative correlation between Governance Risk and Profit Margin therefore implies that _better governance (lower risk score) is associated with higher profitability_!

### Governance Risk Tier (`Governance_Risk_Level` — Variable ordinale)

To enable categorical contingency tables (Chi-Square) and group tests, the 1–10 continuous score is classified into three ordered tiers:

- **Low Risk** (Scores 1 to 3): Premier governance compliance ($n = 150$, $30.2\%$).
- **Medium Risk** (Scores 4 to 6): Standard market governance ($n = 149$, $30.0\%$).
- **High Risk** (Scores 7 to 10): Elevated governance friction ($n = 197$, $39.7\%$, Modal tier).

---

## 4. Session 1: Univariate Statistics & Shape Parameters

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

- **Standard Deviation ($s$ — Écart-type)**:
  $$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}$$
  The average distance of an observation from the mean. Tells you whether the mean accurately represents the typical case (Slide 22).
- **Variance ($s^2$)**: The square of the standard deviation.
- **Range (Étendue)**: The absolute distance between maximum and minimum ($\text{Max} - \text{Min}$).
- **Interquartile Range ($IQR$ — Écart interquartile)**:
  $$IQR = Q_3 - Q_1$$
  The range covering the central 50% of observations. Highly robust against outliers.

### Distribution Shape: Skewness & Kurtosis (Forme de distribution)

- **Skewness ($g_1$ — Asymétrie)**:
  $$g_1 = \frac{n}{(n-1)(n-2)} \sum_{i=1}^n \left(\frac{x_i - \bar{x}}{s}\right)^3$$
  Measures the lack of symmetry in a distribution.
  - $g_1 \approx 0$: Symmetric distribution ($\text{Mean} \approx \text{Median} \approx \text{Mode}$).
  - $g_1 > 0$ (**Positive / Right Skew**): Mean > Median > Mode. A long tail extending to the right (typical of income, revenue, market cap).
  - $g_1 < 0$ (**Negative / Left Skew**): Mean < Median < Mode. A long tail extending to the left (typical of profit margins with distressed outliers).
- **Kurtosis ($g_2$ — Aplatissement / Acuité)**:
  $$g_2 = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{i=1}^n \left(\frac{x_i - \bar{x}}{s}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}$$
  Measures the "tailedness" and peakedness of the distribution relative to a normal curve.
  - $g_2 = 0$ (Mesokurtic): Standard bell-shaped normal curve.
  - $g_2 > 0$ (Leptokurtic): Sharply peaked with heavy, fat tails (higher probability of extreme outliers).
  - $g_2 < 0$ (Platykurtic): Flatter peak with thin tails.
- **The Normality Rule of Thumb (Slide 23)**: Both skewness and kurtosis falling within **$[-1.0, +1.0]$** is consistent with normality.

### Normality Testing: The Three Converging Pieces of Evidence (Slide 24)

Never rely on a single metric; evaluate all three simultaneously:

1. **Compare the Three Centres**: If $\text{Mean} \approx \text{Median} \approx \text{Mode}$, the distribution is roughly symmetric.
2. **Evaluate Skewness and Kurtosis**: Verify whether both reside inside the $[-1.0, +1.0]$ window.
3. **Visual Inspection & Formal Shapiro-Wilk Test**:
   - _Visual Inspection_: Inspect Histogram, Density curve, and Q-Q Plot.
   - _Shapiro-Wilk Test_: Formal statistical test with null hypothesis $H_0$: _"The data are normally distributed"_.
   - **The Inverted Logic (Slide 24)**: Unlike almost every other test in the course, **$p > 0.05$ means you KEEP normality**. If $p < 0.05$, you **REJECT normality**.

---

## 5. Session 2: Bivariate Associations, Chi-Square & Correlations

### Bivariate Analysis (Analyse bivariée)

The statistical examination of the relationship or association between **two variables simultaneously** (Slide 17 & Session 2).

### The Four-Step Protocol (Slide 9 & 41)

The mandatory answer template for every analytical question:

1. **IDENTIFY**: Which statistical test to execute? Fully justified by the variable scales.
2. **HYPOTHESISE**: Formulate $H_0$ and $H_1$ in clear, non-technical business language.
3. **DECIDE**: Is $p < 0.05$? If yes, what is the magnitude/strength of the effect?
4. **RECOMMEND**: Actionable executive guidance answering: _"What does the manager do on Monday morning?"_

### Hypotheses: Null ($H_0$) vs. Alternative ($H_1$)

- **Null Hypothesis ($H_0$)**: The hypothesis of "no difference", "no relationship", or "status quo" (e.g., _"Governance risk has no relationship with sector"_).
- **Alternative Hypothesis ($H_1$)**: The research hypothesis proposing an active relationship or group difference (e.g., _"Governance risk varies significantly across sectors"_).

### Statistical Significance ($p$-value) vs. Effect Size (Slide 42)

- **$p$-value (Significance)**: The probability of observing results at least as extreme as the sample data assuming $H_0$ is true. If $p < 0.05$, we reject $H_0$ and conclude that an effect exists.
- **Reporting Standard (Slide 42)**: Never write $p = 0.000$! Software printing `.000` means the value is below three decimal places. Report strictly as **$p < .001$**.
- **Effect Size (Strength)**: While $p$-value tells you _whether_ an effect exists, effect size tells you _how strong_ it is (whether it practically matters to a manager).

### Chi-Square Test of Independence ($\chi^2$ — Nominal $\times$ Ordinal)

Tests whether two qualitative categorical variables are independent or statistically associated.
$$\chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
Where $O_{ij}$ is the observed cell count, and $E_{ij} = \frac{\text{Row Total} \times \text{Column Total}}{N}$ is the expected count under independence. Degrees of freedom: $df = (r - 1)(c - 1)$.

- **Cramér's $V$ (Effect Size for Chi-Square)**:
  $$V = \sqrt{\frac{\chi^2}{N \min(r - 1, c - 1)}}$$
  Measures association strength from $0$ (no relationship) to $1$ (perfect association):
  - $V < 0.10$: Negligible
  - $0.10 \le V < 0.30$: Weak to moderate association (Our result: $V = 0.122$)
  - $V \ge 0.30$: Strong association
- **Standardized Residuals (Résidus standardisés)**:
  $$\text{Residual}_{ij} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}}}$$
  Identifies which specific cells drive the overall Chi-Square result. A residual $> +2.0$ indicates significant over-representation; $< -2.0$ indicates significant under-representation. (In our data, Tech & Comms had $+1.75$ in High Risk; Industrials had $-1.97$).

### Pearson Correlation Coefficient ($r$ — Continuous $\times$ Continuous)

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$
Measures the linear strength and direction of the association between two continuous variables:

- Ranges from $-1.0$ (perfect inverse link) to $+1.0$ (perfect direct link).
- **Fisher $z$-Transformation & 95% Confidence Interval**:
  Constructs exact lower and upper confidence bounds:
  $$z = \frac{1}{2} \ln \left(\frac{1+r}{1-r}\right), \quad SE_z = \frac{1}{\sqrt{n - 3}}$$

### Spearman's Rank Correlation ($\rho$ — Non-Paramétrique)

Calculates Pearson's correlation on the **ranks** of data rather than raw values. Robust to non-normality and monotonic non-linear patterns.

---

## 6. Session 3: Group Comparisons, Welch's ANOVA & Games-Howell

### One-Way Analysis of Variance (ANOVA — Qualitative 3+ groups $\times$ Quantitative)

Tests whether the population means of a continuous outcome variable differ significantly across 3 or more categorical groups.
$$F = \frac{MS_{\text{between}}}{MS_{\text{within}}} = \frac{SS_{\text{between}} / (k - 1)}{SS_{\text{within}} / (N - k)}$$

### Levene's Test of Homogeneity of Variances (Test de Levene)

Tests whether variances are equal across groups ($H_0: \sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2$).

- _If $p > 0.05$_: Variances are equal (homoscedasticity confirmed; standard Fisher ANOVA is valid).
- _If $p < 0.05$_: Variances are significantly unequal (**heteroscedasticity**; standard Fisher ANOVA is invalid and Welch's ANOVA must be used!).
- _In our project_: Levene's test yielded $F = 5.39, p < .001$ for Profit Margin across sectors.

### Welch's Robust ANOVA ($F_{\text{Welch}}$)

An adjusted ANOVA formulation that weights each group's variance by its sample size ($w_i = n_i / s_i^2$). Valid even when group variances and sample sizes are severely unequal.

### Effect Size: Eta-Squared ($\eta^2$) & Omega-Squared ($\omega^2$)

$$\eta^2 = \frac{SS_{\text{between}}}{SS_{\text{total}}}$$
The percentage of variance in the dependent variable accounted for by group membership:

- $\eta^2 \approx 0.01$: Small effect
- $\eta^2 \approx 0.06$: Medium effect
- $\eta^2 \ge 0.14$: Large effect
- _In our project_: $\eta^2 = 0.0405$ ($4.05\%$ of profit margin variance is explained by sector).

### Kruskal-Wallis Non-Parametric Test ($H$)

The non-parametric rank-based equivalent of One-Way ANOVA. Used when both normality and variance homogeneity are severely violated.

### Post-Hoc Pairwise Comparisons: Tukey HSD vs. Games-Howell

When ANOVA indicates that at least one group differs ($p < 0.05$), post-hoc tests identify _which specific pairs_ differ:

- **Tukey's HSD (Honestly Significant Difference)**: Assumes equal variances across all groups.
- **Games-Howell Post-Hoc Test**:
  $$t = \frac{\bar{x}_i - \bar{x}_j}{\sqrt{\frac{s_i^2}{n_i} + \frac{s_j^2}{n_j}}}$$
  Adjusts degrees of freedom via the Welch-Satterthwaite equation and applies the Studentized Range distribution ($q$). **Required when Levene's test fails!**

---

## 7. Session 4: Multiple Linear Regression & Econometric Diagnostics

### Multiple Linear Regression (Régression linéaire multiple MCO / OLS)

Models the expected value of a continuous dependent variable ($Y$) as a linear combination of explanatory variables ($X_1, X_2, \dots, X_k$):
$$Y_i = \beta_0 + \beta_1 X_{1i} + \beta_2 X_{2i} + \dots + \beta_k X_{ki} + \epsilon_i$$

- **$\beta_0$ (Intercept / Constante)**: The predicted baseline value of $Y$ when all predictors are equal to zero.
- **$\beta_k$ (Unstandardized Regression Coefficient)**: The expected change in $Y$ for a 1-unit increase in $X_k$, holding all other variables constant (_ceteris paribus_).
- **Standardized Beta ($\beta^*$)**:
  $$\beta_k^* = \beta_k \times \frac{s_{X_k}}{s_Y}$$
  Allows direct comparison of predictor importance on a common standard-deviation scale.

### Coefficient of Determination ($R^2$ and Adjusted $R^2$)

- **$R^2$**: The proportion of variance in $Y$ explained by the regression model:
  $$R^2 = 1 - \frac{SS_{\text{residual}}}{SS_{\text{total}}}$$
- **Adjusted $R^2$**: Corrects $R^2$ for the number of predictors ($k$) and sample size ($N$):
  $$R_{\text{adj}}^2 = 1 - \left[\frac{(1 - R^2)(N - 1)}{N - k - 1}\right]$$

### Logarithmic Transformations ($\ln(X)$)

Applying natural logarithms to positively skewed financial metrics (Market Capitalization and Revenue).

- _Econometric Rationale_: Compresses extreme mega-cap outliers (NVIDIA, Apple) and transforms multiplicative scale dynamics into linear additive relationships.

### Econometric Assumptions & Diagnostic Suite (Slide 133–137)

1. **Linearity**: Evaluated via the Residuals vs. Fitted plot (should show a flat horizontal band with no curvature).
2. **Normality of Residuals**: Model errors ($\epsilon$) must be normally distributed (Q-Q plot of residuals).
3. **Homoscedasticity (Equal Error Variance)**:
   - **Breusch-Pagan Test**: Regresses squared residuals on explanatory variables.
   - _If $p < 0.05$_: Heteroscedasticity is present (White's robust standard errors HC3 are required).
4. **Absence of Multicollinearity (VIF & Tolerance)**:
   - **Variance Inflation Factor (VIF)**:
     $$\text{VIF}_j = \frac{1}{1 - R_j^2}$$
     Measures how much the variance of an estimated regression coefficient increases due to collinearity with other predictors:
     - $\text{VIF} < 5.0$: Safe / Low collinearity (Our maximum VIF was $1.89$).
     - $\text{VIF} > 10.0$: Severe multicollinearity (distorts $t$-statistics and inflates standard errors).
   - **Tolerance**: The inverse of VIF ($\text{Tol} = 1 / \text{VIF}$). Tolerance $< 0.20$ signals high collinearity risk.

---

## 8. Jamovi Software Operations & Costly Student Traps

### What is Jamovi?

A free, open-source, point-and-click statistical software package built on top of the R statistical programming language, providing SPSS-style output tables and real-time reactive calculations (Slide 37).

### Jamovi Measure Types (Slide 38)

- **ID**: Column used solely to identify entities (e.g., `Ticker`). Jamovi never computes statistics on ID columns.
- **Nominal**: Unordered qualitative categories (icon: three colored circles).
- **Ordinal**: Ranked qualitative categories (icon: small step chart).
- **Continuous**: Numeric measurements with decimals (icon: small ruler).

### The `.omv` File Format

The proprietary Jamovi file format that bundles the spreadsheet dataset, variable configurations, and all statistical output tables and graphs together into a single file. **This is the primary file submitted for lab coursework** (Slide 37).

### Top 6 Errors That Cost Marks Every Year (Slide 42)

1. **Reporting a mean for a nominal variable**: e.g., writing _"average sector = 2.4"_.
2. **Setting the wrong measure type in Jamovi**: e.g., setting `Sector` as Continuous or `Profit_Margin` as Nominal, causing Jamovi to hide the required statistical tests.
3. **Reading "Sig. = 0.000" as $p = 0$**: Always format as **$p < .001$**.
4. **Confusing significance with strength**: A test can be statistically significant ($p < 0.05$) because sample size $N$ is large, but have a tiny, negligible effect size ($r = 0.08$).
5. **Pasting output tables without interpretation**: Half the marks are awarded for explaining what the numbers mean in plain English.
6. **Stopping at the statistic without recommending action**: Always conclude with what the executive or portfolio manager does on Monday morning.
