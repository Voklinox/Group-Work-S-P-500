# To-do du projet S&P 500

Mise à jour : **11 novembre 2026**. Une case cochée signifie que le livrable décrit existe ; elle ne valide pas automatiquement l’étape suivante. Les mentions **EN COURS**, **À DÉCIDER** et **À FAIRE** précisent les cases ouvertes. Aucun pourcentage global n’est estimé.

## Ordre prioritaire confirmé par David

**Étape 1 : projet intégral de référence par l’agent, indépendant de Jamovi. Étape 2 : David reproduit avec guidage dans Jamovi. Étape 3 : finalisation du Google Doc et du PDF.** Les analyses, graphiques et le rapport de référence ne doivent pas attendre Jamovi. Les tâches P01–P09 font partie de l’étape 1.

## À reprendre en premier

1. **G05** — 290 observations (5 pilotes + 285 lues, à auditer), 51 non résolues (data/quarantine/governance_unresolved.csv), **159 sociétés pas encore lues**. Sans sous-agents (DEC21) : `python3 -m src.governance_packets build` puis `show 0 10`, décisions dans un JSON, `src.governance_promote <n°> <fichier>`, `src.governance_check`, `src.merge_governance_shards`, `src.governance`. Environ 1 société sur 3 des paquets se conclut par lecture ciblée ; les autres demandent un second passage (administrateurs partants, candidats nouveaux).
2. **F06 est terminé (11 nov.)** ; passer à F08–F09 (relecture des revenus bancaires, valeurs extrêmes) pendant que la gouvernance est lue en parallèle.
3. **T01–T03** — justifier la mesure de taille et les quartiles avant de construire la base finale.

Le choix de la gouvernance publique est déjà approuvé. Lire docs/REPRISE_AGENT.md avant de relancer un programme. Les 1 000 réponses financières principales sont déjà présentes.

## A — Cadre et organisation

- [x] **A01** Préserver les travaux antérieurs dans les archives et organiser le nouveau dossier dans le dépôt Git commun. Preuve : README parent et dossiers 01/02.
- [x] **A02** Consigner l’équipe, l’échéance indiquée, les consignes du cours et le complément Moodle. Preuve : docs/CONSIGNES_PROFESSEUR.md.
- [x] **A03** Enregistrer les décisions de David : exercices clos en 2025, une entreprise par ligne, sources publiques, Jamovi et commits gérés par lui. Preuve : docs/DECISIONS.md et AGENTS.md.
- [x] **A04** Créer un point d’entrée, un guide de reprise, un journal et cette liste de tâches. Preuve : README.md, docs/REPRISE_AGENT.md, docs/JOURNAL_PROJET.md.
- [x] **A05** Conserver les consignes originales complètes : texte des 175 pages, message Moodle fourni, quatre PDF identiques aux sources et point d’accès à la racine du dépôt. Preuve : docs/CONSIGNES_PROFESSEUR.md et docs/sources/cours/sources_manifest.json.

## U — Population historique

- [x] **U01** Archiver la révision historique de Wikipédia et identifier l’annonce S&P de décembre. Preuve : data/raw/universe_2025_revision_1329075976.json et registre des téléchargements.
- [x] **U02** Documenter les corrections, conserver les 503 titres et regrouper en 500 CIK uniques. Preuve : data/reference/universe_reconciliation.json et universe_2025-12-31.csv.
- [ ] **U03 — EN COURS (12 nov.)** Contrôler indépendamment la population complète, les changements de société et les CIK. Fait : 503 titres rapprochés de la table officielle SEC des tickers (data/reference/universe_ticker_check.csv) : 492 concordances ; les 11 écarts sont expliqués par des événements de 2026 (rachats/radiations, changements de ticker ou de nom, réorganisation d’Exxon) avec dépôts SEC ; les 18 ajouts de 2025 du tableau des changements sont tous présents, SOLS absent comme décidé ; 0 CIK en double. Reste : énumérer et contrôler les retraits de 2025 (le tableau des changements de la révision n’a pas pu être analysé automatiquement de façon fiable) et rapprocher le total officiel de l’indice.

## F — Comptes et qualité financière

- [x] **F01** Vérifier le pilote Apple, Nvidia, Alphabet, JPMorgan et Fiserv, y compris les clôtures décalées. Preuve : sources locales, preuves de faits et tests de sélection.
- [x] **F02** Récupérer les réponses SEC Company Facts et Submissions pour les 500 entreprises. Preuve : data/raw/sec et manifestes ; aucune nouvelle collecte nécessaire pour les relire.
- [x] **F03** Extraire les données avec périodes, unités, concepts et dépôts ; documenter six correspondances particulières. Preuve : financial_evidence.json et reviewed_mappings.json.
- [x] **F04** Produire la couverture et les contrôles d’intégrité. Preuve : outputs/collection_coverage.json et integrity_audit.json ; 494 marges calculables à l’époque (495 depuis F06), pas encore certifiées comparables.
- [x] **F05** Recenser les six exceptions centrales, les champs manquants et les 42 différences de résultat net. Preuve : data/quarantine/core_exceptions.csv, financial_review.csv, definition_review.csv.
- [x] **F06** (11 nov. 2026, DEC17 et DEC19) Résoudre les six exceptions. Preuve : data/reference/core_exception_resolutions.csv ; trois clôtures au 3 janvier 2026 incluses (et L3Harris, Leidos, Trimble corrigées vers leur exercice 2025) ; Synchrony défini ; Paramount et Dayforce manquantes avec motif ; 498 marges. Tests : 20 réussis, audit 0 erreur.
- [x] **F07** (11 nov. 2026, DEC16) Harmoniser le résultat net consolidé et celui attribuable à la société mère pour les 42 alertes. Preuve : data/reference/net_income_harmonisation.csv, src/reviewed.py (parent_income), tests/test_parent_income.py, audit 0 erreur, 9 alertes restantes (aucun minoritaire déclaré). Ancien critère : Terminé quand le numérateur de marge/ROA a une définition cohérente, ou des exceptions et analyses distinctes explicites.
- [x] **F08** (12 nov. 2026) Relire les revenus des banques/assurances et un échantillon de rapports. Preuve : src/report_sample.py → data/reference/report_sample_check.csv : 25 rapports tirés au hasard (graine 2026), 73 cellules (revenus, résultat net, actif) sur 75 retrouvées dans le texte ; les 2 non retrouvées (Clorox) s’expliquent par des états financiers placés en annexe du 10-K, non lus. Dépistage src/screening.py ; 3 revenus corrigés (Camden, Huntington, M&T) ; 10 sociétés financières à revenu/actif élevé : 9 revenus retrouvés dans le rapport, Progressive à confirmer dans l’annexe (rapport annuel incorporé par référence). Limite : un échantillon de 25 ne certifie pas les 475 autres.
- [ ] **F09 — EN COURS (12 nov.)** Examiner valeurs extrêmes, capitaux propres négatifs et données manquantes sans suppression automatique. Fait : 32 capitaux propres négatifs (rachats d’actions, ex. Altria, McDonald’s, Starbucks) conservés et signalés ; extrêmes réels confirmés (Nvidia ROA 82 % exercice janvier 2025, Moderna −145 %, Take-Two, Verisign, AppLovin) ; 23 écarts de bilan >5 % (intérêts minoritaires/mezzanine) signalés. Reste : journal de nettoyage rédigé (docs/NETTOYAGE.md) et N par variable avec la base finale.

## G — Gouvernance publique

- [x] **G01** Enregistrer l’accord de David pour des indicateurs publics, gratuits et datés, en remplacement d’ISS. Preuve : décision DEC05.
- [x] **G02** Fixer le protocole de lecture du conseil en place et les trois catégories de direction. Preuve : docs/GOUVERNANCE_2025.md ; absence de président distincte de séparation des fonctions.
- [x] **G03** Inventorier 505 documents candidats pour 496 sociétés et identifier quatre sources alternatives. Preuve : governance_proxy_candidates.csv, alternative_governance_sources.json et rapport de couverture documentaire.
- [x] **G04** Contrôler le pilote de cinq sociétés et calculer les proportions à partir des effectifs. Preuve : governance_observations.json, governance_2025_WORKING.json et résumé pilote.
- [ ] **G05 — EN COURS : 290/500 observations (285 à auditer), 51 non résolues, 159 à lire** Collecter les observations restantes ou justifier leur absence. Terminé quand chaque ligne de la file a une conclusion documentée ET que l’audit G09 est passé. Ancien critère :
- [ ] **G09 — EN COURS (12 nov.) file d’audit créée, audit non réalisé** Auditer par sondage les observations lues. File reproductible : `python3 -m src.governance_audit_queue` → data/quarantine/governance_audit_queue.csv (107 cas : 84 à risque — administrateurs partants ou effectifs déduits —, 3 atypiques, 20 d’échantillon aléatoire de 10 %). Terminé quand chaque ligne est relue indépendamment avec statut `audited_ok` ou corrigée ; tout écart impose de relire le fragment. Relecture préliminaire du 12 nov. : 6 observations tirées au hasard cohérentes, 0 incohérence nom/fonction sur 283 ; CBRE et d’autres déduisent des effectifs à justifier. Anciennes consignes :
- [ ] **G06 — À FAIRE** Traiter Blackstone, KKR, Paramount et Qnity via leurs sources alternatives ; traiter les co-CEO/co-présidents et les assemblées spéciales/contestées. Terminé quand les nominations effectives, le périmètre et la date sont établis ou le cas laissé manquant avec motif.
- [ ] **G07 — À FAIRE** Compléter les copies sources, notamment Alphabet et PepsiCo, par une voie publique autorisée lorsque possible. Sinon conserver l’état « lecture en ligne, non archivé » et les références précises. Ne pas annoncer une archive inexistante.
- [ ] **G08 — À FAIRE** Vérifier les écarts de dates gouvernance/comptes, la couverture par secteur et les catégories rares. Terminé quand les limites, N et conséquences sur les tests sont consignés dans le plan d’analyse.

## T — Taille et variables du cours

- [x] **T01** (12 nov. 2026, DEC12 confirmée par David) Mesure de taille = actif total à la clôture de l’exercice ; capitalisation en sensibilité optionnelle.
- [x] **T02** (12 nov.) Valeurs d’actif issues du même dépôt annuel que les comptes (preuve : financial_evidence.json) ; 498 valeurs sur 500 ; pas de cours ni d’actions à rapprocher.
- [x] **T03** (12 nov., brouillon) Quartiles de taille Q1 (plus petits) à Q4 (plus grands) sur l’actif : coupures 25/50/75e centiles avec interpolation linéaire à 13,4 / 31,1 / 73,5 Md USD ; classe ≤ coupure ; 498 valides (125/124/124/125). Code : src/build_dataset.py.
- [x] **T04** (12 nov., brouillon) Spécification du cours vérifiée sur data/processed/sp500_2025_JAMOVI_DRAFT.csv : ≥100 lignes (500) ; nominales 2–5 modalités : ceo_duality (2), board_leadership (3), sector_group (5) ; ordinale : size_quartile (4) ; continues : net_margin_pct, roa_pct, board_independence_pct, assets_bn, ln_assets, revenue_bn. Limite : « No board chair » = 1 société (Nvidia), d’où ceo_duality (DEC23) pour le khi-deux et le test t.

## D — Base finale et plan d’analyse

- [x] **D01** (12 nov., brouillon) Finances et gouvernance jointes par CIK, 500 lignes conservées, statut de gouvernance par ligne (observed 288 / unresolved 51 / not_yet_read 161), aucune valeur remplie artificiellement. À refaire après G05 et G09.
- [ ] **D02 — EN COURS (12 nov.)** Figer les définitions, règles de nettoyage et échantillons valides par analyse. Fait : docs/JOURNAL_NETTOYAGE.md (journal noté du cours) et docs/FICHE_PROVENANCE.md (fiche de provenance), définitions des variables créées. Reste : dictionnaire final des colonnes du CSV Jamovi (docs/DICTIONNAIRE.md à aligner sur sp500_2025_JAMOVI_DRAFT.csv) et tableau des N par analyse (après G05/G09).
- [ ] **D03 — À FAIRE** Établir un plan d’analyse répondant à la question et aux quatre séances ; préciser hypothèses, conditions, tailles d’effet et contrôles. Prévoir une comparaison à deux groupes pertinente pour couvrir la mention du t-test dans la synthèse du cours, sans inventer un nouvel artefact séparé.
- [ ] **D04 — À FAIRE** Produire **un seul CSV final Jamovi clairement identifié**, puis vérifier valeurs manquantes, types, modalités, unités et traçabilité. Dépend de U03, F06–F09, G05–G08, T01–T04 et D01–D03. Les valeurs manquantes justifiées peuvent subsister ; elles doivent être visibles.

## P — Projet d’analyse complet de référence, sans dépendre de Jamovi

**Priorité actuelle de l’agent.** Cette section s’exécute après les données et le plan d’analyse D01–D04. Les fichiers d’analyse et de rapport mentionnés ci-dessous sont des livrables **à créer**, pas des résultats déjà présents. Tous les calculs concernent les nouvelles données 2025.

- [ ] **P01 — À FAIRE** Calculer les cinq profils univariés avec tableaux, graphiques, N, statistiques adaptées et diagnostic de normalité documenté ; rédiger l’interprétation et les deux phrases managériales. Terminé quand chaque résultat est reproductible et relié à la base retenue.
- [ ] **P02 — À FAIRE** Calculer le khi-deux avec pourcentages en ligne, attendus, conditions et V de Cramer ; matrice Pearson **et** Spearman d’au moins trois continues et nuage du couple discuté ; rédiger les deux recommandations chiffrées.
- [ ] **P03 — À FAIRE** Réaliser une comparaison justifiée de deux groupes, avec Student/Welch ou alternative adaptée, descriptifs, conditions, statistique/df/p, taille d’effet et interprétation. Le choix des groupes doit répondre à la question, pas rechercher une p-value favorable.
- [ ] **P04 — À FAIRE** Réaliser les comparaisons de 3–5 groupes : descriptifs/boîtes, Levene, Fisher/Welch ou Kruskal–Wallis selon conditions, post-hoc appropriés et tailles d’effet ; rédiger la conclusion dans le protocole du cours.
- [ ] **P05 — À FAIRE** Calculer et interpréter une régression simple de référence, avec équation, unités, F/p, R² et coefficients/IC ; conserver les diagnostics utiles.
- [ ] **P06 — À FAIRE** Calculer les modèles multiples justifiés, facteurs/références, échantillons et transformations ; vérifier résidus, colinéarité et observations influentes ; interpréter coefficients et limites, sans causalité indue.
- [ ] **P07 — À FAIRE** Vérifier indépendamment les calculs essentiels et les sensibilités justifiées ; fixer la version de données et les options utilisées. Prévoir un index de tableaux/graphiques, les N par analyse, les méthodes/versions et l’empreinte de l’entrée. Toute modification de base impose de mettre à jour les résultats concernés.
- [ ] **P08 — À FAIRE** Rédiger un **rapport local de référence complet** : résumé exécutif, trois recommandations, données/nettoyage, descriptifs, relations, groupes, régressions, limites et sources, avec tableaux/graphiques utilisables. Livrable prévu : docs/RAPPORT_DE_REFERENCE.md ; ce n’est pas encore le Google Doc final.
- [ ] **P09 — À FAIRE** Préparer le guide Jamovi et la grille de rapprochement des résultats : types de variables, menus/options, références de facteurs, échantillons, résultats attendus et écarts tolérables d’arrondi. Terminé quand l’agent peut expliquer et reproduire l’ensemble du projet indépendamment de Jamovi et guider David sur chaque analyse.

**Fin de l’étape 1 :** données justifiées, calculs contrôlés, rapport de référence complet, tableaux/graphiques identifiés et guide de reproduction prêts. Un script présent, un tableau non interprété ou un CSV seul ne remplit pas ce critère. Les sorties externes portent l’étiquette « référence », pas « Jamovi ».

## J — Réalisation guidée dans Jamovi

Ces tâches constituent **l’étape 2**, après P01–P09. Elles reproduisent **les nouvelles données** et les analyses de référence. Les anciennes analyses ne suffisent pas à les cocher. David effectue les manipulations ; l’agent guide et aide à interpréter.

- [ ] **J01 — À FAIRE après P09** Importer le CSV avec David, régler les niveaux de mesure et sauvegarder son fichier de travail Jamovi.
- [ ] **J02 — À FAIRE** Réaliser cinq profils univariés adaptés aux échelles, graphiques et diagnostics de normalité ; documenter nettoyage et N.
- [ ] **J03 — À FAIRE** Réaliser tableau croisé, pourcentages en ligne, khi-deux avec conditions et V de Cramer ; matrice Pearson et Spearman sur au moins trois continues et nuage de points discuté ; rapprocher les résultats de P02.
- [ ] **J04 — À FAIRE** Comparer les groupes avec méthode adaptée, diagnostics, post-hoc, taille d’effet et vérification non paramétrique selon le cours.
- [ ] **J05 — À FAIRE** Réaliser les régressions prévues, diagnostics et contrôles de robustesse utiles ; distinguer associations et causalité.
- [ ] **J06 — À FAIRE** Conserver les sorties Jamovi et vérifier leur cohérence avec les définitions et les N. Terminé quand chaque résultat du rapport possède une sortie identifiable et est rapproché des résultats de référence ; expliquer toute différence avant de la résoudre.

## R — Google Doc et PDF

**Étape 3**, après rapprochement des résultats dans J06. Partir du rapport local complet de P08, puis finaliser la version destinée au professeur.

- [ ] **R01 — À FAIRE** Relire le Google Doc fourni avant édition et mettre à jour problématique/méthode autour des nouvelles données ; retirer ou remplacer les anciens résultats par des résultats vérifiés, sans effacer aveuglément les modifications du groupe.
- [ ] **R02 — À FAIRE** Adapter et finaliser le texte de référence : données/nettoyage, descriptifs, relations, groupes, régression et limites selon IDENTIFY → HYPOTHESISE → DECIDE → RECOMMEND.
- [ ] **R03 — À FAIRE** Finaliser le résumé exécutif sur une page et les trois recommandations de référence, après les dernières vérifications des analyses et de la mise en page.
- [ ] **R04 — À FAIRE avec le groupe** Obtenir les évaluations des membres et les placer près des noms sur la couverture. Ne pas inventer les notes ni leur barème.
- [ ] **R05 — À FAIRE** Vérifier sources, légendes, unités, N, pagination et conformité aux consignes ; exporter et relire le PDF complet. Ne pas supposer une obligation d’oral ou un nombre total de pages non fourni.
- [ ] **R06 — À FAIRE par David/le groupe** Effectuer le dépôt final selon Moodle et les commits/sauvegardes souhaités. L’agent n’effectue pas ces actions de sa propre initiative.

## Entretien du suivi

À chaque lot, cocher uniquement le livrable réalisé, indiquer le compteur réel, actualiser l’état et les décisions si nécessaire, puis ajouter une entrée au journal. Si un contrôle invalide un travail, rouvrir sa tâche et expliquer pourquoi. Le journal est historique ; cette to-do est la référence des actions à mener.
