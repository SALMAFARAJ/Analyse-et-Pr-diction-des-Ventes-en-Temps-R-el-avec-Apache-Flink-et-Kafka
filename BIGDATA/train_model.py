import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation des données
import psycopg2  # Importation de la bibliothèque psycopg2 pour la connexion à PostgreSQL
from sklearn.linear_model import \
    LinearRegression  # Importation de LinearRegression de sklearn pour les modèles de régression linéaire


# Fonction pour charger les données depuis PostgreSQL
def load_data():

    # Connexion à la base de données PostgreSQL avec les informations d'identification
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='root', host='localhost', port='5432')
    cursor = conn.cursor()  # Création d'un curseur pour exécuter les commandes SQL

    # Définition de la requête SQL pour sélectionner les colonnes souhaitées
    query = """
    SELECT transaction_date, product_category, total_amount
    FROM transactions
    """
    cursor.execute(query)  # Exécution de la requête SQL
    data = cursor.fetchall()  # Récupération des résultats de la requête

    # Création d'un DataFrame pandas à partir des résultats de la requête
    df = pd.DataFrame(data, columns=['transaction_date', 'product_category', 'total_amount'])
    df['transaction_date'] = pd.to_datetime(
        df['transaction_date'])  # Conversion de la colonne transaction_date en datetime

    cursor.close()  # Fermeture du curseur
    conn.close()  # Fermeture de la connexion à la base de données

    return df  # Retourne le DataFrame contenant les données des transactions


# Fonction pour entraîner les modèles par catégorie de produit
def train_models(df):

    models = {}  # Initialisation d'un dictionnaire pour stocker les modèles par catégorie de produit
    categories = df['product_category'].unique()  # Récupération des catégories de produit uniques

    for category in categories:  # Boucle sur chaque catégorie de produit
        df_category = df[df['product_category'] == category].copy()  # Filtrage des données pour la catégorie en cours
        df_category['year'] = df_category['transaction_date'].dt.year  # Ajout d'une colonne pour l'année
        df_category['month'] = df_category['transaction_date'].dt.month  # Ajout d'une colonne pour le mois
        df_category['day'] = df_category['transaction_date'].dt.day  # Ajout d'une colonne pour le jour

        X = df_category[
            ['year', 'month', 'day']]  # Sélection des caractéristiques (année, mois, jour) pour l'entraînement
        y = df_category['total_amount']  # Variable cible (montant total des ventes)

        model = LinearRegression()  # Initialisation d'un modèle de régression linéaire
        model.fit(X, y)  # Entraînement du modèle avec les caractéristiques et la variable cible
        models[category] = model  # Ajout du modèle entraîné au dictionnaire avec la catégorie comme clé

    return models  # Retourne le dictionnaire des modèles par catégorie de produit


# Fonction pour générer des prédictions pour une date spécifique pour chaque catégorie de produit
def generate_predictions(models, prediction_date):

    predictions = []  # Initialisation d'une liste pour stocker les prédictions
    year = prediction_date.year  # Extraction de l'année de la date de prédiction
    month = prediction_date.month  # Extraction du mois de la date de prédiction
    day = prediction_date.day  # Extraction du jour de la date de prédiction

    for category, model in models.items():  # Boucle sur chaque catégorie de produit et son modèle associé
        # Création d'un DataFrame pour les caractéristiques de la date de prédiction
        future_data = pd.DataFrame({
            'year': [year],  # Année de la date de prédiction
            'month': [month],  # Mois de la date de prédiction
            'day': [day],  # Jour de la date de prédiction
            'date': [prediction_date],  # Date de prédiction
            'product_category': [category]  # Catégorie de produit
        })
        future_data['predicted_sales'] = model.predict(future_data[['year', 'month', 'day']])  # Prédiction des ventes
        predictions.append(future_data)  # Ajout des prédictions à la liste

    return pd.concat(predictions)  # Retourne un DataFrame concaténé avec toutes les prédictions


# Fonction pour sauvegarder les prédictions dans PostgreSQL
def save_predictions_to_db(predictions_df):

    conn = psycopg2.connect(dbname='postgres', user='postgres', password='root', host='localhost',
                            port='5432')  # Connexion à la base de données
    cursor = conn.cursor()  # Création d'un curseur pour exécuter les commandes SQL

    # Création de la table pour les prédictions par catégorie si elle n'existe pas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_predictions_by_category (
        date DATE,
        product_category VARCHAR,
        predicted_sales FLOAT
    )
    """)

    # Création de la table pour les prédictions globales si elle n'existe pas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_predictions (
        date DATE,
        predicted_sales FLOAT
    )
    """)

    # Boucle sur chaque ligne du DataFrame des prédictions
    for i, row in predictions_df.iterrows():
        # Insertion des données de prédiction dans la table des prédictions par catégorie
        cursor.execute("""
        INSERT INTO sales_predictions_by_category (date, product_category, predicted_sales)
        VALUES (%s, %s, %s)
        """, (row['date'], row['product_category'], row['predicted_sales']))

    conn.commit()  # Validation des transactions
    cursor.close()  # Fermeture du curseur
    conn.close()  # Fermeture de la connexion à la base de données


if __name__ == "__main__":
    # Charger les données depuis PostgreSQL
    df = load_data()
    # Entraîner les modèles de régression linéaire pour chaque catégorie de produit
    models = train_models(df)

    # Définir une date de prédiction spécifique
    prediction_date = pd.Timestamp('2025-01-01')
    # Générer les prédictions pour la date spécifique
    predictions_df = generate_predictions(models, prediction_date)

    # Sauvegarder les prédictions dans la base de données PostgreSQL
    save_predictions_to_db(predictions_df)

    print("Prédictions pour le 2025-01-01 par catégorie sauvegardées dans la base de données avec succès")
