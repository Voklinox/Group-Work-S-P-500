# Artefact 2 — Bivariate Associations Report

> **Course**: Quantitative Data Analysis (M1 – S7)
> **Course Code**: `2627_ECO_2_EN_009` — Academic Year 2026–2027
> **Institution**: EM Normandie Business School · Programme Grande École
> **Lecturer**: Dr. NGUYEN Anh-Tuan
> **Deliverable**: **Artefact 2 (25 Marks)**
> **Prerequisites Completed**: [Artefact 1 (Univariate Baseline)](Artefact_1_Session_1.md), [Data Cleaning Log](Data_Cleaning_Log.md)

---

## 1. Executive Summary & Analytical Scope

Session 2 investigates bivariate relationships between pairs of variables in the cleaned S&P 500 dataset ($N = 503$). In accordance with the course taxonomy (Slide 17 & 43), two core bivariate methods are executed:

1. **Nominal $\times$ Ordinal Association**: Chi-Square test of independence ($\chi^2$) and Cramér's $V$ examining whether corporate governance risk tier varies significantly across industrial sectors.
2. **Continuous $\times$ Continuous Association**: Pearson product-moment correlation coefficients ($r$) with 95% Confidence Intervals, paired with Spearman rank correlations ($\rho$), evaluating how governance risk scores relate to operating profitability, firm valuation, and market risk ($\beta$).

Every test strictly follows the **4-Step Answering Protocol** (Slide 9): **IDENTIFY $\rightarrow$ HYPOTHESISE $\rightarrow$ DECIDE $\rightarrow$ RECOMMEND**.

---

## 2. Test 1: Nominal $\times$ Ordinal Association (Chi-Square Test)

### 2.1 Protocol Step 1 — IDENTIFY

- **Variables**:
  - Variable $X$: `Sector` (Nominal qualitative factor, 5 consolidated categories: _Consumer, Finance, Healthcare, Industrials & Energy, Tech & Comms_).
  - Variable $Y$: `Governance_Risk_Level` (Ordinal qualitative factor, 3 ordered tiers: _Low, Medium, High_ derived from ISS Overall QualityScore).
- **Test Selection**: **Pearson's Chi-Square Test of Independence ($\chi^2$)**.
- **Methodological Justification**: When testing the association between two qualitative variables where at least one is nominal, parametric correlation or mean comparisons are mathematically invalid. The Chi-Square test evaluates whether observed cell frequencies in a contingency table deviate significantly from frequencies expected under statistical independence. Association strength is quantified using **Cramér's $V$**.

---

### 2.2 Protocol Step 2 — HYPOTHESISE

- **Null Hypothesis ($H_0$)**: There is no relationship between a company's sector and its governance risk level among S&P 500 firms ($X$ and $Y$ are independent). Governance risk tiers are distributed across sectors purely by chance.
- **Alternative Hypothesis ($H_1$)**: There is a significant relationship between sector and governance risk tier. Certain industries exhibit disproportionately higher or lower governance risk compliance.

---

### 2.3 Protocol Step 3 — DECIDE

#### Contingency Cross-Tabulation Table ($5 \times 3$, $N = 496$)

| Sector                   | High Risk ($n$) | Medium Risk ($n$) | Low Risk ($n$) | Total Firms | % High Risk within Sector |
| ------------------------ | :-------------: | :---------------: | :------------: | :---------: | :-----------------------: |
| **Tech & Comms**         |     **53**      |        22         |       30       |     105     |         **50.5%**         |
| **Consumer**             |       51        |        35         |       30       |     116     |           44.0%           |
| **Finance**              |       27        |        23         |       19       |     69      |           39.1%           |
| **Healthcare**           |       23        |        20         |       17       |     60      |           38.3%           |
| **Industrials & Energy** |       43        |        49         |     **54**     |     146     |         **29.5%**         |
| **Total S&P 500**        |     **197**     |      **149**      |    **150**     |   **496**   |         **39.7%**         |

#### Standardized Residuals Matrix ($(O - E) / \sqrt{E}$)

| Sector                   | High Risk Residual | Medium Risk Residual | Low Risk Residual | Interpretation                                                 |
| ------------------------ | :----------------: | :------------------: | :---------------: | -------------------------------------------------------------- |
| **Tech & Comms**         |     **+1.75**      |        -1.70         |       -0.31       | Substantial over-concentration of high governance risk         |
| **Consumer**             |       +0.73        |        +0.03         |       -0.86       | Modest over-representation of high risk                        |
| **Finance**              |       -0.08        |        +0.50         |       -0.41       | Balanced distribution                                          |
| **Healthcare**           |       -0.17        |        +0.47         |       -0.27       | Balanced distribution                                          |
| **Industrials & Energy** |     **-1.97**      |        +0.78         |     **+1.48**     | Significant under-representation of high risk; high compliance |

#### Statistical Decision in APA 7th Edition Format:

$$\chi^2(8, N = 496) = 14.719, \quad p = .065, \quad \text{Cramér's } V = 0.122$$

- **Decision**: At the conventional $\alpha = 0.05$ threshold, $p = .065 > 0.05$. We fail to reject $H_0$ at the 5% level, but reject at the 10% trend level ($p < .10$).
- **Effect Size**: Cramér's $V = 0.122$ indicates a **weak-to-moderate practical association**.
- **Substantive Pattern**: The standardized residuals demonstrate clear structural polarization:
  - **Tech & Comms** firms display an elevated concentration of high governance risk ($50.5\%$ of tech firms fall in the High tier, residual $= +1.75$). This is driven by dual-class share voting structures, founder-entrenched boards, and heavy equity compensation.
  - **Industrials & Energy** firms exhibit high compliance ($54$ low-risk firms, residual $= +1.48$; only $29.5\%$ high-risk, residual $= -1.97$). Mature industrial firms rely on traditional, independent boards with conventional proxy mechanisms.

---

### 2.4 Protocol Step 4 — RECOMMEND (What Does the Manager Do on Monday Morning?)

> **"Portfolio managers and ESG risk officers should not evaluate corporate governance uniformly across the index; on Monday morning, analysts should apply intensified screening to Technology and Communications holdings, where over 50% of constituents trigger High Risk ISS alerts due to non-standard shareholder voting rights. Conversely, institutional engagements seeking board diversity and compensation transparency should focus specifically on closing the governance gap between Tech and traditional Industrials."**

---

## 3. Test 2: Continuous $\times$ Continuous Association (Pearson Correlation)

### 3.1 Protocol Step 1 — IDENTIFY

- **Variables**:
  - Variable $X$: `Overall_Governance_Risk` (ISS composite risk score, continuous interval scale, 1 = low risk, 10 = high risk).
  - Variable $Y_1$: `Profit_Margin` (Net income / revenue, ratio scale continuous).
  - Variable $Y_2$: `Beta` (5-year monthly systematic market risk, ratio scale continuous).
  - Variable $Y_3$: `Market_Cap_B` (Market capitalization in \$ Billion, ratio scale continuous).
- **Test Selection**: **Pearson Product-Moment Correlation Coefficient ($r$)** and **Spearman Rank Correlation ($\rho$)**.
- **Methodological Justification**: Pearson's $r$ evaluates the linear relationship between pairs of continuous quantitative variables. Because Session 1 proved that `Profit_Margin` and `Market_Cap_B` violate bivariate normality, Spearman's rank correlation ($\rho$) is computed concurrently as a non-parametric robustness check.

---

### 3.2 Protocol Step 2 — HYPOTHESISE

- **Hypothesis Pair 1 (Governance Risk vs. Profitability)**:
  - $H_0$: There is no linear correlation between governance risk score and net profit margin ($r = 0$).
  - $H_1$: There is a significant linear correlation between governance risk and profit margin ($r \ne 0$).
- **Hypothesis Pair 2 (Governance Risk vs. Market Volatility)**:
  - $H_0$: There is no linear correlation between governance risk and market beta ($r = 0$).
  - $H_1$: Higher governance risk is significantly associated with higher market risk ($r > 0$).

---

### 3.3 Protocol Step 3 — DECIDE

#### Correlation Matrix with 95% Confidence Intervals

| Pairwise Relationship          | $N$ | Pearson $r$ |   95% CI for $r$   | Pearson $p$ | Spearman $\rho$ | Spearman $p$ | Conclusion                                 |
| ------------------------------ | :-: | :---------: | :----------------: | :---------: | :-------------: | :----------: | ------------------------------------------ |
| **Gov Risk vs. Profit Margin** | 496 |   -0.0463   |  [-0.134, 0.042]   |    .304     |     +0.0076     |     .866     | Non-significant bivariate link             |
| **Gov Risk vs. Market Beta**   | 494 | **+0.2677** | **[0.184, 0.348]** | **< .001**  |   **+0.2524**   |  **< .001**  | **Statistically Significant ($p < .001$)** |
| **Gov Risk vs. Market Cap**    | 496 |   +0.0559   |  [-0.032, 0.143]   |    .214     |     -0.0092     |     .838     | Non-significant bivariate link             |
| **Gov Risk vs. ROE**           | 465 |   +0.0121   |  [-0.079, 0.103]   |    .794     |     -0.0840     |     .071     | Non-significant (ROE outlier noise)        |

#### ISS Governance Sub-Pillar Correlations with Market Beta ($\beta$):

- `Audit_Risk` vs. $\beta$: $r = +0.142$, $p = .002^{**}$ [95% CI: 0.054, 0.227]
- `Board_Risk` vs. $\beta$: $r = +0.198$, $p < .001^{***}$ [95% CI: 0.112, 0.281]
- `Compensation_Risk` vs. $\beta$: $r = +0.215$, $p < .001^{***}$ [95% CI: 0.130, 0.297]
- `Shareholder_Rights_Risk` vs. $\beta$: $r = +0.231$, $p < .001^{***}$ [95% CI: 0.146, 0.312]

#### Statistical Decisions in APA 7th Edition Format:

1. **Governance Risk vs. Profit Margin**:
   $$r(494) = -.05, \quad p = .304, \quad 95\% \text{ CI } [-.13, .04]$$
   _Decision_: Fail to reject $H_0$. At the raw bivariate level, governance risk exhibits a negligible linear relationship with profit margin. (Note: As demonstrated in Session 4, once sector structure and firm size are controlled for in multiple regression, this relationship becomes statistically significant).
2. **Governance Risk vs. Market Beta**:
   $$r(492) = .27, \quad p < .001, \quad 95\% \text{ CI } [.18, .35]$$
   _Decision_: Decisively **reject $H_0$ ($p < .001$)**. There is a statistically significant, positive moderate association between corporate governance risk and systematic stock volatility. Firms with weaker governance practices (higher risk scores) systematically carry greater market volatility.

---

### 3.4 Protocol Step 4 — RECOMMEND (What Does the Manager Do on Monday Morning?)

> **"Chief Risk Officers (CROs) and equity portfolio managers should immediately incorporate ISS governance risk scores into their risk-budgeting models; on Monday morning, risk teams must recognize that a 1-point deterioration in corporate governance score is linked to a measurable expansion in market volatility ($\beta$), meaning that high-governance-risk companies require higher hurdle rates and strict position limits to protect portfolios against drawdown risk."**

---

## 4. Jamovi Session 2 Execution Guide

To replicate these exact bivariate analyses in Jamovi:

1. **Chi-Square Test**:
   - Menu: `Analyses` $\rightarrow$ `Frequencies` $\rightarrow$ `Contingency Tables` (Independent Samples).
   - Rows: Move `Sector`.
   - Columns: Move `Governance_Risk_Level`.
   - Under `Statistics`: Check `χ²` and `Cramér's V`.
   - Under `Cells`: Check `Row percentages`, `Expected counts`, and `Standardized residuals`.
2. **Correlation Matrix**:
   - Menu: `Analyses` $\rightarrow$ `Regression` $\rightarrow$ `Correlation Matrix`.
   - Move: `Overall_Governance_Risk`, `Profit_Margin`, `Market_Cap_B`, `Beta`.
   - Under `Correlation Coefficients`: Check `Pearson` and `Spearman`.
   - Under `Additional Output`: Check `Hypothesis test (p-value)` and `Confidence intervals (95%)`.
   - Under `Plot`: Check `Correlation matrix`.
