# Dictionnaire du CSV Jamovi (fichier final du 12 novembre 2026)

Fichier : `data/processed/sp500_2025_JAMOVI.csv`, 500 lignes, une par entreprise (CIK). Niveaux de mesure à régler dans Jamovi : cik et company = ID ; sector, sector_group, finance_vs_other, profitable = Nominal ; size_quartile = Ordinal (Q1 < Q2 < Q3 < Q4) ; les autres = Continuous. Cellule vide = valeur non disponible (jamais zéro).

| Colonne | Sens, unité, N valide |
|---|---|
| cik, company | Identifiant SEC à dix chiffres (texte) et nom de l'entreprise. 500 |
| sector | Secteur GICS (11 modalités). 500 |
| sector_group | Cinq groupes : Tech & Comms, Healthcare, Finance, Industrials & Energy, Consumer (immobilier dans Consumer, DEC22). 500 |
| finance_vs_other | Finance (secteur Financials) contre Non-finance. 500 |
| profitable | Profit si résultat net attribuable > 0, sinon Loss. 498 (470 Profit, 28 Loss) |
| period_end | Date de clôture de l'exercice annuel retenu (jj exacts). 498 |
| net_margin_pct | 100 × résultat net attribuable / revenus, en %. 498 |
| roa_pct | 100 × résultat net attribuable / moyenne de l'actif d'ouverture et de clôture, en %. 498 |
| revenue_bn, assets_bn | Revenus de l'exercice et actif à la clôture, en milliards USD. 498 |
| ln_assets | Logarithme naturel de l'actif en USD (taille continue). 498 |
| debt_ratio_pct | 100 × (actif − capitaux propres) / actif, en % ; peut dépasser 100 (capitaux propres négatifs, 32 sociétés). 498 |
| revenue_growth_pct | Croissance des revenus vs exercice précédent du même rapport, en %. 488 |
| asset_turnover | Revenus / moyenne de l'actif d'ouverture et de clôture (fois). 498 |
| size_quartile | Q1 (actif ≤ 13,4 Md USD), Q2 (≤ 31,1), Q3 (≤ 73,5), Q4 (au-delà). 498 |

Les définitions détaillées, sources et corrections sont dans JOURNAL_NETTOYAGE.md et FICHE_PROVENANCE.md. Le reste de ce document décrit la table de collecte intermédiaire.

---

# Dictionnaire — collecte financière provisoire

Chaque ligne du tableau financier représente une entreprise (identifiant CIK), pas une catégorie d’actions. Le seul futur fichier à ouvrir dans Jamovi sera annoncé après validation. `financials_2025_WORKING.csv` est un tableau de contrôle, pas le fichier analytique final.

| Colonne | Sens, unité et période |
|---|---|
| cik | Identifiant SEC sur dix chiffres, à lire comme texte. Clé entreprise. |
| company | Nom dans l’univers historique. |
| sec_name | Nom renvoyé par la SEC à la collecte ; peut refléter un changement postérieur. |
| sector | Secteur GICS du relevé historique, ou de l’annonce S&P pour les ajouts de décembre. Les 11 secteurs ne satisfont pas seuls la consigne nominale de 2–5 modalités. |
| tickers | Tous les titres de l’entreprise présents dans l’univers, séparés par une barre verticale. Aucun ticker n’est choisi pour valoriser arbitrairement l’ensemble de l’entreprise. |
| universe_date | 31 décembre 2025 : date de la population étudiée. |
| period_start / period_end | Dates réelles du dernier exercice annuel clos en 2025, ou d’un exercice de 52/53 semaines clos du 1er au 7 janvier 2026 (DEC19). Les exercices peuvent couvrir une partie de 2024. |
| accession | Numéro du dépôt annuel retenu, première publication annuelle régulière retrouvée pour cet exercice. |
| filing_date | Date du dépôt, souvent en 2026 pour les comptes clos en décembre 2025. |
| report_url | Lien direct au document annuel résolu par le catalogue SEC. Lien présent ne signifie pas document HTML téléchargé. |
| collection_status | État de l’extraction, jamais un certificat de validation. |
| revenue_usd | Revenus annuels publiés en dollars, selon le concept XBRL indiqué dans le registre. Les banques/assurances doivent faire l’objet d’une vérification particulière de définition. |
| net_income_usd | Résultat net annuel **attribuable à la société mère** (DEC16, 11 nov. 2026). `net_income_basis` indique l’origine (reported_parent, computed_parent_minus_nci, reviewed_report, consolidated_no_nci_tagged) et `net_income_consolidated_usd` conserve le résultat consolidé quand il a été corrigé. Ancienne note : `NetIncomeLoss` est prioritaire ; `ProfitLoss` ou son équivalent IFRS peut couvrir le résultat consolidé avec minoritaires. Le concept exact est conservé ; ces exceptions doivent être harmonisées avant analyse. |
| assets_usd | Total de l’actif à la clôture de l’exercice, dollars. Mesure comptable de taille possible ; ce n’est pas la capitalisation boursière. |
| assets_open_usd | Total de l’actif à la veille du début de l’exercice, dans le même dépôt annuel. |
| equity_usd | Capitaux propres à la clôture. Le concept peut inclure ou exclure les minoritaires ; indiqué dans les preuves. Une valeur négative n’est pas automatiquement une erreur. |
| liabilities_usd | Passif hors capitaux propres, si publié sous le concept normalisé attendu. Pas d’imputation automatique par différence. |
| cash_usd | Trésorerie et équivalents selon le concept publié. Peut être manquant si la société utilise une autre présentation. |
| net_margin_pct | 100 × résultat net / revenus, uniquement si revenus strictement positifs. Une marge de 12 signifie 12 %, pas 0,12. |
| roa_pct | 100 × résultat net / moyenne de l’actif d’ouverture et de clôture, si les deux actifs sont positifs. Comparabilité sectorielle à discuter. |

Les cellules vides signifient « non extrait/à vérifier », jamais zéro. Les montants sont en dollars bruts, sans conversion silencieuse en millions. Tous les flux proviennent de la même période et du même numéro de dépôt. Les ratios sont calculés, pas présentés comme directement publiés.

## Variables du cours (état au 12 novembre 2026)

Réalisé : variable ordinale `size_quartile` (actif total, Q1 à Q4), nominales `sector_group`, `finance_vs_other`, `profitable`, continues listées en tête de ce document. La capitalisation boursière n'est pas utilisée (DEC12 : actif total). Les scores ISS ne sont pas utilisés (DEC05).

## Gouvernance publique — registre pilote (ARCHIVÉ, DEC25 : non utilisé dans l'analyse)

Cinq entreprises renseignées dans governance_observations.json et governance_2025_WORKING.json, pas 500. Choix public approuvé par David.

| Champ | Sens |
|---|---|
| publication_date | Date du document décrivant le conseil, en 2025 ; ni moyenne annuelle ni garantie au 31 décembre. |
| board_scope / date_basis | Périmètre du conseil et repère temporel. |
| board_size / independent_directors | Effectif en place / nombre déclaré indépendant dans ce même effectif. |
| board_independence_reported_pct | 100 × independent_directors / board_size, pourcentage. |
| board_leadership | Fonctions cumulées / personnes distinctes / absence de président : nominale à trois modalités sans ordre de qualité. |
| ceo_name / chair_name | Personnes occupant les fonctions ; chair_name vide signifie absence de président seulement si le texte le confirme et que No board chair est renseigné. |
| lead_director_name | Nom si collecté ; vide = non collecté, pas preuve d’absence. Ce rôle n’est pas automatiquement celui de président. |
| accession / source_url / evidence | Dépôt, lien public et rubriques justificatives. |
| archive_file / capture_status | Copie locale effectivement récupérée, sinon lecture en ligne explicitement signalée. |

Ces mesures ne sont pas un score ISS ni une preuve automatique de bonne gouvernance ou de causalité sur la rentabilité.
