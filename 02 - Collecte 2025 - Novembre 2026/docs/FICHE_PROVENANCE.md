# Fiche de provenance du jeu de données (équivalent de la « approval slip » du cours)

Mise à jour du **12 novembre 2026**. Le choix du jeu de données S&P 500 a été validé par le professeur selon David ; la fiche signée n'est pas disponible et n'est pas redemandée.

| Champ du cours | Valeur |
|---|---|
| Équipe | David Wanono, Olyvan Perrin, Guillaume Da Cruz |
| Titre | Caractéristiques publiques du conseil d'administration et rentabilité des entreprises du S&P 500, exercices clos en 2025 |
| Une ligne = un(e)… | **entreprise** (identifiée par son CIK SEC), composition du S&P 500 au 31 décembre 2025 |
| N (lignes) | **500** entreprises (503 titres, trois entreprises ayant deux catégories de titres) |
| Fichier | `data/processed/sp500_2025_JAMOVI_DRAFT.csv` (brouillon tant que G05, G09 et D02–D04 ne sont pas finis) |
| Variable nominale (2–5 modalités) | `ceo_duality` (2), `board_leadership` (3), `sector_group` (5) |
| Variable ordinale | `size_quartile` (Q1 à Q4, d'après l'actif total) |
| Variables continues (≥ 3) | `net_margin_pct`, `roa_pct`, `board_independence_pct`, `assets_bn`, `ln_assets`, `revenue_bn` ; discrète : `board_size` |
| Question managériale | Les caractéristiques publiques du conseil (indépendance, séparation président/CEO) sont-elles associées à la rentabilité, compte tenu de la taille et du secteur ? Association, pas causalité |

## Sources et producteurs

| Données | Producteur | Source (accès public et gratuit) | Période / date |
|---|---|---|---|
| Comptes (revenus, résultat net, actif) | Les sociétés, via la SEC (formulaires 10-K) | API SEC Company Facts et Submissions : https://www.sec.gov/search-filings/edgar-application-programming-interfaces ; rapports annuels HTML sur sec.gov | Dernier exercice annuel clos en 2025 (ou 52/53 semaines clos début janvier 2026, DEC19) ; collecte du 11 nov. 2026 |
| Composition du conseil, indépendance, direction | Les sociétés, via la SEC (procurations DEF 14A, quelques documents alternatifs) | sec.gov/Archives, URL dans `governance_proxy_candidates.csv` et chaque observation | Publiés en 2025 ; date de publication conservée |
| Composition du S&P 500 | S&P Dow Jones Indices ; rapprochement Wikipédia (révision 1329075976) | Annonce S&P du 5 décembre 2025 et révision archivée | 31 décembre 2025 |
| Table des tickers | SEC | https://www.sec.gov/files/company_tickers.json | téléchargée le 12 nov. 2026 |

## Traçabilité

- Chaque cellule financière renvoie à un fait (CIK, concept XBRL, unité, dates de période, numéro de dépôt, date de dépôt, formulaire) dans `data/reference/financial_evidence.json` ; chaque ratio à sa formule et à ses entrées dans `derived_evidence.csv`.
- Chaque réponse téléchargée est enregistrée avec URL, date UTC, taille et SHA-256 dans `data/reference/download_manifest.jsonl` (1 599 sources vérifiées, 0 erreur d'intégrité).
- Chaque observation de gouvernance contient des citations copiées mot pour mot (contrôlées automatiquement), le dépôt, la date et le périmètre.
- Les copies brutes SEC sont locales et ignorées par Git (taille) ; les URL et empreintes permettent de les retrouver.

## Qualité de la source

Source officielle et réglementée (documents déposés auprès de la SEC) ; collectée en novembre 2026 ; pas de score fournisseur ni de donnée « prétraitée ». Limites : indépendance déclarée selon les règles de cotation ; date de gouvernance différente de la clôture comptable ; entreprises cotées américaines uniquement ; lecture de gouvernance encore incomplète et à auditer. Voir `JOURNAL_NETTOYAGE.md`.
