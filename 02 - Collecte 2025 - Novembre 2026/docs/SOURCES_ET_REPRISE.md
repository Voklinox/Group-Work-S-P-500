# Sources, preuves et reprise

## Lire les preuves

1. `data/reference/universe_2025-12-31.csv` donne la population, les CIK et tous les tickers.
2. `universe_reconciliation.json` décrit chaque correction à la révision Wikipédia 1329075976, datée du 23 décembre 2025. Le relevé comportait 501 titres et 498 CIK : les ajouts CRH, CVNA et FIX manquaient, SOLS était encore présent ; LKQ et MHK étaient déjà absents. L’annonce officielle S&P du 5 décembre, effective le 22 décembre, justifie les corrections. Résultat : 503 titres, 500 entreprises. Ce rapprochement ne remplace pas une certification exhaustive de toute la liste par S&P.
3. `source_probe_manifest.json` conserve les téléchargements exploratoires ; `download_manifest.jsonl` ajoute une ligne par téléchargement du collecteur, avec URL, date UTC, chemin, taille, SHA-256 ou erreur. Une réponse en cache n’a pas une nouvelle date fictive.
4. `financial_evidence.json` relie chaque cellule financière à un identifiant de fait, au concept XBRL et à sa définition, à l’unité, aux dates de période, au dépôt, à sa date et au lien du rapport. La source machine correspond à `data/raw/sec/CIK<CIK>.json`, dont l’empreinte figure dans les registres. Ces fichiers sont des réponses officielles SEC. Exception explicite : la transcription manuelle APA pointe vers reviewed_mappings.json et le rapport lu en ligne ; elle ne prétend pas être présente dans le JSON Company Facts. Les sommes de concepts conservent leurs faits d’entrée imbriqués. derived_evidence.csv relie chaque ratio à ses identifiants de faits et à sa formule.
5. `filing_catalogue.csv` référence les dépôts annuels et procurations d’assemblée (DEF 14A) 2025–2026 retrouvés dans le catalogue récent. Ce n’est pas une liste exhaustive de tous les dépôts historiques, ni une preuve que chaque rapport HTML a été téléchargé.
6. `data/quarantine/financial_review.csv` recense les points manquants ou rejetés. « Absent des concepts normalisés » ne signifie pas absent du rapport.

## Sources utilisées

- SEC, documentation des API : https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- SEC, règles d’accès : https://www.sec.gov/about/developer-resources
- Révision historique Wikipédia : https://en.wikipedia.org/w/index.php?title=List_of_S%26P_500_companies&oldid=1329075976
- Rééquilibrage officiel S&P : https://press.spglobal.com/2025-12-05-CRH,-Carvana-and-Comfort-Systems-USA-Set-to-Join-S-P-500-Others-to-Join-S-P-MidCap-400-and-S-P-SmallCap-600
- Exemple de gouvernance publique Apple, DEF 14A déposé le 10 janvier 2025 : https://www.sec.gov/Archives/edgar/data/320193/000130817925000008/aapl4359751-def14a.htm

Le proxy Apple permet de constater l’indépendance du conseil et la séparation président/directeur général à la date indiquée. Son titre « 2025 » ne transforme pas ses tableaux de rémunération ou ses honoraires d’audit relatifs à 2024 en données de 2025. Toute extraction future doit dater l’observation précise, distinguer administrateurs en place et candidats, et ne pas assimiler une information ponctuelle à une moyenne annuelle.

## Reproduire

Pour une prise de connaissance, lire d’abord [REPRISE_AGENT.md](REPRISE_AGENT.md) : les commandes ci-dessous reconstruisent des sorties et ne constituent pas un parcours obligatoire de lecture. Le guide précise les fichiers remplacés, le risque de `src.collect --limit` et l’ordre de reconstruction de la gouvernance.


Depuis ce dossier, Python 3.9 ou supérieur et la bibliothèque standard suffisent :

```sh
python3 -m unittest discover -s tests -v
python3 -m src.universe
python3 -m src.download_all
python3 -m src.collect
python3 -m src.audit
```

`download_all` conserve au maximum six requêtes en vol, avec au plus quatre démarrages par seconde. Ne pas exécuter deux collecteurs en parallèle. En cas de refus du fournisseur, interrompre et examiner l’erreur ; ne pas contourner les restrictions. Les téléchargements réussis sont réutilisés. `collect` reconstruit les tables à partir des fichiers disponibles et peut compléter un document de métadonnées absent.

Les grands fichiers bruts SEC sont conservés localement mais ignorés par Git pour éviter un dépôt de plusieurs gigaoctets. Les registres, sélections, scripts, documentation et preuves extraites restent versionnables. Un dépôt Git seul n’est donc pas une sauvegarde complète des réponses brutes : les recopier séparément si nécessaire. Aucune clé API ni donnée privée n’est nécessaire.

## Contrôles avant Jamovi

- 500 CIK uniques et rapprochement documenté de 503 titres ; vérifier les changements d’entreprise et de CIK.
- Fins d’exercice en 2025 ; montants USD ; même dépôt pour les données d’une ligne ; rejets explicites pour les exercices courts ou les concepts manquants.
- Relire un échantillon de rapports originaux et toutes les anomalies de chiffre d’affaires ; harmoniser les résultats nets attribuables à la société et consolidés.
- Publier les N valides par variable et par analyse. Ne jamais remplir les cellules vides avec une constante pour garder N=500.
- Définir et sourcer les variables de gouvernance, de taille et les catégories exigées par le cours.
- Générer un seul CSV final nommé clairement ; les tables de preuve restent des diagnostics, pas d’autres versions à choisir dans Jamovi.

## Gouvernance publique

Accord de David enregistré le 11 novembre 2026. Voir GOUVERNANCE_2025.md. Les originaux effectivement téléchargés sont dans data/raw/governance, exclus de Git, avec URL et empreinte dans download_manifest.jsonl. Les lectures sans copie locale sont signalées. Refus et redirections ne sont pas transformés en fausses archives.

L’inventaire consulte aussi les anciennes pages SEC et reconnaît procurations définitives, contestées et déclarations d’information. Les observations contrôlées et la couverture réelle sont distinctes de cet inventaire.

## Supports du professeur conservés dans le dépôt

Les quatre supports de cours ont une copie identique dans docs/sources/cours. Le registre sources_manifest.json conserve nom, producteur, emplacement d’origine, chemin copié, nombre de pages, taille et SHA-256. Ces copies ne sont pas placées dans les grands caches bruts ignorés par Git ; elles sont versionnables avec le projet. Le texte intégral des 175 pages est dans CONSIGNES_PROFESSEUR.md, avec un point d’accès à la racine Git. Le message Moodle est celui transmis par David, pas une vérification en ligne nouvelle.

Les phases de calculs de référence, reproduction Jamovi et finalisation du rapport sont désormais séparées dans tasks/plan.md. L’absence de Jamovi ne bloque pas le travail d’analyse de référence de l’agent.

Le registre docs/sources/cours/transcription_manifest.json conserve le nombre de pages attendu et transcrit, l’empreinte de chaque texte de page et celle du fichier Markdown complet. Aucune page n’est exclue. Les illustrations et la mise en page des formules restent dans les PDF originaux inclus.

## Chaîne de calcul complète (état du 12 novembre 2026)

```sh
python3 -m src.collect && python3 -m src.audit      # comptes SEC, preuves, audit d'intégrité
python3 -m src.extra_variables                      # croissance du chiffre d'affaires et preuves
python3 -m src.screening                            # dépistage des valeurs extrêmes
SEC_CONTACT_EMAIL=<adresse> python3 -m src.report_sample 25 2026   # contrôle de 25 rapports (téléchargement)
python3 -m src.build_dataset                        # CSV final data/processed/sp500_2025_JAMOVI.csv
python3 -m venv .venv && .venv/bin/pip install -r requirements-analysis.txt
.venv/bin/python -m src.analysis && .venv/bin/python -m src.verify_analysis
```

Le téléchargement de documents sur sec.gov exige un contact déclaré (variable `SEC_CONTACT_EMAIL`, jamais écrit dans les fichiers : dépôt public).
