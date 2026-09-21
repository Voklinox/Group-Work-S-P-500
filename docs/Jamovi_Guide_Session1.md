# Jamovi Step-by-Step Lab Guide — Session 1

> **Course**: Quantitative Data Analysis (M1 – S7)  
> **Software**: [Jamovi](https://www.jamovi.org/) (Version 2.3+)  
> **Session**: Session 1 — Data Setup & Univariate Descriptives  
> **Target File**: `data/processed/sp500_esg_jamovi.csv`  
> **Final Output**: `sp500_esg_session1.omv`

---

## Step 1: Open the Dataset in Jamovi
1. Launch **Jamovi** on your computer.
2. Click the top-left **`≡` menu** (hamburger icon).
3. Select **`Open`** $\rightarrow$ **`Browse`**.
4. Navigate to your project folder:
   `Group Work S&P 500/data/processed/`
5. Select **`sp500_esg_jamovi.csv`** (or `sp500_esg_jamovi.xlsx`).
6. Click **`Open`**.

---

## Step 2: Configure Variable Measure Types (Crucial Step!)

> [!CAUTION]
> As Dr. NGUYEN Anh-Tuan warns in **Slide 38**: *"If the measure type is wrong, Jamovi will silently refuse to offer you the right test in week 2. This is the number one cause of a lost lab session."*

Double-click on each column header in the **Data** tab and set the **Measure type** and **Data type**:

| Column Name | Measure Type in Jamovi | Data Type | Missing Values / Levels |
|---|---|---|---|
| `Ticker` | **ID** | Text | Identifier (never analysed) |
| `Company` | **Nominal** | Text | Company names |
| `Sector` | **Nominal** | Text | 5 levels: *Consumer, Finance, Healthcare, Industrials & Energy, Tech & Comms* |
| `Total_Revenue_B` | **Continuous** | Decimal | None |
| `Market_Cap_B` | **Continuous** | Decimal | None |
| `Market_Cap_Quartile` | **Ordinal** | Text | 4 ordered levels: *Q1 < Q2 < Q3 < Q4* |
| `Profit_Margin` | **Continuous** | Decimal | None |
| `ROE` | **Continuous** | Decimal | 32 missing values (leave empty) |
| `Beta` | **Continuous** | Decimal | 4 missing values |
| `Headcount` | **Continuous** | Integer | 3 missing values |
| `Overall_Governance_Risk`| **Continuous** | Integer | Scores 1 to 10 |
| `Governance_Risk_Level` | **Ordinal** | Text | 3 ordered levels: *Low < Medium < High* |

---

## Step 3: Run Univariate Analysis on Categorical Variables (Slide 40)

1. Click on the **`Analyses`** tab in the top ribbon.
2. Click **`Exploration`** $\rightarrow$ **`Descriptives`**.
3. In the variable selection box:
   - Move **`Sector`** and **`Governance_Risk_Level`** into the **`Variables`** box.
4. Expand the **`Statistics`** panel below:
   - Check **`Frequency tables`** (for qualitative variables).
   - Uncheck Mean/Median/SD for qualitative variables (avoids the "average sector = 2.4" trap!).
5. Expand the **`Plots`** panel:
   - Check **`Bar plot`**.
6. **Expected Output in Jamovi**:
   - `Sector`: Industrials & Energy (148, 29.4%), Consumer (116, 23.1%), Tech & Comms (108, 21.5%), Finance (71, 14.1%), Healthcare (60, 11.9%).
   - `Governance_Risk_Level`: High (197, 39.7%), Low (150, 30.2%), Medium (149, 30.0%).

---

## Step 4: Run Univariate Analysis & Normality Tests on Continuous Variables

1. Still in **`Analyses`** $\rightarrow$ **`Exploration`** $\rightarrow$ **`Descriptives`** (or create a new Descriptives block):
2. Move the continuous variables into **`Variables`**:
   - `Profit_Margin`
   - `ROE`
   - `Market_Cap_B`
   - `Total_Revenue_B`
   - `Overall_Governance_Risk`
3. Expand **`Statistics`**:
   - **Central Tendency**: Check `Mean`, `Median`, `Mode`.
   - **Dispersion**: Check `Std. deviation`, `Variance`, `Minimum`, `Maximum`, `IQR` (Interquartile range).
   - **Distribution Shape**: Check `Skewness` and `Kurtosis`.
   - **Normality**: Check **`Shapiro-Wilk`**.
4. Expand **`Plots`**:
   - Check **`Histogram`**.
   - Check **`Density`**.
   - Check **`Box plot`** (and check `Outliers`).
   - Check **`Q-Q plot`**.

---

## Step 5: Save and Export Your `.omv` File (Slide 37 & 41)

1. Click the top-left **`≡` menu**.
2. Select **`Save As`** $\rightarrow$ **`Browse`**.
3. Name your file: **`sp500_esg_session1.omv`**.
4. Save it in your project folder.
   *(The `.omv` format bundles both your dataset and all interactive analysis output tables together into a single file ready for submission to Dr. NGUYEN Anh-Tuan).*
