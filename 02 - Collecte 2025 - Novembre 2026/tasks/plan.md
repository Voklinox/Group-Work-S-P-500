# Plan de réalisation — trois étapes ordonnées

Clarification de David enregistrée le **11 novembre 2026**. Les tâches et critères détaillés restent dans [todo.md](todo.md). Les [consignes du professeur](../docs/CONSIGNES_PROFESSEUR.md) distinguent les attentes du cours de cet ordre de travail choisi par le groupe.

## Étape 1 — Projet complet de référence par l’agent, indépendamment de Jamovi

**C’est la priorité actuelle.** L’agent ne s’arrête pas au CSV en attendant David.

| Sous-étape | Travail et résultat attendu | Tâches |
|---|---|---|
| Cadre et sources | Consignes dans le dépôt, archives, décisions, population et preuves | A, U |
| Données complètes et vérifiées | Finances, gouvernance publique, exceptions motivées, taille et quartiles | F, G, T |
| Base et protocole | Jointure par CIK, dictionnaire, N par analyse, plan et CSV identifié | D01–D04 |
| Analyses complètes | Profils, normalité, khi-deux, Pearson/Spearman, t-test pertinent, groupes/post-hoc, régressions et diagnostics | P01–P06 |
| Vérification et contenu de référence | Calculs contrôlés, sensibilités utiles, tableaux/graphiques, version de données identifiée | P07 |
| Rapport et préparation pédagogique | Rapport local complet, recommandations et guide Jamovi avec résultats attendus | P08–P09 |

Livrables à produire dans cette étape : calculs reproductibles, tableaux et figures de référence, journal de nettoyage et N, rapport local complet et guide de reproduction. Les fichiers et dossiers futurs tels que `outputs/analyses_reference/`, `outputs/figures_reference/`, `docs/RAPPORT_DE_REFERENCE.md` et `docs/GUIDE_JAMOVI.md` sont des destinations prévues, **pas encore créées comme résultats validés**. Documenter les dépendances nécessaires pour les analyses ; la collecte actuelle repose sur la bibliothèque standard, mais cela ne garantit pas que toute l’analyse statistique future puisse s’y limiter.

**Critère de passage à l’étape 2** : l’ensemble du projet est calculé, interprété et rédigé en référence, avec preuves et options suffisantes pour sa reproduction. Ne pas présenter ces calculs comme des sorties Jamovi.

## Étape 2 — Reproduction guidée dans Jamovi

David manipule l’application ; l’agent guide l’import et les analyses. Reprendre chaque résultat de référence, vérifier types/échelles, modalités, N, options, facteurs et méthodes ; rapprocher les statistiques, degrés de liberté, p-values et tailles d’effet. Expliquer les différences d’arrondi ou de convention et corriger les incohérences de fond.

Livrables : fichier de travail .omv produit par David, sorties identifiées et rapprochement avec la référence. Tâches **J01–J06**. Ne pas déléguer à David la réalisation initiale de l’analyse de référence.

## Étape 3 — Finalisation du Google Doc et du PDF

Relire le Google Doc courant avant modification. Partir du rapport local complet, intégrer les résultats rapprochés, finaliser le résumé d’une page et les trois recommandations, compléter les évaluations du groupe et vérifier les sources et la mise en page. Exporter et relire le PDF ; dépôt par le groupe. Tâches **R01–R06**.

## Règles transversales

Les choix acquis et les questions ouvertes figurent dans [DECISIONS.md](../docs/DECISIONS.md). Toute nouvelle collecte doit rester publique, sourcée et datée. Pas de données de remplacement arbitraires ni d’analyse héritée des archives présentée comme résultat 2025. Mettre à jour le journal et la to-do après chaque lot. David conserve la main sur les commits et sur Jamovi.
