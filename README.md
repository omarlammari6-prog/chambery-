\# Georeferenced Irradiance \& Temperature Analysis – Chambéry, France



Ce projet présente un workflow scientifique reproductible pour analyser

l’irradiance solaire et la température de l’air à partir de données

géoréférencées issues de Copernicus.



\## Objectif

\- Télécharger des données climatiques (irradiance + température)

\- Nettoyer et fusionner les données dans un dataset unique

\- Produire une carte et une série temporelle



\## Région et période étudiées

\- Région : Chambéry, France

\- Période : Janvier 2023

\- Zone définie par une bounding box dans `step1\_data\_extraction/config.py`



\## Structure du dépôt

\- `step1\_data\_extraction/` : téléchargement des données (ERA5 \& CAMS)

\- `step2\_processing/` : nettoyage et fusion des données

\- `step3\_analysis\_visualization/` : visualisations (carte et série temporelle)

\- `data/raw/` : données brutes

\- `data/processed/` : données fusionnées

\- `data/outputs/` : figures générées



\## Prérequis

\- Python 3.x

\- Un compte Copernicus Climate Data Store

\- Configuration de l’API Copernicus (`cdsapi` et fichier `.cdsapirc`)

\- Acceptation des licences des jeux de données Copernicus



Documentation officielle :

https://cds.climate.copernicus.eu/how-to-api



\## Installation

Depuis la racine du projet :

```bash

pip install -r requirements.txt



