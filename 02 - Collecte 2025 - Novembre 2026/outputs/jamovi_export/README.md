# Export Jamovi (12 novembre 2026)

Source : `data/processed/sp500_2025.omv` (Jamovi 2.7.38.0), enregistré à 15 h 58. Tout ce dossier est reproductible depuis ce fichier.

| Dossier / fichier | Contenu | Comment il a été produit |
|---|---|---|
| `resultats_complets.pdf` | Toutes les sorties Jamovi (31 pages, tableaux vectoriels) | ≡ → Export → PDF |
| `figures_pdf/` | 18 graphiques en PDF vectoriel | Clic droit sur le graphique → Image → Export (PDF) |
| `figures_png/` | Les mêmes 18 graphiques en PNG 300 dpi | `python -m src.convert_jamovi_figures` |
| `tables_png/` | Les 46 tableaux de sortie en PNG (rendu du HTML de Jamovi) | `python -m src.render_jamovi_tables` (Chrome sans fenêtre) |

## Graphiques (figures_png)

| Fichier | Contenu |
|---|---|
| `s1_marge_*`, `s1_endettement_*`, `s1_croissance_*` | Histogramme, box plot et Q-Q plot des trois variables continues (séance 1) |
| `s1_secteurs_barres`, `s1_quartiles_barres` | Diagrammes en barres du secteur et du quartile de taille |
| `s2_khi2_barres` | Barres secteur × quartile (khi-deux) |
| `s2_matrice_correlations` | Matrice de nuages de points (corrélations) |
| `s2_nuage_marge_croissance` | Nuage de points marge × croissance avec droite |
| `s3_anova_moyennes`, `s3_anova_qq` | Moyennes par secteur avec IC 95 % et Q-Q plot des résidus (ANOVA) |
| `s4_regression_qq`, `s4_residus_valeurs_ajustees` | Diagnostics de la régression multiple |

Limites : sur `s1_secteurs_barres` et `s2_khi2_barres`, les libellés de secteurs se chevauchent ; `s2_matrice_correlations` est peu lisible. Jamovi 2.7 ne permet pas de redimensionner ces graphiques : le rapport utilise à la place les tableaux de fréquences et la matrice sous forme de tableau.

## Tableaux (tables_png)

| Numéros | Analyse |
|---|---|
| t01, t02 | Descriptives (marge, endettement, croissance ; secteur, quartile) |
| t03, t04 | Fréquences du secteur et du quartile de taille |
| t05 à t07 | Khi-deux secteur × quartile (effectifs, χ², V de Cramér) |
| t08 | Matrice de corrélations (Pearson et Spearman) |
| t09 à t12 | Test t Finance contre Non-finance (résultats, Shapiro, Levene, descriptives) |
| t13 à t17 | ANOVA à un facteur (Welch, Fisher), descriptives, Shapiro, Levene, Games-Howell |
| t18 à t20 | ANOVA avec η², Kruskal-Wallis, DSCF |
| t21, t22 | Régression simple (ajustement, coefficients) |
| t23 à t28 | Régression multiple (ajustement, coefficients, Cook, Durbin-Watson, VIF, Shapiro) |
| t29 à t34 | Variante ROA comme dépendante |
| t35 à t40 | Variante sans les 20 observations influentes (N = 468) |
| t41 à t46 | Variante sans le secteur financier (N = 418) |
