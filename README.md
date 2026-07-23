# 🛒 Ecommerce Data Platform - End-to-End Data Engineering Project


## 📌 Description

Ce projet consiste à construire une plateforme complète de données e-commerce.

L'objectif est de mettre en place un pipeline Data Engineering permettant de :

- générer des données e-commerce ;
- nettoyer et transformer les données ;
- charger les données dans un Data Warehouse PostgreSQL ;
- créer des modèles analytiques ;
- produire des indicateurs business via SQL et Dashboard.


---

# 🏗️ Architecture du projet

            DATA SOURCES
                |
                |
          CSV Raw Data
                |
                |
         Python ETL Pipeline
      (Pandas + SQLAlchemy)
                |
                |
      PostgreSQL Data Warehouse
                |
    -----------------------------
    |                           |




---

# 🛠️ Technologies utilisées


## Langages

- Python 3
- SQL


## Data Engineering

- Pandas
- SQLAlchemy
- PostgreSQL


## Data Visualization

- Streamlit
- Plotly


## Version Control

- Git
- GitHub



---

# 📂 Structure du projet

ecommerce-data-platform

│
├── data
│ ├── raw
│ └── cleansed
│
├── pipelines
│ └── loading.py
│
├── warehouse
│ └── models
│
├── database
│ └── connection.py
│
├── dashboard
│ └── app.py
│
├── sql
│
├── config
│
├── requirements.txt
│
├── docker-compose.yml
│
└── README.md



---

# 🔄 Pipeline ETL


## 1. Extraction

Lecture des fichiers CSV :

- customers.csv
- produits.csv
- payments.csv
- orders.csv


## 2. Transformation

Nettoyage :

- gestion des valeurs manquantes ;
- contrôle des types ;
- préparation des tables analytiques.


## 3. Loading

Chargement dans PostgreSQL :

Tables dimensions :

- dim_customers
- dim_produits
- dim_payments
- dim_date


Table de faits :

- fact_orders


---

# ⭐ Modèle Data Warehouse


Le projet utilise un modèle en étoile :

         dim_customers
                |
                |

dim_produits ---- fact_orders ---- dim_date
|
|
dim_payments



---

# 📊 Analyses SQL disponibles


## KPI principaux


### Chiffre d'affaires

```sql
SELECT SUM(total_amount)
FROM fact_orders;

Nombre de commandes

SELECT COUNT(order_id)
FROM fact_orders;

Top produits

SELECT produit_id,
SUM(quantity)
FROM fact_orders
GROUP BY produit_id;

🚀 Installation
Cloner le projet

git clone https://github.com/username/ecommerce-data-platform.git

Entrer dans le dossier :

cd ecommerce-data-platform

Installer les dépendances

pip install -r requirements.txt

🗄️ Configuration PostgreSQL

Créer la base :

CREATE DATABASE ecommerce_dw;

Configurer la connexion dans :

config/settings.py
▶️ Exécuter le pipeline
python pipelines/loading.py
📊 Lancer le dashboard
streamlit run dashboard/app.py

Le dashboard sera disponible :

http://localhost:8501
📈 Dashboard

Fonctionnalités :

✅ Chiffre d'affaires total

✅ Nombre de commandes

✅ CA par pays

✅ Top produits

✅ Evolution mensuelle des ventes

🎯 Compétences démontrées

Ce projet met en avant :

Data Pipeline ETL
Data Warehouse Design
Star Schema Modeling
SQL Analytics
Python Data Engineering
PostgreSQL
BI Dashboard
Git Workflow

👨‍💻 Auteur

Gnabo Fabrice

Data Engineer 

Côte d'Ivoire


---

## 2) Enregistrer puis envoyer sur GitHub

Dans PowerShell :

```powershell
git add README.md

Puis :

git commit -m "Improve project documentation README"

Puis :

git push