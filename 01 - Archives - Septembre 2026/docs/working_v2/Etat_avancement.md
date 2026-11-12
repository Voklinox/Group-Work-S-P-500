# Avancement au 11 novembre 2026

Équipe : David Wanono, Olyvan Perrin, Guillaume Da Cruz.

## Travail réalisé

- Base préparée : `data/processed/sp500_company_level_v2.csv`, 500 entreprises et 17 variables.
- Archive brute préservée. Les trois doublons d'émetteurs ont été résolus ; aucune valeur financière ou de gouvernance n'a été imputée. La catégorie analytique de Fiserv est explicitement codée Finance et ses champs non observés restent manquants.
- Dictionnaire : `data/processed/sp500_codebook_v2.csv`. Les scores ISS sont décrits comme des rangs ordinaux en déciles.
- Les 13 vérifications du projet réussissent. Les valeurs financières et de gouvernance des lignes conservées correspondent à l'archive brute.
- Les résultats de référence ont été recalculés dans `docs/working_v2/results/`.
- Le Google Doc fourni a été modifié sur place : couverture avec les trois noms, problématique, méthode, cinq profils descriptifs, structure des analyses, limites et liens de sources. Texte vérifié par relecture et export de travail examiné visuellement.

Document de travail : https://docs.google.com/document/d/1I5zWY43G_JIrLmYNwKz_dlHEgy46E5B4YRlmDasl3qc/edit

## Prochaine étape avec David

David manipule lui-même Jamovi. L'assistant le guide étape par étape sans contrôler l'application. Commencer par l'import de la version 2, vérifier 500 lignes et 17 variables, puis régler les types avant les descriptifs.

La reproduction dans Jamovi n'a pas encore eu lieu. Les sections d'analyses correspondantes du Google Doc sont donc explicitement à compléter. Le résumé exécutif et les trois recommandations seront finalisés après cette reproduction.

## Points à compléter pour le dépôt

- Évaluations des membres et barème applicable : à fournir par le groupe, sans notes inventées.
- Date précise d'extraction et périodes des champs : non vérifiées. Maintenir la présentation comme instantané archivé et éviter la qualification collective de comptes audités FY2025.
- Graphiques et anciens rapports : versions historiques ; ne pas mélanger leurs chiffres avec ceux de la version 2.
- Dépôt final PDF avant l'échéance indiquée par David, le 2 décembre 2026. Aucun dépôt n'a été effectué.
