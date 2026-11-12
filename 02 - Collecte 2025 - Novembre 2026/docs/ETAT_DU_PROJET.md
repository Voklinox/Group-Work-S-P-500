# État réel au 12 novembre 2026

Lecture rapide : [to-do détaillée](../tasks/todo.md), [journal](JOURNAL_PROJET.md), [décisions](DECISIONS.md), [guide de reprise](REPRISE_AGENT.md).

## Où en est le projet

**Étape 1 (projet de référence indépendant de Jamovi) : terminée le 12 novembre 2026.** Données justifiées, calculs contrôlés, rapport de référence complet, tableaux et graphiques, guide de reproduction. **Étape 2 en cours : séances Jamovi 1 et 2 faites et rapprochées le 12 novembre 2026 (J01 à J03) ; les séances 3 (ANOVA) et 4 (régressions et variantes) sont faites aussi ; reste J06 (exports des sorties et cohérence finale). David reproduit les analyses dans Jamovi** avec le guide [GUIDE_JAMOVI.md](GUIDE_JAMOVI.md) et la grille de rapprochement ; puis **étape 3** : Google Doc et PDF avec les sorties Jamovi.

Question de travail (DEC25) : **qu'est-ce qui explique la rentabilité (marge nette, ROA) des entreprises du S&P 500 : taille, endettement, croissance du chiffre d'affaires, secteur ?** La gouvernance a été étudiée puis abandonnée le 12 novembre 2026 (travail archivé).

## Livrables disponibles

| Livrable | Fichier |
|---|---|
| CSV final unique pour Jamovi (500 lignes) | `data/processed/sp500_2025_JAMOVI.csv` |
| Dictionnaire des colonnes | [DICTIONNAIRE.md](DICTIONNAIRE.md) |
| Journal de nettoyage (noté dans le cours) | [JOURNAL_NETTOYAGE.md](JOURNAL_NETTOYAGE.md) |
| Fiche de provenance | [FICHE_PROVENANCE.md](FICHE_PROVENANCE.md) |
| Analyses de référence (séances 1 à 4) | `outputs/analyses_reference/`, `outputs/figures_reference/` (programme `src/analysis.py`) |
| Vérification indépendante de 12 résultats | `src/verify_analysis.py` (tous identiques) |
| Rapport de référence | [RAPPORT_DE_REFERENCE.md](RAPPORT_DE_REFERENCE.md) |
| Guide Jamovi et grille de rapprochement | [GUIDE_JAMOVI.md](GUIDE_JAMOVI.md) |

## Faits établis (preuves dans les fichiers cités)

- **Population** : 503 titres regroupés en 500 entreprises/CIK au 31 décembre 2025 ; rapprochement avec la table officielle SEC des tickers (492 concordances, 11 écarts expliqués par des événements de 2026) ; 19 ajouts et 19 retraits de 2025 contrôlés. Limite : pas de liste officielle S&P des constituants (accès payant).
- **Comptes** : réponses SEC Company Facts et Submissions pour les 500 entreprises ; **498** marges nettes et ROA (Dayforce : aucun rapport annuel 2025 ; Paramount : prédécesseur/successeur) ; croissance du chiffre d'affaires pour 488. 3,264 faits financiers reliés à leurs preuves et 996 ratios reliés à leurs formules ; 1,629 fichiers sources vérifiés par empreinte, **0 erreur d'intégrité** ; 9 alertes de définition (résultat consolidé sans minoritaires déclarés).
- **Conventions** : exercice annuel clos en 2025 (ou 52/53 semaines clos début janvier 2026) ; résultat net attribuable à la société mère ; revenus bancaires par convention ; taille = actif total, quartiles Q1–Q4 ; cinq groupes de secteurs. Voir [DECISIONS.md](DECISIONS.md).
- **Contrôles qualité** : 100 rapports tirés au hasard (298 cellules sur 300 retrouvées dans le texte) ; contrôles de robustesse de la régression (bootstrap, Huber, médiane, 11 secteurs) ; dépistage des valeurs extrêmes ; trois revenus corrigés (Camden, Huntington, M&T) ; 20 tests automatiques réussis.

## Limites connues (à écrire dans le rapport final)

Association et non causalité ; dates de clôture différentes selon les entreprises ; revenus bancaires reconstitués ; résidus des régressions non normaux à cause de valeurs extrêmes réelles (erreurs robustes et sensibilités fournies) ; regroupement de l'immobilier avec Consumer ; deux entreprises sans comptes 2025.

## Ce qui reste à faire

1. **Étape 2** : J01 à J05 faits (12 nov.) ; reste J06 (séance 4, régressions) et J06 (sorties conservées, cohérence finale).
2. **Étape 3 (R01–R06)** : Google Doc final (relire le Doc avant édition), évaluations des membres sur la couverture (à fournir par le groupe), PDF, dépôt Moodle (échéance indiquée : 2 décembre 2026).
3. **Décision de David (prise, voir le journal)** : il n'est pas nécessaire de prévenir le professeur du changement de question (jeu de données inchangé).

## Entretien du dossier

La to-do porte les actions et critères de fin ; le journal conserve les étapes ; le registre distingue décisions de David et conventions de travail. Après chaque lot, mettre à jour ces documents ainsi que les compteurs concernés. Les pièges de reconstruction et les pièces non présentes dans Git sont détaillés dans REPRISE_AGENT.md.
