# To-do du projet S&P 500

Mise à jour : **12 novembre 2026**. Une case cochée signifie que le livrable décrit existe ; elle ne valide pas automatiquement l’étape suivante. Les mentions **EN COURS**, **À DÉCIDER** et **À FAIRE** précisent les cases ouvertes. Aucun pourcentage global n’est estimé.

## Ordre prioritaire confirmé par David

**Étape 1 : projet intégral de référence par l’agent, indépendant de Jamovi. Étape 2 : David reproduit avec guidage dans Jamovi. Étape 3 : finalisation du Google Doc et du PDF.** Les analyses, graphiques et le rapport de référence ne doivent pas attendre Jamovi. Les tâches P01–P09 font partie de l’étape 1.

## À reprendre en premier

**Étape 1 (projet de référence) : presque terminée.** Analyses, rapport local (docs/RAPPORT_DE_REFERENCE.md) et guide Jamovi (docs/GUIDE_JAMOVI.md) existent. Reste avant l’étape 2 : **U03** (retraits de 2025), **F09** (clôture du journal de nettoyage) puis **D04** (CSV final unique, renommé sans « DRAFT », et nouvelle exécution de src.analysis + src.verify_analysis pour figer les chiffres). Ensuite **étape 2 : J01–J06 avec David dans Jamovi**.

La gouvernance est abandonnée (DEC25) : ne pas la reprendre sans décision de David. Lire docs/REPRISE_AGENT.md avant de relancer un programme.

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
- [x] **G05 — ABANDONNÉE le 12 nov. 2026 (DEC25)** Collecte de gouvernance : 290 observations lues, 159 non lues, 51 non résolues ; travail archivé, non utilisé.
- [x] **G09 — ABANDONNÉE (DEC25)** Audit par sondage : sans objet puisque la gouvernance n’est plus une variable ; file d’audit conservée (data/quarantine/governance_audit_queue.csv).
- [x] **G06 — ABANDONNÉE (DEC25)**
- [x] **G07 — ABANDONNÉE (DEC25)**
- [x] **G08 — ABANDONNÉE (DEC25)**

## T — Taille et variables du cours

- [x] **T01** (12 nov. 2026, DEC12 confirmée par David) Mesure de taille = actif total à la clôture de l’exercice ; capitalisation en sensibilité optionnelle.
- [x] **T02** (12 nov.) Valeurs d’actif issues du même dépôt annuel que les comptes (preuve : financial_evidence.json) ; 498 valeurs sur 500 ; pas de cours ni d’actions à rapprocher.
- [x] **T03** (12 nov., brouillon) Quartiles de taille Q1 (plus petits) à Q4 (plus grands) sur l’actif : coupures 25/50/75e centiles avec interpolation linéaire à 13,4 / 31,1 / 73,5 Md USD ; classe ≤ coupure ; 498 valides (125/124/124/125). Code : src/build_dataset.py.
- [x] **T04** (12 nov., mis à jour DEC25) Spécification du cours vérifiée sur data/processed/sp500_2025_JAMOVI_DRAFT.csv : 500 lignes ; nominales : sector_group (5), finance_vs_other (2), profitable (2) ; ordinale : size_quartile (4) ; continues : net_margin_pct, roa_pct, ln_assets, debt_ratio_pct, revenue_growth_pct (488), asset_turnover. Khi-deux secteur × quartile : effectif attendu minimal 14,9 ≥ 5.

## D — Base finale et plan d’analyse

- [x] **D01** (12 nov., mis à jour DEC25) Base brouillon sans gouvernance : 500 lignes, une par CIK, variables ci-dessus, aucune valeur remplie artificiellement. Code : src/build_dataset.py, src/extra_variables.py (preuves : data/reference/revenue_growth_evidence.csv).
- [x] **D02** (13 nov. 2026) Définitions et règles figées : JOURNAL_NETTOYAGE.md, FICHE_PROVENANCE.md, dictionnaire du CSV Jamovi (DICTIONNAIRE.md), N par analyse dans le rapport. À actualiser si D04 modifie la base.
- [x] **D03** (13 nov. 2026) Plan d’analyse appliqué et documenté dans docs/RAPPORT_DE_REFERENCE.md (hypothèses, conditions, tailles d’effet, sensibilités).
- [ ] **D04 — À FAIRE** Produire **un seul CSV final Jamovi clairement identifié**, puis vérifier valeurs manquantes, types, modalités, unités et traçabilité. Dépend de U03, F09 et D02–D03 (G05–G09 abandonnées, DEC25). Les valeurs manquantes justifiées peuvent subsister ; elles doivent être visibles.

## P — Projet d’analyse complet de référence, sans dépendre de Jamovi

**Priorité actuelle de l’agent.** Cette section s’exécute après les données et le plan d’analyse D01–D04. Les fichiers d’analyse et de rapport mentionnés ci-dessous sont des livrables **à créer**, pas des résultats déjà présents. Tous les calculs concernent les nouvelles données 2025.

- [x] **P01** (13 nov. 2026, version référence) Cinq profils (secteur, quartile de taille, marge, endettement, croissance) avec N, statistiques, Shapiro-Wilk, normalité de la marge sur trois preuves, deux phrases managériales. Preuve : src/analysis.py → outputs/analyses_reference/s1_*, figures s1_*, docs/RAPPORT_DE_REFERENCE.md §3.
- [x] **P02** (13 nov. 2026, version référence) Khi-deux secteur × quartile (χ²(12) = 91,76 ; V = 0,248 ; attendus ≥ 14,9), matrice Pearson et Spearman de six variables, nuages de points, recommandations chiffrées. Preuve : s2_*, rapport §4.1–4.2.
- [x] **P03** (13 nov. 2026, version référence) Test t Finance contre Non-finance sur la marge (Levene, Student, Welch, Mann-Whitney, d = 0,59). Preuve : s2_ttest dans results.json, rapport §4.3.
- [x] **P04** (13 nov. 2026, version référence) ANOVA de la marge par 5 groupes de secteurs : Levene (variances inégales) → Welch + Games-Howell, Fisher, Kruskal-Wallis + DSCF, Tukey, η² = 0,058. Preuve : s3_*, rapport §5.
- [x] **P05** (13 nov. 2026, version référence) Régression simple marge ~ ln actif (B = 0,958 ; p = 0,059 ; R² = 0,007) avec diagnostics. Preuve : s4_simple_*, rapport §6.1.
- [x] **P06** (13 nov. 2026, version référence) Régression multiple (N = 488 ; R² = 0,114 ; croissance B = 0,248 ; prime Finance 7,84), VIF, Durbin-Watson, Breusch-Pagan, Cook, HC3 ; quatre sensibilités (sans influentes, sans finance, tronquée, ROA). Preuve : s4_*, rapport §6.2–6.3.
- [x] **P07** (13 nov. 2026, version référence) Vérification indépendante de 12 résultats essentiels par formules à la main et autres fonctions (src/verify_analysis.py : tous identiques) ; sensibilités faites ; empreinte SHA-256 des données dans results.json ; versions dans requirements-analysis.txt. À refaire si la base change (D04).
- [x] **P08** (13 nov. 2026, version référence) Rapport local de référence complet : résumé d’une page avec trois recommandations, données, profils, relations, groupes, régressions, limites, sources. Livrable : docs/RAPPORT_DE_REFERENCE.md (pas encore le Google Doc). À mettre à jour si la base final diffère du brouillon.
- [x] **P09** (13 nov. 2026, version référence) Guide Jamovi et grille de rapprochement avec les valeurs de référence et tolérances : docs/GUIDE_JAMOVI.md.

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
