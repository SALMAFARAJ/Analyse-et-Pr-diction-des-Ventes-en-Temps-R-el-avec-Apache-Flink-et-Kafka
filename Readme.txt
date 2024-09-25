Projet BIGDATA - Analyse et Prévision des Ventes

Membres du Groupe :
Salma Faraj
Salwa Faraj
Rabab Razik
Wissal Ryad

Structure du Projet :
1. Dossier flinkCom
Ce dossier contient le projet Java Flink qui permet le traitement des données en temps réel.

Contenu Principal :

flinkCom : Ce projet Java configure et exécute un job Flink pour traiter des flux de transactions financières en provenance de Kafka, et les stocker dans une base de données PostgreSQL. Les principales fonctionnalités incluent :
Lecture des données de Kafka.
Création de tables dans PostgreSQL pour stocker les transactions, les ventes par catégorie, par jour et par mois.
Insertion et mise à jour des transactions dans la base de données.
Agrégation des ventes par catégorie, par jour et par mois et stockage de ces agrégations dans PostgreSQL.
2. Dossier BIGDATA
Ce dossier contient les configurations Docker et les scripts nécessaires pour générer des flux de données avec Kafka, ainsi qu'un code de prédiction de ventes utilisant le machine learning. De plus, il inclut des fichiers pour la visualisation des analyses et des prédictions avec Power BI.

Contenu Principal :

docker-compose.yml : Fichier de configuration Docker qui met en place les services nécessaires, y compris Kafka, Zookeeper, et PostgreSQL. Ce fichier permet de lancer facilement tous les services requis pour le projet.
Kafka Scripts : Scripts pour générer et envoyer des flux de données vers Kafka.
Code de Prédiction des Ventes :
Machine Learning : Scripts et modèles pour prédire les ventes futures basés sur les données historiques. Ces scripts utilisent des bibliothèques de machine learning pour entraîner et évaluer les modèles de prédiction.
Power BI Files :
Fichiers de Visualisation : Rapports et tableaux de bord Power BI pour visualiser les analyses et les prédictions. Ces visualisations permettent de comprendre les tendances des ventes et d'anticiper les futures performances.
Description Détaillée des Composants
1. Traitement des Données avec Flink (flinkCom)
Le projet Flink est conçu pour traiter des flux de transactions en temps réel. Voici une vue d'ensemble de son fonctionnement :

Lecture des Données de Kafka : Utilise KafkaSource pour consommer des messages de transactions financières.
Transformation des Données : Les transactions sont transformées et agrégées pour calculer les ventes par catégorie, par jour et par mois.
Stockage des Données : Les résultats sont stockés dans une base de données PostgreSQL pour un accès et une analyse ultérieurs.
2. Génération et Prévision des Données (BIGDATA)
Configuration Docker : Le fichier docker-compose.yml simplifie le déploiement des services nécessaires, comme Kafka et PostgreSQL.
Génération de Flux Kafka : Les scripts Kafka génèrent des flux de transactions simulées pour alimenter le job Flink.
Prédiction des Ventes :
Utilise des modèles de machine learning pour prédire les ventes futures.
Les prédictions sont basées sur les données agrégées et historiques des ventes.
Visualisation avec Power BI :
Les fichiers Power BI permettent de créer des rapports interactifs et des tableaux de bord pour analyser les données et les prédictions.
Facilite la prise de décisions basée sur les données en fournissant des insights visuels sur les tendances des ventes.