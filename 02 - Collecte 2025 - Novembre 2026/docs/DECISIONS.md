# Registre des décisions

Mis à jour le 11 novembre 2026. Ce registre distingue un choix explicitement confirmé par David, une convention de travail appliquée par l’agent et une question ouverte. Les confirmations proviennent des échanges de ce chat ; les preuves de données sont dans les fichiers cités. Ne pas attribuer au professeur nos choix méthodologiques.

| ID | Décision / état | Origine et raison | Conséquence et référence |
|---|---|---|---|
| DEC01 | **Confirmé par David** : nouvelle collecte consacrée à 2025 | Les anciens CSV ne permettaient pas de garantir la période de chaque indicateur. David demande une base sourcée et justifiable. | Les résultats des archives ne deviennent pas les résultats 2025. Voir JOURNAL_PROJET.md et METHODOLOGIE.md. |
| DEC02 | **Confirmé par David** : dernier exercice annuel clos en 2025 | David a choisi cette option pour les exercices décalés. | Conserver début/fin exacts ; Nvidia clos en janvier couvre principalement 2024. FY2025 ne suffit pas à classer un exercice. |
| DEC03 | **Confirmé par David** : une ligne par entreprise, cible 500 | Éviter de compter deux fois les comptes d’Alphabet, Fox et News Corp. | Regrouper par CIK et garder tous les tickers ; ne pas additionner les comptes ni les capitalisations de titres sans méthode. |
| DEC04 | **Convention de travail de l’agent** : univers au 31 décembre 2025 | Population cohérente avec l’année cible. Révision Wikipédia historique corrigée par annonce S&P officielle. | 503 titres / 500 CIK ; certification indépendante exhaustive encore absente. Voir universe_reconciliation.json. Ne pas présenter cette date comme une exigence du professeur. |
| DEC05 | **Confirmé par David** : gouvernance publique, gratuite et accessible légalement | Pas d’accès FactSet/ISS/LSEG historique. David accepte le changement de mesure. | Étudier des caractéristiques du conseil, sans prétendre reproduire ISS. L’accord est acquis ; ne pas le redemander. |
| DEC06 | **Méthode appliquée au pilote** : indépendance déclarée et structure de direction | Mesures retrouvées dans les publications officielles 2025. Nvidia nécessite une catégorie sans président. | Trois catégories nominales sans ordre de qualité ; pourcentage calculé sur les effectifs du même conseil. Voir GOUVERNANCE_2025.md. |
| DEC07 | **Convention de travail de l’agent** : date du document de gouvernance, conseil en place | Une publication 2025 ne décrit pas automatiquement une moyenne annuelle ni le 31 décembre. | Conserver les deux dates gouvernance/comptes, signaler leur écart ; interprétation associative, pas causale. |
| DEC08 | **Conventions d’extraction** : premier dépôt annuel régulier, USD, période comparable | Éviter le mélange de versions et les additions de cumuls trimestriels. Intervalle 330–385 jours utilisé comme contrôle. | Les exercices courts ou les corrections exigent relecture. Ce seuil n’est pas une consigne du professeur. Voir src/financials.py et METHODOLOGIE.md. |
| DEC09 | **Exigence de David** : provenance de chaque valeur et documentation reprenable | Toute donnée doit être compréhensible, sourcée et reproductible. | URL, date, unité, période, concept ou rubrique, dépôt, preuve locale si disponible, formule et entrées ; sinon valeur manquante motivée. |
| DEC10 | **Confirmé par David** : dépôt Git existant, archives séparées, commits par David | Conserver l’historique et repartir dans un dossier lisible. | Aucun dépôt imbriqué, commit ou push de l’agent. Les déplacements restent non commités. |
| DEC11 | **Confirmé par David** : il manipule Jamovi | Objectif d’apprentissage et de réalisation par David. | Fournir des étapes adaptées et vérifier ses sorties ; ne pas piloter l’application. |
| DEC12 | **Ouvert** : mesure de taille et quartiles | Capitalisation historique pas encore validée ; actif comptable disponible mais de sens différent. | Présenter source, date, définition et limites ; ne pas remplacer silencieusement la capitalisation par l’actif. |
| DEC13 | **Ouvert** : six exceptions financières et 42 résultats nets consolidés | Incompatibilités de période, périmètre ou définition recensées. | Résolution sourcée ou maintien de valeurs manquantes ; ne pas forcer N=500 pour chaque analyse. |

## DEC14 — Ordre des étapes confirmé par David, 11 novembre 2026

**Accepté, instruction explicite de David.** Réaliser d’abord le projet dans son intégralité indépendamment de Jamovi : données, toutes les analyses, graphiques, diagnostics, interprétations, recommandations et rapport local complet. Ensuite guider David pour reproduire et vérifier dans Jamovi ; enfin finaliser Google Doc et PDF.

Cette décision complète DEC11 (David manipule Jamovi) et remplace l’interprétation précédente où la phase d’analyse pouvait attendre les manipulations Jamovi après la préparation du CSV. Les analyses de référence n’ont pas déjà été faites : P01–P09 sont ouvertes. Les calculs externes ne doivent pas être présentés comme des sorties Jamovi. Les exigences du professeur restent distinctes de cet ordre d’organisation choisi par David.

## DEC15 — Consignes originales complètes, 11 novembre 2026

**Accepté, instruction explicite de David.** Les consignes du professeur doivent être disponibles intégralement et proprement dans le dépôt, et ne pas être remplacées par un résumé. Les formulations originales sont conservées dans docs/CONSIGNES_PROFESSEUR.md avec les 175 pages des supports, le complément Moodle transmis et les quatre PDF sources. Les choix de méthode et de travail du groupe restent séparés. Les PDF font foi pour la présentation des formules, tableaux et schémas ; le texte intégral permet la recherche et la reprise par un agent.

## DEC16 — Numérateur de rentabilité : résultat attribuable à la société mère, 11 novembre 2026

**Convention de travail de l'agent** (DEC13 reste ouverte pour les exceptions F06). 42 sociétés ne publiaient dans les données normalisées que le résultat consolidé (`ProfitLoss`), contrairement aux 452 autres. Règle retenue : numérateur de la marge et du ROA = résultat net attribuable à la société mère, avant dividendes sur ses propres actions de préférence. Application : lecture du rapport si un cas particulier est identifié (Entergy, LyondellBasell, Mastercard) ; sinon `ProfitLoss` moins `NetIncomeLossAttributableToNoncontrollingInterest` du même dépôt et de la même période ; sinon valeur consolidée si aucun minoritaire n'est déclaré (9 cas). La valeur consolidée reste dans `net_income_consolidated_usd`. Raison : cohérence avec la majorité des sociétés et avec la marge « pour les actionnaires » ; écarts jusqu'à 4,4 fois (Interactive Brokers). Preuves : net_income_harmonisation.csv. Alternative écartée : conserver le consolidé, qui mélangerait deux définitions.

## DEC17 — Revenu de Synchrony, 11 novembre 2026

**Convention de travail de l'agent.** Revenu = revenu net d'intérêts 18 466 − reversements aux partenaires commerciaux 4 005 + autres revenus 520 = 14 981 M USD, car le compte de résultat présente ces reversements en déduction avant la provision. Sensibilité sans déduction : 18 986 (marge 18,7 % au lieu de 23,7 %). À rappeler dans le journal de nettoyage et le test de sensibilité (P07).

## DEC18 — Contact déclaré à la SEC, 11 novembre 2026

**Accord explicite de David.** www.sec.gov/Archives refuse les outils non déclarés (403, « Undeclared Automated Tool »). L'adresse e-mail de David est déclarée dans le User-Agent du seul téléchargeur de documents (src/documents.py), conformément à la règle d'accès de la SEC. Les requêtes data.sec.gov gardent l'agent générique. Ne pas étendre cet usage à d'autres services sans accord.

## DEC19 — Exercices de 52/53 semaines clos début janvier 2026, 11 novembre 2026

**Accord explicite de David** (« inclure les trois entreprises… cela ne change pas grand-chose en rigueur statistique »). Snap-on, Stanley Black & Decker et Textron : exercice du 29 décembre 2024 au 3 janvier 2026 (371 jours) retenu comme exercice 2025. Règle générale codée (src/financials.py, `closes_in_target_year`) : un exercice clos du 1er au 7 janvier 2026 qui couvre au moins 360 jours de 2025 est retenu. Conséquence découverte à l’application : L3Harris, Leidos et Trimble (exercice clos le 2 janvier 2026) étaient jusqu’ici représentés par l’exercice clos le 2–3 janvier 2025, qui couvre 2024 ; ils passent à leur exercice 2025. L’agent a appliqué cette conséquence de la même règle ; David peut la renverser. Nvidia et les exercices clos entre janvier et novembre 2025 restent selon DEC02. Résultat : 498 marges.

## DEC20 — Lecture parallèle de la gouvernance, 11 novembre 2026 (ARRÊTÉE le 12 novembre : voir DEC21)

**Accord explicite de David** pour confier la lecture des procurations à plusieurs agents en parallèle, « tout en gardant un sérieux » et avec vérification avant Jamovi. Méthode : 20 fragments, protocole docs/PROTOCOLE_LECTURE_GOUVERNANCE.md, contrôle automatique des citations mot pour mot et des noms (src/governance_check.py), cas ambigus laissés non résolus, puis audit par sondage (tâche G09) avant de considérer les valeurs comme vérifiées.

## DEC12 — mise à jour 11 novembre 2026 (taille) : orientation en attente de confirmation

David a répondu : actif total « selon ce qui est le plus adapté », capitalisation boursière « intéressante » récupérable via Yahoo Finance, éventuellement les deux, et demande une explication. Orientation proposée par l'agent (non confirmée) : **actif total comme mesure principale** (déjà sourcée pour 498 sociétés, même dépôt et même période que les comptes), **capitalisation comme variable de sensibilité** si une collecte datée et documentée est réalisée (cours de clôture au 31/12/2025 × nombre d'actions par catégorie, avec source et date ; Yahoo n'est pas une source officielle et ses champs « actuels » ne conviennent pas). Les deux ne remplacent pas les quartiles : un seul jeu de quartiles est retenu dans le CSV final. **Confirmé par David le 12 novembre 2026 (« Oui, d'accord »)** : actif total en principal, capitalisation en sensibilité optionnelle.

## DEC21 — Plus de sous-agents ; lecture seul par petits lots, 12 novembre 2026

**Instruction explicite de David** : la lecture parallèle a consommé trop de quota (plafond de 5 heures atteint deux fois) ; tous les sous-agents sont arrêtés, on avance petit à petit, éventuellement dans une nouvelle conversation. Les fragments déjà écrits (277 observations lues, 46 non résolues) sont conservés et fusionnés ; ils restent « agent_read_pending_audit » jusqu'à l'audit G09. La suite de G05 se fait sans agents.

## DEC22 — Groupes de secteurs, 12 novembre 2026

**Convention de l'agent.** Variable nominale à 5 modalités `sector_group` regroupant les 11 secteurs GICS comme dans le travail de septembre (Tech & Comms ; Healthcare ; Finance ; Industrials & Energy ; Consumer, avec Real Estate rangé dans Consumer). Raison : exigence du cours (nominale 3–5 groupes pour l'ANOVA) et comparabilité avec l'ancien travail. Limite à écrire dans le rapport : le regroupement de l'immobilier est un choix de présentation ; test de sensibilité possible avec les 11 secteurs.

## DEC23 — Variable de dualité CEO/président, 12 novembre 2026

**Convention de l'agent.** `ceo_duality` : Combined (une seule personne CEO et président) contre Not combined (président séparé ou absence de président). Raison : « No board chair » ne compte qu'une société (Nvidia) ; les effectifs attendus du khi-deux seraient inférieurs à 5. `board_leadership` à trois modalités reste dans la base pour la description.

## DEC24 — Commits et envoi GitHub par l'agent, 12 novembre 2026

**Instruction explicite de David** : « n'hésite pas à envoyer un commit sur github ». Cela remplace pour ce dépôt l'interdiction antérieure (DEC10) : l'agent peut committer et pousser sur la branche `main` quand David le demande ou l'a demandé comme ici. Précautions : le dépôt GitHub est **public** ; aucune adresse personnelle, clé ou jeton dans les fichiers (le contact SEC est lu dans la variable d'environnement `SEC_CONTACT_EMAIL`, voir DEC18) ; les fichiers volumineux (réponses SEC brutes, procurations, rapports) restent ignorés par Git ; pas de réinitialisation ni de réécriture d'historique ; Jamovi reste manipulé par David.

## DEC25 — Gouvernance abandonnée ; nouvelle question, 12 novembre 2026

**Décision de David (option 3 proposée par l'agent)** : abandonner la gouvernance comme variable d'analyse, par simplicité et pour avancer plus vite. Raisons : le cours n'exige pas de gouvernance ; sa collecte exige une lecture manuelle des procurations (3 sociétés par séance, 159 non lues, 51 non résolues) ; les variables financières sont disponibles pour les 500 sociétés par programme.
Nouvelle question de travail : **qu'est-ce qui explique la rentabilité (marge nette, ROA) des entreprises du S&P 500 : taille, endettement, croissance du chiffre d'affaires, secteur ?** Association, pas causalité.
Variables : continues net_margin_pct, roa_pct, ln_assets, debt_ratio_pct, revenue_growth_pct, asset_turnover ; ordinale size_quartile ; nominales sector_group (5), finance_vs_other (2), profitable (2).
Conséquences : DEC05–DEC07, DEC20 et le protocole de gouvernance sont **archivés, pas supprimés** (290 observations, protocole et outils restent dans le dépôt comme travail documenté, non utilisés dans l'analyse). DEC22 reste valable ; DEC23 (ceo_duality) est caduque. Les tâches G05–G09 sont closes comme « abandonnées ». À signaler au professeur : le jeu de données (S&P 500) est inchangé, la question managériale a changé ; David décide s'il informe le professeur.

## Décisions remplacées et alternatives écartées

La V2 de novembre préparée à partir de l’ancien relevé Yahoo reste **archivée**. Ses instructions « Use … in Jamovi » ne s’appliquent plus à cette collecte. Elle corrigeait certains traitements, sans établir des comptes homogènes 2025. David a ensuite choisi la nouvelle collecte ; aucune donnée ni ancien résultat n’est automatiquement transféré.

Le score ISS actuel n’est pas une observation historique 2025. L’accès payant n’est pas retenu ; les sources historiques gratuites restent utilisables si leur date et leur droit d’accès sont établis. Les valeurs non sourcées ne sont pas réintroduites pour compléter Fiserv ou une autre entreprise.

## Comment modifier une décision

Ajouter une entrée datée expliquant le changement, son auteur, la preuve ou l’accord disponible, les données et analyses concernées. Marquer l’ancienne décision comme remplacée en conservant son texte et son motif. Actualiser ensuite la méthode, le dictionnaire, l’état, les tâches et le journal. Un résultat statistique plus favorable ne constitue pas à lui seul une justification de changement.
