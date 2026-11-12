# Consignes et supports du professeur — texte intégral

Mise à disposition : **11 novembre 2026**. Les formulations originales anglaises sont conservées. **Toutes les pages des quatre supports sont incluses ci-dessous : 175 pages, sans sélection ni réduction du contenu textuel.** Les cas, exemples, consignes de laboratoire et indications de rendu restent dans leur contexte.

Les quatre PDF originaux sont également copiés dans le dépôt. Ils font foi pour les schémas, figures, tableaux et formules mis en page : la transcription textuelle ne remplace pas leur présentation visuelle. Chaque page ci-dessous possède un lien vers sa page PDF. Les blocs de texte préservent le texte extrait sans le transformer en règles nouvelles.

Les instructions propres au groupe et son ordre de travail sont séparés dans [DECISIONS.md](DECISIONS.md) et [le plan](../tasks/plan.md). Ils ne doivent pas être attribués au professeur.

## Documents originaux complets

| Support | Pages | Original inclus |
|---|---:|---|
| S01 | 44 | [PDF complet](<sources/cours/S01 - Slides.pdf>) |
| S02 | 43 | [PDF complet](<sources/cours/S02 - Slides.pdf>) |
| S03 | 48 | [PDF complet](<sources/cours/S03 - Slides (revised).pdf>) |
| S04 | 40 | [PDF complet](<sources/cours/S04 - Slides (revised).pdf>) |

Les empreintes et emplacements d’origine sont dans [sources_manifest.json](sources/cours/sources_manifest.json). La couverture de la transcription et les empreintes du texte de chaque page sont dans [transcription_manifest.json](sources/cours/transcription_manifest.json).

## Accès direct aux pages de prescriptions

Cet index sert à naviguer ; il ne remplace pas les textes intégraux reproduits ensuite.

- Session 1 : [protocole, p.9](#s01-p009), [normalité, p.24](#s01-p024), [barème général, p.28](#s01-p028), [spécification des données, p.29](#s01-p029), [fiche, p.35](#s01-p035), [variables/nettoyage/laboratoire, p.38–40](#s01-p038), [artefact 1, p.41](#s01-p041), [préparation suivante, p.43](#s01-p043).
- Session 2 : [protocole, p.10](#s02-p010), [conditions du khi-deux, p.21](#s02-p021), [corrélations, p.31–33](#s02-p031), [laboratoire/application/artefact 2, p.37–40](#s02-p037), [préparation suivante, p.42](#s02-p042).
- Session 3 : [t-test et ANOVA, p.7](#s03-p007), [conditions et choix des méthodes, p.15–17](#s03-p015), [taille d’effet, p.22](#s03-p022), [post-hoc, p.25](#s03-p025), [laboratoire/application, p.44–45](#s03-p044), [préparation régression, p.47](#s03-p047).
- Session 4 : [diagnostics, p.25–27](#s04-p025), [laboratoire/application, p.32–33](#s04-p032), [table de révision, p.36](#s04-p036), [rapport final, p.37](#s04-p037), [échéance renvoyée à la page du cours, p.40](#s04-p040).

## Complément Moodle — texte transmis par David

Ce texte a été fourni dans le chat par David ; il n’a pas été récupéré à nouveau sur Moodle :

> Dear everyone, Please submit your final project here. When you submit, please remember that you submit in pdf format. One more thing, you need to evaluate your group members by giving them scores, and you place them next to their names on the cover of the submission. Best regards, Tuan.

## Informations communiquées par David, distinctes des slides

- Échéance indiquée : **2 décembre 2026**.
- Équipe : **David Wanono, Olyvan Perrin, Guillaume Da Cruz**.
- Le choix du jeu de données S&P 500 a été validé par le professeur selon David.
- Le complément Moodle transmis ne précise pas le barème d’évaluation des membres, une longueur totale du rapport ou un oral. Ne pas inventer ces modalités.

---

## S01 — support complet (44 pages)

[Ouvrir le PDF original complet](<sources/cours/S01 - Slides.pdf>)

<a id="s01-p001"></a>
### S01 — page 1

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=1>)

```text
Quantitative Data Analysis
Session 1 — Finding Data & Univariate Analysis
NGUYEN Anh-Tuan
EM Normandie — Programme Grande École
Course code 2627_ECO_2_EN_009 · 2026–2027
```

<a id="s01-p002"></a>
### S01 — page 2

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=2>)

```text
Your lecturer
NGUYEN Anh-Tuan
PhD completed in 2025,
Université Paris Nanterre
Lecturer, Sciences Po Paris — Le Havre
campus
Teaching Quantitative Data Analysis
at EM Normandie
How I want to work with you
I will not ask you to memorise formu-
las.
I will ask you to find real data , anal-
yse it, and defend your conclusions
to a manager.
That is the entire course.
AQD – Session 1 NGUYEN Anh-Tuan 2
```

<a id="s01-p003"></a>
### S01 — page 3

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=3>)

```text
The course in one slide
Session Method Question it answers
1
today
Univariate descriptive analysis What does my data look like?
2 Chi-square & Pearson correlation Are two variables related?
3 ANOVA + post-hoc tests Do groups differ from each other?
4 Simple & multiple regression What drives my outcome?
14 hours face-to-face · 36 hours independent work · 5 ECTS
Software: Jamovi (free). One dataset — yours — carried through all four sessions.
AQD – Session 1 NGUYEN Anh-Tuan 3
```

<a id="s01-p004"></a>
### S01 — page 4

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=4>)

```text
What you must be able to do by session 4
1. Identify and justify the appropriate statistical method for a given managerial problem
2. Implement it in data analysis software
3. Interpret the statistical output accurately
4. Draw conclusions and formulate actionable managerial recommendations
Notice what is not on this list: calculating anything by hand.
The software computes. You decide, interpret, and recommend.
AQD – Session 1 NGUYEN Anh-Tuan 4
```

<a id="s01-p005"></a>
### S01 — page 5

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=5>)

```text
Today: 3 hours 30
Time What happens Mode
0:00 – 0:15 Introduction, course contract Lecture
0:15 – 1:30 Theory: variables, descriptive statistics, distribu-
tions
Lecture + quiz
1:30 – 1:45 Break
1:45 – 2:45 Data hunt: find your own dataset Teams of 3
2:45 – 3:15 Jamovi lab: build and describe your database Hands-on
3:15 – 3:30 Approval gate + submission of Artefact 1 Checkpoint
You do not leave this room without an approved dataset.It is the foundation of every session that
follows, and of your coursework mark.
AQD – Session 1 NGUYEN Anh-Tuan 5
```

<a id="s01-p006"></a>
### S01 — page 6

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=6>)

```text
Why this matters
```

<a id="s01-p007"></a>
### S01 — page 7

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=7>)

```text
From data to decision
Managerial
question
Data
collection
Database
construction
Statistical
analysis Interpretation Decision
Sessions 1–4 live in the middle of this chain. But you are graded on both ends: the ques-
tion you ask, and the decision you recom-
mend.
AQD – Session 1 NGUYEN Anh-Tuan 7
```

<a id="s01-p008"></a>
### S01 — page 8

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=8>)

```text
Why managers need this
Without data
“I think our customers prefer. . . ”
“It seems sales are up”
“Everyone knows that segment is loyal”
With data
“56% of our buyers choose the regional
brand”
“Spending rises 12 e per additional visit”
“Retirees score 15.6/20 on loyalty; students
4.8”
The second column wins budget arguments. The first does not.
That is the whole professional case for this course.
AQD – Session 1 NGUYEN Anh-Tuan 8
```

<a id="s01-p009"></a>
### S01 — page 9

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=9>)

```text
The protocol — your answer template all term
1. IDENTIFY — Which test? Justify from the nature of the variables.
2. HYPOTHESISE — State H0 and H1 in business language.
3. DECIDE — Is p < 0.05? Then: how strong is the effect?
4. RECOMMEND — What does the manager do on Monday morning?
Students lose marks at steps 1 and 4. Almost never at step 3.
Computing is easy. Choosing and concluding are the skill.
AQD – Session 1 NGUYEN Anh-Tuan 9
```

<a id="s01-p010"></a>
### S01 — page 10

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=10>)

```text
Variables: the foundation
```

<a id="s01-p011"></a>
### S01 — page 11

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=11>)

```text
First: what is one row of your data?
One row = one
This is called the unit of observation. If you cannot finish that sentence, you do not understand
your dataset yet.
Examples
one row = one customer
one row = one firm
one row = one firm-year
one row = one country
one row = one transaction
Vocabulary
Observation (row) — one individual case
Variable (column) — one measured
characteristic
N — number of observations
AQD – Session 1 NGUYEN Anh-Tuan 11
```

<a id="s01-p012"></a>
### S01 — page 12

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=12>)

```text
The variable taxonomy
VARIABLE
Qualitative
(categorical)
Quantitative
(numerical)
Nominal Ordinal Discrete Continuous
no order
sector, region
ordered
rating, size band
countable
no. of employees
measurable
turnover, ROI
This single diagram decides every test you will use in sessions 2, 3 and 4.
AQD – Session 1 NGUYEN Anh-Tuan 12
```

<a id="s01-p013"></a>
### S01 — page 13

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=13>)

```text
Qualitative variables
Nominal
Names or labels. No natural order.
Examples:
Industry sector
Country of listing
Brand purchased
Legal form (SA, SARL, SAS)
Y ou may count them. Y ou maynot average them.
Ordinal
Ordered categories, but unequal gaps.
Examples:
Credit rating (AAA, AA, A. . . )
Satisfaction 1–5 stars
ESG grade (A+ to D–)
Firm size band
AA to A is not the same “distance” as B to C.
AQD – Session 1 NGUYEN Anh-Tuan 13
```

<a id="s01-p014"></a>
### S01 — page 14

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=14>)

```text
Quantitative variables
Discrete
Countable values, usually integers.
Examples:
Number of employees
Number of stores
Monthly visits
Number of board members
Continuous
Any value within a range.
Examples:
Turnover (e)
ROI (%)
Share price
CO2 emissions per unit
Interval vs ratio. Temperature in ◦C is interval: 20 ◦ is not “twice” 10 ◦, because zero is arbitrary.
Turnover is ratio: zero means none, and 2Me really is twice 1Me.
Correlation and regression need interval or ratio data.
AQD – Session 1 NGUYEN Anh-Tuan 14
```

<a id="s01-p015"></a>
### S01 — page 15

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=15>)

```text
Quiz — name the variable type
1. Customer satisfaction, 1–5 stars
2. Number of stores in a region
3. Postcode (75008, 76600)
4. Time spent on a website, in seconds
5. Moody’s credit rating
6. Temperature in ◦C
7. Annual turnover in e
8. Loyalty score, 0–20
T ake 3 minutes. Discuss with your neighbour.
AQD – Session 1 NGUYEN Anh-Tuan 15
```

<a id="s01-p016"></a>
### S01 — page 16

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=16>)

```text
Quiz — answers
Variable Type Why / trap
Satisfaction 1–5 stars Ordinal The classic trap. Gaps between stars are not equal.
Number of stores Discrete quant. Countable, integer.
Postcode Nominal Digits, but not a number. Never average a post-code.
Time on site (seconds) Continuous quant. Ratio scale, true zero.
Moody’s rating Ordinal Ordered, unequal gaps.
Temperature ◦C Continuous ( interval) Arbitrary zero: no ratios.
Annual turnover Continuous ( ratio) True zero.
Loyalty score 0–20 Debatable Ordinal in principle, treated as continuous in prac-tice.
The last one matters: composite scores are conventionally treated as continuous. That is exactly why we can run an ANOVA on a
loyalty score in session 3.
AQD – Session 1 NGUYEN Anh-Tuan 16
```

<a id="s01-p017"></a>
### S01 — page 17

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=17>)

```text
Why the typology decides everything
Variable X Variable Y Test Session
Qualitative Qualitative Chi-square ( χ2) + Cramér’s
V
2
Quantitative Quantitative Pearson correlation ( r) 2
Qualitative (3+ groups) Quantitative ANOVA + post-hoc 3
Several quantitative Quantitative Multiple regression 4
Read this table again. Choosing the right test is not a matter of taste or memory — it ismechanically
determined by the nature of your variables.
This is why the dataset you find today must contain the right types of variables.
AQD – Session 1 NGUYEN Anh-Tuan 17
```

<a id="s01-p018"></a>
### S01 — page 18

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=18>)

```text
Describing one variable
```

<a id="s01-p019"></a>
### S01 — page 19

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=19>)

```text
What “univariate” means
Univariate analysis = describing one variable at a time.
No relationships, no causes, no predictions — yet.
Qualitative variable Quantitative variable Both
Frequency table
Percentages
Mode
Bar chart / pie chart
Mean, median, mode
Standard deviation
Min–max, quartiles
Skewness, kurtosis
Histogram, boxplot
Count of valid cases
Missing values
The most common error in this course: computing a mean for a qualitative variable.
“Average gender = 1.79” is meaningless.
AQD – Session 1 NGUYEN Anh-Tuan 19
```

<a id="s01-p020"></a>
### S01 — page 20

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=20>)

```text
Frequency tables and the mode
Example: brand purchased (N = 325)
Category Frequency %
National brand 142 43.7
Regional brand “Grain d’Or” 183 56.3
Total 325 100
Mode
The most frequent category or value.
Here: Regional brand, with 183 obser-
vations (56.3%).
The mode is the only measure of central tendency valid for nominal data.
Y ou cannot compute a mean or a median of “sector” — but you can say which sector is most common.
AQD – Session 1 NGUYEN Anh-Tuan 20
```

<a id="s01-p021"></a>
### S01 — page 21

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=21>)

```text
Central tendency: three different answers
Mean
Arithmetic average.
+ Uses all the data
+ Mathematically tractable
– Destroyed by outliers
– Misleading if skewed
Median
Middle value.
+ Robust to outliers
+ Works on ordinal data
– Ignores magnitudes
– Less convenient in models
Mode
Most frequent value.
+ Only option for nominal
+ Identifies the typical case
– May not be unique
– Ignores the rest
Exam question: “What are the main advantages and disadvantages of the mean, and which statistic
avoids these disadvantages?”
Answer: the median (robust to outliers and skew). Confirm the shape with a normality test —
Shapiro–Wilk or Kolmogorov–Smirnov.
AQD – Session 1 NGUYEN Anh-Tuan 21
```

<a id="s01-p022"></a>
### S01 — page 22

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=22>)

```text
Dispersion: the number managers forget
Two shops. Both average 50 e per basket.
Shop A Shop B
Mean 50 e 50 e
Std. deviation 4 e 35 e
The same mean. Completely different businesses.
Standard deviation = the typical distance of
an observation from the mean.
Small SD → homogeneous customers. One
offer works for everyone.
Large SD → heterogeneous market. Y ou
must segment or you will satisfy nobody.
The mean tells you where the market is. The standard deviation tells you whether the mean means
anything at all.
AQD – Session 1 NGUYEN Anh-Tuan 22
```

<a id="s01-p023"></a>
### S01 — page 23

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=23>)

```text
The shape of a distribution
Symmetric (normal) Positively skewed
Symmetric
mean ≈ median ≈ mode
skewness ≈ 0
Skewed right (typical of income, turnover)
mean > median > mode
skewness > 0 — a few large values pull the mean up
Skewness = asymmetry. Kurtosis = how heavy the tails are.
Rule of thumb: both between −1 and +1 is consistent with normality.
AQD – Session 1 NGUYEN Anh-Tuan 23
```

<a id="s01-p024"></a>
### S01 — page 24

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=24>)

```text
Is my variable normally distributed?
Three converging pieces of evidence — use all three, never just one:
1. Compare the three centres.
If mean ≈ median ≈ mode, the distribution is roughly symmetric. Large divergence signals skew.
2. Check skewness and kurtosis.
Both roughly within ±1.
3. Look at the histogram.
Does it actually look bell-shaped? Y our eyes are a legitimate instrument.
Formal test: Shapiro–Wilk. Here H0 = “the data are normal”.
So p > 0.05 means you keep normality — the opposite logic to every other test in this course. Be
careful.
AQD – Session 1 NGUYEN Anh-Tuan 24
```

<a id="s01-p025"></a>
### S01 — page 25

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=25>)

```text
Read output critically — a real example
Variable N Mean Median Mode Std. dev. Min–Max
Age 325 41.2 41 41.3 10.5 18–70
Monthly spending (e) 325 56.7 50 70 3.3 10–110
Two things are wrong here.
Can you spot them before I tell you?
Mode of age = 41.3 — age is recorded in
whole years. A mode cannot be fractional.
SD of spending = 3.3 — with a range of 10–
110 e? Impossible.
Software never refuses to print a number. Sanity-checking output is your job.
AQD – Session 1 NGUYEN Anh-Tuan 25
```

<a id="s01-p026"></a>
### S01 — page 26

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=26>)

```text
The limit of univariate analysis
Knowing that average spending is 56.70 e tells you
nothing about who spends it, or why.
Univariate analysis describes variables in isolation. It cannot:
establish a relationship between two variables
compare groups
identify what drives an outcome
support any prediction
That is why we need sessions 2, 3 and 4.
And it is the answer to the exam question “why are univariate analyses insufficient?”
AQD – Session 1 NGUYEN Anh-Tuan 26
```

<a id="s01-p027"></a>
### S01 — page 27

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=27>)

```text
Finding your own data
```

<a id="s01-p028"></a>
### S01 — page 28

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=28>)

```text
The “fil rouge” project
You find one real dataset today. Y ou analyse it for four weeks.
It becomes a consulting report — and your coursework mark.
Artefact Content Marks
1 (today) Clean database + univariate description 20
2 Chi-square + correlation 25
3 ANOVA + post-hoc 20
4 Regression + consolidated recommendations 25
Provenance Source quality, assessed today 10
Choose a topic you can stand to look at for four weeks.
Sustainability, CSR, green business and retail are especially welcome — they are part of the course
design.
AQD – Session 1 NGUYEN Anh-Tuan 28
```

<a id="s01-p029"></a>
### S01 — page 29

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=29>)

```text
Dataset specification — all boxes must be ticked
□ ≥ 100 observations (rows)
□ ≥ 1 nominal variable with 2–5 categories
your grouping variable for sessions 2 and 3 — without it those labs are impossible
□ ≥ 1 ordinal variable
□ ≥ 3 continuous variables
your correlation and regression material for sessions 2 and 4
□ One row = one — answerable in one sentence
□ A real downloadable file (.csv or .xlsx) — not a screenshot, not a chart
□ Provenance: URL, producer, year, sample size
Banned: Titanic, Iris, Boston Housing, anything labelled “cleaned” or “for beginners”.
Pre-processed data teaches you nothing.
AQD – Session 1 NGUYEN Anh-Tuan 29
```

<a id="s01-p030"></a>
### S01 — page 30

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=30>)

```text
Where to find financial data — the map
Company-level
accounts, ra-
tios, ESG scores
Market data
prices, returns, indices
Macro & sector
GDP , inflation, rates
ESG & CSR
emissions, ratings, reports
For this course, company-level data is the richest choice. One row = one firm (or one firm-year),
with sector as your nominal variable and turnover, ROI, headcount and emissions as your continuous
variables.
That structure supports all four sessions.
AQD – Session 1 NGUYEN Anh-Tuan 30
```

<a id="s01-p031"></a>
### S01 — page 31

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=31>)

```text
Company & financial data — where to actually go
Source What you get Access
Diane French company accounts: turnover, net
profit, headcount, ratios EM Normandie library
Orbis (BvD) Same, worldwide, 400M+ companies
EM Normandie library
Infogreffe / Pappers French company filings, free tier pappers.fr
SEC EDGAR US-listed filings (10-K, financials), free sec.gov/edgar
Yahoo Finance Prices, key ratios, some ESG; easy CSV ex-
port
finance.yahoo.com
Euronext Listed companies
Paris/Amsterdam/Brussels
live.euronext.com
LSEG / Bloomberg Professional terminals, everything If your campus has a terminal
Start with Diane or Orbis. Ask the Learning Centre for access. Y ou can export a sector, a size band and a year
directly to Excel — that is a ready-made dataset of several hundred firms.
AQD – Session 1 NGUYEN Anh-Tuan 31
```

<a id="s01-p032"></a>
### S01 — page 32

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=32>)

```text
Macro, sector and open data
Source What you get Access
INSEE French demographics, household spending,
firm demography
insee.fr
data.gouv.fr French open data, all ministries — large and
realistically messy
data.gouv.fr
Eurostat EU-comparable statistics, excellent docu-
mentation
ec.europa.eu/eurostat
Banque de France Webstat: rates, credit, business surveys webstat.banque-france.fr
ECB Data Portal Euro area monetary & financial statistics data.ecb.europa.eu
World Bank Country indicators, 1960–present data.worldbank.org
OECD Data Explorer Cross-country economic and social data data-explorer.oecd.org
IMF Balance of payments, fiscal, financial sound-
ness
data.imf.org
Careful: macro data often gives you one row = one country-year. With 27 EU countries you have few rows.
Combine several years, or go to firm level.
AQD – Session 1 NGUYEN Anh-Tuan 32
```

<a id="s01-p033"></a>
### S01 — page 33

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=33>)

```text
ESG, CSR and sustainability data
Source What you get Access
CDP Corporate climate, water & forest disclosures cdp.net
ADEME French emissions factors, Bilan GES of or-
ganisations
bilans-ges.ademe.fr
Our World in Data Emissions, energy, food systems; clean CSV
export
ourworldindata.org
EU ETS registry Verified emissions per installation, per year climate.ec.europa.eu
Yahoo Finance Sustainability tab: ESG risk scores by firm finance.yahoo.com
CSRD reports Since 2024, large EU firms publish standard-
ised sustainability data
Company websites
A strong project shape: one row = one listed firm.
Nominal: sector. Ordinal: ESG grade. Continuous: turnover, ROI, emissions per employee.
Question: do greener firms perform better financially? That carries all four sessions.
AQD – Session 1 NGUYEN Anh-Tuan 33
```

<a id="s01-p034"></a>
### S01 — page 34

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=34>)

```text
General repositories — and how to judge a source
Repositories
Google Dataset Search
datasetsearch.research.google.com
Kaggle Datasets
but avoid the “beginner” sets
UCI ML Repository
Harvard Dataverse
replication data from published research
Zenodo
Before you download, ask:
1. Who produced it? Statistical office, regulator, com-
pany, anonymous user?
2. When was it collected? Not published — collected.
3. How was it collected? Survey, administrative
record, scraping?
4. Is there a codebook explaining what each column
means?
5. What is missing, and why?
“Garbage in, garbage out. ” No statistical method can rescue a bad dataset.
Ten minutes spent judging the source saves four weeks of wasted work.
AQD – Session 1 NGUYEN Anh-Tuan 34
```

<a id="s01-p035"></a>
### S01 — page 35

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=35>)

```text
Approval slip — complete before you leave
Team members
Dataset title
Source URL
Producer & year
One row = one. . .
N (rows)
Nominal variable (2–5 categories)
Ordinal variable
Continuous variables (≥ 3)
Managerial question
Lecturer signature
No signature ⇒ you receive the backup dataset and forfeit the 10 provenance marks.
AQD – Session 1 NGUYEN Anh-Tuan 35
```

<a id="s01-p036"></a>
### S01 — page 36

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=36>)

```text
Jamovi lab
```

<a id="s01-p037"></a>
### S01 — page 37

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=37>)

```text
Jamovi in five minutes
Why Jamovi
Free and open source — jamovi.org
Installs in five minutes, Mac & Windows
Output tables look like SPSS, so everything
transfers
Results update live as you change the data
Two tabs matter
Data — your spreadsheet and variable
settings
Analyses — every test in this course
Import your file
≡ menu → Open → Browse → your .csv or .xlsx
Save your work
≡ menu → Save As → .omv
The .omv file stores data and analyses together.
That is what you submit.
AQD – Session 1 NGUYEN Anh-Tuan 37
```

<a id="s01-p038"></a>
### S01 — page 38

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=38>)

```text
Setting up your variables — do not skip this
Double-click any column header in the Data tab:
1. Name — short, no spaces, no accents
2. Description — what it actually measures, and in which units
3. Measure type — the critical setting:
Nominal — categories, no order
Ordinal — ordered categories
Continuous — numeric measurements
ID — identifiers, never analysed
4. Levels — rename and reorder categories here
If the measure type is wrong, Jamovi will silently refuse to offer you the right test in week 2.
This is the number one cause of a lost lab session.
AQD – Session 1 NGUYEN Anh-Tuan 38
```

<a id="s01-p039"></a>
### S01 — page 39

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=39>)

```text
Cleaning: what to hunt for
Missing values in disguise
99, −1, 9999, “N/A”, empty strings
Duplicate rows
the same firm listed twice
Impossible values
age 150, negative turnover, ROI of 4000%
Inconsistent categories
“Paris” / “paris” / “PARIS” / “Paris ”
Wrong decimal separator
French data uses commas: 56,7 not 56.7
Numbers stored as text
Jamovi will treat them as nominal
Keep a cleaning log. What you found, what you did, why.
This is graded — and in professional practice it is what makes your analysis defensible.
AQD – Session 1 NGUYEN Anh-Tuan 39
```

<a id="s01-p040"></a>
### S01 — page 40

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=40>)

```text
Running your univariate analysis
Analyses → Exploration → Descriptives
For qualitative variables
Tick Frequency tables
Read counts and percentages
Identify the mode
Plots: Bar plot
For quantitative variables
Statistics: mean, median, mode, SD, min, max
Tick skewness and kurtosis
Plots: Histogram + Box plot
Split by a grouping variable if useful
Then write it up in the protocol format. Not “the mean is 56.7”, but
“spending is right-skewed, so the median of 50 e better represents the typical customer; the high SD
suggests two distinct segments. ”
AQD – Session 1 NGUYEN Anh-Tuan 40
```

<a id="s01-p041"></a>
### S01 — page 41

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=41>)

```text
Artefact 1 — submit before you leave (20 marks)
1. The cleaned .omv file
2. The completed approval slip (provenance)
3. A cleaning log: what was wrong, what you did about it
4. Univariate description of five variables , written out in sentences
5. For one continuous variable: is it normal? Justify with the three pieces of evidence
6. Two sentences on what a manager learns from your descriptive statistics
Half the marks are for points 4–6 — the interpretation.
Producing output is not analysis. Explaining it is.
AQD – Session 1 NGUYEN Anh-Tuan 41
```

<a id="s01-p042"></a>
### S01 — page 42

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=42>)

```text
Errors that cost marks every year
Reporting a mean for a nominal variable — “average sector = 2.4”
Setting the measure type wrong, then wondering why the test will not run
Reading “Sig. = 0.000” as p = 0 — it means p < 0.001
Confusing significance (is there an effect?) with strength (does it matter?)
Copying output into a report with no interpretation
Stopping at the statistic. The manager asked a question. Answer it.
AQD – Session 1 NGUYEN Anh-Tuan 42
```

<a id="s01-p043"></a>
### S01 — page 43

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=43>)

```text
Before session 2
1. Finish cleaning your dataset. Session 2 assumes it is ready.
2. Identify two pairs of variables in your own data:
one pair of qualitative variables → we will run a chi-square
one pair of quantitative variables → we will run a correlation
3. Write the managerial question each pair could answer.
4. Read: Navarro & Foxcroft, Learning Statistics with Jamovi , chapters on descriptives.
Y ou will arrive next week with a live question and the data to answer it.
That is how this course is supposed to feel.
AQD – Session 1 NGUYEN Anh-Tuan 43
```

<a id="s01-p044"></a>
### S01 — page 44

[Voir cette page dans le PDF](<sources/cours/S01 - Slides.pdf#page=44>)

```text
Questions?
NGUYEN Anh-Tuan
Session 2: relationships between two variables
```

## S02 — support complet (43 pages)

[Ouvrir le PDF original complet](<sources/cours/S02 - Slides.pdf>)

<a id="s02-p001"></a>
### S02 — page 1

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=1>)

```text
Quantitative Data Analysis
Session 2 — Statistical Tests: Chi-square & Correlation
NGUYEN Anh-Tuan
EM Normandie — Programme Grande École
Course code 2627_ECO_2_EN_009 · 2026–2027
```

<a id="s02-p002"></a>
### S02 — page 2

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=2>)

```text
Where we are
Session Method Question it answers
1 Univariate descriptive analysis What does my data look like?
2
today
Statistical tests: chi-square &
Pearson correlation
Are two variables related?
3 ANOVA + post-hoc tests Do groups differ from each other?
4 Simple & multiple regression What drives my outcome?
Last week ended on a limit: univariate analysis cannot establish a relationship.
Today we cross that line. From now on, every result you report is the answer to atest.
AQD – Session 2 NGUYEN Anh-Tuan 2
```

<a id="s02-p003"></a>
### S02 — page 3

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=3>)

```text
Today: 3 hours 30
Time What happens Mode
0:00 – 0:15 Dataset check: is your .omv clean and correctly typed? Checkpoint
0:15 – 1:00 Theory: the logic of a statistical test & the map of all
tests
Lecture + quiz
1:00 – 1:30 Chi-square test of independence + Cramér’s V Lecture
1:30 – 1:45 Break
1:45 – 2:15 Pearson & Spearman correlation Lecture
2:15 – 3:00 Jamovi lab: run both tests on your own dataset Teams of 3
3:00 – 3:30 Write-up in protocol format + submission of Artefact 2 Checkpoint
You leave today with two tested relationships from your own data: one chi-square, one
correlation, each written up as a managerial conclusion.
AQD – Session 2 NGUYEN Anh-Tuan 3
```

<a id="s02-p004"></a>
### S02 — page 4

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=4>)

```text
The logic of a statistical test
```

<a id="s02-p005"></a>
### S02 — page 5

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=5>)

```text
Why we need a test at all
In our retail sample, 71% of customers aged 55+
buy the regional brand, against 42% of those aged
18–34.
Is that a real difference in the population of
shoppers. . . or just the luck of these 325 people?
A different sample would give slightly different
figures. This is sampling fluctuation.
A statistical test answers one question:
Is the pattern I see too large to be
explained by chance alone?
Yes → we generalise to the population.
No → we say nothing beyond our sample.
Descriptive statistics describe your sample. Tests let you speak about the market.
AQD – Session 2 NGUYEN Anh-Tuan 5
```

<a id="s02-p006"></a>
### S02 — page 6

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=6>)

```text
Two hypotheses, stated in business language
H0 — the null hypothesis
Nothing is going on.
No relationship, no difference, no effect.
It is the hypothesis the test tries to reject.
H1 — the alternative hypothesis
Something is going on.
There is a relationship / a difference.
Usually what the manager wants to know.
Managerial question H0 H1
Does brand choice depend on
age?
Brand and age band are
independent
Brand and age band are
related
Do frequent visitors spend
more?
No linear correlation
between visits and spending
A correlation exists
Exam habit: never write “H0: ρ = 0” alone. Always translate into the manager’s words.
AQD – Session 2 NGUYEN Anh-Tuan 6
```

<a id="s02-p007"></a>
### S02 — page 7

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=7>)

```text
The p-value and the 5% rule
p-value = the probability of observing a pattern at
least this strong if H0 were true.
α = 5% = the risk we accept of rejecting H0 wrongly.
Fixed before looking at the result.
In Jamovi the p-value is in the column p.
“< .001” means p < 0.001 — never write p = 0.
p < 0.05
Reject H0 → the relationship is
statistically significant.
p ≥ 0.05
We cannot reject H0 → no evidence of
a relationship.
Remember Shapiro–Wilk (Session 1): there H0 = “the data are normal”, so p > 0.05 was the
good news. For every test today,p < 0.05 is the finding.
AQD – Session 2 NGUYEN Anh-Tuan 7
```

<a id="s02-p008"></a>
### S02 — page 8

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=8>)

```text
Two ways to be wrong
In reality: H0 true
(no relationship)
In reality: H0 false
(a relationship exists)
We reject H0 Type I error (α)
False alarm: we launch a
targeted campaign for a
segment effect that does not
exist
Correct
We do not reject H0 Correct Type II error ( β)
Missed opportunity: a real
segment effect goes
unnoticed
We control the first risk by fixing α = 5%. The second one shrinks as the sample size grows —
one more reason for your N ≥ 100 rule.
AQD – Session 2 NGUYEN Anh-Tuan 8
```

<a id="s02-p009"></a>
### S02 — page 9

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=9>)

```text
Significance is not strength
The p-value answers:
Is there a relationship?
Y es / no, with a 5% risk.
The effect size answers:
Does it matter for the business?
Weak, moderate or strong.
Test Effect size Range Session
Chi-square Cramér’s V 0 to 1 2
Pearson correlation r (and r 2) −1 to +1 2
ANOVA η2 (eta squared) 0 to 1 3
Regression R2, coefficients B 0 to 1 4
With N = 5 000, a trivial correlation of r = 0.04 is “significant”. Always report both numbers.
AQD – Session 2 NGUYEN Anh-Tuan 9
```

<a id="s02-p010"></a>
### S02 — page 10

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=10>)

```text
The protocol — same template, now with a test inside
1. IDENTIFY — Which test? Justify from the nature of the variables. Check its
conditions.
2. HYPOTHESISE — State H0 and H1 in business language.
3. DECIDE — Report the statistic, df and p. Is p < 0.05? Then: how strong is the
effect, and in which direction?
4. RECOMMEND — What does the manager do on Monday morning?
Step 1 now has a second half: every test has conditions. A correct test on data that violate its
conditions is a wrong answer.
AQD – Session 2 NGUYEN Anh-Tuan 10
```

<a id="s02-p011"></a>
### S02 — page 11

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=11>)

```text
The map of statistical tests
```

<a id="s02-p012"></a>
### S02 — page 12

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=12>)

```text
Five questions that choose the test for you
1. What is my objective? Relate two variables, compare groups, or explain an outcome?
2. How many variables? One, two, or several at once?
3. What type is each variable? Nominal, ordinal, discrete, continuous — Session 1 taxonomy.
4. How many groups, and are they independent? Two groups or three and more? Different
people, or the same people measured twice?
5. Are the conditions met? Normality, sample size, expected counts → parametric or
non-parametric test.
Answer the five questions and the test is mechanically determined. There is no taste involved.
AQD – Session 2 NGUYEN Anh-Tuan 12
```

<a id="s02-p013"></a>
### S02 — page 13

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=13>)

```text
Parametric and non-parametric tests
Parametric
Quantitative outcome (interval/ratio)
Assumes an approximately normal
distribution — or a large sample
Works on means and variances
More powerful when conditions hold
t-tests, ANOVA, Pearson, regression
Non-parametric
Nominal or ordinal data, or skewed
quantities
No normality assumption
Works on counts or ranks
Robust to outliers; slightly less
powerful
chi-square, Spearman, Mann–Whitney,
Kruskal–Wallis
Y our Session 1 normality check (three centres, skewness/kurtosis, histogram, Shapiro–Wilk) is exactly
what decides between the two columns.
AQD – Session 2 NGUYEN Anh-Tuan 13
```

<a id="s02-p014"></a>
### S02 — page 14

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=14>)

```text
The full map — all the tests you should recognise
Situation Parametric test Non-parametric Jamovi menu
Two qualitative variables — Chi-square + Cramér’s V Frequencies → Independent
Samples
Two quantitative
variables
Pearson correlation (r) Spearman (ρ) Regression → Correlation
Matrix
Quantitative × 2
independent groups
Independent-samples
t-test
Mann–Whitney U T -Tests → Independent
Samples
Quantitative × 3+ groups One-way ANOVA +
post-hoc
Kruskal–Wallis ANOVA → One-Way
ANOVA
Same people measured
twice
Paired-samples t-test Wilcoxon signed-rank T -Tests → Paired Samples
One mean vs a target
value
One-sample t-test Wilcoxon (one sample) T -Tests → One Sample
One qualitative vs
expected split
— χ2 goodness of fit Frequencies → N Outcomes
Several predictors →
quantitative Y
Multiple regression — Regression → Linear
Regression
Highlighted = today. ANOVA (session 3) and regression (session 4) build on the same logic.
AQD – Session 2 NGUYEN Anh-Tuan 14
```

<a id="s02-p015"></a>
### S02 — page 15

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=15>)

```text
Quiz — which test?
1. Is the choice of loyalty card (none / silver / gold)
related to the customer’s region?
2. Do firms with higher turnover also emit more CO2?
3. Do online and in-store customers have the same
average basket?
4. Is ESG grade (A to D) associated with the credit
rating (AAA to B)?
5. Does satisfaction (0–20) differ across 4 store
formats?
6. The same 40 employees rate their motivation
before and after training.
7. Is our customer base split 50/50 between men and
women, as in the city?
8. Which of ROI, headcount and debt ratio drive net
profit?
Take 4 minutes. Use the five questions, then the map.
AQD – Session 2 NGUYEN Anh-Tuan 15
```

<a id="s02-p016"></a>
### S02 — page 16

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=16>)

```text
Quiz — answers
# Test Why / trap
1 Chi-square + Cramér’s V Nominal × nominal. Card level is ordinal, but χ2 still applies.
2 Pearson (or Spearman) Two continuous variables. Both are right-skewed: check,
then consider Spearman.
3 Independent-samples t-test Quantitative outcome, 2 independent groups.
4 Spearman correlation Two ordinal variables: ranks, not means. χ2 is acceptable
but ignores the order.
5 One-way ANOVA + post-hoc Quantitative outcome, 4 groups — Session 3.
6 Paired-samples t-test The same people twice: the samples are not independent.
7 χ2 goodness of fit One qualitative variable against an expected distribution.
8 Multiple regression Several predictors at once — Session 4.
Questions 2 and 4 are the ones students miss: the conditions and the measurement level both matter.
AQD – Session 2 NGUYEN Anh-Tuan 16
```

<a id="s02-p017"></a>
### S02 — page 17

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=17>)

```text
Two qualitative variables: chi-square
```

<a id="s02-p018"></a>
### S02 — page 18

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=18>)

```text
The question
Retail case (same data as Session 1, N = 325). The regional brand “Grain d’Or” is bought by
56% of customers. Marketing wants to know whether to target an age group.
Variable 1: age band — 18–34 / 35–54 / 55+
qualitative, 3 categories
Variable 2: brand purchased — National / Grain
d’Or
qualitative (nominal), 2 categories
Question: is brand choice related to age?
Qualitative × qualitative
→ Chi-square test of independence
→ effect size: Cramér’s V
That sentence is your IDENTIFY step. It costs one line and earns a point.
AQD – Session 2 NGUYEN Anh-Tuan 18
```

<a id="s02-p019"></a>
### S02 — page 19

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=19>)

```text
Start with the contingency table
Observed counts (row %)
Age band National Grain d’Or Total
18–34 58 (58%) 42 (42%) 100
35–54 55 (44%) 70 (56%) 125
55+ 29 (29%) 71 (71%) 100
Total 142 183 325
Read row percentages: they compare age bands of
different sizes fairly. 18–34 35–54 55+
0
20
40
60
80
58
44
29
42
56
71
% buying
National Grain d’Or
The pattern is visible: the older the customer, the more regional brand. The test tells us whether
it is more than chance.
AQD – Session 2 NGUYEN Anh-Tuan 19
```

<a id="s02-p020"></a>
### S02 — page 20

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=20>)

```text
What the chi-square actually does
1. It builds the table you would expect if H0 were
true — if brand did not depend on age:
E = row total × column totalN
e.g. 18–34 & Grain d’Or: 100 × 183/325 = 56.3
expected, but only 42 observed.
2. It adds up the gaps between observed and
expected:
χ2 = X (O − E)2
E
Expected counts under H0
Age band National Grain d’Or
18–34 43.7 56.3
35–54 54.6 70.4
55+ 43.7 56.3
Big gaps → big χ2 → small p.
Here the 35–54 row matches almost perfectly;
the gaps are at both ends.
Y ou will never compute this by hand. Y ou need it to explain what the number means.
AQD – Session 2 NGUYEN Anh-Tuan 20
```

<a id="s02-p021"></a>
### S02 — page 21

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=21>)

```text
Conditions of the chi-square test
1. Counts, not percentages. The test works on frequencies of individuals.
2. Independent observations. Each person appears in one cell only.
3. Expected counts large enough: at least 80% of cells with E ≥ 5, and none below 1.
Our case: smallest expected count = 43.7.
Condition met.
If violated: merge small categories (e.g. “AAA”
+ “AA”) or, for a 2×2 table, use Fisher’s exact
test.
Y our nominal variable must have2–5 categories — this is why that rule was in the dataset
specification.
AQD – Session 2 NGUYEN Anh-Tuan 21
```

<a id="s02-p022"></a>
### S02 — page 22

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=22>)

```text
Hypotheses, degrees of freedom, decision
H0: brand choice is independent of age band.
H1: brand choice depends on age band.
Degrees of freedom
df = (rows − 1)(columns − 1) = (3 − 1)(2 − 1) =2
A 2×2 table always has df = 1. Remember this — we
will use it in five minutes.
χ2 Tests (Jamovi)
Value df p
χ2 17.10 2 < .001
N 325
p < 0.001 < 0.05 → reject H0.
Brand choice is significantly related to age.
AQD – Session 2 NGUYEN Anh-Tuan 22
```

<a id="s02-p023"></a>
### S02 — page 23

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=23>)

```text
How strong? Cramér’s V
V =
s
χ2
N × (k − 1)
k = the smaller number of rows or columns.
Our case:
p
17.10/(325 × 1) =0.23
Nominal (Jamovi)
Value
Phi-coefficient 0.229
Cramér’s V 0.229
0 0.1 0.3 0.5 1
negl. weak moderate strong
V = 0.23
A real but weak-to-moderate association: age
matters, but it is far from the whole story.
Direction? V has none. Go back to the row percentages to say who buys what.
AQD – Session 2 NGUYEN Anh-Tuan 23
```

<a id="s02-p024"></a>
### S02 — page 24

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=24>)

```text
Writing it up — model answer
1. IDENTIFY. Age band and brand purchased are both qualitative, so we use a chi-square test of
independence, with Cramér’s V for strength. All expected counts exceed 5 (minimum 43.7).
2. HYPOTHESISE. H0: brand choice does not depend on age. H1: brand choice depends on age.
3. DECIDE. χ2(2) =17.10, p < .001: we reject H0 at the 5% level. Cramér’s V = 0.23 indicates a
weak-to-moderate association. The share buying Grain d’Or rises from 42% (18–34) to 71% (55+).
4. RECOMMEND. Keep the core Grain d’Or message for customers aged 55+, who are already loyal to it;
test a dedicated offer (digital coupons, sampling) to convert 18–34 year-olds, where the national brand still
dominates.
Step 4 must follow from the numbers. “Improve marketing” earns nothing. “Target the segment where the
gap is” does.
AQD – Session 2 NGUYEN Anh-Tuan 24
```

<a id="s02-p025"></a>
### S02 — page 25

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=25>)

```text
Read output critically — a real example
Test of association: gender × brand purchased (National / Regional), N = 325
Value df p
χ2 221.43 2 0.000
Cramér’s V 0.765
N 325
Two things are wrong here.
Can you spot them before I tell
you?
df = 2 — gender (2) × brand (2) is a 2×2 table: df = 1.
V = 0.765 — with χ2 = 221.43 and N = 325,
V =
p
221.43/325 = 0.83. The two numbers cannot
come from the same table.
Same lesson as Session 1: software never refuses to print a number. Checking is your job.
AQD – Session 2 NGUYEN Anh-Tuan 25
```

<a id="s02-p026"></a>
### S02 — page 26

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=26>)

```text
Two quantitative variables: correlation
```

<a id="s02-p027"></a>
### S02 — page 27

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=27>)

```text
The question
Same retail data. Does a customer
who visits more often also spend
more per month?
Variable 1: monthly visits (discrete)
Variable 2: monthly spending e (continuous,
ratio)
Quantitative × quantitative
→ Pearson correlation r
(Spearman ρ if conditions fail)
0 2 4 6 8 10 12 14
0
50
100
Monthly visits
Monthly spending (e)
Always plot first (N = 325)
AQD – Session 2 NGUYEN Anh-Tuan 27
```

<a id="s02-p028"></a>
### S02 — page 28

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=28>)

```text
Pearson’s r: direction and strength
Negative, r = −0.96 None, r = −0.05 Positive, r = +0.95
Sign = direction. Size = strength.
r runs from −1 (perfect negative) to +1 (perfect
positive); 0 = no linear link.
|r | Strength
< 0.3 weak
0.3 – 0.7 moderate
> 0.7 strong
AQD – Session 2 NGUYEN Anh-Tuan 28
```

<a id="s02-p029"></a>
### S02 — page 29

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=29>)

```text
The Jamovi output — and how to read it
Correlation Matrix
Visits Spending Age
Visits Pearson’s r —
p-value —
Spending Pearson’s r 0.618 —
p-value < .001 —
Age Pearson’s r −0.099 −0.046 —
p-value 0.075 0.413 —
df = N − 2 = 323 for every pair.
H0: no linear relationship between visits and
spending.
Visits–spending: r = 0.62, p < .001 →
reject H0: a moderate positive correlation.
Age–spending: r = −0.05, p = .413 →
cannot reject H0: no evidence that age is
linked to spending.
AQD – Session 2 NGUYEN Anh-Tuan 29
```

<a id="s02-p030"></a>
### S02 — page 30

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=30>)

```text
r 2: how much the two variables share
Visits Spending
38%
r 2 = 0.6182 = 0.38
38% of the variation in monthly spending goes together
with the variation in visits.
The other 62% depends on something else: basket size,
income, promotions. . .
This is the seed of R2 in Session 4: regression will tell us
how many euros one more visit is worth.
AQD – Session 2 NGUYEN Anh-Tuan 30
```

<a id="s02-p031"></a>
### S02 — page 31

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=31>)

```text
Conditions of Pearson’s r
1. Interval or ratio variables — not ordinal codes, never nominal ones.
2. A linear relationship — check the scatterplot.
3. Approximate normality of both variables — your Session 1 evidence.
4. No extreme outliers — one point can create or destroy r.
5. Homoscedasticity — the spread of Y is similar along X (no “funnel”).
Our case: visits are right-skewed (skewness 0.90, Shapiro–Wilk p < .001). With N = 325, Pearson is
robust — but we confirm with Spearman: ρ = 0.61, p < .001. Same conclusion, so the result is solid.
AQD – Session 2 NGUYEN Anh-Tuan 31
```

<a id="s02-p032"></a>
### S02 — page 32

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=32>)

```text
Two scatterplots that fool the coefficient
Strong curve, yet r = 0.01 One outlier: r = 0.83 (without it: −0.01)
Pearson only sees straight lines and is hijacked by extreme points. A coefficient without a
scatterplot is not an analysis.
AQD – Session 2 NGUYEN Anh-Tuan 32
```

<a id="s02-p033"></a>
### S02 — page 33

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=33>)

```text
Pearson or Spearman?
Pearson r Spearman ρ
Variables Interval / ratio Ordinal, or skewed quantities
Relationship detected Linear Monotonic (always up or always
down)
Normality Needed (or large N) Not needed
Outliers Very sensitive Robust — works on ranks
Reading −1 to +1 −1 to +1, same rules
Use Spearman for two ordinal variables (ESG
grade × credit rating) or for heavily skewed data
(turnover, emissions).
Good practice: tick both in Jamovi. If they
agree, report Pearson; if they disagree, trust
Spearman and say why.
AQD – Session 2 NGUYEN Anh-Tuan 33
```

<a id="s02-p034"></a>
### S02 — page 34

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=34>)

```text
Correlation is not causation
Temperature
Ice-cream sales Sunburn cases
r = 0.8 — but no cause
A correlation can come from:
a third variable driving both
reverse causality (do visits cause
spending, or do big spenders visit more?)
pure coincidence
In your write-up say “is associated with”, never “causes” or “increases”. Isolating the effect of one
variable, the others held constant, is the job of regression in Session 4.
AQD – Session 2 NGUYEN Anh-Tuan 34
```

<a id="s02-p035"></a>
### S02 — page 35

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=35>)

```text
Writing it up — model answer
1. IDENTIFY. Monthly visits and monthly spending are both quantitative, so we use Pearson’s correlation.
The scatterplot shows a linear pattern without extreme outliers; visits are right-skewed, so we check with
Spearman.
2. HYPOTHESISE. H0: there is no linear relationship between visits and spending. H1: there is one.
3. DECIDE. r (323) =0.62, p < .001: we reject H0. The correlation is positive and moderate; Spearman
confirms it (ρ = 0.61). Visits share 38% of their variance with spending. Age is not related to spending
(r = −0.05, p = .41).
4. RECOMMEND. Visit frequency, not age, is the lever: a loyalty mechanism that rewards the next visit
(points expiring monthly, weekly offers) is a better bet than age-targeted promotions. Session 4 will quantify
the euro value of one extra visit.
AQD – Session 2 NGUYEN Anh-Tuan 35
```

<a id="s02-p036"></a>
### S02 — page 36

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=36>)

```text
Jamovi lab
```

<a id="s02-p037"></a>
### S02 — page 37

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=37>)

```text
Chi-square in Jamovi
Analyses → Frequencies → Independent
Samples (χ2 test of association)
1. Move one variable to Rows, the other to Columns
2. Statistics: tick χ2 and Phi and Cramér’s V
3. Cells: tick Observed and Expected counts, and
Row percentages
4. Optional: Plots → bar plot, percentages within rows
Read, in this order:
1. Expected counts — condition OK?
2. χ2 Tests — value, df, p
3. Nominal — Cramér’s V
4. Row % — who does what?
Both variables must be set to Nominal or Ordinal. A continuous variable dropped here gives a table with
one column per value — and a meaningless test.
AQD – Session 2 NGUYEN Anh-Tuan 37
```

<a id="s02-p038"></a>
### S02 — page 38

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=38>)

```text
Correlation in Jamovi
Analyses → Regression → Correlation Matrix
1. Move all your continuous variables in at once (at
least 3)
2. Correlation coefficients: tick Pearson and Spearman
3. Additional options: Report significance, Flag
significant correlations
4. Plot: tick Correlation matrix to see the scatterplots
For one pair in detail: Exploration → Scatterplot, add a
linear regression line.
Read, in this order:
1. The scatterplot — linear? outliers?
2. p — significant?
3. r — sign and strength
4. Spearman — does it agree?
Firm-level data? Turnover and emissions
are usually very skewed. Rely on
Spearman, or create a log variable via
Compute.
AQD – Session 2 NGUYEN Anh-Tuan 38
```

<a id="s02-p039"></a>
### S02 — page 39

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=39>)

```text
Apply it to your fil rouge dataset
Chi-square pair
Two qualitative variables, 2–5 categories
each.
Firm data: sector × ESG grade band
Retail data: region × brand purchased
Correlation set
At least three continuous variables.
Firm data: turnover, ROI, emissions per
employee
Retail data: visits, spending, basket size
For each pair, before you touch Jamovi, write one line: “A manager would care because. . . ”
If you cannot finish that sentence, pick another pair.
A non-significant result is still a result. “Sector is not related to ESG grade” is useful news — report it
honestly.
AQD – Session 2 NGUYEN Anh-Tuan 39
```

<a id="s02-p040"></a>
### S02 — page 40

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=40>)

```text
Artefact 2 — submit before you leave (25 marks)
1. The updated .omv file, with any new cleaning added to your cleaning log
2. One chi-square : contingency table with row %, check of expected counts, χ2, df, p, Cramér’s V
3. One correlation matrix of at least three continuous variables, with the scatterplot of the pair you
discuss, Pearson and Spearman
4. Each test written up in the four-step protocol
5. Two managerial recommendations , each tied to a specific number
Indicative weighting: chi-square 10 · correlation 10 · recommendations 5.
As in Artefact 1, half the marks are for interpretation. Output alone is not analysis.
AQD – Session 2 NGUYEN Anh-Tuan 40
```

<a id="s02-p041"></a>
### S02 — page 41

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=41>)

```text
Errors that cost marks every year
Running a correlation on nominal codes — “r between sector and region = 0.12”
Reporting χ2 with percentages instead of counts
Ignoring the expected-count condition when categories are small
Reading a significant p as a strong effect — report V or r every time
Writing “visits cause higher spending” — a correlation shows association only
Reporting r without looking at the scatterplot
Stating “H0 is proven” — we only fail to reject it
AQD – Session 2 NGUYEN Anh-Tuan 41
```

<a id="s02-p042"></a>
### S02 — page 42

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=42>)

```text
Before session 3
1. Finish Artefact 2 if your write-up is not complete.
2. Identify in your dataset a qualitative variable with 3–5 groups and a quantitative outcome.
e.g. sector → ROI; store format → satisfaction; region → spending
3. Write the managerial question: do the groups differ on this outcome?
4. Check the outcome’s distribution within each group (Descriptives → split by).
5. Read: Navarro & Foxcroft, Learning Statistics with Jamovi, chapters on categorical data analysis and
correlation.
Today you askedare two variables related? Next week: do groups differ — and which ones?
AQD – Session 2 NGUYEN Anh-Tuan 42
```

<a id="s02-p043"></a>
### S02 — page 43

[Voir cette page dans le PDF](<sources/cours/S02 - Slides.pdf#page=43>)

```text
Questions?
NGUYEN Anh-Tuan
Session 3: comparing groups — ANOVA & post-hoc tests
```

## S03 — support complet (48 pages)

[Ouvrir le PDF original complet](<sources/cours/S03 - Slides (revised).pdf>)

<a id="s03-p001"></a>
### S03 — page 1

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=1>)

```text
Quantitative Data Analysis
Session 3 — Comparing Groups: ANOVA & Post-hoc Tests
NGUYEN Anh-Tuan
EM Normandie — Programme Grande École
Course code 2627_ECO_2_EN_009 · 2026–2027
```

<a id="s03-p002"></a>
### S03 — page 2

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=2>)

```text
Where we are
Session Method Question it answers
1 Univariate descriptive analysis What does my data look like?
2 Chi-square, correlation & t-tests Are two variables related? Do two
groups differ?
3 ANOVA + post-hoc tests Do groups differ from each other?
today
4 Simple & multiple regression What drives my outcome?
Last week: two qualitative variables ( χ2), two quantitative ones ( r), and two groups (Student or
Welch t-test).
Today, the general mixed case: a quantitative outcome compared across three or more groups
of a qualitative variable.
AQD – Session 3 NGUYEN Anh-Tuan 2
```

<a id="s03-p003"></a>
### S03 — page 3

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=3>)

```text
Today: 3 hours 30
Time What happens Mode
0:00 – 0:15 Recap: the three most common mistakes of Session 2 Plenary
0:15 – 1:00 Theory: why ANOVA, the logic of variance, the F test Lecture + quiz
1:00 – 1:25 Conditions and what to do when they fail Lecture
1:25 – 1:40 Break
1:40 – 2:25 Post-hoc tests: which groups differ — and which test to use,
on four datasets NEW
Lecture
2:25 – 3:00 Jamovi lab: one ANOVA on your own dataset Teams of 3
3:00 – 3:30 Write-up of your results in protocol format Checkpoint
Y ou leave today knowing not onlywhether your groups differ, but which ones — which post-hoc
test to trust — and what a manager should do about it.
AQD – Session 3 NGUYEN Anh-Tuan 3
```

<a id="s03-p004"></a>
### S03 — page 4

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=4>)

```text
Why ANOVA?
```

<a id="s03-p005"></a>
### S03 — page 5

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=5>)

```text
The question
Same retail data ( N = 325). Customers
shop mainly in one of four store formats.
Does monthly spending depend on the for-
mat?
Outcome (Y): monthly spending e
quantitative, continuous
Factor (X): store format
nominal, 4 groups
Quantitative × qualitative (3+ groups)
→ one-way ANOVA + post-hoc
Spending by store format
Hyper Super Convenience Online0
50
100
Monthly spending (e)
AQD – Session 3 NGUYEN Anh-Tuan 5
```

<a id="s03-p006"></a>
### S03 — page 6

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=6>)

```text
Two groups or more than two?
2 groups (e.g. card holders vs non-
holders)
→ independent-samples t-test (Session 2)
3 groups or more (e.g. 4 store formats)
→ one-way ANOVA,one single test for all
groups at once
Why not six t-tests? Each test carries a 5%
risk of a false alarm. The risks add up:
P(≥ 1 false alarm) =1 − 0.95m
m = number of pairs = k(k − 1)/2.
Risk of ≥ 1 false alarm (%)
2 3 4 5 6
0
20
40
60
5
14.3
26.5
40.1
53.7
Number of groups
dashed line: α = 5%
ANOVA keeps the overall risk at 5%, whatever
the number of groups.
AQD – Session 3 NGUYEN Anh-Tuan 6
```

<a id="s03-p007"></a>
### S03 — page 7

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=7>)

```text
From the t-test to ANOVA: the same family NEW
Situation 2 groups (Session 2) 3+ groups (today)
Equal variances (Levene
p > .05)
Student’s t-test Fisher’s ANOVA+ Tukey
Unequal variances (Levene
p ≤ .05)
Welch’s t-test Welch’s ANOVA+
Games–Howell
Small groups, not normal Mann–Whitney U Kruskal–Wallis + DSCF
Effect size Cohen’s d η2
Everything you learned about Student vs Welch carries over: Fisher’s ANOVA and Tukey pool
one common variance ; Welch’s ANOVA and Games–Howell keep each group’s own. When
spreads and group sizes differ, pooling gives false alarms or missed effects — exactly as with the
t-test.
AQD – Session 3 NGUYEN Anh-Tuan 7
```

<a id="s03-p008"></a>
### S03 — page 8

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=8>)

```text
The idea: compare two kinds of variation
A B C
Groups clearly differ
A B C
Same means — lost in the noise
Between-group variation: how far the group
means (orange) are from each other. Identical in
both panels.
Within-group variation: how spread out cus-
tomers are inside each group. Small on the left,
large on the right.
AQD – Session 3 NGUYEN Anh-Tuan 8
```

<a id="s03-p009"></a>
### S03 — page 9

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=9>)

```text
The F ratio
F = variation between groupsvariation within groups = MSbetweenMSwithin
• F ≈ 1: the means differ no more than
individuals do → noise
• F ≫ 1: the gap between groups stands out
→ signal
The name “analysis of variance” is misleading:
it is a test on means, done by comparing
variances.
Our case: total variation split in two
0 20 40 60 80 100
% of total variation in spending (SS)
Between formats (11%) Within formats (89%)
SStotal = SSbetween + SSwithin
200 661 = 22 151 + 178 510
AQD – Session 3 NGUYEN Anh-Tuan 9
```

<a id="s03-p010"></a>
### S03 — page 10

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=10>)

```text
From F to a p-value
F distribution if H0 is true (df = 3, 321)
0 2 4 6
critical value 2.63 (5%)
our F = 13.28
(far off the chart) →
F
Density
If H0 were true, F would usually be close
to 1.
Beyond 2.63, it happens less than 5% of
the time.
Our F = 13.28 → p < .001.
The software does this for you. What you
must be able to say: “ the gap between
formats is far larger than the gap be-
tween customers of the same format.”
AQD – Session 3 NGUYEN Anh-Tuan 10
```

<a id="s03-p011"></a>
### S03 — page 11

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=11>)

```text
Hypotheses — and a classic trap
H0: average spending is the same in all four
store formats.
µHyper = µSuper = µConv = µOnline
H1: at least one format has a different aver-
age spending.
Trap: H1 is not “all the formats are different”. A significant ANOVA only says the four means are
not all equal. It does not say which ones differ.
ANOVA
is there a difference?
Post-hoc tests
where is it?
Effect size η2
does it matter?
if p < .05
AQD – Session 3 NGUYEN Anh-Tuan 11
```

<a id="s03-p012"></a>
### S03 — page 12

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=12>)

```text
Quiz — ANOVA, t-test or something else?
1. ROI (%) of firms in 5 sectors.
2. Satisfaction of customers who did / did not use
click-and-collect.
3. Share of women (%) among the managers of 3
subsidiaries.
4. Emissions per employee across ESG grades A, B,
C, D.
5. Brand purchased (national / regional) across 4
regions.
6. Basket size before and after a store refit, same 60
stores.
7. Sales of 12 stores in 3 regions (4 per region), very
skewed.
8. Turnover and number of employees of 300 firms.
Take 3 minutes. What is the outcome? What is the grouping variable?
AQD – Session 3 NGUYEN Anh-Tuan 12
```

<a id="s03-p013"></a>
### S03 — page 13

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=13>)

```text
Quiz — answers
# Test Why / trap
1 One-way ANOVA + post-hoc Quantitative outcome, 5 groups.
2 Independent-samples t-test Only 2 groups (ANOVA gives the same p, but the t-test is the
convention). Levene → Student or Welch.
3 Chi-square The “%” hides the real data: each manager is a woman or a man →
two qualitative variables.
4 One-way ANOVA + post-hoc ESG grade is ordinal, but used here as 4 groups.
5 Chi-square The outcome is qualitative. ANOVA needs a quantitative Y .
6 Paired-samples t-test The same stores twice: not independent groups.
7 Kruskal–Wallis (+ DSCF) Tiny groups and skewed data: non-parametric version of ANOVA.
8 Correlation (Session 2) Two quantitative variables, no groups.
AQD – Session 3 NGUYEN Anh-Tuan 13
```

<a id="s03-p014"></a>
### S03 — page 14

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=14>)

```text
Conditions: can I trust the F test?
```

<a id="s03-p015"></a>
### S03 — page 15

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=15>)

```text
Three conditions
1. Independence — each customer belongs to one group only, and is measured once.
2. Normality within each group — or at least 30 observations per group.
3. Homogeneity of variances — the spread is similar in all groups. Tested withLevene’s test.
A B C
Homogeneous: similar spreads
A B C
Heterogeneous: one group spreads out
AQD – Session 3 NGUYEN Anh-Tuan 15
```

<a id="s03-p016"></a>
### S03 — page 16

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=16>)

```text
Levene’s test — the opposite logic again
H0: the variances are equal in all groups.
So, like Shapiro–Wilk in Session 1, p > 0.05 is
the good news.
Homogeneity of Variances Test (Levene’s)
F df1 df2 p
0.52 3 321 0.666
p = 0.666 > 0.05 → we keep H0: variances
are homogeneous. Classic (Fisher) ANOVA
is fine.
Normality: Shapiro–Wilk is significant in three
groups (skewness ≈ 0.3), but every group
has n ≥ 49. With groups this large, ANOVA
is robust — and we will confirm with a non-
parametric test.
AQD – Session 3 NGUYEN Anh-Tuan 16
```

<a id="s03-p017"></a>
### S03 — page 17

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=17>)

```text
When the conditions fail: a decision path
Groups roughly normal,
or n ≥ 30 per group?
Levene: variances
equal (p > .05)?
Welch’s ANOVA
+ Games–Howell
Kruskal–Wallis
+ Dwass–Steel–
Critchlow–Fligner
Fisher’s ANOVA
+ Tukey post-hoc
yes no
no yes
Jamovi runs Welch by default inANOVA → One-Way ANOVA. Good practice: tick both Welch and Fisher. If
they agree, the conclusion is robust.
Our case: Fisher F (3, 321) = 13.28; Welch F (3, 158) = 14.34; Kruskal–Wallis χ2(3) = 33.99 — all
p < .001.
AQD – Session 3 NGUYEN Anh-Tuan 17
```

<a id="s03-p018"></a>
### S03 — page 18

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=18>)

```text
Why Welch’s ANOVA exists NEW
Fisher’s F divides by MSwithin — one pooled
variance for all groups, weighted by group size.
Same weakness as Student’s t:
• small groups with large spread → F
overstated
• large groups with large spread → F
understated
Welch’s ANOVA weights each group bynj /s2j and
corrects the second df (a decimal number).
Example (Dataset 2 below): 4 channels, SDs from
8 to 30 e, n from 20 to 120. Levene
F (3, 221) =37.81, p < .001.
Test F p
Fisher F (3, 221) =5.99 < .001
Welch F (3, 48.7) =4.21 .010
Both are significant here, but Fisher overstates the evidence by a factor of 10 inp. With a smaller
effect, Fisher alone could give a false “significant”. A decimal second df in the output = Welch.
AQD – Session 3 NGUYEN Anh-Tuan 18
```

<a id="s03-p019"></a>
### S03 — page 19

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=19>)

```text
Running and reading the ANOVA
```

<a id="s03-p020"></a>
### S03 — page 20

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=20>)

```text
Step 1: describe the groups
Group Descriptives
Format N Mean SD SE
Hypermarket 83 60.08 24.01 2.64
Supermarket 101 53.18 25.05 2.49
Convenience 92 40.76 22.52 2.35
Online 49 62.27 21.59 3.08
Standard deviations are close (21.6 to 25.1): con-
sistent with Levene. Convenience customers spend
about 20 e less per month. SE = SD/√n.
Means with 95% confidence intervals
Hyper Super Conv. Online30
40
50
60
70
Mean spending (e)
AQD – Session 3 NGUYEN Anh-Tuan 20
```

<a id="s03-p021"></a>
### S03 — page 21

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=21>)

```text
Step 2: the ANOVA table
ANOVA — Monthly spending(Jamovi, ANOVA module)
Sum of Squares df Mean Square F p η2
Store format 22 151 3 7 384 13.28 < .001 0.110
Residuals 178 510 321 556
How to read it:
• dfbetween = k − 1 = 4 − 1 = 3
• dfwithin = N − k = 325 − 4 = 321
• MS = SS/df and F = 7 384/556 = 13.28
• Report as: F (3, 321) =13.28, p < .001
p < 0.05 → we reject H0.
Average spending is not the same in all
store formats.
AQD – Session 3 NGUYEN Anh-Tuan 21
```

<a id="s03-p022"></a>
### S03 — page 22

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=22>)

```text
Step 3: how much does it matter? η2
η2 = SSbetween
SStotal
= 22 151200 661 = 0.11
Store format accounts for 11% of the differences
in spending between customers.
η2 Effect
≈ 0.01 small
≈ 0.06 medium
≥ 0.14 large
89%
11%
Store format (orange) vs everything else
A medium effect: format matters, but 89% of
the variation lies elsewhere — visits, income. . .
Session 4 will put them in one model.
AQD – Session 3 NGUYEN Anh-Tuan 22
```

<a id="s03-p023"></a>
### S03 — page 23

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=23>)

```text
Post-hoc tests: which groups differ?
```

<a id="s03-p024"></a>
### S03 — page 24

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=24>)

```text
Four groups, six comparisons
Hyper
60.1
Super
53.2
Conv.
40.8
Online
62.3
significant not significant
With k groups there are k(k − 1)/2 pairs: 6 pairs
here.
Post-hoc tests compare every pair while
correcting the p-values, so that the overall risk
stays at 5%.
The picture: one format stands apart. Every link to
Convenience is significant; the other three formats
do not differ from each other.
AQD – Session 3 NGUYEN Anh-Tuan 24
```

<a id="s03-p025"></a>
### S03 — page 25

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=25>)

```text
Which post-hoc test?
Test When How it corrects Comment
Tukey Equal variances (Levene
p > .05)
Pooled MSwithin for every pair;
studentized range distribution,
built for “all pairs at once”
The standard choice after a
Fisher ANOVA
Games–Howell Unequal variances Each pair gets its own SEq
s21/n1 + s22/n2 and Welch df
The partner of Welch’s
ANOVA
Bonferroni Few planned
comparisons
padj = min(1, p × m), m =
number of comparisons
Very conservative: multiplies
each p by the number of pairs
Dwass–Steel–
Critchlow–Fligner
After Kruskal–Wallis Ranks each pair of groups
together (Wilcoxon), then
studentized range
Non-parametric pairwise
comparisons
Only run post-hoc tests after a significant ANOVA. Ifp ≥ .05 overall, there is nothing to locate — stop there
and report it.
Next: four datasets, one per test, showing what goes wrong with the wrong choice.
AQD – Session 3 NGUYEN Anh-Tuan 25
```

<a id="s03-p026"></a>
### S03 — page 26

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=26>)

```text
Why correct at all? A simulation NEW
4 000 datasets in which all group means are truly equal
(n = 30 per group). How often does at least one pair
come out “significant”? Every one of those is a false
alarm.
Groups Pairs Uncorrected Tukey Bonferroni 1 − 0.95m
3 3 11.9% 4.8% 3.9% 14.3%
4 6 19.1% 4.5% 3.3% 26.5%
5 10 29.1% 5.5% 4.3% 40.1%
Uncorrected t-tests raise false alarms 2
to 6 times too often.
Tukey sits on 5%.
Bonferroni stays under 5%: safe but
over-cautious, which costs power.
The real rate is below the formula 1 − 0.95m because pairs share groups — but it is still far above 5%.
AQD – Session 3 NGUYEN Anh-Tuan 26
```

<a id="s03-p027"></a>
### S03 — page 27

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=27>)

```text
Dataset 1 — equal variances → Fisher + Tukey
Data: monthly spending by store format (the case above). Levenep = .666 → Fisher’s ANOVAF (3, 321) =
13.28, p < .001 → Tukey.
Post Hoc Comparisons — Store format (Tukey)
Comparison Mean diff. SE t ptukey
Hyper Super 6.90 3.49 1.97 0.200
Hyper Conv. 19.32 3.57 5.41 < .001
Hyper Online −2.19 4.25 −0.52 0.955
Super Conv. 12.43 3.40 3.66 0.002
Super Online −9.09 4.11 −2.21 0.122
Conv. Online −21.51 4.17 −5.16 < .001
Mean diff. = first group minus second group. The sign tells you who is higher.
Significant: Convenience spends less
than Hypermarket ( −19.3 e), Super-
market (−12.4 e) and Online (−21.5 e).
Not significant: Hyper, Super and On-
line. The 9 e gap Super–Online is not a
proven difference (p = .122).
AQD – Session 3 NGUYEN Anh-Tuan 27
```

<a id="s03-p028"></a>
### S03 — page 28

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=28>)

```text
Dataset 1 — what an uncorrected analysis would have claimed NEW
Pair Mean diff. p uncorrected p Tukey p Bonferroni (×6)
Hyper Super 6.90 0.049 0.200 0.295
Hyper Conv. 19.32 < .001 < .001 < .001
Hyper Online −2.19 0.607 0.955 1.000
Super Conv. 12.43 < .001 0.002 0.002
Super Online −9.09 0.028 0.122 0.165
Conv. Online −21.51 < .001 < .001 < .001
Computed on a dataset rebuilt with the slide’s group means and SDs.
Why correct: six uncorrected t-tests would “find”
Hyper > Super and Online > Super. With six
tries, a p just under .05 is what chance produces.
Tukey sends both back.
Why Tukey, not Bonferroni: same verdicts, but
Bonferroni’s p are larger (0.295 vs 0.200; 0.165
vs 0.122). Tukey is built for all pairs; Bonferroni
wastes power there.
AQD – Session 3 NGUYEN Anh-Tuan 28
```

<a id="s03-p029"></a>
### S03 — page 29

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=29>)

```text
Summarise the result in one picture
Groups sharing a letter do not differ (Tukey, 5%)
Online Hyper Super Conv.
0
20
40
60
a a
a
b
Mean spending (e)
The letter display is the fastest way to
show a post-hoc result to a manager:
• same letter = no significant difference
• different letters = significant difference
Online ≈ Hyper ≈ Super
> Convenience
AQD – Session 3 NGUYEN Anh-Tuan 29
```

<a id="s03-p030"></a>
### S03 — page 30

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=30>)

```text
Dataset 1 — writing it up (model answer)
1. IDENTIFY. Monthly spending is quantitative and store format is a nominal variable with four groups: one-
way ANOVA with post-hoc tests. Groups are independent; Levene’s test is not significant (F (3, 321) =0.52,
p = .666); every group has n ≥ 49, so ANOVA is robust to the mild skewness.
2. HYPOTHESISE. H0: average spending is the same in the four formats. H1: at least one format differs.
3. DECIDE. F (3, 321) = 13.28, p < .001: we reject H0. η2 = 0.11, a medium effect. Tukey tests show that
Convenience customers spend significantly less (40.8 e) than Hypermarket (60.1 e), Supermarket (53.2 e)
and Online (62.3 e) customers; the other three formats do not differ. Welch and Kruskal–Wallis confirm.
4. RECOMMEND. Convenience is the under-performing format: raise its basket with larger-pack promotions
and cross-selling at the till, rather than spreading a single promotional budget across all four formats. Do not
invest to “close the gap” between Supermarket and Online: that gap is not established.
AQD – Session 3 NGUYEN Anh-Tuan 30
```

<a id="s03-p031"></a>
### S03 — page 31

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=31>)

```text
Dataset 2 — unequal variances: the data NEW
Monthly spending by purchase channel. Store and
app customers are numerous and homogeneous;
click-and-collect and delivery customers are few and
very heterogeneous.
Channel n Mean (e) SD ( e)
Store 120 50.00 8.00
App 60 54.50 10.00
Click & collect 20 61.00 30.00
Home delivery 25 44.00 28.00
Levene F (3, 221) = 37.81, p < .001 → variances
not equal → Welch’s ANOVA: F (3, 48.7) = 4.21,
p = .010 → Games–Howell.
Store App C&C Delivery
0
50
100
Monthly spending (e)
AQD – Session 3 NGUYEN Anh-Tuan 31
```

<a id="s03-p032"></a>
### S03 — page 32

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=32>)

```text
Dataset 2 — Tukey and Games–Howell disagree NEW
Pair Mean diff. Tukey SE p Tukey G–H SE p Games–Howell
Store App −4.50 2.36 0.230 1.48 0.016
Store Click & collect −11.00 3.61 0.014 6.75 0.386
Store Delivery 6.00 3.29 0.264 5.65 0.715
App Click & collect −6.50 3.86 0.335 6.83 0.778
App Delivery 10.50 3.56 0.018 5.75 0.283
Click & collect Delivery 17.00 4.49 0.001 8.74 0.226
Tukey: 3 false alarms. It uses one pooled SD
(
√
MSwithin = 15.0 e) for every pair — too small
for the pairs involving C&C and delivery (own SDs
28–30 e, only 20–25 customers).
Tukey: 1 real effect missed. The same pooled
SD is too large for Store vs App (SDs 8 and 10e,
180 customers). Their 4.5e gap is measured pre-
cisely: only Games–Howell sees it.
AQD – Session 3 NGUYEN Anh-Tuan 32
```

<a id="s03-p033"></a>
### S03 — page 33

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=33>)

```text
Dataset 2 — proof by simulation, and the write-up
Same n and SDs, equal true
means, 3 000 datasets: how often
is at least one pair “significant”?
Tukey G–H
0
10
20
30
40 34.4
4.6
% false alarms
1. IDENTIFY. Spending is quantitative, channel nominal with 4 independent
groups: one-way ANOVA. Levene is significant (F (3, 221) = 37.81, p < .001)
and group sizes are very unequal → Welch’s ANOVA + Games–Howell.
2. HYPOTHESISE. H0: average spending is the same in all channels. H1: at
least one differs.
3. DECIDE. Welch F (3, 48.7) = 4.21, p = .010: reject H0. Games–Howell:
app customers spend 4.5e more than store customers (p = .016). Larger gaps
involving C&C and delivery (up to 17e) are not significant: those customers are
few and very dispersed.
4. RECOMMEND. Push store customers to the app (app-only offers): the only
established gain, +4.5 e/month. Do not reallocate budget to click-and-collect on
its high average; collect more data first.
AQD – Session 3 NGUYEN Anh-Tuan 33
```

<a id="s03-p034"></a>
### S03 — page 34

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=34>)

```text
Dataset 3 — a few planned comparisons: the data NEW
A retailer tests four new store layouts (A–D)
against the current one (control), 30 stores each,
average basket (e).
Before collecting data , management decided it
only cares about two questions:
(1) is layout A better than control?
(2) is layout B better than control?
Levene F (4, 145) =0.08, p = .99. Fisher
F (4, 145) =3.90, p = .005, η2 = 0.10.
Layout n Mean (e) SD ( e)
Control 30 50.00 12.00
A 30 58.00 12.00
B 30 51.00 12.00
C 30 55.00 12.00
D 30 47.00 12.00
5 groups → 10 possible pairs. But only 2 were
planned.
AQD – Session 3 NGUYEN Anh-Tuan 34
```

<a id="s03-p035"></a>
### S03 — page 35

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=35>)

```text
Dataset 3 — Bonferroni on the planned comparisons NEW
Comparison Mean diff. p uncorrected Bonferroni, 2 planned (×2) Tukey, all 10 pairs Bonferroni, all 10 ( ×10)
A – Control 8.00 0.011 0.022 → significant 0.079 0.108
B – Control 1.00 0.747 1.000 0.998 1.000
Bonferroni’s penalty is the number of compar-
isons m. With 2 planned comparisons each p
is only doubled: layout A’s +8 e is significant
(p = .022).
Tukey protects all 10 pairs — which nobody asked
about — and misses A ( p = .079). Bonferroni
over all 10 pairs is stricter still ( p = .108): hence
“very conservative” with many pairs.
The rule that makes this honest: the comparisons are chosen before seeing the data. Looking at the
means, picking the biggest gap and “planning” it afterwards is cheating — the real number of comparisons
was 10.
AQD – Session 3 NGUYEN Anh-Tuan 35
```

<a id="s03-p036"></a>
### S03 — page 36

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=36>)

```text
Dataset 3 — writing it up (model answer)
1. IDENTIFY. Basket value is quantitative, layout is nominal with five independent groups: one-way ANOVA.
Levene is not significant (p = .99). Two comparisons against control were planned before the study, so we
test them with a Bonferroni correction (m = 2).
2. HYPOTHESISE. H0: layout A (resp. B) has the same average basket as the current layout. H1: it differs.
3. DECIDE. The ANOVA is significant (F (4, 145) =3.90, p = .005, η2 = 0.10). Layout A raises the average
basket by 8 e (58 vs 50 e; Bonferroni p = .022). Layout B does not differ from control (p = 1.00).
4. RECOMMEND. Roll out layout A (+8e per basket, about +16%); drop layout B. Layouts C and D were not
part of the plan: any idea about them is a new hypothesis for a new study.
Among all 10 pairs, Tukey finds only A vs D significant (+11e, p = .005) — an unplanned finding to be
confirmed later.
AQD – Session 3 NGUYEN Anh-Tuan 36
```

<a id="s03-p037"></a>
### S03 — page 37

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=37>)

```text
Dataset 4 — skewed data and an outlier: the data NEW
Weekly sales (ke) of 12 stores per region. North
includes one flagship store at 190 ke.
Region Mean Median SD Shapiro–Wilk
North 40.17 26.5 47.46 W = 0.43, p < .001
East 31.25 30.5 7.41 p = .98
South 52.83 50.5 10.41 p = .74
Groups of 12 ( < 30) and North is far from nor-
mal (skewness 2.95) → the decision path leads to
Kruskal–Wallis + DSCF.
North East South
0
50
100
150
200
flagship
Weekly sales (ke)
mean median
AQD – Session 3 NGUYEN Anh-Tuan 37
```

<a id="s03-p038"></a>
### S03 — page 38

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=38>)

```text
Dataset 4 — ANOVA sees nothing, Kruskal–Wallis does NEW
Omnibus test Result Verdict
Fisher’s ANOVA F (2, 33) =1.75, p = .19 n.s.
Kruskal–Wallis χ2(2) =18.80, p < .001 Significant
Pair p Tukey DSCF W p DSCF
North – East 0.724 −1.55 0.515
North – South 0.525 −4.90 0.002
East – South 0.166 −5.55 < .001
The 190 k e store drags North’s mean to 40.2
(median 26.5) and inflates the within-group vari-
ance: MSwithin = 805 with it, 65 without it. The
noise swamps the signal.
Ranks do not care how far 190 is from the rest
— only that it is the largest. DSCF sees what
the medians show: South sells more than both
other regions; North and East do not differ.
Do not simply delete the flagship: it is a real store. Choosing the rank-based test is the honest fix. Effect size:
ε2 = H/(N − 1) =18.80/35 = 0.54.
AQD – Session 3 NGUYEN Anh-Tuan 38
```

<a id="s03-p039"></a>
### S03 — page 39

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=39>)

```text
Dataset 4 — writing it up (model answer)
1. IDENTIFY. Weekly sales are quantitative and region is nominal with three independent groups. Groups
are small (n = 12) and North is strongly skewed by one flagship store (Shapiro–Wilk p < .001), so we use
Kruskal–Wallis with DSCF pairwise comparisons.
2. HYPOTHESISE. H0: sales have the same distribution in the three regions. H1: at least one region tends
to sell more or less.
3. DECIDE. χ2(2) = 18.80, p < .001, ε2 = 0.54: we reject H0. DSCF shows that South (median 50.5
ke) sells more than North (26.5 k e, p = .002) and East (30.5 k e, p < .001); North and East do not differ
(p = .515).
4. RECOMMEND. Study what South stores do differently (range, staffing, location) and transfer it to North
and East. Analyse the North flagship separately: it is a different kind of store and should not set targets for
the other North stores.
With a rank-based test, report medians, not means.
AQD – Session 3 NGUYEN Anh-Tuan 39
```

<a id="s03-p040"></a>
### S03 — page 40

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=40>)

```text
What the four datasets teach NEW
Dataset Condition that decides Right tests What the wrong test did
1. Store formats Levene p > .05, n ≥ 49 Fisher + Tukey Uncorrected t-tests: 2 false
differences. Bonferroni: same
verdicts, less power
2. Channels Levene p < .001, unequal
n
Welch + Games–Howell Tukey: 3 false differences, 1 real
one missed
3. Layouts 2 comparisons planned in
advance
Bonferroni (m = 2) Tukey on all 10 pairs: misses layout
A’s +8 e
4. Regional sales Small n, strong skew, outlier Kruskal–Wallis + DSCF Fisher + Tukey: nothing significant
at all
The post-hoc test is not a matter of taste: it follows from the same checks that chose the ANOVA
— normality or group size, then Levene — plus one question: were the comparisons planned?
AQD – Session 3 NGUYEN Anh-Tuan 40
```

<a id="s03-p041"></a>
### S03 — page 41

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=41>)

```text
Read output critically — a real example
ANOVA: customer satisfaction (0–20) by region — North, South, East, West (N = 200)
Sum of Squares df Mean Square F p
Region 120 4 40.0 12.4 < .001
Residuals 1 764 196 9.0
Two things are wrong here.
Can you spot them before I tell you?
df = 4 — four regions givedf = k −1 = 3. (And 3 +196 =
199 = N − 1: the table itself says so.)
F = 12.4 — F = 40.0/9.0 = 4.44. The F printed does not
come from these mean squares.
Check df, check F = MSbetween/MSwithin. Thirty seconds, every time.
AQD – Session 3 NGUYEN Anh-Tuan 41
```

<a id="s03-p042"></a>
### S03 — page 42

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=42>)

```text
Going further: two factors at once
Illustration: format × loyalty card
Hyper Super Conv. Online
40
60
80
Mean spending (e)
Card holders
No card
A two-way ANOVAtests two factors and
their interaction.
Interaction = the effect of one factor
depends on the other. Here the card matters
a lot online and in hypermarkets, much less
in convenience stores: the lines are not
parallel.
Beyond this course — Jamovi does it in
ANOVA → ANOVAby adding a second fixed
factor.
AQD – Session 3 NGUYEN Anh-Tuan 42
```

<a id="s03-p043"></a>
### S03 — page 43

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=43>)

```text
Jamovi lab
```

<a id="s03-p044"></a>
### S03 — page 44

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=44>)

```text
One-way ANOVA in Jamovi
Analyses → ANOVA → One-Way ANOVA
1. Dependent Variables: your quantitative outcome
2. Grouping Variable: your nominal variable (3–5 groups)
3. Variances: tick Don’t assume equal (Welch’s) and Assume equal
(Fisher’s)
4. Additional Statistics: Descriptives table and Descriptives plots
5. Assumption Checks: Equality of variances, Normality
6. Post-Hoc Tests: Tukey (equal variances) or Games–Howell
(unequal)
Non-parametric: ANOVA → Non-Parametric → One-Way ANOVA
(Kruskal–Wallis); tick DSCF pairwise comparisons.
Bonferroni: ANOVA → ANOVA → Post Hoc Tests, correction
“Bonferroni”.
Read, in this order:
1. Descriptives + plot — the story
2. Levene — which ANOVA?
3. F , df, p — is there a difference?
4. Post-hoc — where is it?
5. η2 — does it matter?
η2 is not in One-Way ANOVA: use
ANOVA → ANOVA and tick η2 under
Effect Size.
AQD – Session 3 NGUYEN Anh-Tuan 44
```

<a id="s03-p045"></a>
### S03 — page 45

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=45>)

```text
Apply it to your fil rouge dataset
Firm-level data
sector → ROI
ESG grade band → emissions per employee
size band → net margin
Retail / customer data
region → monthly spending
store format → satisfaction score
socio-professional category → loyalty score
Before running anything:
• Is the grouping variable set to Nominal (or
Ordinal)?
• Are there 3–5 groups? Merge tiny ones (e.g.
n < 10) into “Other”.
• Plot the outcome by group (Descriptives → split
by, box plot).
• Compare the SDs and group sizes: very
different? Think Welch + Games–Howell.
• Firm data: turnover and emissions are often
very skewed → think Kruskal–Wallis or a log.
AQD – Session 3 NGUYEN Anh-Tuan 45
```

<a id="s03-p046"></a>
### S03 — page 46

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=46>)

```text
Errors that cost marks every year
• Writing H1 as “all groups are different”
• Stopping after a significant F — without post-hoc tests, you cannot say which groups differ
• Running post-hoc tests after a non-significant ANOVA and “finding” a difference
• Reading Levene backwards — p > .05 means the variances are equal
• Using Tukey when Levene is significant — use Games–Howell NEW
• “Planning” a Bonferroni comparison after looking at the means NEW
• Comparing groups with a qualitative outcome — that is a chi-square
• Reporting F without its two degrees of freedom, or without η2
• Recommending action on a difference that is not significant
AQD – Session 3 NGUYEN Anh-Tuan 46
```

<a id="s03-p047"></a>
### S03 — page 47

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=47>)

```text
Before session 4
1. Choose the quantitative outcome your manager cares most about (profit, spending,
emissions. . . ).
2. List at least three predictors: continuous variables, plus one qualitative variable you can
code 0/1.
3. Plot the outcome against each continuous predictor (Exploration → Scatterplot). Linear?
Outliers?
4. Read: Navarro & Foxcroft, Learning Statistics with Jamovi, chapters on comparing several
means and linear regression.
Today: do groups differ — and which ones? Next week: what drives my outcome — and by how
many euros?
AQD – Session 3 NGUYEN Anh-Tuan 47
```

<a id="s03-p048"></a>
### S03 — page 48

[Voir cette page dans le PDF](<sources/cours/S03 - Slides (revised).pdf#page=48>)

```text
Questions?
NGUYEN Anh-Tuan
Session 4: what drives my outcome? Simple & multiple regression
```

## S04 — support complet (40 pages)

[Ouvrir le PDF original complet](<sources/cours/S04 - Slides (revised).pdf>)

<a id="s04-p001"></a>
### S04 — page 1

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=1>)

```text
Quantitative Data Analysis
Session 4 — What Drives My Outcome? Simple & Multiple Regression
NGUYEN Anh-Tuan
EM Normandie — Programme Grande École
Course code 2627_ECO_2_EN_009 · 2026–2027
```

<a id="s04-p002"></a>
### S04 — page 2

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=2>)

```text
Where we are
Session Method Question it answers
1 Univariate descriptive analysis What does my data look like?
2 Chi-square, correlation & t-tests Are two variables related? Do two
groups differ?
3 ANOVA + post-hoc tests Do groups differ from each other?
4 Simple & multiple regression What drives my outcome?
today
Session 2 told us visits and spending are correlated ( r = 0.62). Session 3 told us store format
matters (η2 = 0.11).
Today we put everything in one model — and put aeuro value on each driver.
AQD – Session 4 NGUYEN Anh-Tuan 2
```

<a id="s04-p003"></a>
### S04 — page 3

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=3>)

```text
Today: 3 hours 30
Time What happens Mode
0:00 – 0:15 Recap of Session 3 Plenary
0:15 – 0:50 Simple regression: from a correlation to a line Lecture
0:50 – 1:30 Multiple regression: several drivers, all else equal Lecture + quiz
1:30 – 1:45 Break
1:45 – 2:10 Conditions and diagnostics: can I trust the model? Lecture
2:10 – 3:00 Jamovi lab: your regression model Teams of 3
3:00 – 3:30 From four analyses to one recommendation: the final report Workshop
The last session of the fil rouge. Y ou leave with a model of your outcome and the plan of the
consulting report that closes the course.
AQD – Session 4 NGUYEN Anh-Tuan 3
```

<a id="s04-p004"></a>
### S04 — page 4

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=4>)

```text
Simple regression: from a correlation to a line
```

<a id="s04-p005"></a>
### S04 — page 5

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=5>)

```text
The question
Session 2: visits and spending are corre-
lated, r = 0.62.
The manager’s next question: how many
euros is one more visit worth?
Correlation is symmetric and has no unit.
Regression is directional (X → Y ) and
speaks in the units of Y: euros, tonnes,
percentage points.
The line that fits the cloud best
0 5 100
50
100
ˆY = 24.61 + 6.61X
Monthly visits
Monthly spending (e)
AQD – Session 4 NGUYEN Anh-Tuan 5
```

<a id="s04-p006"></a>
### S04 — page 6

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=6>)

```text
Anatomy of a regression line
X
Y
+1 unit of X
slope b1
residual e
intercept b0
Y = b0 + b1X + e
b0 (intercept): predicted Y when X = 0. Often
meaningless on its own.
b1 (slope): change in Y for one more unit of X.
The number managers want.
e (residual): observed minus predicted. What
the line does not explain.
AQD – Session 4 NGUYEN Anh-Tuan 6
```

<a id="s04-p007"></a>
### S04 — page 7

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=7>)

```text
Least squares: how the line is chosen
X
Y
Each red segment is a residual: the prediction
error for one observation.
The regression line is the one that makes the
sum of squared residuals as small as
possible — hence “ordinary least squares”
(OLS).
Y ou will never compute it. Y ou need to know that a
residual is the part of each customer’s spend-
ing the model gets wrong — we will inspect
them later.
AQD – Session 4 NGUYEN Anh-Tuan 7
```

<a id="s04-p008"></a>
### S04 — page 8

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=8>)

```text
Worked by hand: 8 stores NEW
Advertising x (ke) vs sales y (ke), 8 stores
(Session 2):
Advertising x Sales y
Mean 5.50 38.875
SD 2.449 6.289
Correlation r 0.969
b1 = r × sy
sx
= 0.969 × 6.2892.449 = 2.49
b0 = ¯y − b1¯x = 38.875 − 2.49 × 5.5 = 25.19
Sales = 25.19 + 2.49× advertising
Each extra 1 k e of advertising is associ-
ated with 2.49 ke more sales.
R2 = r 2 = 0.94.
The slope is the correlation translated into
units: r says “how tightly”,b1 says “how much”.
Same sign, always.
AQD – Session 4 NGUYEN Anh-Tuan 8
```

<a id="s04-p009"></a>
### S04 — page 9

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=9>)

```text
The Jamovi output
Model Fit Measures
R R2 Adj. R2 F df1 df2 p
0.618 0.383 0.381 200.1 1 323 < .001
Model Coefficients — Spending
Predictor Estimate SE t p
Intercept 24.61 2.27 10.85 < .001
Visits 6.61 0.47 14.14 < .001
H0: visits have no effect on spending
(b1 = 0).
t = 14.14, p < .001 → reject H0.
Each additional monthly visit is asso-
ciated with 6.61 e more spending per
month.
In simple regression, R = |r | and R2 = r 2:
the 38% of Session 2 again.
Check: t = B/SE = 6.61/0.47 = 14.1 ✓
AQD – Session 4 NGUYEN Anh-Tuan 9
```

<a id="s04-p010"></a>
### S04 — page 10

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=10>)

```text
R2: how much of the outcome the model explains
Visits alone
0 20 40 60 80 100
% of the variation in spending
Explained by the model Residual (unexplained)
R2 ranges from 0 (the model explains nothing)
to 1 (it explains everything).
R2 Reading (management data)
< 0.10 weak
0.10 – 0.40 moderate
0.40 – 0.70 substantial
> 0.70 strong
62% of spending is unexplained by visits. Something else matters — income, the loyalty card,
distance? One predictor is rarely enough.
AQD – Session 4 NGUYEN Anh-Tuan 10
```

<a id="s04-p011"></a>
### S04 — page 11

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=11>)

```text
Predicting — and the danger of extrapolation
Data range: 1 to 13 visits
0 5 10 15 200
50
100
150
no data here:
do not predict
Monthly visits
Spending (e)
Prediction for a customer with 5 visits:
ˆY = 24.61 + 6.61 × 5 = 57.66 e
“A customer with 20 visits would spend
157 e” — no. No one in the data visits more
than 13 times. Outside the observed range,
the line is a guess.
AQD – Session 4 NGUYEN Anh-Tuan 11
```

<a id="s04-p012"></a>
### S04 — page 12

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=12>)

```text
Multiple regression: all else being equal
```

<a id="s04-p013"></a>
### S04 — page 13

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=13>)

```text
Why several predictors?
Visits
Household income
Loyalty card
Distance to store
Age
Monthly
spending
r = 0.39
Spending has several drivers, and the drivers
are related to each other: card holders also
visit more often (r = 0.39).
In a simple regression, the “visits” effect
silently includes part of the card effect.
Multiple regression estimates the effect of
each driver holding the others constant
— ceteris paribus.
AQD – Session 4 NGUYEN Anh-Tuan 13
```

<a id="s04-p014"></a>
### S04 — page 14

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=14>)

```text
The model
Y = b0 + b1X1 + b2X2 + · · ·+ bkXk + e
Y — the outcome
Quantitative (interval / ra-
tio): spending, profit,
emissions.
b0 — intercept
Predicted Y when every
X = 0. Rarely a real sit-
uation.
bj — coefficients
Change in Y for +1 unit
of Xj, the other X held
constant.
e — error
Everything the model
does not capture. It ex-
ists in every estimation.
Predictors can be quantitative or qualitative — if you code them as dummy variables.
AQD – Session 4 NGUYEN Anh-Tuan 14
```

<a id="s04-p015"></a>
### S04 — page 15

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=15>)

```text
Qualitative predictors: dummy variables
Loyalty card: 1 = holder, 0 = no card.
Its coefficient = the gap between the two
groups, all else equal.
A variable with k categories needs k − 1
dummies. The missing one is the reference:
store format → Super, Conv., Online vs Hyper
(reference).
Jamovi codes this for you: put the variable inFac-
tors, choose the reference level.
Same slope, shifted line
0 5 10
20
40
60
80
100
+11.83 e
Monthly visits
Predicted spending (e)
Card holder
No card
AQD – Session 4 NGUYEN Anh-Tuan 15
```

<a id="s04-p016"></a>
### S04 — page 16

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=16>)

```text
The case: our model of monthly spending
Variable Type Unit
Y Monthly spending Continuous e per month
X1 Monthly visits Discrete visits
X2 Household income Continuous k e per year
X3 Loyalty card Dummy (0/1) 1 = holder (39%)
X4 Distance to store Continuous km
X5 Age Continuous years
Managerial question: which levers raise a cus-
tomer’s monthly spending, and by how much?
Sample size rule: at least 10–15 observations
per predictor. N = 325 for 5 predictors: comfort-
able.
AQD – Session 4 NGUYEN Anh-Tuan 16
```

<a id="s04-p017"></a>
### S04 — page 17

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=17>)

```text
Reading the output: three steps, in this order
1
Is the model
useful at all?
Overall F test
H0: all b = 0
p < .05?
2
How much
does it explain?
R2 and adjusted R2
3
Which drivers,
how much?
For each X: p,
then B (in units),
then β (ranking)
If step 1 fails (p ≥ .05), stop: the model as a whole explains nothing, and individual coefficients
are not worth interpreting.
AQD – Session 4 NGUYEN Anh-Tuan 17
```

<a id="s04-p018"></a>
### S04 — page 18

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=18>)

```text
Steps 1 and 2: the model as a whole
Model Fit Measures
R R2 Adj. R2 F df1 df2 p
0.769 0.592 0.586 92.55 5 319 < .001
Step 1. F (5, 319) = 92.55, p < .001: the model is signifi-
cant. ( df1 = number of predictors = 5; df2 = N − k − 1 =
325 − 5 − 1 = 319.)
Step 2. Together, the five predictors explain59% of the vari-
ation in monthly spending — up from 38% with visits alone.
Explained variation
Visits only Five predictors
0
0.2
0.4
0.6
0.38
0.59
R2
Adjusted R2 penalises useless predictors: report it
when comparing models.
AQD – Session 4 NGUYEN Anh-Tuan 18
```

<a id="s04-p019"></a>
### S04 — page 19

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=19>)

```text
Step 3: the coefficients
Model Coefficients — Monthly spending (Jamovi)
Predictor Estimate (B) SE t p Stand. ( β) VIF
Intercept −8.50 6.14 −1.38 0.167
Visits 5.08 0.42 12.10 < .001 0.475 1.20
Income (ke) 0.98 0.10 9.36 < .001 0.345 1.06
Loyalty card: Y es – No 11.83 2.02 5.86 < .001 0.233 1.23
Distance (km) −0.75 0.30 −2.47 0.014 −0.090 1.04
Age 0.03 0.10 0.31 0.759 0.011 1.01
Four significant drivers (p < .05): visits, in-
come, loyalty card, distance.
Age is not significant (p = .759) — consistent
with Session 2 (r = −0.05).
AQD – Session 4 NGUYEN Anh-Tuan 19
```

<a id="s04-p020"></a>
### S04 — page 20

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=20>)

```text
Interpreting B: always in the units, always “all else equal”
Driver Interpretation
Visits (B = 5.08) One more visit per month → +5.08 e of monthly spending, for
customers with the same income, card status, distance and age.
Income (B = 0.98) +1 k e of annual household income → +0.98 e per month.
Loyalty card
(B = 11.83)
Card holders spend 11.83 e more per month than comparable
non-holders.
Distance (B = −0.75) Each extra km between home and store → −0.75 e per month.
Intercept (−8.50) Customer with 0 visits, 0 income, 0 km, aged 0: meaningless. Do not
interpret.
Why did visits drop from 6.61 e to 5.08 e? In the simple model, visits also carried part of the
loyalty-card effect. Controlling for it gives the own effect of a visit.
AQD – Session 4 NGUYEN Anh-Tuan 20
```

<a id="s04-p021"></a>
### S04 — page 21

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=21>)

```text
Which driver matters most? Standardised coefficients
Relative importance of each driver
−0.2 0 0.2 0.4 0.6
Age
Distance
Loyalty card
Income
Visits
Standardised coefficient β with 95% CI
B values have different units (visits, ke,
km): you cannot compare them.
β puts every variable in standard
deviations: now they are comparable.
Ranking: visits (0.48) > income (0.35)
> card (0.23) > distance (−0.09). A CI
crossing 0 (age) = not significant.
In a sensible model |β| is almost always
below 1.
AQD – Session 4 NGUYEN Anh-Tuan 21
```

<a id="s04-p022"></a>
### S04 — page 22

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=22>)

```text
Quiz — interpret it right
1. A colleague writes: “Card holders spend 11.83 e more, so the card causes 11.83 e of
spending.” What is the problem?
2. “Visits have the biggest effect because 5.08 is bigger than 0.98.” True or false?
3. “Age has no effect on spending.” How should it be phrased?
4. Can we predict the spending of a customer with 30 visits a month?
5. Adding 10 random variables to the model raises R2 from 0.592 to 0.604. Good news?
AQD – Session 4 NGUYEN Anh-Tuan 22
```

<a id="s04-p023"></a>
### S04 — page 23

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=23>)

```text
Quiz — answers
# Answer
1 Association, not causation: customers who spend a lot may choose to take a card. Say “is
associated with”.
2 False reasoning — the units differ (visits vs k e). The right conclusion comes from β: 0.475
vs 0.345.
3 “We find no significant effect of age, once the other variables are controlled for ( p = .759).”
4 No: the data go up to 13 visits. That is extrapolation.
5 No: R2 always rises when you add variables. Check adjusted R2 — it will fall.
AQD – Session 4 NGUYEN Anh-Tuan 23
```

<a id="s04-p024"></a>
### S04 — page 24

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=24>)

```text
Conditions: can I trust the model?
```

<a id="s04-p025"></a>
### S04 — page 25

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=25>)

```text
The conditions of linear regression
1. Linearity — each X relates to Y roughly along a straight line (scatterplots).
2. Independence of residuals — Durbin–Watson close to 2 (between 1.5 and 2.5).
3. Normality of residuals — Q-Q plot of residuals along the diagonal.
4. Equal variance of residuals (homoscedasticity) — no funnel in the residual plot.
5. No multicollinearity — predictors not too correlated with each other: VIF < 5.
Note: the condition is on the residuals, not on Y itself. A skewed Y can still give well-behaved residuals.
Our case: Durbin–Watson = 1.83; all VIF ≤ 1.23; residuals checked on the next slide.
AQD – Session 4 NGUYEN Anh-Tuan 25
```

<a id="s04-p026"></a>
### S04 — page 26

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=26>)

```text
Diagnostics: the two plots to look at
50 100
−50
0
50
Fitted values (e)
Residuals
Residuals vs fitted: a shapeless band
−2 0 2
−4
−2
0
2
Theoretical quantiles
Standardised residuals
Q-Q plot: points on the diagonal
No pattern, no funnel, points along the line: the conditions hold. (Shapiro–Wilk on the residuals:
p = .349.)
AQD – Session 4 NGUYEN Anh-Tuan 26
```

<a id="s04-p027"></a>
### S04 — page 27

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=27>)

```text
What a problem looks like
Funnel: heteroscedasticity Curve: non-linearity
X1 X2 X3 X4
0
2
4
6
8
10
VIF: multicollinearity
Problem What to do
Funnel Log-transform Y (turnover, emissions); report robust conclusions with
caution
Curve Log-transform X, or add X 2
VIF > 5 Drop one of the correlated predictors (e.g. keep turnover or headcount, not
both)
AQD – Session 4 NGUYEN Anh-Tuan 27
```

<a id="s04-p028"></a>
### S04 — page 28

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=28>)

```text
Prediction with the full model
Customer profile: 6 visits, income 40 ke, card holder,
lives 3 km away, aged 41.
ˆY = −8.50 + 5.08(6) +0.98(40) +11.83(1)
−0.75(3) +0.03(41) ≈ 71.8 eper month
(Computed with unrounded coefficients.)
Same customer, card or not
No card Card holder
0
20
40
60
80
59.9
71.8
Predicted spending (e)
This is the language of a business case: “converting this customer to the card is worth about
12 e a month, 142 e a year.”
AQD – Session 4 NGUYEN Anh-Tuan 28
```

<a id="s04-p029"></a>
### S04 — page 29

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=29>)

```text
Writing it up — model answer
1. IDENTIFY. Monthly spending is quantitative and we want the simultaneous effect of several predictors:
multiple linear regression. Residual plots show no pattern, the Q-Q plot is on the diagonal, Durbin–Watson
= 1.83, all VIF ≤ 1.23: the conditions hold.
2. HYPOTHESISE. Overall: H0, none of the predictors explains spending. For each predictor: H0, it has no
effect once the others are controlled for.
3. DECIDE. The model is significant, F (5, 319) = 92.55, p < .001, and explains 59% of the variation
(adjusted R2 = 0.586). Visits ( B = 5.08, p < .001), income ( B = 0.98, p < .001) and the loyalty card
(B = 11.83, p < .001) increase spending; distance reduces it ( B = −0.75, p = .014). Age has no
significant effect. By standardised coefficients, visits are the strongest driver (β = 0.48).
4. RECOMMEND. (1) Push visit frequency — each extra monthly visit is worth about 5 e: weekly offers,
app notifications. (2) Grow the loyalty card base: +12 e per holder per month, all else equal; test whether
a sign-up bonus below that value pays off. (3) Stop age-based targeting: it adds nothing once behaviour is
known.
AQD – Session 4 NGUYEN Anh-Tuan 29
```

<a id="s04-p030"></a>
### S04 — page 30

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=30>)

```text
Read output critically — a real example
Regression of monthly sales (ke) on price and advertising, 48 stores
R R2 Adj. R2
0.79 0.62 0.71
Predictor Estimate SE t p
Intercept 52.10 8.40 6.20 < .001
Price (e) −4.20 2.10 −5.60 < .001
Advertising (ke) 1.30 0.40 3.25 0.002
Two things are wrong here.
Can you spot them before I tell
you?
Adj. R2 = 0.71 > R2 = 0.62 — impossible: the adjustment
can only lower R2.
t = −5.60 for price — t = B/SE = −4.20/2.10 = −2.00.
The p-value built on it is wrong too.
Checks for every regression: Adj. R2 ≤ R2, t = B/SE, R 2 = R × R, and signs that make business sense.
AQD – Session 4 NGUYEN Anh-Tuan 30
```

<a id="s04-p031"></a>
### S04 — page 31

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=31>)

```text
Jamovi lab
```

<a id="s04-p032"></a>
### S04 — page 32

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=32>)

```text
Linear regression in Jamovi
Analyses → Regression → Linear Regression
1. Dependent Variable: your quantitative outcome
2. Covariates: continuous predictors; Factors: qualitative ones
(set the Reference Levels)
3. Model Fit: R, R2, Adjusted R2, F test
4. Model Coefficients: Standardized estimate, confidence interval
5. Assumption Checks: Autocorrelation test, Collinearity
statistics, Q-Q plot of residuals, Residual plots
6. Optional: Save → predicted values, residuals
Read, in this order:
1. Assumption checks —
trustworthy?
2. F test — useful at all?
3. R2 / adjusted R2 — how much?
4. Each p, then B in units
5. β — ranking of drivers
Firm data: log-transform skewed
variables first (Data → Compute:
LN(Turnover) ). Then B reads approxi-
mately as a % effect.
AQD – Session 4 NGUYEN Anh-Tuan 32
```

<a id="s04-p033"></a>
### S04 — page 33

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=33>)

```text
Apply it to your fil rouge dataset
Firm-level data
Y: net profit, or ROI
X: turnover (log), headcount, debt ratio, emis-
sions per employee, sector (factor)
Do greener firms perform better, all else equal?
Customer data
Y: spending, or satisfaction score
X: visits, income, distance, segment (factor)
Build the model in three moves:
1. Start from the predictors your Session 2
correlations flagged
2. Add the grouping variable of Session 3 as a
factor
3. Check VIF: two predictors correlated at r > 0.8?
Keep one.
Aim for a model a manager can read: 3 to 6
predictors, each with a reason to be there.
AQD – Session 4 NGUYEN Anh-Tuan 33
```

<a id="s04-p034"></a>
### S04 — page 34

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=34>)

```text
From four analyses to one recommendation
```

<a id="s04-p035"></a>
### S04 — page 35

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=35>)

```text
The whole course on one slide
SESSION 1
Describe
frequencies, mean,
median, SD, shape
What does my
data look like?
SESSION 2
Relate
χ2 + Cramér’s V
Pearson r / Spearman
Student / Welch t
Are two variables related?
SESSION 3
Compare
ANOVA (Fisher / Welch
/ KW), η2, post-hoc
Do groups differ
— which ones?
SESSION 4
Explain
regression, R2, B, β
What drives my outcome?
One template for all of it: IDENTIFY → HYPOTHESISE → DECIDE (significance and strength)
→ RECOMMEND.
AQD – Session 4 NGUYEN Anh-Tuan 35
```

<a id="s04-p036"></a>
### S04 — page 36

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=36>)

```text
Revision table: one line per method
Method Variables H0 Report Strength
Chi-square 2 qualitative Independent χ2(df ), p Cramér’s V
Pearson / Spearman 2 quantitative (or ordinal) No correlation r (df ), p |r |, r 2
Student / Welch t Quantitative Y , 2 groups
(Levene decides)
Equal means t(df ), p Cohen’s d
One-way ANOVA Quantitative Y , 3+ groups All means equal F (df1, df2), p + post-hoc η2
Fisher + Tukey Levene p > .05
Welch + Games–Howell Levene p ≤ .05
Kruskal–Wallis + DSCF small n, not normal ε2
Bonferroni few planned pairs p × m
Multiple regression Quantitative Y , several X All b = 0 / each
b = 0
F, p; each B, p R 2, adj. R2, β
Opposite logic (p > .05 = good news): Shapiro–
Wilk (normality) and Levene (equal variances).
Always three numbers: the statistic with its df,
the p-value, and the effect size.
AQD – Session 4 NGUYEN Anh-Tuan 36
```

<a id="s04-p037"></a>
### S04 — page 37

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=37>)

```text
The final consulting report
1. Executive summary — 1 page, 3
recommendations
2. Data — source, provenance, cleaning
3. Profile — univariate (S1)
4. Relationships — χ2, r, t-test (S2)
5. Group differences — ANOVA (S3)
6. Drivers — regression (S4)
7. Limits — what the data cannot say
Write the executive summary last — but put it
first.
Each recommendation must be:
• traced to a specific result (“B = 11.83, p < .001”)
• quantified in business units (e, %, customers)
• actionable on Monday morning
Where two sessions disagree (e.g. a raw correlation vs
a controlled regression coefficient), say so and trust
the model. That is analysis.
AQD – Session 4 NGUYEN Anh-Tuan 37
```

<a id="s04-p038"></a>
### S04 — page 38

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=38>)

```text
Errors that cost marks every year
• Interpreting coefficients before checking the F test and the conditions
• Comparing raw B values across variables with different units — use β
• Forgetting “all else being equal” in every interpretation
• Interpreting a non-significant coefficient as a real effect
• Reading the intercept as a meaningful quantity
• Writing “causes” — observational data show associations
• Predicting outside the range of the data
• Putting a qualitative variable in Covariates instead of Factors
AQD – Session 4 NGUYEN Anh-Tuan 38
```

<a id="s04-p039"></a>
### S04 — page 39

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=39>)

```text
What you can now do
1. Identify and justify the appropriate statistical
method for a managerial problem
2. Implement it in Jamovi
3. Interpret the output accurately — and spot
when it is wrong
4. Draw conclusions and formulate actionable
recommendations
These were the four objectives of
Session 1.
Y ou have now done each of them four
times, on your own data.
The software computed. You
decided, interpreted, and recom-
mended.
AQD – Session 4 NGUYEN Anh-Tuan 39
```

<a id="s04-p040"></a>
### S04 — page 40

[Voir cette page dans le PDF](<sources/cours/S04 - Slides (revised).pdf#page=40>)

```text
Questions?
NGUYEN Anh-Tuan
Final report due as announced on the course page.
Good luck!
```
