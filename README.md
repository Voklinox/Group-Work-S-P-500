# S&P 500 Corporate Governance & Financial Performance Analysis

> **Quantitative Data Analysis — M1 S7 Group Consulting Project**  
> **Course Code**: `2627_ECO_2_EN_009` · **Institution**: EM Normandie Business School · **Lecturer**: Dr. NGUYEN Anh-Tuan  
> **Academic Year**: 2026–2027

---

## 1. Managerial Research Question (Problematic)

> **"Does corporate governance risk (ISS QualityScore) compromise financial profitability and market valuation among S&P 500 firms, or does strong governance provide a resilience and performance premium?"**

This consulting-oriented research investigation examines whether high compliance and institutional governance mechanisms impose operational frictions that hinder financial returns, or conversely protect shareholder value and command a valuation premium in large-cap equities.

---

## 2. Repository Architecture

```
Group Work S&P 500/
├── data/
│   ├── raw/
│   │   └── sp500_esg_dataset_raw.csv         # Pristine unedited extraction archive
│   └── processed/
│       ├── sp500_esg_cleaned.csv             # Cleaned analytical dataset (Python / R)
│       ├── sp500_esg_jamovi.csv              # Jamovi-specific CSV (clean headers, typed)
│       └── sp500_esg_jamovi.xlsx             # Jamovi/Excel workbook with Codebook sheet
├── docs/
│   ├── AQD_Session1.pdf                      # Course syllabus & lecture slides
│   ├── PROJECT_JOURNAL.md                    # Master audit log & chronological development diary
│   ├── Approval_Slip.md                      # Official dataset approval slip (Coursework Part 1 - 10 marks)
│   ├── Data_Cleaning_Log.md                  # Granular data cleaning & diagnostic audit log
│   ├── Artefact_1_Session_1.md               # Session 1 submission deliverable (20 marks)
│   ├── Jamovi_Guide_Session1.md              # Click-by-click Jamovi navigation guide
│   └── dashboard.html                        # Interactive executive data visualization dashboard
├── figures/                                  # Publication-quality charts (APA 7th edition format)
│   ├── sector_distribution.png               # Frequency bar chart of 5 sectors
│   ├── market_cap_quartiles.png              # Ordinal distribution of market cap
│   ├── governance_risk_distribution.png      # Distribution of ISS overall risk
│   ├── profit_margin_normality.png           # 3-evidence normality diagnostic (Hist + KDE + QQ)
│   ├── market_cap_distribution.png           # Distribution of market capitalization
│   └── correlation_preview.png               # Continuous variable correlation matrix
├── src/                                      # Modular Python package
│   ├── __init__.py
│   ├── config.py                             # Paths, variable definitions, Jamovi types, styling
│   ├── cleaning.py                           # Systematic cleaning, imputation & feature engineering
│   ├── stats_univariate.py                   # Univariate engine (Mean, Median, Mode, SD, Skew, Kurt, Shapiro-Wilk)
│   └── visualize.py                          # Visual generator following strict APA guidelines
├── tests/
│   └── test_dataset_integrity.py             # Automated pytest suite validating course constraints
├── CLAUDE.md                                 # AI assistant context & system guidelines
├── README.md                                 # Project documentation (this file)
└── requirements.txt                          # Locked scientific dependencies
```

---

## 3. Quick Start & Execution

### 3.1 Environment Setup
```bash
# 1. Activate virtual environment
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

### 3.2 Run the End-to-End Pipeline
```bash
# Run data cleaning, harmonization, and Jamovi export
python -m src.cleaning

# Run statistical univariate calculations
python -m src.stats_univariate

# Generate APA 7 publication figures
python -m src.visualize

# Execute automated data integrity test suite
python -m pytest tests/test_dataset_integrity.py -v
```

---

## 4. Key Course Deliverables (Session 1)

1. **[Approval Slip (10 marks)](docs/Approval_Slip.md)**: Official dataset specification and provenance sheet for instructor signature (Slide 35).
2. **[Data Cleaning Log](docs/Data_Cleaning_Log.md)**: Granular audit table of all detected anomalies and applied treatments (Slide 39).
3. **[Artefact 1 Report (20 marks)](docs/Artefact_1_Session_1.md)**: Comprehensive submission document with 5 univariate profiles, 3-evidence normality diagnostic, and managerial recommendations (Slide 41).
4. **[Jamovi Lab Guide](docs/Jamovi_Guide_Session1.md)**: Step-by-step navigation instructions for Jamovi desktop software.
5. **[Project Master Journal](docs/PROJECT_JOURNAL.md)**: Chronological development log and methodological documentation.

---

## 5. 4-Week Course Roadmap

| Session | Focus Area | Statistical Methods & Tests | Deliverable |
|:---:|---|---|:---:|
| **1** | Data Cleaning & Univariate Description | Central tendency, dispersion, shape, Shapiro-Wilk | **Artefact 1 (20 pts) + Provenance (10 pts)** |
| **2** | Bivariate Associations | Chi-Square ($\chi^2$), Cramér's $V$, Pearson $r$ (95% CI) | Artefact 2 (25 pts) |
| **3** | Group Mean Comparisons | One-Way ANOVA, Welch's ANOVA, Games-Howell post-hoc | Artefact 3 (20 pts) |
| **4** | Predictive Regression & Strategy | Simple & Multiple Linear Regression (OLS), VIF, diagnostics | Artefact 4 (25 pts) |

---

## 6. Academic & Methodological Protocol

All analyses strictly follow the 4-step framework (Slide 9):
1. **IDENTIFY**: Method justified strictly by variable scale (Nominal, Ordinal, Continuous).
2. **HYPOTHESISE**: $H_0$ and $H_1$ articulated in business language.
3. **DECIDE**: Statistical significance evaluated at $\alpha = 0.05$ with effect size strength.
4. **RECOMMEND**: Actionable executive takeaways answering *"What does the manager do on Monday morning?"*
