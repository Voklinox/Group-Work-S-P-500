# Guide Jamovi et grille de rapprochement (étape 2 : David manipule, l'agent guide)

Ce guide dit **quoi faire dans Jamovi** et **quels chiffres de référence retrouver** (calculés par programme, `docs/RAPPORT_DE_REFERENCE.md`). Les valeurs « référence » ne sont pas des sorties Jamovi : à l'étape 2, David reproduit chaque analyse, note la sortie Jamovi dans la colonne de droite, et on explique tout écart. Tolérance : arrondi à la dernière décimale affichée ; pour les p-valeurs, même conclusion (< .001 ou valeur à 3 décimales).

## 0. Préparation (à faire une seule fois)

1. Version de Jamovi installée : 2.7.38.0 (≡ → About ; vérifié le 12 nov. 2026). Interface passée en anglais pour correspondre aux noms de menus du guide. Ouvrir `data/processed/sp500_2025_JAMOVI.csv` (fichier final unique ; SHA-256 90c51dd28abc31e57aa3d4ef78aa34890c1391676a5213791f584d581e90c93e) : ≡ → Open → Browse. Ne pas utiliser un autre fichier.
2. Onglet **Data**, double-clic sur chaque en-tête, régler le type :
   - `cik`, `company` → **ID** ;
   - `sector`, `sector_group`, `finance_vs_other`, `profitable` → **Nominal** ;
   - `size_quartile` → **Ordinal**, niveaux dans l'ordre Q1, Q2, Q3, Q4 ;
   - `net_margin_pct`, `roa_pct`, `revenue_bn`, `assets_bn`, `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct`, `asset_turnover` → **Continuous** ; `period_end` → Nominal ou ID (non analysée).
   - Contrôle : 500 lignes ; `net_margin_pct` N = 498 ; `revenue_growth_pct` N = 488 ; deux lignes vides (Dayforce, Paramount) sont normales.
3. Sauvegarder : ≡ → Save As → `.omv` (fichier de travail de David : `data/processed/sp500_2025.omv`, non suivi par Git ; ce n'est pas une version concurrente du CSV). Ne pas modifier les données sans le dire.

## 1. Séance 1 — profils et normalité (Analyses → Exploration → Descriptives)

- Variables continues : `net_margin_pct`, `debt_ratio_pct`, `revenue_growth_pct` ; options : moyenne, médiane, mode, écart-type, min, max, asymétrie, aplatissement, quartiles ; **Shapiro-Wilk** coché ; graphiques histogramme et box plot.
- Qualitatives : `sector_group` et `size_quartile` : tableaux de fréquences, bar plot.

| Résultat | Référence | Jamovi |
|---|---|---|
| Marge : N, moyenne, médiane, écart-type | 498 ; 13,75 ; 12,90 ; 14,72 | 498 ; 13,8 ; 12,9 ; 14,7 : OK |
| Marge : asymétrie, aplatissement (excès) | −2,67 ; 31,3 | −2,67 ; 31,3 : OK |
| Marge : Shapiro-Wilk | W = 0,791 ; p < .001 | W = 0,791 ; p < .001 : OK |
| Endettement : moyenne, médiane, écart-type | 66,73 ; 64,21 ; 28,01 | 66,7 ; 64,2 ; 28,0 : OK |
| Croissance CA : N, moyenne, médiane | 488 ; 8,64 ; 6,37 | 488 ; 8,64 ; 6,37 : OK |
| Secteurs (effectifs) | Industrials & Energy 159, Consumer 115, Tech & Comms 90, Finance 76, Healthcare 60 | 159 / 115 / 90 / 76 / 60 : OK |
| Quartiles de taille | 125 / 124 / 124 / 125 (2 manquants) | 125 / 124 / 124 / 125 (25,1 / 24,9 / 24,9 / 25,1 % sur 498 valides) : OK |

Note : l'aplatissement de Jamovi est l'excès (0 pour une normale). Le **mode** d'une variable continue peut différer de la référence (arrondi à l'entier dans la référence) ; ne pas s'en inquiéter.

## 2. Séance 2 — khi-deux, corrélations, test t

**Khi-deux** : Analyses → Frequencies → Independent Samples (χ² test of association). Lignes : `sector_group` ; colonnes : `size_quartile`. Statistics : χ², Phi et Cramér's V. Cells : Observed, Expected, Row percentages.

| Résultat | Référence | Jamovi |
|---|---|---|
| χ² (df) ; p ; N | 91,76 (12) ; < .001 ; 498 | 91,8 (12) ; < .001 ; 498 : OK |
| V de Cramér | 0,248 | 0,248 : OK |
| Plus petit effectif attendu | 14,9 | 14,9 (Healthcare Q2 et Q3) : OK |
| Ligne Finance en % (Q1/Q2/Q3/Q4) | 6,6 / 13,2 / 19,7 / 60,5 | 6,6 / 13,2 / 19,7 / 60,5 : OK |

**Corrélations** : Analyses → Regression → Correlation Matrix ; variables : `net_margin_pct`, `roa_pct`, `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct`, `asset_turnover` ; cocher Pearson **et** Spearman, Report significance, Flag significant, Plot : Correlation matrix. Nuage détaillé : Exploration → Scatterplot (`revenue_growth_pct` en X, `net_margin_pct` en Y, ligne de régression linéaire).

| Paire (N) | Pearson r | Spearman ρ | Jamovi |
|---|---|---|---|
| Marge – croissance (488) | 0,266 (p < .001) | 0,295 (p < .001) | 0,266 (< .001) / 0,295 (< .001), df 486 : OK |
| Marge – rotation (498) | −0,217 (< .001) | −0,375 (< .001) | −0,217 (< .001) / −0,375 (< .001) : OK |
| Marge – ln actif (498) | 0,085 (p = .059) | 0,057 (p = .204) | 0,085 (.059) / 0,057 (.204) : OK |
| Marge – endettement (498) | 0,044 (p = .332) | −0,059 (p = .190) | 0,044 (.332) / −0,059 (.190) : OK |
| ROA – ln actif (498) | −0,295 (< .001) | −0,377 (< .001) | −0,295 (< .001) / −0,377 (< .001) : OK |

Attention : Jamovi traite les valeurs manquantes **paire par paire** par défaut ; les N de la ligne ci-dessus doivent apparaître.

**Test t** : Analyses → T-Tests → Independent Samples ; variable dépendante `net_margin_pct`, groupes `finance_vs_other`. Cocher Student, Welch, Mann-Whitney U ; Effect size (Cohen's d) ; Assumption checks : Equality of variances, Normality ; Descriptives.

| Résultat | Référence | Jamovi |
|---|---|---|
| Moyennes Finance / Non-finance (N) | 20,90 (76) / 12,46 (422) | 20,9 (76) / 12,5 (422) : OK |
| Levene | F = 0,12 ; p = .73 (mean) | F = 0,117 ; p = .733 (df 1 et 496) : OK |
| Student | t(496) = 4,70 ; p < .001 | t(496) = 4,70 ; p < .001 : OK |
| Welch | t(127,9) = 5,70 ; p < .001 | t(128) = 5,70 ; p < .001 : OK |
| Mann-Whitney U | 22 745 (U de Finance) ; p < .001. Jamovi affiche l'autre U, **9 327** (22 745 + 9 327 = 76 × 422) ; corrélation bisériale de rangs −0,418 (signe selon le groupe) | 9 327 ; p < .001 ; −0,418 (12 nov., rapproché) |
| Cohen's d ; écart de moyennes | 0,585 ; 8,44 (IC Welch 5,51 à 11,37) | d de Student 0,585 ; 8,44 (IC Welch 5,51 à 11,4) : OK (d de Welch 0,639, voir notes) |

**Notes de rapprochement, séances 1 et 2 (12 nov. 2026, sorties Jamovi relues sur l'écran et dans le `.omv`).**
- Le **mode** affiché par Jamovi (−145 ; 44,5 ; 3,67, avec la mention « plusieurs modes ») est la première valeur la plus fréquente : sans intérêt pour une variable continue, ne pas l'interpréter.
- Les pourcentages de `size_quartile` sont calculés par Jamovi sur les 498 valides (25,1 / 24,9 / 24,9 / 25,1 %) ; la référence les donnait sur 500.
- Khi-deux : le Phi-coefficient affiche NaN (défini seulement pour un tableau 2 × 2) ; les effectifs de Industrials & Energy (158) et Tech & Comms (89) excluent les deux entreprises sans quartile.
- Test t : Jamovi affiche le **U de Non-finance (9 327)** ; le U de Finance est 22 745 (somme 76 × 422 = 32 072). Le d de Cohen de **Welch (0,639)** utilise les écarts-types séparés ; celui de Student (0,585) est le d de référence. Corrélation bisériale de rangs : −0,418 (signe selon l'ordre des groupes). L'écart de localisation de Mann-Whitney est 7,93 (Hodges-Lehmann, recalculé : 7,929). Le **Shapiro-Wilk du test t (W = 0,781)** porte sur les résidus (valeurs centrées par groupe), d'où l'écart avec W = 0,791 de la variable entière.
- Valeurs extrêmes repérées par les box plots (numéro de ligne Jamovi = ligne du CSV) : marge −145 % Moderna (317), −80 % Take-Two (433), −47 % Alexandria (17), +73 % Simon Property (411), +69 % Vici (471) ; endettement 327 % Domino's (156), 262 % Verisign (466) ; croissance +186 % Expand Energy (184), +114 % Nvidia (344). Ce sont des valeurs réelles, conservées (F09).
- Vérification complète faite : les données du `.omv` sont identiques au CSV (3 974 cellules numériques, 0 écart) ; tous les tableaux ont été recalculés indépendamment (Python) : aucun écart.

## 3. Séance 3 — ANOVA et post-hoc

**One-Way ANOVA** : Analyses → ANOVA → One-Way ANOVA ; dépendante `net_margin_pct`, groupes `sector_group`. Variances : cocher **Don't assume equal (Welch)** et **Assume equal (Fisher)**. Additional : Descriptives table et plot ; Assumption checks : Equality of variances, Normality ; Post-Hoc : **un seul choix à la fois** (boutons radio : None, Games-Howell, Tukey). Choisir **Games-Howell** (variances inégales) ; pour voir aussi Tukey, créer une seconde analyse One-Way ANOVA avec Tukey (facultatif : Tukey a été vérifié le 12 nov., identique à la référence). η² : Analyses → ANOVA → ANOVA, Effect size η².
**Non paramétrique** : ANOVA → Non-Parametric → One-Way ANOVA (Kruskal-Wallis) ; cocher DSCF pairwise comparisons.

| Résultat | Référence | Jamovi |
|---|---|---|
| Levene (moyenne) | F(4, 493) = 3,61 ; p = .0065 (version médiane : 3,45 ; p = .0086) | F(4, 493) = 3,61 ; p = .007 (version moyenne) : OK |
| Welch | F(4 ; 189,1) = 10,41 ; p < .001 | F(4 ; 189) = 10,4 ; p < .001 : OK |
| Fisher | F(4, 493) = 7,53 ; p < .001 | F(4, 493) = 7,52 ; p < .001 : OK |
| η² | 0,058 | 0,058 : OK |
| Kruskal-Wallis | χ²(4) = 46,2 ; p < .001 (ε² = 0,093) | χ²(4) = 46,2 ; p < .001 ; ε² = 0,0930 : OK |
| Moyennes | Consumer 11,92 ; Finance 20,90 ; Healthcare 9,51 ; Industrials & Energy 12,07 ; Tech & Comms 15,87 | identiques (N = 115 / 76 / 60 / 158 / 89) : OK |
| Games-Howell (p) | Finance–Consumer < .001 ; Finance–Healthcare = .007 ; Finance–Industrials < .001 ; Finance–Tech = .137 ; autres paires non significatives | Finance–Consumer < .001 ; –Healthcare .007 ; –Industrials < .001 ; –Tech .137 ; autres .248 à 1,000 : OK |
| DSCF (p) | Consumer–Tech = .022 ; Industrials–Tech = .014 ; Finance–{Consumer, Healthcare, Industrials} < .001 | Consumer–Tech .022 ; Industrials–Tech .014 ; Finance–{Consumer, Healthcare, Industrials} < .001 ; Finance–Tech .077 : OK |

Jamovi peut centrer Levene sur la moyenne ou la médiane : comparer avec les deux valeurs. Games-Howell et DSCF doivent donner les mêmes **décisions** (signification), les p exacts peuvent différer légèrement selon l'algorithme du quantile de l'étendue studentisée.

**Notes de rapprochement, séance 3 (12 nov. 2026).** Jamovi n'affiche qu'une version de Levene (centrée sur la moyenne, 3,61) ; la version médiane (3,45) reste « référence ». Les statistiques W du DSCF ont le signe opposé à la référence (ordre des groupes) ; les p sont identiques. Tukey, affiché avant le passage à Games-Howell, concordait avec la référence (Finance–Consumer, –Healthcare, –Industrials < .001 ; autres .063 à 1,000). Le Shapiro-Wilk des résidus (0,781) est celui de l'ANOVA. Analyses enregistrées dans le `.omv` (9 analyses).

## 4. Séance 4 — régressions

**Simple** : Analyses → Regression → Linear Regression ; dépendante `net_margin_pct` ; covariable `ln_assets`. Model Fit : R, R², R² ajusté, F ; Coefficients : estimation, IC 95 %, estimation standardisée.

| Résultat | Référence | Jamovi |
|---|---|---|
| N ; R² ; F(1, 496) ; p | 498 ; 0,0072 ; 3,59 ; .059 | 498 ; 0,00719 (ajusté 0,00519) ; 3,59 ; .059 : OK |
| Constante ; B(ln_assets) ; ES ; t ; p | −9,49 ; 0,958 ; 0,506 ; 1,90 ; .059 | −9,489 ; 0,958 ; 0,506 ; 1,895 ; .059 (β = 0,0848) : OK |

**Multiple** : dépendante `net_margin_pct` ; Covariables : `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct` ; **Factors** : `sector_group` (c'est un facteur, pas une covariable) avec **Reference Level = Industrials & Energy** (Reference Levels). Model Fit : R, R², R² ajusté, F ; Coefficients : estimation, ES, IC, standardisé ; Assumption Checks : Autocorrelation test (Durbin-Watson), Collinearity statistics (VIF), Normality test (Shapiro), Q-Q plot, Residual plots, **Cook's distance**. Jamovi n'offre pas de Breusch-Pagan ni d'erreurs HC3 dans cette procédure : ces résultats restent « référence ». **Attention aux coefficients standardisés (β) des modalités de facteur** (secteurs) : la référence ne standardise pas les variables indicatrices ; si Jamovi les standardise, les β des secteurs différeront alors que les B, ES, t et p doivent être identiques : comparer B et p pour les facteurs, β pour les covariables. Pour les distances de Cook par entreprise : Save → Cook's distance dans le tableur, puis trier la colonne.

| Résultat | Référence | Jamovi |
|---|---|---|
| N ; R² ; R² ajusté | 488 ; 0,114 ; 0,101 | 488 ; 0,114 ; 0,101 : OK |
| F(7, 480) ; p | 8,80 ; < .001 | 8,80 ; < .001 : OK |
| B croissance (ES ; p ; β) | 0,248 (0,043 ; < .001 ; 0,25) | 0,2482 (0,0429 ; < .001 ; 0,2544) : OK |
| B Finance vs Industrials & Energy (p) | 7,84 (< .001) | 7,838 (< .001 ; β 0,531) : OK |
| B Tech & Comms ; Healthcare ; Consumer (p) | 2,40 (.202) ; −2,21 (.300) ; 0,24 (.891) | 2,396 (.202) ; −2,208 (.300) ; 0,241 (.891) : OK |
| B ln actif ; endettement (p) | 0,012 (.982) ; 0,018 (.447) | 0,0119 (.982) ; 0,0177 (.447) : OK |
| VIF maximal ; Durbin-Watson | 1,41 ; 1,96 | VIF 1,08 (ln_assets) ; DW 1,96 (p = .656) : écart expliqué (notes) |
| Shapiro-Wilk des résidus | W = 0,80 ; p < .001 (résidus non normaux) | W = 0,798 ; < .001 : OK |
| Plus grandes distances de Cook | Expand Energy 0,66 ; Moderna 0,59 | maximum 0,659 (OK) ; noms non vérifiés dans Jamovi (colonne Save non créée) |

**Variantes à reproduire** (Data → Filter pour exclure les observations, ou Compute) : sans Expand Energy et Moderna et autres observations influentes (N = 468 : exclure les observations dont la distance de Cook dépasse 4/488) ; sans le secteur financier (N = 418, filtre `sector_group != "Finance"`) ; ROA comme dépendante (N = 488 ; B ln actif = −1,97 ; p < .001). Les valeurs de référence sont dans `outputs/analyses_reference/s4_sens_*`.

**Variantes de robustesse reproduites dans Jamovi (12 nov. 2026).** Un filtre Jamovi (Data → Filters) s'applique à *toutes* les analyses du fichier et les recalcule : il aurait faussé les autres résultats. Les variantes ont donc été faites avec deux **variables calculées** ajoutées au `.omv` (Data → Compute ; les 16 colonnes d'origine sont inchangées, vérifié : 3 974 cellules identiques au CSV) : `margin_noinfl` = `IF(ROW() == 17 or ROW() == 39 or … , NA, net_margin_pct)` pour les 20 observations de distance de Cook > 4/488 (lignes 17, 39, 84, 92, 184, 191, 254, 277, 297, 317, 344, 403, 405, 411, 433, 441, 466, 470, 471, 472) et `sector_nofin` = `IF(sector_group == "Finance", NA, sector_group)`. Les trois régressions sont des duplicatas de la régression multiple (clic droit → Duplicate), niveau de référence Industrials & Energy ; ces deux colonnes n'existent pas dans le CSV (Jamovi a typé `sector_nofin` en « Ordinal » : sans effet, elle sert de facteur).

| Variante | Référence | Jamovi |
|---|---|---|
| ROA comme dépendante (N ; R² ; R² ajusté ; F) | 488 ; 0,190 ; 0,178 ; F(7, 480) = 16,07 | 488 ; 0,190 ; 0,178 ; 16,1 (7, 480) : OK |
| ROA : B ln actif ; endettement ; croissance ; Tech & Comms | −1,967 (< .001) ; 0,050 (< .001) ; 0,145 (< .001) ; 2,998 (.005) | −1,9670 ; 0,0503 ; 0,1449 ; 2,9983 (.005) : OK |
| ROA : Finance – Industrials ; Durbin-Watson ; Shapiro | −0,08 (.946) ; 1,77 ; 0,866 | −0,0816 (.946) ; 1,77 ; 0,866 : OK |
| Sans influentes (N ; R² ; R² ajusté ; F) | 468 ; 0,1417 ; 0,1286 ; F(7, 460) = 10,85 | 468 ; 0,142 ; 0,129 ; 10,8 (7, 460) : OK |
| Sans influentes : Finance ; croissance ; endettement | 6,85 (< .001) ; 0,193 (< .001) ; −0,035 (.040) | 6,8506 ; 0,1934 ; −0,0354 (.039) : OK |
| Sans influentes : Durbin-Watson ; Cook max | 2,10 ; 0,092 (Domino's) | 2,10 ; 0,0924 : OK |
| Sans finance (N ; R² ; R² ajusté ; F) | 418 ; 0,0829 ; 0,0695 ; F(6, 411) = 6,19 | 418 ; 0,0829 ; 0,0695 ; 6,19 (6, 411) : OK |
| Sans finance : croissance ; ln actif ; endettement | 0,250 (< .001) ; −0,160 (.800) ; 0,011 (.645) | 0,2500 ; −0,1601 (.800) ; 0,0114 (.645) : OK |
| Sans finance : Durbin-Watson ; Cook max | 1,86 ; 0,87 | 1,86 ; 0,870 : OK |

Lecture : l'association croissance–marge se maintient dans les trois variantes (0,19 à 0,25 point par point de croissance) ; la prime de la finance en marge reste forte sans les observations influentes (6,85 points) et disparaît avec le ROA (−0,08) ; la taille n'a d'effet significatif que sur le ROA (−1,97 par unité de log de l'actif).

**Contrôles supplémentaires reproductibles dans Jamovi (optionnels, §6.4 du rapport)** : (a) ANOVA de Welch et Kruskal-Wallis de la marge avec le facteur `sector` (11 secteurs) : Welch F = 8,04, Kruskal-Wallis H = 80,7, η² = 0,116 ; (b) régression multiple avec `sector` comme facteur (référence : Industrials) : croissance B = 0,233 (p < .001), secteur Financials +6,15 (p = .013). Le bootstrap, la régression de Huber et la régression médiane ne sont pas dans Jamovi de base : ils restent des résultats « référence ».

**Notes de rapprochement, séance 4 (12 nov. 2026, analyses réglées à l'écran avec David puis relues dans le `.omv`).** Régression simple et régression multiple (N = 488, `sector_group` en facteur, niveau de référence Industrials & Energy) reproduites ; tous les coefficients, erreurs standard, p et β des covariables concordent. **VIF** : Jamovi affiche le VIF généralisé ajusté, GVIF^(1/(2·df)) (ln_assets 1,08 ; endettement 1,03 ; croissance 1,02 ; sector_group 1,03), alors que la référence donne le VIF brut de chaque indicatrice (max 1,41, Finance) ; recalculés : GVIF du secteur 1,274, soit 1,031 après ajustement, et VIF brut de ln_assets 1,177 (racine : 1,085). Les deux lectures concluent à l'absence de colinéarité. Les β des indicatrices (Finance 0,531, etc.) sont ceux de Jamovi (variables indicatrices standardisées) : comparer B et p pour les facteurs. Les graphiques de résidus (résidus contre valeurs ajustées, contre chaque prédicteur, contre la marge) montrent surtout quelques points extrêmes (Moderna) sans structure nette.

## 5. Points de vigilance (erreurs fréquentes d'après le cours)

Type de mesure faux (`sector_group` en Continuous) ; facteur mis dans Covariates ; lire Levene à l'envers ; oublier « toutes choses égales par ailleurs » ; interpréter la constante ; écrire « cause » ; ne pas indiquer N, df et taille d'effet ; sortie copiée sans interprétation. Vérifier à chaque sortie : df = N − k − 1 ; F = MS inter / MS intra ; t = B / ES ; R² ajusté ≤ R² ; V de Cramér = √(χ² / (N (k − 1))).

## 6. Sauvegardes à conserver pour le rapport

Le fichier `.omv` ; les sorties (copie ou export PDF/HTML de chaque analyse) ; les graphiques exportés ; la grille ci-dessus complétée avec l'écart éventuel et son explication. Chaque chiffre du Google Doc devra renvoyer à une sortie identifiable.
