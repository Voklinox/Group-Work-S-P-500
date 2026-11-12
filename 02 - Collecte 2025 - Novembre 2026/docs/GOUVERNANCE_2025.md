# Gouvernance publique 2025 — protocole approuvé

## Décision de David

Le 11 novembre 2026, David autorise explicitement le remplacement du score ISS par des indicateurs publics, gratuits et légalement accessibles. Il n’a pas d’accès historique payant. Ne pas redemander cet accord. Les observations ci-dessous ne reproduisent pas le score ISS et ne sont pas un classement global de qualité de gouvernance.

Question de travail : **Are publicly disclosed board characteristics in 2025 associated with profitability for fiscal years ending in 2025, accounting for company size and sector?**

## Mesures

| Variable | Définition | Échelle |
|---|---|---|
| board_size | Nombre d’administrateurs effectivement en place dans le périmètre décrit. | Quantitative discrète |
| independent_directors | Nombre de ces mêmes administrateurs déclarés indépendants selon les règles de cotation indiquées. | Quantitative discrète |
| board_independence_reported_pct | 100 × independent_directors / board_size. | Continue, pourcentage |
| board_leadership | Combined CEO and chair / Separate CEO and chair / No board chair. | Nominale, trois catégories |
| publication_date | Date du document décrivant le conseil en place en 2025. | Métadonnée temporelle |

Nvidia justifie la troisième catégorie : la société déclare fonctionner avec un Lead Director, sans chairperson. Un administrateur référent n’est pas automatiquement président. Chez JPMorgan et PepsiCo, l’existence d’un administrateur référent indépendant ne supprime pas le cumul président/CEO. Ces catégories n’ont pas d’ordre de qualité et ne remplacent pas la variable ordinale exigée par le cours.

## Date et périmètre

La cible est une description du conseil en place publiée en **2025**, généralement dans le document d’assemblée annuelle 2025. La date retenue est celle du document, avec conservation d’une date d’effet différente si le texte la précise. Ce n’est ni une moyenne de gouvernance en 2025, ni une observation garantie au 31 décembre. Un proxy 2025 peut contenir des rémunérations, honoraires d’audit et résultats financiers de 2024 : ils ne sont pas repris comme valeurs de 2025.

Les comptes restent ceux de l’exercice annuel clos en 2025. Gouvernance et clôture comptable ont deux dates distinctes. Pour Nvidia, le proxy de mai 2025 est postérieur à la clôture de janvier 2025. Expliquer ce décalage ; ne pas présenter l’étude comme une démonstration d’effet causal de la gouvernance sur les résultats.

Contrôler le conseil **en place**, puis son indépendance. La liste de candidats ne peut servir de dénominateur qu’après rapprochement avec les administrateurs déjà en fonction. Ne pas mélanger nouvel élu futur, sortant et observateur. L’indépendance Nasdaq/NYSE est une déclaration sous un référentiel de cotation, pas une mesure objective universelle de liberté de jugement.

## Sources et sélection

1. Document définitif d’assemblée annuelle 2025 sur SEC ou copie officielle de l’entreprise. Examiner aussi les procurations contestées (DEFC14A) et déclarations d’information (DEF 14C). Ne pas confondre un document d’actionnaire dissident avec celui de l’émetteur.
2. Sans document annuel standard : rapport ou publication de gouvernance datée en 2025, uniquement si la rubrique décrit effectivement le conseil en place à cette date.
3. Pour les nouvelles sociétés : dépôt d’introduction, de scission ou de clôture d’acquisition, avec vérification des nominations effectivement entrées en vigueur. Une composition simplement proposée ne suffit pas.

Si plusieurs documents 2025 existent, lire leur objet (assemblée annuelle, spéciale, acquisition, complément) ; ne pas retenir automatiquement le plus récent. Garder la décision de sélection et les différences de périmètre. Les documents 2026 ne sont pas une source par défaut pour observer 2025.

Les pages actuelles « Board of Directors » non archivées servent à naviguer, pas à produire une mesure historique. Aucun accès privé/payant, aucun contournement d’un refus d’accès. Les copies librement accessibles sur le site officiel ou son hébergeur sont acceptables ; conserver l’origine et la copie utilisée. Inscrire échecs et redirections au registre.

## Avancement

- **496 entreprises** possèdent une procuration ou déclaration d’information candidate, **505 documents** au total. Les anciennes pages du catalogue SEC ont été consultées lorsque le récent ne couvrait pas toute l’année. Ce sont des documents retrouvés, pas 496 mesures vérifiées.
- Quatre autres dossiers : Blackstone, KKR, Paramount Skydance, Qnity Electronics. Des sources officielles alternatives sont identifiées dans alternative_governance_sources.json ; mesures encore à extraire et dater.
- **Cinq entreprises contrôlées** : Apple, Nvidia, Alphabet, JPMorgan Chase, PepsiCo. Voir outputs/governance_pilot_summary.md. Échantillon de méthode, pas échantillon statistique représentatif.
- Originaux archivés pour Apple, Nvidia, JPMorgan ; Alphabet et PepsiCo lus sur SEC mais originaux non archivés. Ne pas prétendre avoir téléchargé les cinq.

## Fichiers et reprise

- data/reference/governance_proxy_candidates.csv : dépôts et liens ; aucune mesure inférée du formulaire.
- data/reference/governance_observations.json : observations contrôlées, effectifs, fonctions, dates, périmètres, rubriques de preuve.
- data/processed/governance_2025_WORKING.json : observations validées et pourcentages recalculés.
- data/quarantine/governance_review_queue.csv : 500 entreprises, états de recherche et de lecture séparés.
- outputs/governance_measurement_coverage.json : couverture réelle des mesures.

```sh
python3 -m src.governance_catalogue
python3 -m src.archive_governance
python3 -m src.governance
python3 -m unittest discover -s tests -v
```

archive_governance réutilise les copies locales et télécharge uniquement les copies officielles explicitement identifiées dans le registre ; il ne cherche pas à contourner les refus.

L’inventaire remet les états de lecture à not_reviewed : relancer ensuite governance pour réappliquer les observations contrôlées. Une correspondance de mots ne suffit pas à créer une valeur. Toute absence reste manquante avec raison. Pour les co-CEO/co-présidents ou structures ambiguës, conserver toutes les personnes et examiner le cas avant de classer.

Ces fichiers sont des preuves internes ; aucun nouveau CSV final Jamovi n’est produit ici. La variable ordinale de taille, les contrôles comptables et les exceptions financières restent à résoudre.
