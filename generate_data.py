import pandas as pd
import random
from datetime import datetime, timedelta
import os


# Création du dossier destination

DATA_PATH = "data/sample"

os.makedirs(DATA_PATH, exist_ok=True)


# -------------------------
# 1. CUSTOMERS
# -------------------------

def generate_customers():

    cities = [
        "Abidjan",
        "Bouake",
        "Yamoussoukro",
        "Paris",
        "Dakar",
        "Casablanca"
    ]

    countries = [
        "Cote d'Ivoire",
        "France",
        "Senegal",
        "Maroc"
    ]


    customers = []


    for i in range(1,501):

        customers.append({

            "customer_id": i,
            "first_name": f"Customer_{i}",
            "last_name": f"User_{i}",
            "email": f"customer{i}@gmail.com",
            "city": random.choice(cities),
            "country": random.choice(countries)

        })


    df = pd.DataFrame(customers)

    df.to_csv(
        f"{DATA_PATH}/customers.csv",
        index=False
    )


# -------------------------
# 2. PRODUITS
# -------------------------

def generate_produits():

    categories = [
        "Electronics",
        "Smartphone",
        "Fashion",
        "Gaming",
        "Home",
        "Accessories"
    ]


    produits=[]


    for i in range(1,501):

        produits.append({

            "produit_id": i,
            "produit_name": f"Produit_{i}",
            "category": random.choice(categories),
            "price": random.randint(10,3000)

        })


    df=pd.DataFrame(produits)

    df.to_csv(
        f"{DATA_PATH}/produits.csv",
        index=False
    )


# -------------------------
# 3. ORDERS
# -------------------------

def generate_orders():

    orders=[]

    start_date=datetime(2026,1,1)


    for i in range(1,2001):

        orders.append({

            "order_id": i,
            "customer_id": random.randint(1,500),
            "produit_id": random.randint(1,500),
            "quantity": random.randint(1,5),
            "order_date":
            (
                start_date +
                timedelta(
                    days=random.randint(0,365)
                )
            ).strftime("%Y-%m-%d")

        })


    df=pd.DataFrame(orders)

    df.to_csv(
        f"{DATA_PATH}/orders.csv",
        index=False
    )


# -------------------------
# 4. PAYMENTS
# -------------------------

def generate_payments():

    methods=[
        "Mobile Money",
        "Credit Card",
        "PayPal",
        "Bank Transfer"
    ]


    payments=[]


    for i in range(1,2001):

        payments.append({

            "payment_id": i,
            "order_id": i,
            "amount": random.randint(20,10000),
            "payment_method":
            random.choice(methods)

        })


    df=pd.DataFrame(payments)


    df.to_csv(
        f"{DATA_PATH}/payments.csv",
        index=False
    )



# -------------------------
# EXECUTION
# -------------------------

if __name__ == "__main__":


    print("Génération des données...")


    generate_customers()

    generate_produits()

    generate_orders()

    generate_payments()


    print("Données générées avec succès !")