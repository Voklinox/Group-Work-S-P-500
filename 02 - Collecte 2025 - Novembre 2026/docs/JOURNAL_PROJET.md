# Journal d’avancement du projet

Ce journal conserve les étapes et leurs motifs. Les compteurs actuels sont dans ETAT_DU_PROJET.md et les rapports de outputs/. Les tâches à exécuter sont uniquement suivies dans tasks/todo.md.

## Travaux antérieurs — préservés dans les archives

Un ensemble de données, programmes, analyses, graphiques et rapports existait déjà. Le dossier porte le nom « Septembre 2026 », mais cette étiquette ne prouve pas la date exacte de collecte de toutes ses valeurs.

Le 11 novembre 2026, un audit des anciens travaux a confirmé de nombreux calculs tout en signalant la provenance temporelle, les doublons de sociétés, le traitement Fiserv et certaines interprétations. Référence conservée : `../../01 - Archives - Septembre 2026/docs/audit_2026-11-11/Audit_du_projet.md`.

Une V2 provisoire de 500 entreprises a ensuite été construite à partir du même relevé, avec retrait de valeurs non étayées et recalcul de catégories. Elle n’établissait pas une collecte homogène 2025. David a demandé de clarifier les variantes, les sources et les quartiles avant de retenir une base. Référence : `../../01 - Archives - Septembre 2026/docs/Data_Preparation_v2.md`.

Ces documents restent utiles pour comprendre le travail et les corrections, sans fournir les résultats de la nouvelle étude.

## 11 novembre 2026 — déroulement de la nouvelle collecte

Les étapes suivantes sont consignées dans leur ordre de travail. Aucun horaire précis ni date de confirmation du professeur n’est reconstitué artificiellement.

| Étape | Action et raison | Résultat / preuve | Suite |
|---|---|---|---|
| 01 — Repartir | David choisit une nouvelle collecte 2025, une entreprise par ligne et une provenance complète. | Nouveau périmètre, consigné dans DECISIONS.md, DEC01–DEC03 et DEC09. | Conserver les archives sans réutilisation silencieuse. |
| 02 — Organiser | Séparation des archives et du nouveau travail dans le dépôt existant. | Dossiers 01 - Archives - Septembre 2026 et 02 - Collecte 2025 - Novembre 2026 ; README parent mis à jour. | Aucun commit ou push ; David les gère. |
| 03 — Fixer les périodes | David confirme l’exercice annuel clos en 2025 pour les sociétés à calendrier décalé. | Dates exactes dans les preuves et le tableau financier. | Ne pas confondre année fiscale et année de clôture. |
| 04 — Tester les comptes | Essai SEC sur Apple, Nvidia, Alphabet, JPMorgan et Fiserv. | Sélection des périodes et versions de dépôts testée ; sources présentes dans les registres. | Étendre sans réintroduire les anciennes constantes. |
| 05 — Reconstituer l’univers | Le relevé historique Wikipédia est incomplet pour le rééquilibrage de décembre. | 501 titres / 498 CIK au départ ; ajout CRH, CVNA, FIX et retrait SOLS par rapprochement S&P ; LKQ et MHK déjà absents. Résultat 503 titres / 500 entreprises. Voir universe_reconciliation.json. | Contrôle indépendant complet de la population encore à faire. |
| 06 — Collecter les finances | Téléchargement public SEC avec cache, limites de requêtes et registre d’empreintes. | Company Facts et Submissions disponibles pour les 500 entreprises. Extraction et six correspondances particulières documentées. | Comparabilité et exceptions à contrôler. |
| 07 — Contrôler | Rapprochement cellules/preuves, périodes, formules et empreintes locales. | 495 exercices, 494 marges, 3 244 faits et 989 ratios ; audit sans erreur d’intégrité, 42 alertes de définition. | Un contrôle d’intégrité ne vaut pas validation comptable complète. |
| 08 — Expliquer les absences | Six cas empêchent une marge par entreprise. | Snap-on, Stanley Black & Decker, Textron : clôture FY2025 au 3 janvier 2026 ; Paramount : prédécesseur/successeur ; Dayforce : annual 2025 à retrouver ; Synchrony : revenu à définir. Voir core_exceptions.csv. | Pas d’imputation ou de changement de règle implicite. |
| 09 — Choisir la gouvernance publique | David indique ne pas avoir d’accès payant, puis accepte explicitement les indicateurs publics gratuits. | DEC05 accepté ; aucun nouvel accord nécessaire pour leur collecte. | Prouver la disponibilité et le périmètre des mesures. |
| 10 — Tester la gouvernance | Lecture d’Apple, Nvidia, Alphabet, JPMorgan et PepsiCo. | 5 observations contrôlées ; 3 originaux archivés, 2 lectures SEC sans copie locale. Nvidia impose une catégorie sans président. Voir governance_pilot_summary.md. | Étendre aux 495 autres sociétés. |
| 11 — Préparer l’extension | Recherche des documents 2025, y compris anciennes pages SEC, procurations contestées et déclarations d’information. | 505 documents candidats pour 496 entreprises ; alternatives identifiées pour Blackstone, KKR, Paramount et Qnity. | Ne pas transformer ce compteur documentaire en compteur de mesures validées. |
| 12 — Rendre la reprise autonome | David demande un suivi de A à Z pour lui-même et un autre agent. | Guide REPRISE_AGENT.md, registre DECISIONS.md, ce journal ; to-do détaillée avec priorités, critères de fin et liens vers les preuves ; README et AGENTS actualisés. | Maintenir ces documents à chaque lot de travail. |

## Vérifications et limites conservées

Dernier contrôle d’intégrité enregistré : 1 042 fichiers sources vérifiés, zéro erreur d’intégrité, 42 alertes de définition. Quinze tests réussissaient à la fin de la préparation du pilote de gouvernance. La présente mise à jour documentaire vérifie les compteurs locaux, la présence des fichiers, les liens internes et la conservation des données/programmes ; elle ne relance pas toute la collecte ni les analyses statistiques. Contrôle documentaire effectué : 30 liens locaux résolus, 44 identifiants de tâches uniques (15 tâches réalisées, 29 ouvertes), aucune modification des données, programmes ou rapports machine existants.

Le Google Doc fourni par David a servi de brouillon de l’ancienne approche. Son état actuel doit être relu en ligne avant toute modification : aucune nouvelle lecture/édition du Doc ni opération Jamovi n’a été faite pour cette mise à jour documentaire.

## 11 novembre 2026 — complément : consignes autonomes et ordre de réalisation

David demande que les consignes soient disponibles à l’intérieur du dépôt et précise l’ordre : projet de référence intégral par l’agent sans dépendre de Jamovi, reproduction guidée par David, puis finalisation Google Doc/PDF.

- Les consignes existaient sous forme résumée dans docs/CONSIGNES_PROFESSEUR.md. Les quatre supports originaux ont été relus aux pages de prescriptions ; le résumé a été complété avec exigences, pages, .omv de séance, Pearson et Spearman, diagnostics et structure finale. La mention du t-test dans la synthèse est distinguée de la liste de dépôt S02.
- Les quatre PDF ont été copiés, sans modifier les originaux, dans docs/sources/cours ; leurs empreintes source/copie sont identiques et enregistrées dans sources_manifest.json. Leur total est d’environ 1,17 Mo. Les informations du professeur sont désormais disponibles sans le dossier de cours extérieur.
- Un point d’entrée CONSIGNES_PROFESSEUR.md et des instructions AGENTS.md sont ajoutés à la racine Git ; la version détaillée reste unique dans le projet actif.
- DEC14 formalise l’ordre demandé. Le plan, la to-do, les README, les instructions, l’état et le guide de reprise ont été alignés. Les tâches P01–P09 rendent explicites les analyses et le rapport de référence complet **avant** Jamovi.
- Cette mise à jour ne prétend pas réaliser les analyses encore ouvertes ; aucune donnée financière ou de gouvernance et aucun programme d’analyse n’est modifié. Aucun commit n’est effectué.

Prochaine action opérationnelle : poursuivre G05 et les vérifications F06–F07, finaliser taille/base/protocole, puis exécuter toutes les analyses de référence P01–P09 sans attendre Jamovi.

## 11 novembre 2026 — précision suivante : consignes intégrales, sans résumé

David précise qu’il ne veut pas d’un résumé des consignes. La synthèse intermédiaire est remplacée par les textes originaux des **175 pages** des quatre supports, avec index de navigation, lien vers chaque page PDF et message Moodle transmis reproduit intégralement. Les quatre PDF restent identiques aux originaux pour conserver formules, schémas et tableaux. Un registre de transcription conserve couverture et empreintes du texte de chaque page ; DEC15 enregistre cette exigence.

Le point d’accès à la racine Git renvoie à cette version complète unique. Les consignes originales sont séparées du plan et des conventions du groupe. Les tâches P01–P09 et l’ordre fixé par DEC14 restent inchangés : projet complet de référence, puis Jamovi guidé, puis Google Doc/PDF. Les données et programmes existants restent inchangés. Vérification finale : 175 textes de page rapprochés à l’extraction source, quatre copies PDF identiques aux originaux, 230 liens locaux valides et 54 tâches uniques (16 réalisées, 38 ouvertes). Aucun commit.

## 11 novembre 2026 (soir) — reprise avec un nouveau modèle : F07, F06 et outillage de gouvernance

- **Demande** : continuer G05 et les questions financières dans l'ordre fixé (référence complète avant Jamovi).
- **F07 réalisé** : règle du résultat attribuable à la société mère (DEC16). 42 alertes traitées : 30 calculées, 3 lues dans le rapport, 9 sans minoritaires (7 vérifiées dans le rapport ; Monster et Paychex : aucun minoritaire dans le rapport ou les données). Nouveau champ net_income_basis et net_income_consolidated_usd. Audit : 0 erreur, 9 alertes. Tests : 18 réussis.
- **F06 partiel** : Synchrony défini (DEC17, 495 marges) ; Dayforce définitivement manquante (aucun 10-K 2025 : radiation 2026-02-04, 15-12G 2026-02-17) ; Paramount manquante (prédécesseur/successeur) ; les trois clôtures au 3 janvier 2026 attendent DEC19.
- **Accès SEC** : refus 403 sur www.sec.gov ; contact déclaré après accord de David (DEC18). Les refus de la première tentative sont conservés au registre des téléchargements.
- **Gouvernance** : src/documents.py et src/governance_extract.py créés ; 11 procurations 2025 (première société alphabétique de chaque secteur, choix indépendant de la rentabilité) téléchargées dans data/raw/governance/. Aucune nouvelle observation validée : la lecture et le rapprochement conseil en place/candidats restent à faire. Constat de débit : environ 3 000 à 5 000 jetons de lecture par société ; 495 sociétés exigent de nombreux lots ou une lecture en parallèle.
- **Limites** : sensibilité de Synchrony à documenter (P07) ; les valeurs non retrouvées par recherche de texte (Ball, Interactive Brokers, Match, Simon, WEC) reposent sur l'identité consolidé − minoritaires et non sur une ligne lue.
- **Prochaine action** : décision de David sur DEC19 et sur la méthode de lecture de gouvernance ; sinon continuer G05 par lots de 10 à 15.

## 11 novembre 2026 (suite) — décisions de David, F06 terminé, lecture parallèle de la gouvernance

- **Décisions de David** : inclure les trois exercices clos le 3 janvier 2026 (DEC19) ; lire la gouvernance avec plusieurs agents en parallèle, avec sérieux, et vérifier tout avant Jamovi (DEC20).
- **F06 terminé** : règle `closes_in_target_year` (exercice clos du 1er au 7 janvier 2026 couvrant au moins 360 jours de 2025). Snap-on, Stanley Black & Decker et Textron incluses. Effet de bord corrigé : L3Harris, Leidos et Trimble étaient représentées par leur exercice clos le 2–3 janvier 2025 (donc 2024) ; elles passent à leur exercice 2025. Revenu L3Harris (21 865 M USD) transcrit du compte de résultat, car aucun concept standard. Résultat : 498 marges (manquent Dayforce et Paramount, avec motif). Audit : 0 erreur ; 20 tests réussis ; seules six lignes de la table ont changé (comparées à la sauvegarde précédente).
- **Gouvernance, préparation** : téléchargement unique des 505 documents candidats (0 échec, 1,2 Go, ignorés par Git) et des 4 sources alternatives ; protocole docs/PROTOCOLE_LECTURE_GOUVERNANCE.md ; vérificateur de fragments (citations mot pour mot, noms, arithmétique, correspondance avec la liste officielle) testé avec une citation inventée, rejetée à raison ; script de fusion.
- **Gouvernance, lecture** : 20 agents lancés en parallèle (fragments 01–19 de 23 à 26 sociétés, fragment 00 pour Blackstone, KKR, Paramount, Qnity). Les 495 sociétés hors pilote sont réparties par ordre alphabétique ; les 5 pilotes sont déjà contrôlés. Les résultats ne sont pas encore connus à l’écriture de cette entrée ; ils seront fusionnés puis audités par sondage (tâche G09) avant tout usage.
- **Limites** : un contrôle automatique des citations garantit que le texte cité existe dans le document, pas que l’effectif est bien interprété ; d’où l’audit par sondage. Les agents n’ont pas accès au réseau ; les copies locales sont des documents SEC téléchargés (empreintes au registre).
- **Prochaine action** : fusionner les fragments, relancer `python3 -m src.governance`, auditer, traiter les non résolues ; poursuivre F08–F09 et la taille (T01–T03).

## 12 novembre 2026 — arrêt des sous-agents, fusion de la lecture déjà faite

- **Incident** : la lecture parallèle (DEC20) a atteint deux fois le plafond d'usage de 5 heures ; 19 agents sur 20 ont été interrompus en cours de lecture, leurs fichiers partiels étant sauvegardés. David demande d'arrêter tous les sous-agents et d'avancer petit à petit (DEC21). Vérification : plus aucun agent actif.
- **Résultat conservé** : 277 observations lues et 46 sociétés non résolues, 0 échec au vérificateur de citations. Fusion dans governance_observations.json (282 au total avec les 5 pilotes), reconstruction par src.governance (statuts séparés : pilote contrôlé / lue à auditer), 20 tests réussis. Répartition provisoire : 164 présidents séparés, 117 fonctions cumulées, 1 sans président. Raisons de non-résolution dominantes : président ou CEO en transition à la date du document, indépendance non déclarée pour tous.
- **Décision** : taille = actif total en principal, capitalisation en sensibilité optionnelle (DEC12 confirmée).
- **Limite** : ces 277 valeurs ne sont pas des valeurs vérifiées avant l'audit G09 ; la présence mot pour mot des citations ne garantit pas l'interprétation.
- **Prochaine action** : lire par lots de 10 à 15 les 172 sociétés restantes sans sous-agents, puis audit par sondage.

## 12 novembre 2026 (suite) — lecture solo, premier lot

- Lot de test sans sous-agents : 2 observations ajoutées (Altria 11 administrateurs/10 indépendants, président indépendant séparé ; American Electric Power 12/11, président indépendant séparé), fragment shard_20.json, 0 échec au vérificateur. Total : 284 observations (5 pilotes + 279 à auditer), 46 non résolues, 170 pas encore lues.
- **Constat de débit** : à ce niveau de rigueur (rapprochement conseil en place/candidats, noms, citations), la lecture solo coûte environ 8 000 à 10 000 jetons par société ; ni Ameren (un administrateur partant encore en poste), ni Amcor, AIG, Amazon, American Express n'ont pu être conclus sans lectures supplémentaires. Les 170 restantes ne tiennent pas dans une conversation.
- **Option proposée à David** : le cours exige au moins 100 observations ; 284 sont déjà disponibles, ordonnées alphabétiquement par fragment sans lien avec la rentabilité. Priorité possible : audit G09, traitement de F08–F09, base finale, et lecture des 170 restantes seulement en complément. Décision attendue.

## 12 novembre 2026 (soir) — outillage gouvernance et dépistage financier (F08–F09)

- **Demande de David** : rédiger du code pour traiter les 500 sociétés avec de bonnes sources officielles, par lots, et avancer sur la to-do générale. Il a aussi demandé de s'inspirer de septembre : le script de septembre (extract_sp500_esg.py) récupérait en un passage des scores ISS actuels via l'API Yahoo, non historiques et écartés par DEC05 ; il n'existe pas de source officielle structurée de l'indépendance du conseil, qui se lit dans les procurations SEC.
- **Code ajouté** : src/governance_auto.py (propositions automatiques avec niveaux de confiance ; 9 niveaux B sur 170 : insuffisant), src/governance_packets.py (paquets de phrases candidates numérotées, citations exactes par construction) et src/governance_promote.py (observations construites à partir des décisions). Constat : les 170 sociétés restantes sont les cas difficiles (administrateurs partants encore en poste, candidats nouveaux, présidents exécutifs) ; la lecture reste manuelle pour la plupart.
- **F08–F09** : src/screening.py ; 3 revenus mal sélectionnés corrigés (Camden 12,9 M$ → 1 573,5 M$ ; Huntington 8 166 M$ ; M&T 9 690 M$) via correspondances revues avec drapeau `override` dans src/collect.py. Audit 0 erreur, 20 tests réussis, 498 marges. Les extrêmes restants sont réels.
- **Limite** : l'échantillon de relecture de rapports (au moins 25) n'est pas encore fait ; les compteurs de gouvernance sont inchangés (284 observations, 46 non résolues, 170 non lues).
- **Prochaine action** : lire les paquets de gouvernance par lots (src.governance_packets show), puis relecture d'échantillon F08, puis U03.

## 12 novembre 2026 (nuit) — U03 partiel et gouvernance : lot 21

- **U03** : table officielle SEC des tickers téléchargée (data/raw/sec_company_tickers.json) ; 492 des 503 titres concordent ; 11 écarts expliqués un par un par des dépôts SEC de 2026 (AvalonBay, Coterra, Dayforce, EA, Hologic, WBD : radiations après rachat ; BNY et Marsh McLennan : nouveaux tickers ; Equity Residential et Paramount : nouveaux noms ; Exxon : réorganisation de 2026). Les 18 ajouts de 2025 sont dans l'univers. Reste le contrôle des retraits.
- **G05** : lot 21 : Amazon (12/10, président exécutif séparé), AvalonBay (11/10), AIG (12/11, fonctions cumulées), C.H. Robinson (12/11) ; 5 sociétés classées non résolues avec raison (administrateurs partants encore en poste). Total : 288 observations, 51 non résolues, 161 non lues.
- **Constat** : environ 1 société sur 3 des paquets est concluable avec une lecture ciblée ; les autres demandent un second passage.

## 12 novembre 2026 (relecture d'ensemble demandée par David)

- **Tests et audit** : 20 tests réussis ; audit d'intégrité 0 erreur sur 1 599 sources vérifiées par empreinte, 3 264 faits, 996 ratios ; 9 alertes de définition (résultat consolidé sans minoritaires déclarés).
- **Financier** : 498 marges ; corrections F06/F07/F08 relues ; extrêmes restants réels ; échantillon de relecture des rapports (au moins 25) toujours à faire.
- **Gouvernance, plausibilité de 283 observations** : 0 incohérence nom/fonction (le nom du CEO et du président figure près de la fonction dans le document) ; indépendance 44 % à 95,5 % (médiane 90 %) ; effectifs 6 à 22 ; 6 profils atypiques plausibles (Ares, Berkshire, CME, Interactive Brokers, Palantir, T-Mobile : sociétés contrôlées ou grand conseil). Échantillon aléatoire de 6 relu : 5 cohérents, 1 (CBRE) avec effectif déduit et documenté.
- **Risque identifié** : 76 observations sur 283 mentionnent des administrateurs partants encore en poste ou des effectifs déduits ; elles forment l'essentiel de la file d'audit G09 (107 cas).
- **Documentation** : compteurs de README, ETAT, REPRISE et to-do réalignés (288/51/161). Rien n'est commité.
- **Verdict de la relecture** : la base financière est cohérente et auditée ; la gouvernance est utilisable seulement après G09 ; le projet n'est pas encore prêt pour Jamovi (G05, G09, F08, U03, T02–T04, D01–D04 ouverts).

## 12 novembre 2026 (contrôle demandé par David : conformité aux consignes du prof)

- **Question de David** : a-t-on suivi les consignes ; les sources sont-elles fiables ; le rendu est-il prêt ; que signifient « 161 pas lues » ; ne pas compliquer.
- **Constat** : le cours exige au moins 100 lignes, pas 500 ; les 500 sont notre cible de population (DEC03). Les 161 sont des sociétés dont la procuration n'a pas encore été lue ; leur gouvernance reste vide avec le statut `not_yet_read`, comme prévu par la méthode, et les analyses utilisent les N valides (287 cas complets gouvernance + marge à ce jour).
- **Fait** : base brouillon data/processed/sp500_2025_JAMOVI_DRAFT.csv (src/build_dataset.py), quartiles de taille (actif total), groupes de secteurs (DEC22), variable ceo_duality (DEC23) ; T01–T04 et D01 cochés en brouillon.
- **Vérification de la spécification du cours** sur les données : toutes les cases cochées (voir T04).
- **Pas encore prêt** : journal de nettoyage, fiche de provenance (source, producteur, année, N), audit G09, analyses P01–P09, guide Jamovi.

## 12 novembre 2026 (suite) — journal de nettoyage, fiche de provenance, commit

- Livrables notés du cours rédigés : docs/JOURNAL_NETTOYAGE.md et docs/FICHE_PROVENANCE.md (D02 partiel). Décalage gouvernance/clôture calculé sur 287 observations : médiane −271 jours (242 documents publiés avant la clôture, 45 après).
- DEC24 : David autorise commits et push ; dépôt public, donc l'adresse de contact SEC est sortie du code (variable SEC_CONTACT_EMAIL).

## 12 novembre 2026 (soir) — F08 terminé, commit e70648a poussé

- Commit e70648a poussé sur GitHub (main) à la demande de David (DEC24) ; contact SEC retiré du code.
- F08 : 25 rapports aléatoires, 73/75 cellules retrouvées ; Clorox : états en annexe ; 10 sociétés financières à ratio élevé : 9/10 retrouvées, Progressive à confirmer.

## 13 novembre 2026 — lot de gouvernance 22 et essai d'automatisation

- Deux observations ajoutées (Cincinnati Financial 13/9, président exécutif séparé ; Corteva 12/11, effectif fondé sur les candidats) : total 290 observations, 51 non résolues, 159 pas encore lues. 0 échec au vérificateur.
- **Essai d'automatisation abandonné** : comptage des « cartes d'administrateurs » (ancre « Director since » et étiquette « Independent »), testé sur les 285 observations lues : effectif exact dans 60 cas sur 234 seulement. Trop imprécis, code supprimé. Conclusion : la lecture reste manuelle, environ 2 à 4 sociétés conclues pour 12 000 jetons.

## 13 novembre 2026 — gouvernance abandonnée, nouvelle question (DEC25)

- **Décision de David** (option 3) : abandonner la gouvernance, pour avancer plus vite et simplifier. Raison explicitée : le cours ne l'exige pas ; la collecte exige une lecture manuelle (159 non lues, 51 non résolues).
- **Nouvelle question** : qu'est-ce qui explique la rentabilité (marge nette, ROA) des entreprises du S&P 500 : taille, endettement, croissance, secteur ?
- **Fait** : src/extra_variables.py (croissance du chiffre d'affaires à partir du même rapport : 488 valeurs, preuves dans revenue_growth_evidence.csv) ; src/build_dataset.py réécrit sans gouvernance (500 lignes, debt_ratio_pct, asset_turnover, profitable, finance_vs_other) ; documents alignés (AGENTS, README, ÉTAT, REPRISE, DECISIONS, todo, dictionnaire, fiche de provenance, journal de nettoyage). Travail de gouvernance archivé, non supprimé.
- **Vérification de la spécification du cours** : toutes les exigences satisfaites ; khi-deux secteur × quartile : effectif attendu minimal 14,9.
- **Prochaine action** : plan d'analyse D03, CSV final D04, puis calculs de référence P01–P09.

## 13 novembre 2026 (suite) — étape 1 : analyses, rapport de référence et guide Jamovi

- Environnement `.venv` (pandas 2.3.3, SciPy 1.13.1, statsmodels 0.14.6, matplotlib 3.9.4) ; src/analysis.py : séances 1 à 4, 29 tableaux et 17 graphiques, empreinte des données dans results.json.
- **Résultats principaux** (500 entreprises, N = 498 ou 488) : marge médiane 12,9 % (non normale) ; secteur × taille χ²(12) = 91,76, V = 0,25 ; Finance +8,4 points de marge (d = 0,59) ; ANOVA de Welch F(4 ; 189,1) = 10,41, η² = 0,058 ; régression multiple R² = 0,114 : croissance du CA B = 0,248 et prime Finance 7,84, taille et endettement non significatifs ; ROA négativement associé à la taille.
- **Vérification** (P07) : src/verify_analysis.py recalcule 12 résultats par formules à la main : tous identiques. Deux formulations du rapport corrigées après relecture des chiffres (robustesse de la croissance avec erreurs HC3 : p de 0,04 à 0,08).
- Livrables : docs/RAPPORT_DE_REFERENCE.md (P08), docs/GUIDE_JAMOVI.md (P09). P01–P09 cochés, avec la réserve : base encore « DRAFT » (D04).
- **Limites** : résidus non normaux (valeurs extrêmes), erreurs robustes à privilégier ; rapport en version de référence, pas encore reproduit dans Jamovi ni rédigé dans le Google Doc.
- **Prochaine action** : U03, F09, D04 (figer le CSV et relancer analyses et vérifications), puis Jamovi avec David.

## Format pour les prochaines entrées

Ajouter une section datée avec : demande ou objectif ; action et motif ; fichiers/preuves ; résultat et nombre de cas vérifiés ; tâche terminée ou restant ouverte ; décision éventuelle ; prochaine action. Conserver les entrées précédentes. Si une ancienne conclusion est corrigée, ajouter la correction et sa raison au lieu d’effacer l’historique.
