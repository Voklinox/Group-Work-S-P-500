# Reprendre le projet sans l’historique du chat

Dernière mise à jour : **11 novembre 2026**. Ce guide permet une reprise à partir du dossier local. Les résultats de collecte restent provisoires ; l’objectif est d’abord un projet de référence intégral préparé par l’agent sans dépendre de Jamovi, puis sa reproduction guidée par David dans Jamovi et la finalisation du Google Doc/PDF.

## 1. Lecture minimale

Lire dans cet ordre :

1. [AGENTS.md](../AGENTS.md) : autorisations, limites et règles de travail.
2. [README.md](../README.md) et [ETAT_DU_PROJET.md](ETAT_DU_PROJET.md) : état réel et limites.
3. [Liste des tâches](../tasks/todo.md) : prochaine action, identifiants et critères de fin.
4. [DECISIONS.md](DECISIONS.md) : choix acquis et conventions de travail ; ne pas redemander les accords déjà donnés.
5. [METHODOLOGIE.md](METHODOLOGIE.md), [GOUVERNANCE_2025.md](GOUVERNANCE_2025.md), [DICTIONNAIRE.md](DICTIONNAIRE.md) : règles de sélection et sens des valeurs.
6. [JOURNAL_PROJET.md](JOURNAL_PROJET.md) pour la progression ; [SOURCES_ET_REPRISE.md](SOURCES_ET_REPRISE.md) pour la provenance détaillée ; [CONSIGNES_PROFESSEUR.md](CONSIGNES_PROFESSEUR.md) avant de figer les analyses.

## Ordre prioritaire — instruction explicite de David

**Étape 1 :** terminer données, analyses de toutes les séances, diagnostics, tableaux/graphiques, interprétations, recommandations et rapport local complet, indépendamment de Jamovi. Les tâches P01–P09 ont été ajoutées pour rendre ce travail explicite ; un CSV prêt ne termine pas le projet de référence.

**Étape 2 :** guider David pour reproduire chaque analyse dans Jamovi et rapprocher ses sorties de la référence. David fait les manipulations. Distinguer les calculs externes des véritables sorties de l’application.

**Étape 3 :** finaliser le Google Doc et le PDF à partir du rapport de référence et des résultats rapprochés. Ne pas attendre Jamovi pour effectuer les premiers calculs et rédiger le rapport local.

Les [consignes en texte intégral](CONSIGNES_PROFESSEUR.md) et les [quatre supports copiés](sources/cours/) sont désormais dans le dépôt ; les 175 pages sont transcrites intégralement et reliées aux PDF originaux. Les empreintes des fichiers et du texte sont enregistrées. Un point d’entrée existe aussi à la racine Git.

## 2. Contexte à conserver

- Équipe : **David Wanono, Olyvan Perrin, Guillaume Da Cruz**. Écrire Olyvan avec un seul n, conformément au nom transmis.
- Cours : Quantitative Data Analysis, M1 S7, EM Normandie ; professeur Nguyen Anh-Tuan. Date limite indiquée par David : **2 décembre 2026**. Validation du jeu de données par le professeur rapportée par David ; la fiche non signée n’impose pas de redemander cette validation.
- Question de travail : associations entre caractéristiques publiques du conseil et rentabilité, en tenant compte de taille/secteur. Pas de démonstration causale.
- Finances : dernier exercice annuel **clos en 2025**, dates exactes, pas nécessairement janvier–décembre ni FY2025.
- Population de travail : S&P 500 au **31 décembre 2025**, 500 CIK et 503 titres. Date de population = convention de travail ; vérifier l’univers complet, pas seulement sa taille.
- Gouvernance : David a accepté les indicateurs publics gratuits, datés et accessibles légalement. Le pilote utilise le conseil en place décrit dans des documents publiés en 2025. Date du document ≠ moyenne annuelle ≠ garantie au 31 décembre.
- David manipule Jamovi ; l’agent le guide. David gère les commits. Aucun commit, push ou dépôt imbriqué de l’agent.
- Les archives sont dans le dossier voisin **01 - Archives - Septembre 2026**. Les anciennes instructions et résultats V2 n’ont pas priorité sur ceux de ce dossier.

Le dépôt Git est le dossier parent **Group Work S&P 500**. Les anciens fichiers ont été déplacés : Git peut montrer des suppressions à leurs anciens chemins et des dossiers non suivis à leurs nouveaux chemins. Ce statut ne prouve pas une perte de données. Ne pas lancer de réinitialisation ou de nettoyage pour le faire disparaître.

## 3. État à retrouver dans les preuves

| Élément | Résultat attendu au point de reprise | Preuve principale |
|---|---:|---|
| Entreprises / titres | 500 / 503 | data/reference/universe_2025-12-31.csv et universe_reconciliation.json |
| Réponses principales SEC présentes | 500 Company Facts + 500 Submissions | data/raw/sec et manifestes |
| Exercices extraits | 498 | financials_2025_WORKING.csv et collection_coverage.json |
| Marges calculables | 498 | même tableau et compteur ; comparabilité encore ouverte |
| Faits / ratios financiers | 3 244 / 989 | financial_evidence.json et derived_evidence.csv |
| Audit enregistré | 1 095 sources par empreinte, 0 erreur d’intégrité, 9 alertes de définition (11 nov. après F07) | outputs/integrity_audit.json |
| Documents de gouvernance candidats | 505 pour 496 entreprises | governance_proxy_candidates.csv et governance_catalogue_coverage.json |
| Mesures de gouvernance | 290 observations (5 pilotes + 285 à auditer, G09) ; 51 non résolues ; 159 pas encore lues | governance_observations.json, governance_shards/, governance_unresolved.csv, governance_audit_queue.csv, governance_measurement_coverage.json |
| CSV final / analyses 2025 / PDF final | Aucun résultat final validé | tâches D, J et R ouvertes |

Ces valeurs sont un point de reprise, pas des constantes à imposer aux fichiers. Si les fichiers ont évolué, examiner les changements, mettre à jour les compteurs et le journal ; ne pas ramener les données à ces nombres artificiellement.

Attention au champ `state` de `outputs/collection_coverage.json` : « governance absent » décrit la table financière seule, qui ne contient pas la gouvernance. Le registre de gouvernance distinct contient bien cinq observations ; ne pas conclure qu’il n’en existe aucune dans le projet.

## 4. Carte des fichiers et de leurs rôles

Les chemins suivants sont relatifs à la racine de ce nouveau dossier.

| Fichier / dossier | Rôle et utilisation |
|---|---|
| data/raw/universe_revision_probe.json | Identifiant et date de la révision historique Wikipédia. |
| data/raw/universe_2025_revision_1329075976.json | Copie de la révision historique, pas une liste actuelle. |
| data/raw/spglobal_2025-12-05_rebalance.html | Annonce officielle qui justifie les corrections de décembre. |
| data/reference/universe_2025-12-31.csv | Clé CIK, nom historique, secteur, tous les tickers et date de population. |
| data/reference/universe_reconciliation.json | Corrections et limites de la reconstruction de l’univers. |
| data/raw/sec/CIK<CIK>.json | Company Facts SEC : données normalisées, concepts, unités, périodes, versions de dépôts. |
| data/raw/sec/submissions_CIK<CIK>.json | Catalogue récent des publications, parfois insuffisant pour toute l’année 2025. |
| data/raw/sec/CIK…-submissions-….json | Anciennes pages de catalogue récupérées pour compléter les recherches. |
| data/reference/source_probe_manifest.json | Registre des téléchargements exploratoires. |
| data/reference/download_manifest.jsonl | Journal des récupérations : URL, date UTC, chemin, taille, empreinte ou erreur. Une ligne par événement, pas une table de mesures. |
| data/reference/reviewed_mappings.json | Six correspondances contrôlées, liées à une entreprise, période et version. Une transcription directe APA explicitement signalée ; ne pas généraliser les exceptions à toutes les sociétés. |
| data/reference/financial_evidence.json | Preuves des faits retenus, avec identifiants et entrées des sommes particulières. |
| data/reference/derived_evidence.csv | Preuves des ratios : formule et identifiants des faits d’entrée. |
| data/reference/filing_catalogue.csv | Catalogue issu de l’extraction financière, fondé sur les dépôts récents ; moins complet pour la gouvernance que l’inventaire dédié. |
| data/processed/financials_2025_WORKING.csv | **Table financière provisoire**, 500 entreprises ; pas le CSV final à ouvrir dans Jamovi. |
| data/quarantine/financial_review.csv | Champs non extraits et problèmes ; plusieurs lignes possibles par entreprise. Ne pas interpréter 226 lignes de revue comme 226 entreprises invalides. |
| data/quarantine/core_exceptions.csv | Six exceptions centrales décrites avec source et motif. |
| data/quarantine/definition_review.csv | 9 résultats nets sans minoritaires déclarés (consolidé = mère, 7 vérifiés dans les rapports). Les 42 cas initiaux sont résolus dans data/reference/net_income_harmonisation.csv. |
| data/reference/core_exception_resolutions.csv | Résolution des six exceptions centrales (F06). |
| src/documents.py, src/download_governance.py, src/governance_text.py, src/governance_extract.py, src/governance_check.py, src/merge_governance_shards.py | Chaîne de lecture de la gouvernance : téléchargement en cache (User-Agent avec contact, DEC18), texte brut, passages candidats, vérification des fragments (citations mot pour mot), fusion. Voir docs/PROTOCOLE_LECTURE_GOUVERNANCE.md. |
| (ancienne ligne) src/documents.py, src/governance_extract.py | Téléchargeur de documents SEC (User-Agent avec contact, accord de David) et extracteur de passages de gouvernance (aide à la lecture, n’écrit aucune observation). |
| data/reference/governance_proxy_candidates.csv | Documents candidats et métadonnées : aucune observation chiffrée validée par leur seule présence. |
| data/reference/alternative_governance_sources.json | Pistes pour Blackstone, KKR, Paramount et Qnity ; aucune mesure à inférer automatiquement. |
| data/reference/governance_observations.json | **Entrée contrôlée** du pilote : effectifs, personnes, date, périmètre et preuves. Fichier à enrichir après lecture des documents. |
| data/processed/governance_2025_WORKING.json | Résultat calculé à partir des observations ; ne pas modifier directement pour ajouter une observation. |
| data/quarantine/governance_review_queue.csv | 500 sociétés ; statut documentaire distinct du statut de mesure. |
| data/raw/governance/ | Originaux effectivement récupérés : Apple, Nvidia, JPMorgan au point de reprise. Les deux autres originaux du pilote ne sont pas archivés. |
| outputs/*.json | Compteurs et audits, à rapprocher des données réelles. |
| outputs/governance_pilot_summary.md | Lecture humaine des cinq exemples, avec dates et sources. |
| src/ et tests/ | Programmes de sélection, reconstruction et vérification ; ne pas confondre leurs tests avec une validation scientifique complète. |

Les réponses brutes SEC et les originaux de gouvernance sont **ignorés par Git**. Un autre agent sur cette machine peut les relire ; un agent après clonage seul devra disposer d’une copie/sauvegarde ou les récupérer depuis les sources. Ne pas affirmer que Git contient toutes les pièces. Les registres précisent aussi les refus HTTP et les lectures en ligne sans copie locale.

## 5. Première action concrète : continuer la gouvernance (G05)

1. Ouvrir la file de revue et choisir un petit lot non contrôlé, en conservant une diversité de secteurs et en incluant les cas particuliers. Ne pas sélectionner selon la rentabilité.
2. Retrouver le document dans l’inventaire dédié. S’il y en a plusieurs, vérifier assemblée annuelle/spéciale, date et auteur ; une procuration contestée peut venir d’un tiers.
3. Lire les rubriques sur le conseil en place, l’indépendance et la direction. Vérifier que numérateur et dénominateur décrivent le même conseil ; rapprocher les candidats des administrateurs déjà en fonction.
4. Archiver la copie officielle publique si possible et enregistrer URL/date/empreinte. En cas de refus, conserver le motif et chercher une copie officielle librement accessible ; ne pas contourner une restriction ni déclarer une fausse archive.
5. Ajouter une observation dans `governance_observations.json` en reprenant la structure du pilote : CIK, dépôt, date, effectifs, personnes, catégorie, périmètre et rubriques précises. Une date d’effet différente de la publication doit être conservée dans les preuves. Un doute reste explicite ; aucun zéro de remplacement.
6. Si la source est une alternative nouvelle, documenter aussi ses métadonnées. Le programme vérifie la correspondance CIK/dépôt/date/lien avec l’inventaire ou les alternatives enregistrées.
7. Reconstruire avec `python3 -m src.governance`, vérifier le résultat, actualiser les compteurs et le journal. Ce programme écrit des sorties : le lancer après contrôle des entrées, pas simplement pour lire le projet.
8. Traiter les co-CEO/co-présidents séparément avant extension du schéma : le validateur actuel est fondé sur un nom CEO et un nom de président. Ne pas concaténer arbitrairement plusieurs personnes pour contourner cette limite.

## 6. Autres points ouverts à conserver

Finances : exceptions F06 résolues (voir core_exception_resolutions.csv) ; il reste à relire un échantillon de rapports, les revenus bancaires et les valeurs extrêmes (F08–F09). Les fichiers de revue ne doivent pas être comblés pour obtenir N=500 partout.

Taille : la capitalisation au 31 décembre 2025 n’est pas validée. L’actif comptable est une option différente, pas un remplacement déjà approuvé. Documenter les options avant de figer taille et quartiles.

Cours : la structure de direction à trois catégories peut servir de nominale, sous réserve des effectifs et conditions des tests. La variable ordinale reste à construire. Les onze secteurs GICS ne répondent pas seuls à l’exigence nominale 2–5 catégories.

Les principales conditions de publication du fichier final sont dans les tâches U03, F06–F09, G05–G08, T01–T04 et D01–D04. Toutes les cellules ne doivent pas forcément être remplies, mais leurs absences et l’échantillon de chaque analyse doivent être justifiés. Après D04, poursuivre les calculs et la rédaction de référence P01–P09 avant le guidage Jamovi.

## 7. Commandes et effets

Exécuter depuis **ce nouveau dossier**, et non depuis la racine Git ou les archives. Le traitement principal utilise Python 3.9 ou supérieur et la bibliothèque standard. L’ancien `.venv` du parent est historique ; ne pas supposer qu’il fonctionne ou qu’il est nécessaire. La lecture visuelle de PDF peut utiliser les outils disponibles sur la machine ; elle ne justifie pas de réinstaller les dépendances des anciennes analyses.

| Commande | Effet à connaître |
|---|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` | Vérifie la logique sans reconstruire les tables ni télécharger les sources. Quinze tests réussis lors de la préparation du pilote. |
| `python3 -m src.universe` | Reconstruit et **remplace** l’univers et son rapprochement depuis la révision archivée et les corrections codées. Ne pas lancer pour une simple lecture. |
| `python3 -m src.download_all` | Complète le cache financier ; téléchargements publics si manquants, six requêtes simultanées maximum, quatre démarrages par seconde dans ce processus. |
| `python3 -m src.collect` | Reconstruit et **remplace** table financière, preuves, revue, catalogue récent et couverture. Peut télécharger une source manquante. |
| `python3 -m src.audit` | Contrôle les faits, formules et empreintes ; **réécrit** preuves de ratios, revue des définitions et rapport d’intégrité. Ne remplace pas la relecture comptable. |
| `python3 -m src.governance_catalogue` | Reconstruit les documents candidats ; complète les anciennes pages SEC manquantes. **Réinitialise les statuts de lecture** dans la file. |
| `python3 -m src.archive_governance` | Récupère uniquement les copies publiques explicitement identifiées par source_archive_url dans les observations ; réutilise le cache. Ne collecte pas automatiquement les 500 rapports. |
| `python3 -m src.governance` | Valide les observations, calcule les pourcentages, reconstruit le résumé et la couverture, puis **réapplique les statuts contrôlés** à partir du registre, y compris les observations ajoutées à la file de revue. |

**Piège identifié :** `src.collect --limit` écrit dans les mêmes fichiers que la collecte complète. Ne pas l’utiliser pour tester un petit lot dans le dossier de travail partagé ; il remplacerait temporairement les tables de 500 sociétés. Utiliser une copie isolée si un essai limité est nécessaire.

Ne pas faire tourner deux collecteurs ou deux agents écrivants en même temps sur ces mêmes tables. Après une reconstruction de l’inventaire de gouvernance, relancer gouvernance pour rétablir les statuts issus des observations. Après modification de la sélection financière, reconstruire puis auditer les finances. Les reconstructions ne sont pas nécessaires pour une simple prise de connaissance.

## 8. Rapport et collaboration

Google Doc transmis par David : [document de travail du groupe](https://docs.google.com/document/d/1I5zWY43G_JIrLmYNwKz_dlHEgy46E5B4YRlmDasl3qc/edit?tab=t.0). Dernier état connu : brouillon lié à l’ancienne approche. **Non rouvert lors de cette mise à jour documentaire** ; lire son contenu courant avant toute édition.

Le professeur demande un PDF final et les évaluations des membres à côté des noms sur la couverture, selon le complément Moodle transmis par David. Le barème des évaluations, une longueur totale et un oral ne sont pas établis dans ce complément. Les notes doivent venir du groupe.

L’agent doit d’abord calculer et interpréter les analyses 2025 et rédiger un rapport local de référence complet (P01–P09). Les conclusions sont établies à partir de ces calculs vérifiés, puis contrôlées lors de la reproduction Jamovi par David. La finalisation dans Google Doc vient ensuite. Ne pas convertir les anciens résultats en résultats des nouvelles données.

## 9. Maintenir une reprise fiable

À chaque lot terminé : mettre à jour la to-do, les compteurs de l’état actuel et le journal. Si une convention change, mettre à jour le registre des décisions, la méthode et le dictionnaire. Conserver les anciennes raisons et rendre explicites les limites restantes.

Pour transmettre le projet dans un nouveau chat, il suffit d’indiquer le dossier et de demander la lecture de **AGENTS.md puis docs/REPRISE_AGENT.md**, avec la tâche à reprendre. Ce guide est une base de reprise, pas la preuve que les tâches encore ouvertes sont réalisées.
