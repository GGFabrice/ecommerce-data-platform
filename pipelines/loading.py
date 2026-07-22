import pandas as pd
from sqlalchemy import create_engine


# ==========================
# CONNEXION POSTGRESQL
# ==========================

DATABASE_URL = (
    "postgresql://postgres:Esther123@localhost:5432/ecommerce_dw"
)

engine = create_engine(DATABASE_URL)


PATH = "data/cleansed/"


# ==========================
# CUSTOMERS
# ==========================

def load_customers():

    print("\n📌 Chargement Customers")

    df = pd.read_csv(
        PATH + "customers.csv"
    )

    print(df.head())


    df.to_sql(
        "dim_customers",
        engine,
        if_exists="append",
        index=False
    )


    print("✅ Customers chargés")



# ==========================
# PRODUITS
# ==========================

def load_produits():

    print("\n📌 Chargement Produits")

    df = pd.read_csv(
        PATH + "produits.csv"
    )


    print(df.head())


    df.to_sql(
        "dim_produits",
        engine,
        if_exists="append",
        index=False
    )


    print("✅ Produits chargés")



# ==========================
# PAYMENTS
# ==========================

def load_payments():

    print("\n📌 Chargement Payments")

    df = pd.read_csv(
        PATH + "payments.csv"
    )


    print(df.head())


    df.to_sql(
        "dim_payments",
        engine,
        if_exists="append",
        index=False
    )


    print("✅ Payments chargés")



# ==========================
# DIM DATE
# ==========================

def load_date():

    print("\n📌 Chargement Dim Date")


    df_orders = pd.read_csv(
        PATH + "orders.csv"
    )


    df_orders["order_date"] = pd.to_datetime(
        df_orders["order_date"]
    )


    df_date = pd.DataFrame()


    df_date["full_date"] = (
        df_orders["order_date"]
        .drop_duplicates()
    )


    df_date["day"] = (
        df_date["full_date"]
        .dt.day
    )


    df_date["month"] = (
        df_date["full_date"]
        .dt.month
    )


    df_date["year"] = (
        df_date["full_date"]
        .dt.year
    )


    print(df_date.head())


    df_date.to_sql(
        "dim_date",
        engine,
        if_exists="append",
        index=False
    )


    print("✅ Dim Date chargée")



# ==========================
# FACT ORDERS
# ==========================

def load_orders():

    print("\n📌 Chargement Orders")


    df_orders = pd.read_csv(
        PATH + "orders.csv"
    )


    df_payments = pd.read_csv(
        PATH + "payments.csv"
    )


    # Ajouter payment_id

    df_orders = df_orders.merge(
        df_payments[
            [
                "order_id",
                "payment_id",
                "amount"
            ]
        ],
        on="order_id",
        how="left"
    )


    # Ajouter date_id

    df_date = pd.read_sql(
        """
        SELECT
            date_id,
            full_date
        FROM dim_date
        """,
        engine
    )


    df_orders["order_date"] = pd.to_datetime(
        df_orders["order_date"]
    )


    df_date["full_date"] = pd.to_datetime(
        df_date["full_date"]
    )


    df_orders = df_orders.merge(
        df_date,
        left_on="order_date",
        right_on="full_date",
        how="left"
    )


    # Renommer montant

    df_orders.rename(
        columns={
            "amount":"total_amount"
        },
        inplace=True
    )


    # Sélection finale FACT

    df_fact = df_orders[
        [
            "order_id",
            "customer_id",
            "produit_id",
            "payment_id",
            "date_id",
            "quantity",
            "total_amount",
            "order_date"
        ]
    ]


    print(df_fact.head())


    df_fact.to_sql(
        "fact_orders",
        engine,
        if_exists="append",
        index=False
    )


    print("✅ Orders chargées")



# ==========================
# EXECUTION PIPELINE
# ==========================

if __name__ == "__main__":


    print(
        "\n🚀 Début du chargement Data Warehouse"
    )


    load_customers()

    load_produits()

    load_payments()

    load_date()

    load_orders()


    print(
        "\n🎉 Chargement terminé avec succès"
    )