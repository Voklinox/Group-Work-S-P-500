# Méthodologie de la collecte 2025

## Périodes

Choix confirmé par David : retenir pour chaque entreprise son dernier exercice annuel **clos en 2025**, avec date de début et date de fin exactes. Les exercices décalés restent identifiés comme tels. Un exercice clos en janvier 2025 peut couvrir principalement 2024 ; il est inclus selon la règle approuvée et ne sera pas nommé « année civile 2025 ».

Source privilégiée : dépôt annuel 10-K ou équivalent officiel et données XBRL de la SEC. L’API Company Facts regroupe les concepts normalisés et peut omettre des concepts propres aux entreprises. Un champ absent de l’API ne prouve donc pas qu’il n’existe pas dans le rapport. Les secteurs financiers exigent parfois une définition spécifique du chiffre d’affaires, qui sera documentée et contrôlée.

Les comptes annuels sont privilégiés pour les totaux annuels. Additionner quatre chiffres n’est autorisé que si les périodes ne se chevauchent pas. Les 10-Q publient aussi des cumuls de six ou neuf mois : les additionner comme des trimestres double-compterait des montants. Un quatrième trimestre calculé = total annuel moins cumul neuf mois doit être explicitement marqué « calculé ».

## Univers

Date de référence de travail : 31 décembre 2025. La révision historique Wikipédia 1329075976 est archivée et rapprochée de l’annonce officielle S&P du 5 décembre, effective le 22 décembre ; voir le rapprochement détaillé dans SOURCES_ET_REPRISE.md. Les catégories d’actions sont regroupées par CIK, avec conservation de tous les tickers. Le nom S&P 500 ne dispense pas du contrôle des changements de composition. Les identifiants CIK sont prioritaires pour rattacher les rapports ; les tickers peuvent changer. Aucune liste actuelle ne sera rebaptisée liste historique.

## Provenance

Pour chaque source : URL, date de récupération, taille, empreinte SHA-256 et chemin local. Pour chaque valeur : entreprise, CIK, concept XBRL, unité, période, valeur brute, numéro de dépôt SEC, formulaire, date de dépôt, URL du rapport et identifiant du fichier source. Pour chaque calcul : formule et entrées. Les versions corrigées des publications doivent être identifiées, pas mélangées silencieusement.

## Données boursières

La capitalisation et les scores sont des données datées, non des flux annuels. Toute capitalisation historique exigera une date et une convention explicites, avec contrôle des catégories d’actions. Un cours ajusté pour dividendes ne sera pas multiplié sans justification par un nombre d’actions d’une autre date. Les quartiles ne seront construits qu’après validation de la variable de taille.

## Gouvernance

La disponibilité publique de scores ISS 2025 reste à établir. Les historiques existent dans des offres de données. David confirme ne pas avoir accès aux abonnements concernés. David autorise les mesures publiques datées, décrites dans GOUVERNANCE_2025.md. Le changement est approuvé ; leur disponibilité doit maintenant être vérifiée avant intégration. Aucun score courant ne sera utilisé sous une étiquette 2025. Les mesures retenues devront décrire des caractéristiques précises de gouvernance, sans prétendre reproduire ISS.

## Références officielles

- SEC Company Facts et dates des contextes : https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- Accès raisonnable SEC : https://www.sec.gov/about/developer-resources
- Historique ISS diffusé par FactSet : https://insight.factset.com/resources/iss-gqs-datafeed-at-a-glance

## Limite importante

Cette documentation définit la méthode. Elle ne signifie pas que 500 entreprises ou tous les indicateurs ont déjà été récupérés. L’état réel est décrit dans ETAT_DU_PROJET.md et les registres.

## Version et durée des comptes

La sélection retient la première publication annuelle régulière retrouvée, afin de ne pas mélanger des chiffres de différentes versions ou des comparatifs republiés ultérieurement. Les données sont disponibles au plus tard le 11 novembre 2026. Une correction formelle identifiée ultérieurement devra être examinée et documentée, pas ignorée au nom de cette convention.

Un exercice de durée comparable est repéré par un intervalle de 330 à 385 jours entre début et fin. Ce seuil est un contrôle de sélection ; les périodes courtes de transition sont signalées pour relecture et non déclarées inexistantes. Paramount illustre cette limite. **Exception décidée par David (DEC19)** : un exercice de 52/53 semaines clos du 1er au 7 janvier 2026 et couvrant au moins 360 jours de 2025 est retenu comme exercice 2025 (Snap-on, Stanley Black & Decker, Textron, L3Harris, Leidos, Trimble) ; l’exercice clos début janvier 2025 correspondant couvre 2024 et est écarté. Les exercices FY2025 clos le 3 janvier 2026 ne passent pas la règle de clôture calendaire retenue par David ; ce n’est pas une erreur de collecte.

Pour les valeurs absentes des concepts prioritaires, seules les correspondances propres à une entreprise et à un dépôt, documentées dans reviewed_mappings.json, sont appliquées. Les revenus bancaires reconstitués sont explicitement marqués comme somme des intérêts nets GAAP et des revenus hors intérêts. Les ajustements fiscaux équivalents ne sont pas ajoutés. Chaque définition particulière reste visible pour l’examen de comparabilité.
