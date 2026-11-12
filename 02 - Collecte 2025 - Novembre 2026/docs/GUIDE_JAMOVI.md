# Guide Jamovi et grille de rapprochement (étape 2 : David manipule, l'agent guide)

Ce guide dit **quoi faire dans Jamovi** et **quels chiffres de référence retrouver** (calculés par programme, `docs/RAPPORT_DE_REFERENCE.md`). Les valeurs « référence » ne sont pas des sorties Jamovi : à l'étape 2, David reproduit chaque analyse, note la sortie Jamovi dans la colonne de droite, et on explique tout écart. Tolérance : arrondi à la dernière décimale affichée ; pour les p-valeurs, même conclusion (< .001 ou valeur à 3 décimales).

## 0. Préparation (à faire une seule fois)

1. Version de Jamovi installée : 2.7 (vérifier dans ≡ → About). Ouvrir `data/processed/sp500_2025_JAMOVI_DRAFT.csv` : ≡ → Open → Browse. (Le fichier définitif remplacera ce brouillon à l'étape D04 ; ne pas commencer sur un autre fichier.)
2. Onglet **Data**, double-clic sur chaque en-tête, régler le type :
   - `cik`, `company` → **ID** ;
   - `sector`, `sector_group`, `finance_vs_other`, `profitable` → **Nominal** ;
   - `size_quartile` → **Ordinal**, niveaux dans l'ordre Q1, Q2, Q3, Q4 ;
   - `net_margin_pct`, `roa_pct`, `revenue_bn`, `assets_bn`, `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct`, `asset_turnover` → **Continuous** ; `period_end` → Nominal ou ID (non analysée).
   - Contrôle : 500 lignes ; `net_margin_pct` N = 498 ; `revenue_growth_pct` N = 488 ; deux lignes vides (Dayforce, Paramount) sont normales.
3. Sauvegarder : ≡ → Save As → `.omv`. Ne pas modifier les données sans le dire.

## 1. Séance 1 — profils et normalité (Analyses → Exploration → Descriptives)

- Variables continues : `net_margin_pct`, `debt_ratio_pct`, `revenue_growth_pct` ; options : moyenne, médiane, mode, écart-type, min, max, asymétrie, aplatissement, quartiles ; **Shapiro-Wilk** coché ; graphiques histogramme et box plot.
- Qualitatives : `sector_group` et `size_quartile` : tableaux de fréquences, bar plot.

| Résultat | Référence | Jamovi |
|---|---|---|
| Marge : N, moyenne, médiane, écart-type | 498 ; 13,75 ; 12,90 ; 14,72 | |
| Marge : asymétrie, aplatissement (excès) | −2,67 ; 31,3 | |
| Marge : Shapiro-Wilk | W = 0,791 ; p < .001 | |
| Endettement : moyenne, médiane, écart-type | 66,73 ; 64,21 ; 28,01 | |
| Croissance CA : N, moyenne, médiane | 488 ; 8,64 ; 6,37 | |
| Secteurs (effectifs) | Industrials & Energy 159, Consumer 115, Tech & Comms 90, Finance 76, Healthcare 60 | |
| Quartiles de taille | 125 / 124 / 124 / 125 (2 manquants) | |

Note : l'aplatissement de Jamovi est l'excès (0 pour une normale). Le **mode** d'une variable continue peut différer de la référence (arrondi à l'entier dans la référence) ; ne pas s'en inquiéter.

## 2. Séance 2 — khi-deux, corrélations, test t

**Khi-deux** : Analyses → Frequencies → Independent Samples (χ² test of association). Lignes : `sector_group` ; colonnes : `size_quartile`. Statistics : χ², Phi et Cramér's V. Cells : Observed, Expected, Row percentages.

| Résultat | Référence | Jamovi |
|---|---|---|
| χ² (df) ; p ; N | 91,76 (12) ; < .001 ; 498 | |
| V de Cramér | 0,248 | |
| Plus petit effectif attendu | 14,9 | |
| Ligne Finance en % (Q1/Q2/Q3/Q4) | 6,6 / 13,2 / 19,7 / 60,5 | |

**Corrélations** : Analyses → Regression → Correlation Matrix ; variables : `net_margin_pct`, `roa_pct`, `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct`, `asset_turnover` ; cocher Pearson **et** Spearman, Report significance, Flag significant, Plot : Correlation matrix. Nuage détaillé : Exploration → Scatterplot (`revenue_growth_pct` en X, `net_margin_pct` en Y, ligne de régression linéaire).

| Paire (N) | Pearson r | Spearman ρ | Jamovi |
|---|---|---|---|
| Marge – croissance (488) | 0,266 (p < .001) | 0,295 (p < .001) | |
| Marge – rotation (498) | −0,217 (< .001) | −0,375 (< .001) | |
| Marge – ln actif (498) | 0,085 (p = .059) | 0,057 (p = .204) | |
| Marge – endettement (498) | 0,044 (p = .332) | −0,059 (p = .190) | |
| ROA – ln actif (498) | −0,295 (< .001) | −0,377 (< .001) | |

Attention : Jamovi traite les valeurs manquantes **paire par paire** par défaut ; les N de la ligne ci-dessus doivent apparaître.

**Test t** : Analyses → T-Tests → Independent Samples ; variable dépendante `net_margin_pct`, groupes `finance_vs_other`. Cocher Student, Welch, Mann-Whitney U ; Effect size (Cohen's d) ; Assumption checks : Equality of variances, Normality ; Descriptives.

| Résultat | Référence | Jamovi |
|---|---|---|
| Moyennes Finance / Non-finance (N) | 20,90 (76) / 12,46 (422) | |
| Levene | F = 0,12 ; p = .73 (mean) | |
| Student | t(496) = 4,70 ; p < .001 | |
| Welch | t(127,9) = 5,70 ; p < .001 | |
| Mann-Whitney U | 22 740 ; p < .001 | |
| Cohen's d ; écart de moyennes | 0,585 ; 8,44 (IC Welch 5,51 à 11,37) | |

## 3. Séance 3 — ANOVA et post-hoc

**One-Way ANOVA** : Analyses → ANOVA → One-Way ANOVA ; dépendante `net_margin_pct`, groupes `sector_group`. Variances : cocher **Don't assume equal (Welch)** et **Assume equal (Fisher)**. Additional : Descriptives table et plot ; Assumption checks : Equality of variances, Normality ; Post-Hoc : **Games-Howell** (variances inégales), et Tukey pour comparaison. η² : Analyses → ANOVA → ANOVA, Effect size η².
**Non paramétrique** : ANOVA → Non-Parametric → One-Way ANOVA (Kruskal-Wallis) ; cocher DSCF pairwise comparisons.

| Résultat | Référence | Jamovi |
|---|---|---|
| Levene (moyenne) | F(4, 493) = 3,61 ; p = .0065 (version médiane : 3,45 ; p = .0086) | |
| Welch | F(4 ; 189,1) = 10,41 ; p < .001 | |
| Fisher | F(4, 493) = 7,53 ; p < .001 | |
| η² | 0,058 | |
| Kruskal-Wallis | χ²(4) = 46,2 ; p < .001 (ε² = 0,093) | |
| Moyennes | Consumer 11,92 ; Finance 20,90 ; Healthcare 9,51 ; Industrials & Energy 12,07 ; Tech & Comms 15,87 | |
| Games-Howell (p) | Finance–Consumer < .001 ; Finance–Healthcare = .007 ; Finance–Industrials < .001 ; Finance–Tech = .137 ; autres paires non significatives | |
| DSCF (p) | Consumer–Tech = .022 ; Industrials–Tech = .014 ; Finance–{Consumer, Healthcare, Industrials} < .001 | |

Jamovi peut centrer Levene sur la moyenne ou la médiane : comparer avec les deux valeurs. Games-Howell et DSCF doivent donner les mêmes **décisions** (signification), les p exacts peuvent différer légèrement selon l'algorithme du quantile de l'étendue studentisée.

## 4. Séance 4 — régressions

**Simple** : Analyses → Regression → Linear Regression ; dépendante `net_margin_pct` ; covariable `ln_assets`. Model Fit : R, R², R² ajusté, F ; Coefficients : estimation, IC 95 %, estimation standardisée.

| Résultat | Référence | Jamovi |
|---|---|---|
| N ; R² ; F(1, 496) ; p | 498 ; 0,0072 ; 3,59 ; .059 | |
| Constante ; B(ln_assets) ; ES ; t ; p | −9,49 ; 0,958 ; 0,506 ; 1,90 ; .059 | |

**Multiple** : dépendante `net_margin_pct` ; Covariables : `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct` ; **Factors** : `sector_group` (c'est un facteur, pas une covariable) avec **Reference Level = Industrials & Energy** (Reference Levels). Model Fit : R, R², R² ajusté, F ; Coefficients : estimation, ES, IC, standardisé ; Assumption Checks : Autocorrelation test (Durbin-Watson), Collinearity statistics (VIF), Normality test (Shapiro), Q-Q plot, Residual plots, **Cook's distance**. Jamovi n'offre pas de Breusch-Pagan ni d'erreurs HC3 dans cette procédure : ces résultats restent « référence ».

| Résultat | Référence | Jamovi |
|---|---|---|
| N ; R² ; R² ajusté | 488 ; 0,114 ; 0,101 | |
| F(7, 480) ; p | 8,80 ; < .001 | |
| B croissance (ES ; p ; β) | 0,248 (0,043 ; < .001 ; 0,25) | |
| B Finance vs Industrials & Energy (p) | 7,84 (< .001) | |
| B Tech & Comms ; Healthcare ; Consumer (p) | 2,40 (.202) ; −2,21 (.300) ; 0,24 (.891) | |
| B ln actif ; endettement (p) | 0,012 (.982) ; 0,018 (.447) | |
| VIF maximal ; Durbin-Watson | 1,41 ; 1,96 | |
| Shapiro-Wilk des résidus | W = 0,80 ; p < .001 (résidus non normaux) | |
| Plus grandes distances de Cook | Expand Energy 0,66 ; Moderna 0,59 | |

**Variantes à reproduire** (Data → Filter pour exclure les observations, ou Compute) : sans Expand Energy et Moderna et autres observations influentes (N = 468 : exclure les observations dont la distance de Cook dépasse 4/488) ; sans le secteur financier (N = 418, filtre `sector_group != "Finance"`) ; ROA comme dépendante (N = 488 ; B ln actif = −1,97 ; p < .001). Les valeurs de référence sont dans `outputs/analyses_reference/s4_sens_*`.

## 5. Points de vigilance (erreurs fréquentes d'après le cours)

Type de mesure faux (`sector_group` en Continuous) ; facteur mis dans Covariates ; lire Levene à l'envers ; oublier « toutes choses égales par ailleurs » ; interpréter la constante ; écrire « cause » ; ne pas indiquer N, df et taille d'effet ; sortie copiée sans interprétation. Vérifier à chaque sortie : df = N − k − 1 ; F = MS inter / MS intra ; t = B / ES ; R² ajusté ≤ R² ; V de Cramér = √(χ² / (N (k − 1))).

## 6. Sauvegardes à conserver pour le rapport

Le fichier `.omv` ; les sorties (copie ou export PDF/HTML de chaque analyse) ; les graphiques exportés ; la grille ci-dessus complétée avec l'écart éventuel et son explication. Chaque chiffre du Google Doc devra renvoyer à une sortie identifiable.
