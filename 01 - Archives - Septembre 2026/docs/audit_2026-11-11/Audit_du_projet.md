# Audit du projet S&P 500 avant rédaction finale

**Date : 11 novembre 2026**  
**Cours : Quantitative Data Analysis, M1 S7, EM Normandie**  
**Objet : évaluer les travaux existants, leur conformité au cours et les corrections nécessaires avant le Google Doc et le travail dans Jamovi.**

## 1. Verdict

Le projet couvre les quatre grandes familles d'analyses attendues. Les données, les programmes, les quatre artefacts, les graphiques et une première synthèse finale existent. Plusieurs calculs essentiels sont reproductibles. Il est possible de conserver une grande partie de cette matière.

**Le projet n'est cependant pas prêt à rendre.** Les problèmes prioritaires concernent la traçabilité de certaines données, l'unité d'observation, plusieurs chiffres ou légendes et surtout des interprétations qui dépassent les résultats. La mention « READY FOR OFFICIAL PDF SUBMISSION & ORAL DEFENSE » du rapport actuel n'est pas justifiée par les vérifications réalisées.

| Dimension | État constaté |
|---|---|
| Couverture des méthodes du cours | Les descriptifs, le khi-deux, les corrélations, les ANOVA, les post-hoc et les régressions sont présents |
| Fiabilité des calculs | Nombreux résultats confirmés ; des erreurs et mélanges de modèles restent à corriger |
| Qualité de la base | Structure exploitable ; provenance temporelle et traitement Fiserv à reprendre ; doublons d'entreprises |
| Qualité des conclusions | Révision importante nécessaire, notamment sur la causalité et la robustesse |
| Rapport final | Première version disponible ; informations et tableaux essentiels à compléter |
| Jamovi | Application installée ; aucun fichier .omv trouvé dans le dossier audité |
| Modalités de dépôt | PDF final ; noms et évaluations des membres sur la couverture, selon le message Moodle transmis par David |

Cet audit n'attribue pas de note et ne transforme pas l'état d'avancement en pourcentage arbitraire.

## 2. Périmètre et preuves

L'audit s'appuie sur les quatre supports de cours, les quatre artefacts, le rapport final en Markdown et PDF, les journaux, les guides, le dictionnaire des variables, les programmes d'extraction/nettoyage/analyse et les fichiers de données. Les annales apportent du contexte sur les méthodes ; elles ne remplacent pas les consignes du projet actuel.

Les principaux tests ont été recalculés à partir du CSV préparé. L'ANOVA de Welch a notamment été contrôlée avec une fonction de bibliothèque distincte de celle écrite dans le projet. Les dix vérifications automatiques existantes ont été réexécutées : **10 réussites**. Leur portée est limitée : elles contrôlent surtout la structure et des bornes mathématiques, sans certifier la provenance, le texte des rapports ou l'absence de doublons d'émetteurs.

Les analyses de sensibilité ont été réalisées uniquement en mémoire. Aucun fichier de données, rapport existant, programme du projet ou graphique existant n'a été corrigé pendant cet audit. Seuls ce rapport d'audit et ses tableaux de vérification ont été ajoutés.

**Important : tous les chiffres ci-dessous décrivent le fichier existant avant correction. Ils ne constituent pas les chiffres définitifs du futur rapport.**

Fichier analysé : `data/processed/sp500_esg_cleaned.csv` ; 503 lignes et 17 variables. Empreinte SHA-256 : `41c9be35b02998b2591015aa21245ffd769c294c11f911a96e3ab96db0b5b6e5`.

Les deux CSV préparés sont identiques octet par octet. Le CSV à la racine et l'archive brute sont également identiques. Le classeur comporte les feuilles `Data` et `Codebook_Jamovi`.

## 3. Consignes retenues

David a confirmé que le professeur a validé le choix du jeu de données. L'absence de signature dans la fiche locale n'est donc pas considérée comme un blocage.

Le message Moodle transmis demande un dépôt en **PDF** et des **scores d'évaluation des membres à côté de leurs noms sur la couverture**. L'échéance du **2 décembre 2026** provient de l'indication de David. Le message Moodle copié ne précise ni barème d'évaluation des membres, ni nombre de pages, ni durée ou obligation d'oral. Ces modalités ne sont pas inventées dans cet audit.

Les supports de séance demandent des fichiers .omv pour certains artefacts. La consigne finale communiquée porte sur un PDF : l'absence de .omv est un travail de reproduction et d'apprentissage à effectuer, et ne suffit pas à établir un manquement au format final demandé.

Références du cours :

- [Session 1](<../../../../01 - Cours/S01 - Slides.pdf>), diapositives 9, 24, 28–29, 35 et 37–41 : protocole, normalité, structure du jeu de données, provenance et cinq descriptions univariées.
- [Session 2](<../../../../01 - Cours/S02 - Slides.pdf>), diapositives 21, 28, 31–34 et 40 : conditions du khi-deux, Pearson/Spearman, causalité et contenu de l'artefact 2.
- [Session 3 révisée](<../../../../01 - Cours/S03 - Slides (revised).pdf>), diapositives 15–17, 25 et 44–46 : conditions, choix des post-hoc, taille d'effet et lecture des sorties.
- [Session 4 révisée](<../../../../01 - Cours/S04 - Slides (revised).pdf>), diapositives 15, 23, 25–27 et 32–38 : facteurs, diagnostics, interprétation et plan du rapport final.

## 4. Conformité aux attentes du professeur

| Attente | État du travail existant | Complément ou correction |
|---|---|---|
| Sujet et base validés | Confirmé par David | Conserver cette validation comme contexte |
| Au moins 100 observations | Oui, même après dédoublonnage | Aucun besoin d'agrandir la base |
| Une ligne clairement définie | Déclarée comme une entreprise, mais trois émetteurs ont deux lignes | Retenir une unité cohérente et documenter le choix |
| Variable nominale de 2 à 5 catégories | Oui, cinq secteurs consolidés | Expliquer les regroupements, notamment l'immobilier dans Consumer |
| Au moins une variable ordinale | Oui, quartile de taille et catégorie de risque | Vérifier l'ordre des modalités dans Jamovi |
| Au moins trois variables continues | Oui : marge, chiffre d'affaires, capitalisation, bêta, ROE | Le quota ne dépend pas du traitement du score ISS |
| Source, producteur, année et taille | Partiellement documentés | Distinguer date d'extraction, période comptable, cotation et date du score |
| Journal de nettoyage | Existe | Retirer ou justifier les opérations et diagnostics non démontrés |
| Description de cinq variables | Présente dans l'artefact 1 | Le rapport final n'en synthétise explicitement que trois ; ajouter un tableau de cinq variables et des commentaires |
| Normalité avec plusieurs preuves | Présente, non-normalité confirmée | Distinguer mode exact et mode arrondi ; conserver le graphique, corriger les simplifications |
| Khi-deux, pourcentages en ligne, V de Cramér | Présents | Ajouter la vérification chiffrée des effectifs attendus ; corriger la décision au seuil de 5 % |
| Matrice d'au moins trois variables continues | Heatmap et calculs présents | Ajouter un tableau lisible, préciser les N et la gestion des valeurs manquantes ; inclure Pearson et Spearman |
| Nuage de points du lien discuté | Graphique gouvernance–marge présent | Ajouter celui de gouvernance–bêta si ce résultat devient central ; corriger la légende et les limites d'axe |
| Protocole en quatre étapes | Explicite dans les artefacts | Le réintroduire de façon concise dans les sections du rapport final |
| ANOVA et post-hoc adaptés | Oui, Welch et Games–Howell ; contrôle Kruskal–Wallis | Corriger la justification et distinguer test global, effet et comparaisons |
| Taille d'effet ANOVA | Calculée | Indiquer que l'eta carré présenté vient de la décomposition classique des sommes de carrés |
| Régression simple et multiple | Trois modèles calculés | Corriger N, degrés de liberté et catégorie de référence ; présenter une comparaison des modèles |
| Conditions de la régression | Calculs et graphiques présents | Rapporter les diagnostics du modèle effectivement interprété ; discuter les observations influentes |
| Coefficients B, bêta standardisé, intervalles | Partiellement présents dans l'artefact 4 | Le rapport final doit en montrer un tableau cohérent, avec les N et les catégories de référence |
| Trois recommandations dans un résumé d'une page | Résumé et recommandations présents | Résumé actuel sur plus d'une page ; recommandations trop nombreuses et parfois sans fondement chiffré |
| Limites de l'étude | Section présente | Ajouter les limites concrètes de cette base et les sensibilités observées |
| PDF et couverture demandés par Moodle | PDF disponible, couverture insuffisante | Inscrire les vrais noms et scores ; barème des scores à clarifier |
| Test t | Aucun test t dédié trouvé | Le plan de synthèse S4 le mentionne, mais la liste explicite de l'artefact 2 fourni demande khi-deux et corrélation. Exigence ambiguë : ne pas le déclarer obligatoirement manquant ni fabriquer un découpage sans intérêt métier |

**Conclusion de conformité : les familles de méthodes sont largement couvertes. Le principal manque est la fiabilité et la présentation d'une chaîne complète de preuves, plutôt qu'une accumulation de nouvelles analyses.**

## 5. Données et nettoyage

### A01 — Priorité haute — 503 titres ne sont pas 503 entreprises

Le CSV contient 503 tickers uniques, mais 500 noms d'entreprises distincts. Les couples concernés sont Alphabet (`GOOGL`, `GOOG`), Fox (`FOXA`, `FOX`) et News Corp (`NWSA`, `NWS`). Le test d'unicité des tickers ne détecte pas cette répétition d'émetteurs.

Pour une étude de gouvernance et de rentabilité des entreprises, il faut définir une règle par émetteur et vérifier les catégories d'actions retenues. Un dédoublonnage contrôlé devrait conduire ici à 500 lignes. Il faudra aussi vérifier le sens des capitalisations avant de les agréger : deux valeurs par catégorie d'actions ne se somment pas automatiquement.

Les trois lignes supplémentaires n'ont pas de score global de gouvernance. Elles sont déjà exclues des corrélations et régressions utilisant ce score. Le problème affecte notamment les descriptifs et l'ANOVA sur les marges ; il n'implique pas à lui seul que la régression gouvernance est calculée en comptant deux fois ces trois entreprises.

### A02 — Priorité haute — La correction Fiserv doit être reprise

`src/cleaning.py`, lignes 33–68, remplace `FISV` par `FI` et injecte des chiffres fixes : chiffre d'affaires 19,09 milliards, marge 0,160, bêta 0,880, effectif 42 000 et cinq scores de gouvernance. Aucune pièce justificative de ces valeurs n'est conservée dans le dossier.

L'explication fondée sur le transfert boursier de 2023 est incomplète : Fiserv a annoncé son retour au Nasdaq sous **FISV le 11 novembre 2025**. Cette chronologie est documentée par [Fiserv](https://investors.fiserv.com/news-releases/news-release-details/fiserv-announces-transfer-stock-exchange-listing-nasdaq) et le [formulaire 10-K 2025 déposé à la SEC](https://www.sec.gov/Archives/edgar/data/798354/000079835426000009/fi-20251231.htm). Pour l'extraction décrite comme datant de 2026, la substitution ne peut pas être justifiée uniquement par l'événement de 2023.

Action nécessaire : vérifier la ligne et la période sur une source datée ; remplacer seulement les valeurs démontrées, ou laisser les champs non vérifiés manquants. Une exclusion de cette ligne, testée uniquement pour l'audit, laisse la p-valeur de gouvernance proche de 0,038. Cela montre que ce défaut de provenance ne suffit pas à expliquer le résultat central ; il reste néanmoins à corriger.

### A03 — Priorité haute — FY2025 audité et synchronisé n'est pas démontré

Le programme `extract_sp500_esg.py` lit `stock.info` et des champs tels que `totalRevenue`, `profitMargins` et `marketCap`. Il ne sélectionne pas explicitement l'exercice 2025, ne conserve pas de date de clôture par entreprise et n'archive pas les réponses sources. Il ne télécharge pas directement les états SEC utilisés pour construire chaque ratio.

La documentation de [yfinance get_info](https://ranaroussi.github.io/yfinance/reference/api/yfinance.Ticker.get_info.html) ne fournit d'ailleurs pas de paramètre d'exercice pour cet appel. L'affirmation d'un exercice annuel commun et de scores Q3/Q4 2025 est donc **non établie par le dossier**. Cela ne prouve pas que chaque chiffre est erroné.

Action nécessaire : soit documenter des données annuelles comparables, soit décrire honnêtement un instantané Yahoo Finance avec des périodes potentiellement différentes et une date d'extraction démontrable. Éviter de relancer toute la collecte pendant la rédaction, ce qui changerait la base de comparaison.

### A04 — Priorité haute — Les causes des 32 ROE manquants ne sont pas toutes établies

Le fichier contient bien 32 ROE manquants et 471 valides. En revanche, il ne contient pas les capitaux propres et pièces comptables permettant d'attribuer les 32 absences aux rachats d'actions ou à des capitaux propres négatifs. Fiserv figure parmi les lignes ayant un ROE manquant et plusieurs autres champs absents dans le brut.

Conserver la marge nette comme variable principale est un choix défendable. Il faut remplacer la cause universelle affirmée dans le journal par une explication vérifiée pour certains cas ou par une hypothèse explicitement limitée. La marge nette ne doit pas être décrite comme exempte de toute distorsion comptable.

### A05 — Priorité moyenne — Échelle ISS et classes de risque

ISS décrit le score comme un classement relatif en déciles : 1 correspond à un risque relatif faible et 10 à un risque relatif élevé. Ce n'est pas une mesure continue dont l'égalité des écarts est établie. [Source ISS-Corporate](https://www.iss-corporate.com/resources/blog/governance-qualityscore-as-an-indicator-of-risk-and-investor-sentiment/).

Une analyse numérique peut être présentée comme une approximation de modélisation, accompagnée d'une justification et d'un contrôle par rangs. Pour les associations ordinales, Spearman est particulièrement pertinent. L'ANOVA sur le score doit être interprétée avec prudence et son contrôle Kruskal–Wallis est utile.

Les classes Low 1–3, Medium 4–6, High 7–10 sont une construction du projet. La dernière contient quatre déciles, les autres trois. Présenter 39,7 % dans High comme une découverte surprenante sur la mauvaise gouvernance est excessif ; la largeur inégale des classes contribue directement à cette proportion. Ce sont des catégories relatives, pas des diagnostics de fraude ou de non-conformité.

### A06 — Priorité moyenne — Journal plus affirmatif que les opérations vérifiables

Le journal affirme notamment une vérification des bilans et diverses corrections de format. Le programme de nettoyage réalise surtout la substitution Fiserv et la reconstruction des catégories ordinales ; plusieurs opérations annoncées ne disposent pas d'une trace correspondante. Le regroupement des secteurs est déjà largement réalisé dans l'extraction brute.

Le journal final doit distinguer : anomalies réellement constatées, contrôles sans anomalie, corrections effectivement appliquées, causes vérifiées et hypothèses. Il faut aussi expliquer les regroupements sectoriels et éviter de les qualifier automatiquement d'homogènes.

## 6. Analyses statistiques

### A07 — Descriptifs largement confirmés, modes à corriger

| Variable | N valide | Moyenne vérifiée | Médiane vérifiée | Écart-type vérifié |
|---|---:|---:|---:|---:|
| Marge nette | 503 | 14,7925 % | 13,15 % | 18,5570 points de pourcentage |
| ROE | 471 | 39,5188 % | 16,76 % | 272,3073 points de pourcentage |
| Capitalisation | 503 | 147,5955 milliards USD | 44,467 milliards USD | 490,0121 milliards USD |

La non-normalité de la marge est confirmée : asymétrie −5,4205 ; excès de kurtosis 69,9129 ; Shapiro–Wilk W = 0,6530, p < 0,001.

Le mode exact de la marge est **0,1017**, tandis que **0,11** est le mode après arrondi à deux décimales. Le mode exact du ROE est **0,0798**, et son mode après arrondi est **0,09** ; le 0,12 annoncé dans l'artefact 1 n'est pas reproduit. La capitalisation n'a pas de mode unique dans les observations brutes : quatre valeurs sont ex aequo. Un « cluster modal à 20 milliards » demande une méthode de regroupement explicitée.

Le guide méthodologique affiche aussi des effectifs sectoriels et des coefficients de forme différents de ceux de la base. Il ne peut pas servir de référence numérique unique en l'état.

### A08 — Khi-deux correct, conclusion à réécrire

Résultat confirmé : **χ²(8, N = 496) = 14,7194 ; p = 0,06484 ; V = 0,1218**. Le plus petit effectif attendu est **18,024** : le critère d'effectifs attendus du cours est satisfait.

Au seuil prévu de 5 %, on ne rejette pas l'hypothèse d'indépendance. Les proportions 50,5 % et 29,5 % peuvent être commentées comme descriptives. Elles ne permettent pas d'affirmer une polarisation significative sur la seule base de ce test. Les résidus cités +1,75 et −1,97 ne justifient pas les formulations catégoriques retenues et n'ont pas fait l'objet d'un protocole de comparaisons multiples.

Passer à 10 % après avoir observé p = 0,065 ne doit pas servir à transformer le résultat en succès. Conserver un seuil cohérent et accepter le résultat non significatif.

### A09 — Corrélations principales confirmées, intensité et présentation à revoir

| Paire avec le score global ISS | N | Pearson r | p Pearson | Spearman rho | p Spearman |
|---|---:|---:|---:|---:|---:|
| Marge nette | 496 | −0,04629 | 0,30353 | 0,00765 | 0,86513 |
| Bêta de marché | 494 | 0,26771 | < 0,001 | 0,25240 | < 0,001 |
| Capitalisation | 496 | 0,05585 | 0,21432 | −0,00922 | 0,83768 |

La corrélation gouvernance–bêta est positive et significative, mais **faible selon le repère |r| < 0,3 du cours**. Le bêta mesure la sensibilité au marché ; l'assimiler automatiquement à la volatilité totale, à la volatilité baissière ou à un risque de perte chiffré dépasse l'analyse réalisée.

La heatmap existante supprime les lignes incomplètes sur six variables simultanément : **N = 463**. Le tableau narratif utilise des observations disponibles par paire, avec N = 465, 494 ou 496. Les deux approches sont possibles, mais leur différence doit être expliquée. Le titre annonce des intervalles de confiance alors que la heatmap n'en affiche pas.

Ajouter un tableau complet et les effectifs, plus un nuage de points pour la relation gouvernance–bêta discutée. Les nombreuses corrélations secondaires des sous-scores doivent être signalées comme exploratoires ou faire l'objet d'une stratégie de comparaisons multiples ; elles ne sont pas toutes indispensables au rapport.

### A10 — Comparaison des secteurs bien engagée

Les principaux résultats sont reproduits :

- Marge par secteur : Welch F(4, 191,2098) = **9,30234**, p < 0,001.
- Levene centré sur la médiane : **5,39145**, p = 0,000295.
- Kruskal–Wallis sur la marge : H(4) = **45,98375**, p < 0,001.
- Eta carré descriptif, calculé par les sommes de carrés classiques : **0,04051**, soit environ 4,05 % de variance associée aux secteurs. Ce résultat ne permet pas de dire que les secteurs « dominent » l'explication des marges.
- Scores ISS par secteur : Welch F(4, 207,8417) = **3,96029**, p = 0,00405 ; contrôle Kruskal–Wallis p = 0,00418.

Les Games–Howell sur les marges confirment Finance supérieur à Consumer, Healthcare et Industrials & Energy, et pas de différence établie avec Tech & Comms. Les différences de 9 à 13 **points de pourcentage** doivent être présentées comme des écarts observés, pas comme des objectifs minimaux universels imposés aux entreprises.

Deux compléments sont nécessaires : montrer les distributions dans chaque groupe et les tailles des groupes ; si l'analyse secondaire sur le score ISS reste dans le rapport, ajouter ses post-hoc avant de conclure sur des différences entre deux secteurs nommés. Les tableaux de vérification contiennent ces comparaisons, sans constituer une correction de l'artefact existant.

Welch corrige l'inégalité des variances ; il ne rend pas automatiquement une distribution normale et ne neutralise pas tout effet des valeurs extrêmes. Pour une régression, la normalité s'examine sur les résidus, pas seulement sur la variable Y.

### A11 — Régression principale reproduite, échantillons et références incohérents

| Modèle vérifié | N | R² | R² ajusté | B gouvernance | p gouvernance |
|---|---:|---:|---:|---:|---:|
| Simple, toutes les paires valides | 496 | 0,002143 | 0,000123 | −0,003011 | 0,30353 |
| Simple, échantillon commun aux modèles multiples | 494 | 0,002752 | 0,000725 | −0,003401 | 0,24448 |
| Contrôles de taille et bêta | 494 | 0,123089 | 0,115916 | −0,005159 | 0,07174 |
| Contrôles et secteur | 494 | 0,155925 | 0,142002 | −0,005933 | 0,03744 |

L'artefact 4 donne pour le modèle simple des coefficients calculés sur **494 lignes**, avec un N = 496 et des degrés de liberté correspondant à 496. Le résultat p = 0,244 n'est pas faux en soi : il concerne l'échantillon commun, qui doit être annoncé. Sur 494 lignes, F doit être indiqué avec **(1, 492)**.

Le modèle final utilise **Consumer** comme référence. Le texte annonce pourtant Industrials & Energy, puis le tableau déclare Consumer comme référence et omet le coefficient d'Industrials & Energy (**−0,015282 ; p = 0,4783**). Harmoniser texte, tableau et paramétrage Jamovi.

Le guide méthodologique contient plusieurs autres coefficients et R² qui ne correspondent pas aux modèles reproductibles. Les références croisées à des diapositives 109–137 sont aussi incohérentes avec les supports séparés fournis.

### A12 — Priorité haute — Diagnostics du modèle final mélangés avec ceux du modèle 2

| Diagnostic | Valeur annoncée dans les documents | Modèle final recalculé |
|---|---|---|
| Shapiro–Wilk des résidus | W = 0,771 | **W = 0,50713 ; p < 0,001** |
| Breusch–Pagan | LM = 15,139 ; p = 0,004 | **LM = 17,21927 ; p = 0,02791** |
| VIF maximal | 1,89 | **1,99066** |
| Distance de Cook maximale, guide | 0,082 | **0,47379** |
| p gouvernance avec HC3 | 0,041 | **0,04201**, avec référence t et ddl résiduels |

Les valeurs Breusch–Pagan 15,139 et VIF 1,89 correspondent au **modèle 2**, pas au modèle final. Le graphique à quatre panneaux porte lui-même la mention Model 2. Les deux modèles présentent une hétéroscédasticité détectée et des résidus très éloignés de la normalité.

Le programme de régression existant utilise `.fit()` sans demander de covariance HC3. L'audit confirme indépendamment une p-valeur HC3 proche de 0,042 pour le modèle final, mais cette vérification ne doit pas être attribuée au programme existant. Le seuil de VIF reste satisfaisant ; cela ne garantit ni l'absence de biais, ni la causalité, ni une parfaite stabilité des estimations.

Les écarts-types robustes HC3 traitent l'inférence face à l'hétéroscédasticité. Ils ne corrigent pas automatiquement les observations influentes, une relation mal spécifiée ou les limites de causalité.

### A13 — Priorité haute — La robustesse est suraffirmée

Contrôles de sensibilité, sans modification du CSV et sans décision de suppression :

| Spécification | N | B gouvernance | p classique |
|---|---:|---:|---:|
| Modèle final complet | 494 | −0,005933 | 0,03744 |
| Même modèle sans Moderna, pour sensibilité | 493 | −0,004226 | 0,10063 |
| Même modèle sans Lumentum, pour sensibilité | 493 | −0,004390 | 0,03638 |

Le signe reste négatif, mais le franchissement du seuil de 5 % dépend de certaines observations. Il faut le dire, examiner les entreprises concernées et conserver les observations authentiques dans le modèle principal sauf justification documentée. Il ne faut pas choisir les exclusions pour obtenir une p-valeur souhaitée.

Le passage d'une corrélation non significative à un coefficient ajusté significatif n'établit pas à lui seul un « paradoxe de Simpson résolu », ni l'absence de biais de variables omises.

## 7. Interprétation et portée managériale

### A14 — Priorité haute — Association, causalité et recommandations

La conclusion « améliorer la gouvernance rapporte 0,59 point de marge » transforme une association entre entreprises en effet d'une intervention. Les données transversales ne démontrent pas cet effet. Une formulation défendable serait : **dans le modèle ajusté actuel, un score ISS supérieur d'un décile est associé à une marge nette inférieure d'environ 0,59 point, avec des limites importantes de robustesse et de mesure.**

La différence calculée entre scores 10 et 1 n'est donc pas un gain garanti pour une entreprise qui changerait ses pratiques. Les mots « definitive », « decisively », « zero bias » et les promesses de performance doivent être remplacés par des conclusions proportionnées.

Le rapport recommande notamment une décote de 15 % sur les actifs risqués, une réallocation sectorielle et des réformes précises de rémunération ou de droits de vote. Ces seuils et effets ne sont pas estimés dans l'étude. Une corrélation de 0,268 n'est pas un coefficient permettant de calibrer directement une règle de portefeuille ou une variation du bêta par point de score.

Recommandations admissibles à construire : utiliser des repères de rentabilité par secteur ; intégrer le score de gouvernance à un examen complémentaire du risque sans en faire un signal autonome ; vérifier les cas atypiques et tester les hypothèses sur des données mieux datées avant une décision d'allocation.

### A15 — Problématique trop large par rapport aux résultats

Le projet mesure surtout la **gouvernance**, pas les dimensions environnementale et sociale. La capitalisation n'est pas un multiple de valorisation et ne suffit pas à établir une « prime de valorisation ». Le bêta n'est pas une mesure générale de résilience. Les textes doivent adopter une question commune, par exemple :

> Dans quelle mesure le risque relatif de gouvernance est-il associé à la marge nette et à la sensibilité au marché des entreprises du S&P 500, compte tenu de leur taille et de leur secteur ?

Cette formulation est une proposition à utiliser après vérification de la base, sans faire dépendre la question d'un résultat significatif.

## 8. Graphiques et rapport final

### A16 — Priorité haute — Figures susceptibles de donner une impression erronée

1. **Nuage gouvernance–marge** : la droite dessinée est une régression simple, mais sa légende lui attribue le coefficient ajusté du modèle multiple. Séparer les deux présentations. L'axe s'arrête à −0,5 alors que Lumentum est à −2,301 et Moderna à −1,4143 : ces deux points sont invisibles, sans indication de zoom.
2. **Boxplots sectoriels** : l'axe s'arrête à −0,4 et masque également ces deux observations. Prévoir une vue complète ou un zoom explicitement annoncé, avec les extrêmes documentés.
3. **Diagnostics** : le graphique présenté pour soutenir la régression finale porte sur le modèle 2. Refaire le graphique pour le modèle retenu et commenter ce qu'il montre réellement.
4. **Graphique des sous-piliers** : le nom et la légende parlent d'un radar par niveau de performance ; l'image est un diagramme en barres par secteur. Corriger le descriptif ou retirer cette figure secondaire.
5. **Heatmap** : préciser le N, le traitement des données manquantes et l'absence d'IC dans l'image. Une heatmap ne remplace pas les deux matrices Pearson/Spearman demandées et leurs interprétations.
6. **Unités** : employer « points de pourcentage » pour un écart de marge et « marge nette » au lieu de « marge opérationnelle ». Le même indicateur change actuellement d'appellation selon les passages.

### A17 — Priorité moyenne — PDF existant et contenu final

Le PDF final de huit pages a été examiné visuellement. Les améliorations utiles sont :

- Une couverture avec les noms réels et les évaluations demandées par Moodle, en remplaçant les appellations fictives d'équipe de conseil.
- Un résumé exécutif tenant sur une page et limité à trois recommandations défendables.
- Un tableau descriptif de cinq variables et un tableau clair des données manquantes.
- Un khi-deux avec sa vérification d'effectifs attendus ; des matrices et nuages de points lisibles.
- Un tableau comparatif de régression, des intervalles de confiance et les diagnostics du modèle correct.
- Des limites spécifiques à cette étude : datation, données agrégées, score relatif, émetteurs multiples, sensibilité, sélection du S&P 500 et causalité non établie.
- Une bibliographie et des sources datées ; des légendes qui correspondent exactement aux images.
- Des tableaux moins serrés et un meilleur maintien des titres avec leur contenu. Le titre du tableau d'actions termine actuellement une page et le tableau apparaît sur la suivante.
- Le retrait du bloc d'auto-certification de fin et de la référence à une soutenance orale qui n'est pas confirmée par les consignes communiquées.

Le rapport final ne doit pas supposer que le correcteur consultera tous les artefacts séparés pour retrouver une preuve essentielle. Les détails volumineux peuvent aller en annexe, en restant dans le PDF si c'est le seul fichier déposé.

## 9. Préparation du travail dans Jamovi

Jamovi **2.7.38.0** est installé. Les données Excel/CSV peuvent servir de point de départ après correction et choix de la version définitive. Les guides existants sont une base pédagogique, mais certaines options y sont promises à tort.

L'inspection des options du module `jmv` installé montre que **Breusch–Pagan et HC3 ne sont pas des cases disponibles dans sa régression linéaire standard**. La procédure proposée dans l'artefact 4 doit donc être adaptée. Il faudra présenter ces vérifications comme analyses complémentaires ou choisir et expliquer une extension compatible, seulement si nécessaire.

Ordre de reproduction conseillé :

1. Ouvrir la base finale et configurer les identifiants, secteurs, catégories ordinales et variables numériques. Indiquer que Headcount est un dénombrement, même si l'interface emploie le type Continuous pour l'analyse numérique.
2. Décrire cinq variables avec N valide et données manquantes ; faire les graphiques et la normalité.
3. Faire le khi-deux, les tableaux observés/attendus et les pourcentages en ligne.
4. Produire Pearson et Spearman avec une stratégie de valeurs manquantes annoncée et les nuages de points nécessaires.
5. Faire l'ANOVA de Welch et les Games–Howell, puis le contrôle non paramétrique utile. Calculer l'eta carré dans le module adapté, conformément au support S3.
6. Créer les logarithmes, fixer la catégorie de référence et estimer les modèles sur un échantillon clairement défini. Examiner résidus et influence.
7. Sauvegarder le .omv et exporter les tableaux/figures retenus pour le rapport.

À chaque étape, l'objectif sera de comprendre la question, les réglages, les conditions, les résultats et leur traduction en anglais. Il n'est pas nécessaire d'ajouter des méthodes avancées comme un panel dynamique pour satisfaire le cours.

## 10. Ordre de travail avant le Google Doc

| Priorité | Travail | Critère d'achèvement |
|---|---|---|
| 1 | Stabiliser l'unité d'observation, la datation et la ligne Fiserv | Base documentée, valeurs non justifiées retirées ou sourcées, règle par entreprise explicitée |
| 2 | Recalculer et figer les résultats | Un tableau de référence avec les mêmes chiffres, N et modèles dans tous les documents |
| 3 | Corriger les décisions et les limites | Khi-deux correctement non significatif à 5 %, corrélation faible, sensibilité de la régression reconnue |
| 4 | Compléter les sorties réellement utiles | Cinq descriptifs, effectifs attendus, matrices, post-hoc, régressions et diagnostics cohérents |
| 5 | Reproduire les analyses dans Jamovi avec David | Fichier .omv enregistré, résultats compris et graphiques exploitables |
| 6 | Rédiger dans Google Docs et exporter le PDF | Couverture conforme, résumé d'une page, trois recommandations, tableaux lisibles et sources complètes |

Le Google Doc peut être structuré avant la fin du travail dans Jamovi, mais les chiffres et images du PDF ne doivent être figés qu'après stabilisation des données et des analyses.

## 11. Ce qui peut être conservé

La structure en quatre séances, la question générale de gouvernance, le choix de la marge comme variable principale, l'usage complémentaire de médianes et d'IQR, la comparaison Pearson/Spearman, le choix Welch/Games–Howell face aux variances inégales et la progression des modèles de régression sont des bases utiles.

La forme des conclusions doit évoluer : le résultat non significatif du khi-deux est une information valable, l'association gouvernance–bêta est faible mais détectable, et l'association ajustée gouvernance–marge est une piste limitée par la robustesse. Un rapport qui expose ces nuances répond mieux aux attentes de lecture critique du professeur qu'une démonstration présentée comme définitive.

## 12. Pièces de vérification

Les tableaux du sous-dossier [verifications](verifications/) documentent les calculs de l'audit :

- [Résultats vérifiés](verifications/verified_results.csv), incluant descriptifs, effectifs, corrélations, ANOVA, régressions, diagnostics et sensibilités.
- [Matrice Pearson](verifications/pearson_matrix.csv) et [matrice Spearman](verifications/spearman_matrix.csv), avec observations disponibles par paire.
- [Effectifs observés du khi-deux](verifications/contingency_observed.csv) et [effectifs attendus](verifications/contingency_expected.csv).
- Descriptifs de groupes, Games–Howell, coefficients de chaque modèle et dix observations ayant les distances de Cook les plus élevées.

Les calculs de référence utilisent pandas 2.3.3, SciPy 1.13.1 et statsmodels 0.14.6. Les p-valeurs HC3 indiquées utilisent une référence t aux degrés de liberté résiduels. L'audit établit une reproductibilité sur le CSV fourni, pas une certification indépendante de chaque observation de marché.
