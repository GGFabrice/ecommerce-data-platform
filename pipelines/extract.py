import pandas as pd


def extract_data():

    customers = pd.read_csv("data/raw/customers.csv")

    produits = pd.read_csv("data/raw/produits.csv")

    orders = pd.read_csv("data/raw/orders.csv")

    return customers, produits, orders