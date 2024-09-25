import json  # Importation du module JSON pour manipuler les données JSON
import random  # Importation du module Random pour générer des valeurs aléatoires
import time
# Importation du module Faker pour générer des données factices
from faker import Faker
# Importation du producteur Kafka SerializingProducer
from confluent_kafka import SerializingProducer
# Importation de la classe datetime pour manipuler les dates et heures
from datetime import datetime
# Initialisation de Faker pour générer des données factices
fake = Faker()

def generate_sales_transactions():
    # Génération d'un profil utilisateur factice
    user = fake.simple_profile()
    return {
        # Génération d'un ID de transaction UUID
        "transactionId": fake.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),  # Choix aléatoire d'un ID de produit
        "productName": random.choice(['laptop', 'mobile', 'tablet', 'watch', 'headphone', 'speaker']),  # Choix aléatoire du nom du produit
        'productCategory': random.choice(['electronic', 'fashion', 'grocery', 'home', 'beauty', 'sports']),  # Choix aléatoire de la catégorie du produit
        'productPrice': round(random.uniform(10, 1000), 2),  # Prix aléatoire du produit
        'productQuantity': random.randint(1, 10),  # Quantité aléatoire du produit
        'productBrand': random.choice(['apple', 'samsung', 'oneplus', 'mi', 'boat', 'sony']),  # Marque aléatoire du produit
        'currency': random.choice(['USD', 'GBP']),  # Choix aléatoire de la devise
        'customerId': user['username'],  # ID client à partir du profil généré
        'transactionDate': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f%z'),  # Date et heure actuelles au format UTC
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer'])  # Méthode de paiement aléatoire
    }

def delivery_report(err, msg):
    if err is not None:
        # Affichage en cas d'échec de livraison du message
        print(f'Message delivery failed: {err}')
    else:
        # Affichage en cas de livraison réussie du message
        print(f"Message delivered to {msg.topic} [{msg.partition()}]")

def main():
    # Nom du topic Kafka
    topic = 'financial_transactions'
    producer= SerializingProducer({
        # Configuration du serveur Kafka
        'bootstrap.servers': 'localhost:9092'
    })
    # Heure actuelle
    curr_time = datetime.now()  # Heure actuelle

    while (datetime.now() - curr_time).seconds < 300:  # Boucle pendant 300 secondes (5 minutes)
        try:
            transaction = generate_sales_transactions()  # Génération d'une transaction
            transaction['totalAmount'] = transaction['productPrice'] * transaction['productQuantity']  # Calcul du montant total de la transaction
            # Affichage de la transaction générée
            print(transaction)

            producer.produce(topic,  # Envoi de la transaction au topic Kafka
                             key=transaction['transactionId'],  # Clé de la transaction
                             value=json.dumps(transaction),  # Conversion de la transaction en JSON
                             on_delivery=delivery_report  # Appel à la fonction de rapport de livraison
                             )
            # Appel à la méthode poll du producteur Kafka
            producer.poll(0)

            # Attente de 5 secondes avant d'envoyer la prochaine transaction
            time.sleep(5)
        except BufferError:
            # Affichage en cas de buffer plein
            print("Buffer full! Waiting...")
            # Affichage en cas de buffer plein
            time.sleep(1)
        except Exception as e:
            # Affichage de toute autre exception rencontrée
            print(e)

if __name__ == "__main__":
    # Appel de la fonction principale si le script est exécuté directement
    main()
