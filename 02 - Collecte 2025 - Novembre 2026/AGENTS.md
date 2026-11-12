# Instructions de reprise

## Périmètre et décisions de David

- Étude S&P 500 : **qu’est-ce qui explique la rentabilité (marge nette, ROA) des entreprises : taille, endettement, croissance, secteur ?** (DEC25, 12 nov. 2026). La gouvernance a été abandonnée (travail archivé), pour le cours Quantitative Data Analysis, M1 S7.
- Données du **dernier exercice annuel clos en 2025**. Le choix a été explicitement confirmé par David le 11 novembre 2026. Ce n’est pas forcément janvier–décembre et ce n’est pas nécessairement l’exercice étiqueté FY2025.
- Gouvernance : abandonnée le 12 novembre 2026 (DEC25). Ne pas reprendre sa collecte sans nouvelle décision de David ; l’accord du 11 nov. sur les indicateurs publics et le travail réalisé (290 observations, protocole) restent archivés.
- Une ligne par entreprise. L’univers doit être historique et daté ; 500 lignes est la cible et ne doit jamais être obtenue en ajoutant des entreprises ou des valeurs arbitraires.
- Collecte nouvelle et datée. Chaque valeur doit être reliée à sa publication ou rester manquante avec une raison.
- Les anciens travaux sont des archives. Ne jamais réintroduire les imputations Fiserv ni les scores actuels comme valeurs 2025.
- David manipule lui-même Jamovi : le guider, ne pas contrôler l’application.
- David manipule Jamovi. Commits et push : seulement sur demande explicite de David (accordée le 12 novembre 2026, DEC24) ; jamais de réinitialisation, de réécriture d’historique ni de dépôt imbriqué ; dépôt public : aucune donnée personnelle dans les fichiers.

## Priorité et ordre des trois étapes — confirmé par David

1. **Réaliser entièrement le projet de référence indépendamment de Jamovi** : achever les données, puis toutes les analyses du cours, les diagnostics, tableaux, graphiques, interprétations, recommandations et un rapport local complet, avec calculs reproductibles. Ne pas attendre que David utilise Jamovi pour calculer ou rédiger ce contenu de référence.
2. **Guider David dans Jamovi** : il effectue les manipulations ; rapprocher ses sorties du projet de référence, expliquer et résoudre les écarts. Ne pas présenter les résultats d’un programme externe comme déjà produits dans Jamovi.
3. **Finaliser Google Doc et PDF** : intégrer les résultats rapprochés, réviser le rapport, obtenir les évaluations du groupe et contrôler le PDF.

La priorité actuelle est l’étape 1. Le CSV seul ne termine pas cette étape. Les tâches P01–P09 du suivi couvrent l’analyse complète et le rapport de référence ; elles sont encore ouvertes.

## Ordre de lecture

Lire `README.md`, `docs/REPRISE_AGENT.md`, `docs/ETAT_DU_PROJET.md` et `tasks/todo.md`, puis `docs/CONSIGNES_PROFESSEUR.md`, `docs/DECISIONS.md`, la méthode et le dictionnaire. Consulter `docs/JOURNAL_PROJET.md` pour le déroulement et le protocole de gouvernance avant de collecter. Ne pas annoncer un CSV final tant que ses contrôles et ses sources ne sont pas validés.

## Suivi obligatoire après chaque lot

Actualiser `tasks/todo.md` avec le livrable réellement terminé et sa preuve, puis l’état courant et les compteurs concernés. Ajouter une entrée datée à `docs/JOURNAL_PROJET.md` avec actions, raisons, fichiers, résultats, limites et prochaine étape. Enregistrer tout changement de décision dans `docs/DECISIONS.md` en distinguant accord de David et convention de l’agent. Ne pas effacer les raisons précédentes ni assimiler « document candidat » à « mesure vérifiée ».

Avant toute reconstruction, lire ses effets dans le guide de reprise. `src.collect --limit` remplace les mêmes sorties que la collecte complète ; ne pas l’utiliser dans le dossier partagé pour un simple test. Les co-CEO/co-présidents requièrent un examen du schéma actuel avant codage. Les réponses brutes sont locales et ignorées par Git : vérifier leur présence pour une reprise sur une autre machine.

## Consignes originales à conserver

David demande les consignes complètes, sans les remplacer par un résumé. `docs/CONSIGNES_PROFESSEUR.md` contient le texte des 175 pages des quatre supports et le message Moodle transmis ; les quatre PDF originaux sont dans `docs/sources/cours`. Conserver les formulations originales et les références. Les interprétations, choix du groupe et plans de travail restent séparés dans les décisions et la méthode.

## Exigences de qualité

Conserver les réponses sources localement et enregistrer leurs URL, dates de collecte et empreintes. Relier chaque fait financier à CIK, tag, unité, dates de période, accession SEC, date de dépôt et formulaire. Pour une variable calculée, conserver la formule et les identifiants des faits d’entrée.

Ne pas inférer une année à partir du nom d’un fichier. Ne pas assimiler une donnée instantanée à une moyenne annuelle. Ne pas supposer que la capitalisation d’un ticker est automatiquement celle de toutes les catégories d’actions. Ne pas fabriquer de score de gouvernance historique.

Respecter les limites des fournisseurs ; utiliser les interfaces officielles et un cache, sans contourner les restrictions d’accès. Aucun achat ou contact externe sans demande explicite. Aucun mot de passe, jeton ou information bancaire dans les fichiers.

## Livraison

Prévoir un CSV Jamovi clairement identifié et des fichiers de documentation séparés. Les fichiers de preuve et de diagnostic ne sont pas des versions concurrentes du CSV à analyser. Indiquer les N valides et valeurs manquantes. Le PDF final doit respecter le protocole IDENTIFY → HYPOTHESISE → DECIDE → RECOMMEND, le résumé d’une page et les évaluations de groupe sur la couverture.
