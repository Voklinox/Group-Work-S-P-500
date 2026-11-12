# Journal de nettoyage (livrable noté du cours : « what was wrong, what you did, why »)

Mis à jour le **12 novembre 2026**. Il porte sur `data/processed/sp500_2025_JAMOVI_DRAFT.csv` (500 lignes, une par entreprise). Ce journal sépare : anomalies réellement constatées, contrôles sans anomalie, corrections appliquées, valeurs conservées volontairement et limites. Les causes ne sont écrites que lorsqu'une pièce les établit. Chaque ligne cite sa preuve.

## 1. Population

| Constat | Action | Pourquoi | Preuve |
|---|---|---|---|
| La révision Wikipédia du 23 déc. 2025 comptait 501 titres / 498 CIK ; elle ne contenait pas les entrées de CRH, Carvana, Comfort Systems et contenait encore Solstice (SOLS) | Ajout de CRH, CVNA, FIX ; retrait de SOLS | Annonce officielle S&P du 5 déc. 2025, effective le 22 déc. | universe_reconciliation.json |
| Alphabet, Fox, News Corp ont deux catégories de titres | Une ligne par CIK, tous les tickers conservés | Éviter de compter deux fois les comptes d'une entreprise (DEC03) | universe_2025-12-31.csv |
| 0 CIK en double ; 503 titres rapprochés de la table officielle SEC | Contrôle seul | Contrôle d'intégrité de la clé | universe_ticker_check.csv |
| 11 titres ne concordent plus avec le fichier SEC d'aujourd'hui (rachats radiés, changements de ticker ou de nom, réorganisation d'Exxon) | Aucune ligne retirée : la population est celle du 31 déc. 2025 | Les événements sont de 2026 | explications une à une dans universe_ticker_check.csv |

## 2. Période comptable

| Constat | Action | Pourquoi | Preuve |
|---|---|---|---|
| 134 entreprises ont un exercice qui ne se termine pas le 31 décembre ; 114 le terminent avant décembre 2025 (ex. Nvidia : exercice clos en janvier 2025, couvrant surtout 2024) | Retenir le dernier exercice annuel **clos en 2025**, dates exactes conservées (period_start, period_end) | Choix de David (DEC02) | financials_2025_WORKING.csv |
| Snap-on, Stanley Black & Decker, Textron : exercice 52/53 semaines clos le 3 janv. 2026 ; L3Harris, Leidos, Trimble : clos le 2 janv. 2026 | Exercice clos du 1er au 7 janv. 2026 et couvrant au moins 360 jours de 2025 retenu comme exercice 2025 | Décision de David (DEC19). Pour L3Harris, Leidos et Trimble l'exercice clos début janv. 2025 couvrait 2024 (ex. Trimble : marge 40,8 % due à un gain de 2024, 11,8 % en 2025) | core_exception_resolutions.csv, src/financials.py |
| Seul le premier dépôt annuel régulier est retenu, pas un comparatif ultérieur | Règle de sélection (330 à 385 jours) | Éviter de mélanger deux versions | tests/test_financials.py |

## 3. Valeurs manquantes et exclusions

| Variable | Manquantes (sur 500) | Raison |
|---|---:|---|
| Marge nette, ROA, revenus, résultat net, actif | 2 | **Dayforce** : aucun rapport annuel 2025 (rachat clos le 4 fév. 2026, Form 15 le 17 fév.) ; **Paramount Skydance** : périodes prédécesseur/successeur non comparables. Valeurs laissées vides, jamais imputées |
| Passif, trésorerie | 143 ; 83 | Concept normalisé non publié par ces sociétés (présentation différente). Variables secondaires : non utilisées dans les analyses principales ; pas d'imputation par différence |

Aucun zéro de remplacement n'a été utilisé. Chaque analyse annoncera son N valide.

## 4. Définitions harmonisées

| Constat | Action | Preuve |
|---|---|---|
| 42 sociétés ne publiaient que le résultat consolidé (`ProfitLoss`), les autres le résultat attribuable | Numérateur harmonisé : résultat attribuable à la société mère (DEC16). 30 calculés (consolidé − minoritaires), 3 lus dans le rapport (Entergy, LyondellBasell, Mastercard), 9 sans minoritaires déclarés (7 vérifiés dans le rapport) | net_income_harmonisation.csv |
| Sociétés financières sans concept « revenus » standard | Revenu = intérêts nets + revenus hors intérêts (convention banques) ; Synchrony : intérêts nets − reversements aux partenaires + autres revenus (DEC17) | reviewed_mappings.json |
| Revenu mal sélectionné : Camden 12,9 M$ pour un bénéfice de 384 M$ ; Huntington 1,6 Md$ et M&T 1,7 Md$ pour un bénéfice supérieur | Remplacement par les valeurs du compte de résultat : Camden 1 573,5 M$ ; Huntington 8 166 M$ ; M&T 9 690 M$ | reviewed_mappings.json (drapeau override) ; dépistage src/screening.py |
| Revenus absents des concepts normalisés : APA, L3Harris | Valeur transcrite du compte de résultat | reviewed_mappings.json |

Cause établie pour les revenus de Camden, Huntington et M&T : le concept standard sélectionné ne couvrait qu'une composante (preuve : montants du rapport). Les autres revenus n'ont pas été relus un à un : relecture d'un échantillon d'au moins 25 rapports encore à faire (F08).

## 5. Valeurs extrêmes et cas particuliers conservés

Aucune suppression automatique. Le dépistage (`financial_screening.csv`) signale :

- **32 capitaux propres négatifs** (rachats d'actions et pertes : ex. AbbVie, McDonald's, Starbucks, Altria) : conservés ; la marge nette et le ROA restent calculables ; aucun ratio sur capitaux propres n'est utilisé.
- **Marges ou ROA extrêmes réels** : Nvidia (ROA 82 % sur l'exercice de janv. 2025), Moderna (marge −145 %), Take-Two (ROA −42 %), Verisign (ROA 60 %, capitaux propres négatifs), AppLovin, Simon Property (marge 73 %), CME. Conservés : ce sont des valeurs authentiques ; leur influence sera examinée dans les régressions (distance de Cook) et les médianes seront rapportées.
- **23 écarts de bilan > 5 %** (actif ≠ capitaux propres + passif, à cause des minoritaires et éléments hors capitaux propres) : signalés, sans effet sur les variables retenues.
- **10 sociétés financières à revenu/actif élevé** (assureurs, bourses, Block, Mastercard…) : revenus a priori légitimes, à confirmer (F08).

## 6. Gouvernance (abandonnée)

La gouvernance a été étudiée puis abandonnée le 12 novembre 2026 (DEC25) : 290 observations lues et 159 sociétés non lues, jugées trop coûteuses à compléter ; aucune variable de gouvernance n'est dans le fichier d'analyse. Le travail reste archivé (docs/GOUVERNANCE_2025.md, PROTOCOLE_LECTURE_GOUVERNANCE.md).

## 7. Variables créées

`assets_bn` (actif en milliards USD) ; `ln_assets` (logarithme naturel de l'actif en USD) ; `size_quartile` (Q1 plus petits à Q4 plus grands, coupures 25/50/75e centiles de l'actif à 13,4 / 31,1 / 73,5 Md USD) ; `sector_group` (5 groupes, DEC22) ; `finance_vs_other` (Finance contre Non-finance) ; `profitable` (Profit si résultat net > 0, sinon Loss ; 470 / 28) ; `debt_ratio_pct` = 100 × (actif − capitaux propres) / actif (peut dépasser 100 si capitaux propres négatifs : 32 sociétés, conservées) ; `revenue_growth_pct` = croissance du chiffre d'affaires par rapport à l'exercice précédent publié dans le même rapport (488 valeurs ; manquante lorsque le revenu est une reconstruction ou que l'exercice précédent n'est pas comparable) ; `asset_turnover` = revenus / moyenne de l'actif d'ouverture et de clôture. Pourcentages exprimés en points (12 = 12 %), montants en milliards USD.

## 8. Limites

Croissance du chiffre d'affaires : 488 valeurs sur 500 ; une croissance extrême (jusqu'à +186 %) reflète souvent des acquisitions, conservée. Comptes : périodes différentes entre sociétés (mais toutes dates exactes) ; revenus bancaires par convention ; comparabilité sectorielle des marges non certifiée.
