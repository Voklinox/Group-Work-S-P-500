# État réel au 11 novembre 2026

Lecture rapide : [to-do détaillée](../tasks/todo.md), [journal](JOURNAL_PROJET.md), [décisions](DECISIONS.md), [guide de reprise](REPRISE_AGENT.md).

## Priorité de travail clarifiée par David

**Étape 1 en cours :** projet complet de référence calculé, interprété et rédigé par l’agent indépendamment de Jamovi. Les analyses statistiques, tableaux, graphiques et le rapport de référence restent à réaliser après validation de la base ; tâches P01–P09.

**Étape 2 ensuite :** David reproduit dans Jamovi avec guidage et rapprochement des sorties. **Étape 3 :** finaliser Google Doc/PDF. L’ancien ordre qui pouvait laisser attendre Jamovi après le CSV est remplacé. Les consignes et supports sont disponibles en texte intégral dans docs/CONSIGNES_PROFESSEUR.md ; les 175 pages et quatre PDF originaux sont accessibles depuis la racine Git, avec empreintes de contrôle.

## Ce qui est fait

- Ancien travail préservé dans `01 - Archives - Septembre 2026`. Nouvelle collecte dans le dossier voisin, avec un seul dépôt Git parent. Aucun commit ni push effectué.
- Règle confirmée par David : dernier exercice annuel clos en 2025, dates exactes conservées.
- Univers historique de travail au **31 décembre 2025** reconstitué : **503 titres regroupés en 500 entreprises/CIK**. Toutes les catégories d’actions sont conservées dans la colonne tickers. Révision historique Wikipédia rapprochée de l’annonce officielle S&P de décembre ; corrections détaillées. Une certification indépendante de la liste complète par S&P reste absente.
- Réponses publiques **Company Facts et Submissions téléchargées pour les 500 entreprises**, sans échec sur ces 1 000 téléchargements. Les sources brutes restent locales, ignorées par Git.
- Extraction d’un exercice annuel de durée comparable pour **498 entreprises** ; revenus, marge nette, résultat net, actif et ROA renseignés pour **498** (Synchrony défini et exercices de 52/53 semaines inclus le 11 novembre). Trésorerie : 415 ; passif hors capitaux propres : 355. Les variables secondaires manquantes ne justifient pas d’exclure ces entreprises des analyses qui ne les utilisent pas.
- **3 244 valeurs financières sélectionnées** reliées à leurs preuves ; **989 ratios calculés** reliés à leurs entrées et formules. Six correspondances comptables particulières ont été vérifiées et expliquées dans `reviewed_mappings.json` ; une seule valeur, le revenu APA, a été transcrite directement du rapport faute de concept normalisé adéquat. Elle est identifiée comme lecture manuelle, pas comme valeur extraite de l’API.
- Contrôle d’intégrité : **1 042 fichiers sources vérifiés par empreinte**, aucune incohérence entre cellules, preuves, périodes et formules lors du contrôle. Les tests du collecteur portent notamment sur les périodes décalées, la version de dépôt, les doublons et les exceptions. Cela ne certifie pas encore la comparabilité comptable de toutes les entreprises.

## Les exceptions financières (F06) — résolues le 11 novembre 2026

| Entreprise | Résolution |
|---|---|
| Snap-on, Stanley Black & Decker, Textron | **Incluses** (décision de David, DEC19) : exercice FY2025 de 52/53 semaines clos le 3 janvier 2026, qui couvre toute l’année 2025. Même règle appliquée à L3Harris, Leidos et Trimble (exercice clos le 2 janvier 2026) : leur exercice précédent clos début janvier 2025 couvrait 2024. |
| Paramount Skydance | Manquante : séparation prédécesseur/successeur après l’acquisition d’août 2025 ; aucune période de 12 mois comparable. |
| Dayforce | Manquante : aucun rapport annuel 2025 n’existe (rachat clos le 4 février 2026, Form 15 le 17 février). |
| Synchrony Financial | Revenu défini par l’agent (DEC17) : 14 981 M USD ; marge calculée. |

Détail et sources : `data/reference/core_exception_resolutions.csv`. Les lignes restent présentes ; 500 lignes de population ne signifient pas N=500 pour chaque analyse (498 marges).

## Ce qui reste ouvert

1. **Gouvernance** : **abandonnée le 12 novembre 2026 (DEC25)** ; le travail réalisé (505 documents, 290 observations lues, protocole, outils) est archivé et non utilisé dans l’analyse. La question de travail est désormais : qu’est-ce qui explique la rentabilité (marge nette, ROA) : taille, endettement, croissance, secteur ?
2. **Comparabilité du résultat net** : harmonisée le 11 novembre 2026 sur le résultat attribuable à la société mère (convention DEC16) : 452 valeurs déclarées, 30 calculées (consolidé moins minoritaires), 3 lues dans le rapport (Entergy, LyondellBasell, Mastercard), 9 sans minoritaires déclarés dont 7 lus dans le rapport. Preuves : data/reference/net_income_harmonisation.csv. Reste le contrôle de comparabilité sectorielle (F08).
3. **Taille** : capitalisation historique non validée ; actif comptable disponible mais ce n’est pas la même mesure. Les quartiles ne sont pas encore produits. Définir une mesure justifiable et la règle de classement avec David.
4. **Relecture** : approfondir les exceptions, les revenus des banques/assurances, les changements d’entreprise et un échantillon de rapports originaux. Les contrôles automatiques ne remplacent pas cette étape.
5. **Cours** : la variable nominale de direction du conseil à trois modalités est définie ; vérifier sa couverture et les effectifs, puis construire la variable ordinale et figer le plan d’analyse avant le CSV final. Le fichier de travail actuel n’est pas prêt à être présenté comme jeu de données final.
6. **Analyse complète, Jamovi et rapport** : l’agent calcule d’abord toutes les analyses et rédige le rapport local de référence, puis David réalise leur reproduction guidée dans Jamovi et le rapprochement des sorties. Le dernier état connu du Google Doc reflète l’ancienne approche ; il n’a pas été rouvert lors de la mise à jour documentaire et doit être relu avant toute édition. Ne pas réutiliser ses anciens résultats comme résultats 2025. Ensuite rédaction, graphiques et PDF avec notes d’évaluation du groupe sur la couverture.

## Fichiers utiles

- `README.md` puis `SOURCES_ET_REPRISE.md` pour comprendre le dossier et relancer la collecte.
- `DICTIONNAIRE.md` pour le sens des colonnes ; `METHODOLOGIE.md` pour les conventions.
- `CONSIGNES_PROFESSEUR.md` pour les attentes du cours et le complément Moodle.
- `outputs/collection_coverage.json` et `outputs/integrity_audit.json` pour les compteurs vérifiés.
- `data/processed/financials_2025_WORKING.csv` : **diagnostic provisoire**, unique tableau financier de travail, à ne pas confondre avec un CSV final Jamovi.

## Entretien du dossier

La to-do porte les actions et critères de fin ; le journal conserve les étapes ; le registre distingue décisions de David et conventions de travail. Après chaque lot, mettre à jour ces documents ainsi que les compteurs concernés. Les pièges de reconstruction et les pièces non présentes dans Git sont détaillés dans REPRISE_AGENT.md.
