# Data preparation v2

Prepared on 11 November 2026 for David Wanono, Olyvan Perrin and Guillaume Da Cruz.

## Current analytical file

Use `data/processed/sp500_company_level_v2.csv` in Jamovi. It has 500 distinct companies and 17 variables. The earlier CSVs, Excel workbook, reports and figures remain as historical work and are not the source of final version 2 results.

`python -m src.cleaning` recreates the prepared CSV from the preserved raw archive, exports `sp500_codebook_v2.csv`, and writes the machine-readable preparation log `docs/Data_Preparation_v2.json`. It performs no new download.

## Decisions and evidence

1. The source contains 503 equity records but 500 company identities. Retain GOOGL, FOXA and NWSA; remove the duplicate issuer records GOOG, FOX and NWS. These retained records contain the governance scores for the same respective issuers. This rule is explicit and independent of profitability or the order of the rows. No financial values or capitalisations are summed across share classes.
2. Preserve the raw ticker FISV. Fiserv returned to Nasdaq under FISV in November 2025. [Company announcement](https://investors.fiserv.com/news-releases/news-release-details/fiserv-announces-transfer-stock-exchange-listing-nasdaq).
3. Assign only the consolidated analytical category Finance to Fiserv, based on its financial-technology activities and the project's sector grouping. This is an analyst classification, not a recovered Yahoo Finance raw field. Leave Sector_Raw and all unobserved financial/governance values missing.
4. Keep all other observed source financial values and scores unchanged, including authentic extremes. No missing numerical values are imputed. The reasons for the 32 missing ROE values are not all established.
5. Recompute market-capitalisation quartiles on the 500 issuers. Recompute risk tiers from the observed global scores. Low = 1–3, Medium = 4–6, High = 7–10. The widths of these three groups differ.
6. Describe the data as an archived Yahoo Finance snapshot with ISS governance ranks. Historical notes mention September 2026, but exact retrieval time and per-variable reporting periods have not been independently validated. Do not call the entire dataset harmonised audited FY2025 accounts.

ISS scores are ordinal relative decile ranks. The codebook sets these as Ordinal. Spearman preserves their rank interpretation. If an OLS model uses the numerical score as a covariate, explain that equal spacing and a linear slope are modelling approximations; an interface setting does not establish a continuous measurement scale. [ISS interpretation](https://www.iss-corporate.com/resources/blog/governance-qualityscore-as-an-indicator-of-risk-and-investor-sentiment/).

## Sample sizes

| Field | Valid | Missing |
|---|---:|---:|
| Company, Sector, Market_Cap_B | 500 | 0 |
| Profit_Margin, Total_Revenue_B | 499 | 1 |
| ROE | 468 | 32 |
| Beta | 495 | 5 |
| Overall_Governance_Risk | 495 | 5 |
| Headcount | 496 | 4 |

Pairwise correlation and multiple regression sample sizes depend on the fields included. The regression with all selected controls has 493 complete cases.

## Recalculated results and learning workflow

`docs/working_v2/results/` contains numerical reference tables for version 2. These are independent checks for the upcoming Jamovi work. They are not screenshots or evidence that Jamovi analyses have already been performed.

The Google Doc is a working draft. It contains the cover, research question, source caveats, preparation method, five descriptive profiles and the structure for later analyses. The executive summary, analysis outputs and three final recommendations remain to be completed after the Jamovi reproduction. Peer assessment scores must come from the group and the lecturer's applicable scale.
