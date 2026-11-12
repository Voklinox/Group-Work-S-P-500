# Fiche de provenance du jeu de données (équivalent de la « approval slip » du cours)

Mise à jour du **12 novembre 2026**. Le choix du jeu de données S&P 500 a été validé par le professeur selon David ; la fiche signée n'est pas disponible et n'est pas redemandée.

| Champ du cours | Valeur |
|---|---|
| Équipe | David Wanono, Olyvan Perrin, Guillaume Da Cruz |
| Titre | Ce qui explique la rentabilité des entreprises du S&P 500 : taille, endettement, croissance et secteur, exercices clos en 2025 |
| Une ligne = un(e)… | **entreprise** (identifiée par son CIK SEC), composition du S&P 500 au 31 décembre 2025 |
| N (lignes) | **500** entreprises (503 titres, trois entreprises ayant deux catégories de titres) |
| Fichier | `data/processed/sp500_2025_JAMOVI_DRAFT.csv` (brouillon tant que D02–D04 ne sont pas finis) |
| Variable nominale (2–5 modalités) | `sector_group` (5), `finance_vs_other` (2), `profitable` (2) |
| Variable ordinale | `size_quartile` (Q1 à Q4, d'après l'actif total) |
| Variables continues (≥ 3) | `net_margin_pct`, `roa_pct`, `ln_assets`, `debt_ratio_pct`, `revenue_growth_pct`, `asset_turnover`, `assets_bn`, `revenue_bn` |
| Question managériale | Qu'est-ce qui explique la rentabilité (marge nette, ROA) des entreprises du S&P 500 : taille, endettement, croissance du chiffre d'affaires, secteur ? Association, pas causalité |

## Sources et producteurs

| Données | Producteur | Source (accès public et gratuit) | Période / date |
|---|---|---|---|
| Comptes (revenus, résultat net, actif) | Les sociétés, via la SEC (formulaires 10-K) | API SEC Company Facts et Submissions : https://www.sec.gov/search-filings/edgar-application-programming-interfaces ; rapports annuels HTML sur sec.gov | Dernier exercice annuel clos en 2025 (ou 52/53 semaines clos début janvier 2026, DEC19) ; collecte du 11 nov. 2026 |
| Composition du S&P 500 | S&P Dow Jones Indices ; rapprochement Wikipédia (révision 1329075976) | Annonce S&P du 5 décembre 2025 et révision archivée | 31 décembre 2025 |
| Table des tickers | SEC | https://www.sec.gov/files/company_tickers.json | téléchargée le 12 nov. 2026 |

## Traçabilité

- Chaque cellule financière renvoie à un fait (CIK, concept XBRL, unité, dates de période, numéro de dépôt, date de dépôt, formulaire) dans `data/reference/financial_evidence.json` ; chaque ratio à sa formule et à ses entrées dans `derived_evidence.csv`.
- Chaque réponse téléchargée est enregistrée avec URL, date UTC, taille et SHA-256 dans `data/reference/download_manifest.jsonl` (1 599 sources vérifiées, 0 erreur d'intégrité).
- La croissance du chiffre d'affaires renvoie au même rapport annuel (année précédente) dans `revenue_growth_evidence.csv`.
- Les copies brutes SEC sont locales et ignorées par Git (taille) ; les URL et empreintes permettent de les retrouver.

## Qualité de la source

Source officielle et réglementée (documents déposés auprès de la SEC) ; collectée en novembre 2026 ; pas de score fournisseur ni de donnée « prétraitée ». Limites : exercices de dates différentes selon les entreprises ; revenus bancaires par convention ; entreprises cotées américaines uniquement ; association et non causalité. La gouvernance, d'abord envisagée, est abandonnée (DEC25). Voir `JOURNAL_NETTOYAGE.md`.
