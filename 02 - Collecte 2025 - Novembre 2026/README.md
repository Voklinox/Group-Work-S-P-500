# S&P 500 — projet de groupe, collecte 2025

**Équipe : David Wanono, Olyvan Perrin, Guillaume Da Cruz.** Cours Quantitative Data Analysis, M1 S7, EM Normandie. Échéance indiquée par David : **2 décembre 2026**. Dernière mise à jour documentaire : **12 novembre 2026**.

Étudier ce qui explique la rentabilité (marge nette, ROA) des entreprises du S&P 500 : taille, endettement, croissance du chiffre d’affaires et secteur (DEC25 : la gouvernance a été abandonnée le 12 novembre 2026, travail archivé). Comptes du dernier exercice annuel **clos en 2025**, avec dates exactes ; une ligne par entreprise.

**Étape 1 terminée (12 novembre 2026) : CSV final, analyses de référence, rapport et guide Jamovi sont prêts. Prochaine étape : reproduction dans Jamovi par David.**

## Priorité fixée par David

**1. Projet complet de référence préparé par l’agent sans dépendre de Jamovi → 2. Reproduction guidée par David dans Jamovi → 3. Finalisation du Google Doc et du PDF.**

L’étape 1 comprend données, analyses des quatre séances, diagnostics, tableaux, graphiques, interprétations, recommandations et rapport local complet. Un CSV prêt ne suffit pas à la terminer. Les calculs de référence seront ensuite comparés aux sorties Jamovi ; ils ne sont pas présentés comme des sorties déjà réalisées dans l’application.

Les [consignes et supports du professeur en texte intégral](docs/CONSIGNES_PROFESSEUR.md) et les [quatre supports copiés](docs/sources/cours/) sont dans ce dossier ; un point d’entrée CONSIGNES_PROFESSEUR.md existe aussi à la racine du dépôt Git.

## Trois entrées pour suivre le projet

- [Liste des tâches](tasks/todo.md) : fait, en cours, à décider, ordre de priorité et preuve attendue pour terminer chaque étape.
- [Journal du projet](docs/JOURNAL_PROJET.md) : comment nous sommes arrivés à l’état actuel, corrections et limites rencontrées.
- [Reprise par un autre agent](docs/REPRISE_AGENT.md) : lecture minimale, fichiers à utiliser, commandes, effets des commandes et prochaine action concrète.

## État vérifié dans les fichiers locaux

| Étape | État au 11 novembre 2026 |
|---|---|
| Univers de travail au 31 décembre 2025 | 500 entreprises / CIK, 503 titres ; rapprochement historique documenté, vérification indépendante complète encore à faire |
| Sources SEC financières | Company Facts et Submissions présents pour les 500 entreprises |
| Exercices annuels extraits de durée comparable | 498 (dont 6 exercices de 52/53 semaines clos début janvier 2026, DEC19) |
| Marges nettes calculables | 498 ; numérateur harmonisé sur le résultat attribuable à la société mère (DEC16) ; manquent Dayforce (pas de rapport annuel 2025) et Paramount (prédécesseur/successeur) ; comparabilité à contrôler |
| Gouvernance (abandonnée, DEC25) | Travail archivé : 505 documents téléchargés, 290 observations lues, protocole et outils conservés ; non utilisés dans l’analyse |
| Variables de l’analyse | continues : net_margin_pct, roa_pct, ln_assets, debt_ratio_pct, revenue_growth_pct (488), asset_turnover ; ordinale size_quartile ; nominales sector_group (5), finance_vs_other (2), profitable (2). CSV final : data/processed/sp500_2025_JAMOVI.csv (500 lignes) |
| Taille et quartiles | Actif total, quartiles Q1–Q4 sur 498 entreprises (DEC12 confirmée) |
| Analyses complètes et rapport local de référence | Réalisés le 12 nov. 2026 : docs/RAPPORT_DE_REFERENCE.md, outputs/analyses_reference/, outputs/figures_reference/ ; vérification indépendante des 12 calculs essentiels ; guide Jamovi docs/GUIDE_JAMOVI.md |
| Reproduction Jamovi puis Google Doc/PDF | Prochaine étape : Jamovi avec David (étape 2), puis finalisation (étape 3) |

Ces compteurs ne constituent pas un pourcentage d’achèvement du projet. « Document retrouvé », « valeur extraite » et « donnée validée pour l’analyse » sont trois états différents.

## Documentation de référence

| Besoin | Fichier |
|---|---|
| État actuel et exceptions | [ETAT_DU_PROJET.md](docs/ETAT_DU_PROJET.md) |
| Décisions, auteur du choix et justification | [DECISIONS.md](docs/DECISIONS.md) |
| Périodes, univers et conventions financières | [METHODOLOGIE.md](docs/METHODOLOGIE.md) |
| Règles de gouvernance publique | [GOUVERNANCE_2025.md](docs/GOUVERNANCE_2025.md) |
| Définition des colonnes et unités | [DICTIONNAIRE.md](docs/DICTIONNAIRE.md) |
| Provenance et reproduction | [SOURCES_ET_REPRISE.md](docs/SOURCES_ET_REPRISE.md) |
| Attentes du professeur et complément Moodle | [CONSIGNES_PROFESSEUR.md](docs/CONSIGNES_PROFESSEUR.md) |
| Exemple concret de gouvernance sourcée | [Résumé du pilote](outputs/governance_pilot_summary.md) |

## Organisation et règles de travail

`data/raw/` conserve les réponses et rapports effectivement téléchargés. `data/reference/` contient univers, décisions de correspondance et preuves. `data/processed/` contient les résultats provisoires construits. `data/quarantine/` contient les cas à vérifier ; les observations concernées restent dans la population. `outputs/` contient les compteurs et contrôles. `src/` et `tests/` permettent de reconstruire et contrôler le travail. Le rôle exact des fichiers et leur ordre d’exécution sont dans le guide de reprise.

Le dépôt Git unique est dans le dossier parent, à côté de `01 - Archives - Septembre 2026`. **David fait les commits et manipule lui-même Jamovi.** Les grands fichiers bruts sont locaux et ignorés par Git : un clonage seul ne les restitue pas. Conserver une sauvegarde séparée ; les URL et empreintes permettent de contrôler les copies. Les anciens résultats et CSV V2 appartiennent aux archives.

Pour une première reprise : lire les documents, examiner les preuves et la to-do ; aucune collecte ni reconstruction n’est nécessaire simplement pour prendre connaissance du projet. Voir [AGENTS.md](AGENTS.md) pour les instructions de l’agent.
