# Artefact 3 — Group Comparisons & ANOVA Report

> **Course**: Quantitative Data Analysis (M1 – S7)
> **Course Code**: `2627_ECO_2_EN_009` — Academic Year 2026–2027
> **Institution**: EM Normandie Business School · Programme Grande École
> **Lecturer**: Dr. NGUYEN Anh-Tuan
> **Deliverable**: **Artefact 3 (20 Marks)**
> **Prerequisites Completed**: [Artefact 1 (Univariate)](Artefact_1_Session_1.md), [Artefact 2 (Bivariate)](Artefact_2_Session_2.md)

---

## 1. Executive Summary & Analytical Scope

Session 3 tests whether the means of quantitative financial and governance metrics differ significantly across the 5 economic sectors of the S&P 500 index ($N = 503$).
In accordance with course directives (Slide 17 & Slide 109–125), the analysis focuses on:

1. **Primary ANOVA**: Does **Net Profit Margin** differ significantly across the 5 consolidated sectors?
2. **Secondary ANOVA**: Does **Corporate Governance Risk** differ significantly across the 5 sectors?
3. **Parametric Assumption Checks**: Testing homogeneity of variances (**Levene's Test**) and normality of group residuals.
4. **Robust Inferential Modeling**: Executing **Welch's ANOVA** and non-parametric **Kruskal-Wallis** tests due to severe empirical variance heterogeneity.
5. **Post-Hoc Pairwise Comparisons**: Executing **Games-Howell post-hoc tests** (robust to unequal variances and group sizes) to pinpoint which exact industry sectors drive the differences.

Every test adheres strictly to the **4-Step Answering Protocol** (Slide 9).

---

## 2. Primary Analysis: Sector Differences in Profit Margin

### 2.1 Protocol Step 1 — IDENTIFY

- **Variables**:
  - Independent Variable ($X$): `Sector` (Nominal grouping factor, exactly 5 categories: _Consumer, Finance, Healthcare, Industrials & Energy, Tech & Comms_).
  - Dependent Variable ($Y$): `Profit_Margin` (Quantitative continuous ratio variable, FY2025 net profit margin).
- **Test Selection**: **One-Way ANOVA**, followed by **Levene's Test of Homogeneity of Variances**, **Welch's Robust ANOVA**, and **Games-Howell Post-Hoc Pairwise Comparisons**.
- **Methodological Justification (Slide 17 & 118)**: When comparing a continuous outcome across 3 or more qualitative groups, multiple independent $t$-tests cause severe alpha inflation (accumulation of Type I error). One-Way ANOVA controls the family-wise error rate. Because financial margins exhibit heterogeneous sector variances, standard Fisher ANOVA is invalid; Welch's ANOVA and Games-Howell adjustments are statistically required.

---

### 2.2 Protocol Step 2 — HYPOTHESISE

- **Null Hypothesis ($H_0$)**: There is no significant difference in mean profit margin across the 5 economic sectors ($\mu_{\text{Consumer}} = \mu_{\text{Finance}} = \mu_{\text{Healthcare}} = \mu_{\text{Industrials}} = \mu_{\text{Tech}}$). Industry sector has no bearing on average corporate profitability.
- **Alternative Hypothesis ($H_1$)**: At least one sector's population mean profit margin differs significantly from the others.

---

### 2.3 Protocol Step 3 — DECIDE

#### Sector Group Descriptive Summary ($N = 503$)

| Consolidated Sector      | $n$ |   Mean ($\bar{x}$)    | Std. Dev. ($s$) | Median ($\text{Mdn}$) | Interquartile Range ($IQR$) |
| ------------------------ | :-: | :-------------------: | :-------------: | :-------------------: | :-------------------------: |
| **Finance**              | 71  | **0.2243** ($22.4\%$) |     0.1241      | **0.2273** ($22.7\%$) |           0.1541            |
| **Tech & Comms**         | 108 |   0.1672 ($16.7\%$)   |   **0.2947**    |   0.1628 ($16.3\%$)   |           0.1882            |
| **Consumer**             | 116 |   0.1329 ($13.3\%$)   |     0.1374      |   0.1105 ($11.1\%$)   |           0.1565            |
| **Industrials & Energy** | 148 |   0.1310 ($13.1\%$)   |   **0.0861**    |   0.1199 ($12.0\%$)   |         **0.0900**          |
| **Healthcare**           | 60  | **0.0936** ($9.4\%$)  |     0.2237      | **0.0990** ($9.9\%$)  |           0.1500            |

#### 1. Checking ANOVA Assumptions: Homogeneity of Variances

- **Levene's Test (Brown-Forsythe center = median)**:
  $$F(4, 498) = 5.392, \quad p < .001$$
- **Evaluation**: The Levene test decisively **rejects the assumption of equal variances ($p < .001$)**. Standard deviation ranges from a tight $8.61\%$ in _Industrials & Energy_ to a massive $29.47\%$ in _Tech & Comms_. Standard Fisher's ANOVA is violated; **Welch's ANOVA must be reported** (Slide 118).

#### 2. Welch's Robust ANOVA & Non-Parametric Verification

- **Welch's ANOVA**:
  $$F_{\text{Welch}}(4, 191.21) = 9.302, \quad p < .001$$
- **Standard Fisher's ANOVA (for comparison)**:
  $$F(4, 498) = 5.257, \quad p < .001, \quad \eta^2 = 0.0405, \quad \omega^2 = 0.0327$$
- **Kruskal-Wallis Non-Parametric Test**:
  $$H(4) = 45.984, \quad p < .001$$
- **Decision**: Decisively **reject $H_0$ ($p < .001$)**. Across all parametric, robust, and non-parametric tests, economic sectors display highly significant differences in operating profit margins.
- **Effect Size**: $\eta^2 = 0.0405$ indicates that **$4.05\%$ of the total cross-sectional variance** in profit margins among S&P 500 companies is directly explained by sector classification.

![Figure 1: One-Way ANOVA Boxplots — Net Profit Margin across Economic Sectors](figures/anova_sector_boxplots.png)

---

### 2.4 Games-Howell Post-Hoc Pairwise Comparisons

Because group variances and sample sizes are unequal, the **Games-Howell procedure** is applied across all 10 pairwise sector comparisons:

| Comparison Pair                      | Mean Difference | Standard Error | 95% Confidence Interval | $t$-statistic | Adjusted $p$-value |     Significant?     |
| ------------------------------------ | :-------------: | :------------: | :---------------------: | :-----------: | :----------------: | :------------------: |
| **Finance vs. Consumer**             |   **+0.0914**   |     0.0195     |  **[+0.038, +0.145]**   |   **4.689**   |     **< .001**     | **YES ($p < .001$)** |
| **Finance vs. Healthcare**           |   **+0.1307**   |     0.0324     |  **[+0.040, +0.221]**   |   **4.032**   |      **.001**      | **YES ($p = .001$)** |
| **Finance vs. Industrials & Energy** |   **+0.0933**   |     0.0163     |  **[+0.048, +0.139]**   |   **5.713**   |     **< .001**     | **YES ($p < .001$)** |
| **Finance vs. Tech & Comms**         |     +0.0571     |     0.0320     |    [-0.031, +0.145]     |     1.786     |        .385        |          NO          |
| **Tech & Comms vs. Healthcare**      |     +0.0737     |     0.0405     |    [-0.038, +0.185]     |     1.820     |        .366        |          NO          |
| **Tech & Comms vs. Consumer**        |     +0.0343     |     0.0311     |    [-0.052, +0.120]     |     1.103     |        .805        |          NO          |
| **Tech & Comms vs. Industrials**     |     +0.0363     |     0.0292     |    [-0.045, +0.117]     |     1.241     |        .727        |          NO          |
| **Consumer vs. Healthcare**          |     +0.0394     |     0.0316     |    [-0.049, +0.127]     |     1.247     |        .724        |          NO          |
| **Consumer vs. Industrials**         |     +0.0020     |     0.0146     |    [-0.038, +0.042]     |     0.136     |       1.000        |          NO          |
| **Healthcare vs. Industrials**       |     -0.0374     |     0.0297     |    [-0.121, +0.046]     |    -1.257     |        .718        |          NO          |

#### Substantive Findings:

1. **The Financial Premium**: The **Finance** sector generates a significantly higher average profit margin ($22.43\%$) than Consumer ($13.29\%$), Industrials & Energy ($13.10\%$), and Healthcare ($9.36\%$), with differences exceeding $9$ to $13$ percentage points ($p \le .001$).
2. **Tech Dispersion**: Although Technology exhibits the second-highest mean ($16.72\%$) and median ($16.28\%$), its massive standard deviation ($29.47\%$) prevents its pairwise differences from reaching statistical significance after Games-Howell penalty adjustments.

---

### 2.5 Secondary Analysis: Governance Risk Across Sectors

- **ANOVA Model**: `Overall_Governance_Risk ~ Sector`
- **Welch's Robust ANOVA**:
  $$F_{\text{Welch}}(4, 207.84) = 3.960, \quad p = .004, \quad \eta^2 = 0.0311$$
- **Finding**: Governance risk varies significantly across industries ($p = .004$). **Tech & Comms** registers the highest mean governance risk ($\bar{x} = 6.08$, $\text{Mdn} = 7.0$), whereas **Industrials & Energy** achieves the lowest risk ($\bar{x} = 4.77$, $\text{Mdn} = 5.0$).

![Figure 2: Scatter Plot of Governance Risk Score vs. Net Profit Margin](figures/scatter_governance_margin.png)

---

### 2.6 Protocol Step 4 — RECOMMEND (What Does the Manager Do on Monday Morning?)

> **"Corporate strategists and capital allocators must not benchmark financial profitability against a generic index-wide hurdle rate; on Monday morning, finance executives should establish sector-specific profitability floors ($22\%$ in Finance vs. $13\%$ in Industrials and $10\%$ in Healthcare). Furthermore, boards in Technology and Communications must prioritize corporate governance reforms—particularly dismantling dual-class share rights and tying executive pay to operating margins—to eliminate the industry's elevated governance risk premium ($6.08/10$) identified by ISS."**

---

## 3. Jamovi Session 3 Execution Guide

To replicate these ANOVA and Post-Hoc analyses in Jamovi:

1. Menu: `Analyses` $\rightarrow$ `ANOVA` $\rightarrow$ `One-Way ANOVA`.
2. Move **`Profit_Margin`** to `Dependent Variable`.
3. Move **`Sector`** to `Grouping Variable`.
4. Under `Variances`: Select **`Don't assume equal (Welch's)`**.
5. Under `Assumption Checks`: Check **`Homogeneity test (Levene's)`** and **`Normality test (Q-Q plot)`**.
6. Under `Post-Hoc Tests`: Select **`Games-Howell`**, check `Mean difference`, `Confidence intervals (95%)`, and `Test significance`.
7. Under `Plots`: Check `Descriptives plot`, select `Box plot`, check `Show mean` and `Outliers`.
