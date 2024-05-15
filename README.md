# APRES
### Aide au Pilotage pour le Réseau Emploi pour le Suivi de parcours

![Logo APRES](/hackathon-dsn/logo_moche.svg)

Outiller les acteurs de l’emploi en continu dans le suivi des parcours des personnes par dispositif.

## 🔎 Contexte

Ce projet a été réalisé au cours du Hackathon DSN du 14 et 15 mai 2024 organisé événement par le département Etalab de la Direction interministérielle du numérique (DINUM), en partenariat avec le Ministère du Travail, de la Santé et des Solidarités, le GIP-MDS et la mission interministérielle de pilotage de la collecte et de l’usage des données sociales (MIDS).

## Constitution de l'équipe

### 🏘️ Structures

L’équipe est composée de 11 personnes, représentant 5 structures de l’écosystème Insertion, emploi, travail.
* [ETCLD](https://etcld.fr/) - Fonds d’expérimentation territoriale contre le chômage de longue durée
* [Spirkop](https://www.spirkop.com/fr/) - Société coopérative de développement informatique collaborant avec le Fonds ETCLD
* [Bim Bam Job](https://www.bimbamjob.fr/) - Entreprise sociale et solidaire qui crée, imagine et déploie des dispositifs d'insertion socio-professionnelle
* [Hello Elton](https://www.helloelton.com/) - Entreprise sociale et solidaire qui oeuvre pour l’insertion professionnelle via la formation
* [Plateforme de l’Inclusion](https://inclusion.beta.gouv.fr/) - Groupement d'intérêt public qui crée des services numériques gratuits, pour faciliter la vie des personnes éloignées de l'emploi et de celles et ceux qui les accompagnent
* [data.gouv](https://www.data.gouv.fr/fr/) : Plateforme d’open data de l’Etat

### 👥 Participants

* Aurélie Marre, experte métier
* Stéphane Pomares, expert métier
* Maëlle Toullic, experte métier
* Claire Casubolo, experte métier
* Yannick Passarelli, data scientist
* Edgar Loriot, data scientist
* Lucie Le Rolland, développeuse
* Kévin Aupée, développeur
* Romain Le Gonidec, développeur
* Geoffrey Aldebert, développeur
* Hugo Robellaz, développeur et expert métier

## 🌸 Rendu

### Description

* *Problématique et proposition de valeur.*
* *A quelle problématique s’attaque votre projet ?*
* *Quelle est votre proposition de valeur ?*

### Solution

* *Description de la solution et de ses fonctionnalités*
* *Quel usage est fait des données ? Que vous permettent-elles de faire ?*
* *Quelle est la méthode de création de la solution ?*

### Impact envisagé

* *Que permet de faire la solution ?*
* *Qui sont les usagers visés, et qu’en feraient-ils ?*

### 📑 Ressources

* [Documentation du projet](https://docs.google.com/document/d/1JdpwF7pjL_Ypjh1ReTph-7AocaGXsjiB8OspVxVMiLg)
* [Slides de présentation](https://www.canva.com/design/DAGFSHum68s/jNwJmUF7TDTgW74IOW9PjQ)

### [Facultatif] Retours sur la qualité des données exploitées

* *Quelles sont les difficultés que vous avez rencontrées dans l’usage des données ?*

## Tech

Dans le cadre du hackathon, un mini site web a été développé en utilisant FastAPI et VueJS.
Ce site web incorpore un tableau de bord Metabase utilisant les données disponibles lors du hackathon.
Etant donné le contexte, ce tableau de bord n'est pas accessible au-delà de la démo présentée.

### Installation & lancement

```
pip install -r requirements.txt
cd hackathon-dsn
npm install
```

Dans deux fenêtres différentes :
* Au sein du dossier racine : `fastapi dev main.py`
* Au sein du dossier /hackathon-dsn/ : `npm run dev`

### Données

Les données affichées lors de la démonstration sont des données agrégées à partir du jeu de données mis à disposition lors du hackathon.
