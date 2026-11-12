# Protocole de lecture des procurations (G05)

Mis en place le 11 novembre 2026, après accord de David pour une lecture en parallèle par plusieurs agents. Ce protocole complète [GOUVERNANCE_2025.md](GOUVERNANCE_2025.md) (définitions) et [DECISIONS.md](DECISIONS.md). Il décrit **comment** une société est lue, enregistrée et contrôlée. Chaque lecteur traite un fragment (`shard`) de la liste et n'écrit que son fichier.

## Règles absolues

- Travailler uniquement sur le texte du document candidat de la société (copie locale en cache). **Aucune connaissance extérieure** pour compléter un effectif, un nom ou une fonction : tout doit être trouvé dans le document ou rester non résolu.
- Aucune opération Git, aucune reconstruction (`src.collect`, `src.governance`, `src.audit`, etc.), aucune modification d'un fichier autre que votre fichier de fragment. Aucun accès réseau n'est nécessaire.
- Un doute reste un doute : classer la société dans `unresolved` avec la raison précise. Ne jamais mettre un zéro ou une valeur « plausible » à la place.

## Ce que l'on mesure

À la date de publication du document, pour le **conseil en place** (administrateurs effectivement en fonction) :

- `board_size` : nombre d'administrateurs en fonction. Inclure ceux qui ne se représentent pas mais siègent encore à la date du document. **Exclure** les candidats qui ne sont pas encore administrateurs et les anciens administrateurs partis. Si le document ne donne que la liste des candidats, la rapprocher des biographies (date d'entrée en fonction) pour retrouver le conseil en place.
- `independent_directors` : nombre de ces mêmes administrateurs que le conseil a déclarés indépendants selon les règles de cotation (NYSE ou Nasdaq). Numérateur et dénominateur décrivent exactement le même ensemble de personnes.
- `board_leadership` : `Combined CEO and chair` (la même personne), `Separate CEO and chair` (deux personnes ; un président exécutif non CEO compte comme séparé), `No board chair` (le document dit qu'il n'y a pas de président ; un administrateur référent n'est pas un président).
- `ceo_name`, `chair_name` (vide uniquement pour `No board chair`; identique à `ceo_name` si fonctions cumulées), `lead_director_name` si un administrateur référent est nommé.

**Cas à ne pas trancher : classer en `unresolved`** : co-directeurs généraux ou co-présidents, poste de président ou de CEO vacant ou en transition à la date du document, effectif en place non rapprochable des candidats, indépendance non indiquée pour tous, document qui ne décrit pas un conseil (déclaration de tiers, document sans section conseil), société contrôlée sans déclaration de l'indépendance. Indiquer ce qui manque.

Si deux documents sont candidats, choisir la procuration définitive de l'assemblée annuelle de l'émetteur (pas un complément ni un document d'actionnaire dissident), et consigner la raison dans `selection_note`.

## Fichiers et outils (depuis le dossier du projet actif)

- Liste attribuée : `data/quarantine/governance_assignments/shard_NN.csv` (colonnes : `cik, company, sector, accession, filed, form, source_url, local_file`).
- Texte brut d'un document : `python3 -m src.governance_text <cik> <accession> > <fichier_temporaire>` puis recherche ciblée (Grep) et lecture des seules sections utiles. Les cellules de tableau sont séparées par ` | `.
- Passages candidats (aide, non définitif) : `python3 -m src.governance_extract <cik>`.
- Modèles d'observation : Apple et JPMorgan dans `data/reference/governance_observations.json`.
- Vérification obligatoire avant de terminer : `python3 -m src.governance_check data/reference/governance_shards/shard_NN.json`. Elle contrôle la structure, l'arithmétique, la correspondance avec la liste officielle des documents, la présence mot pour mot de chaque citation dans le document et la présence des noms cités.

## Format du fichier de fragment

`data/reference/governance_shards/shard_NN.json` :

```json
{"shard": "NN", "observations": [ {...}, ... ], "unresolved": [ {"cik": "...", "company": "...", "reason": "...", "detail": "..."} ]}
```

Chaque observation :

```json
{
 "cik": "0000066740", "company": "3M", "accession": "0000066740-25-000029", "publication_date": "2025-03-26",
 "board_size": 11, "independent_directors": 10,
 "board_leadership": "Combined CEO and chair", "ceo_name": "William M. Brown", "chair_name": "William M. Brown",
 "lead_director_name": "James R. Fitterling", "independence_standard": "NYSE",
 "source_url": "<source_url de la liste>", "archive_file": "<local_file de la liste>",
 "evidence": [
  {"group": "board_counts", "locator": "section et page", "quote": "phrase copiée mot pour mot, 400 caractères maximum", "note": "comment l'effectif est établi"},
  {"group": "independence", "locator": "...", "quote": "...", "note": "..."},
  {"group": "leadership", "locator": "...", "quote": "...", "note": "..."}
 ],
 "date_basis": "publication date of 2025 proxy; current board described therein, not a year-end or annual-average measure",
 "board_scope": "incumbent directors; nominee roster reconciled to current membership",
 "checked_at": "2026-11-11", "capture_status": "raw_document_archived", "review_status": "agent_read_pending_audit",
 "selection_note": "(facultatif) pourquoi ce document parmi plusieurs"
}
```

Les trois groupes de preuve sont obligatoires. Les citations doivent être des phrases en prose copiées exactement (éviter de chevaucher plusieurs cellules de tableau). Si l'effectif est déduit (par exemple 12 candidats moins 1 nouveau candidat), l'expliquer dans `note` et citer les deux passages utilisés dans deux entrées de preuve.

## Après la lecture : audit par sondage

Les fragments valides sont fusionnés dans `governance_observations.json` par `src.merge_governance_shards`. Les observations restent marquées `agent_read_pending_audit` jusqu'à un contrôle indépendant par sondage (relecture d'un échantillon par une autre personne ou un autre agent) ; tout écart oblige à relire le fragment concerné. Les résultats ne sont pas présentés comme vérifiés tant que cet audit n'est pas terminé.
