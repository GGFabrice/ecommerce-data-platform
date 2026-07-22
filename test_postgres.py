import psycopg2
import traceback

try:
    print("Connexion en cours...")

    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="ecommerce_dw",
        user="postgres",
        password="Esther123"
    )

    print("Connexion réussie !")

    conn.close()

except Exception:
    traceback.print_exc()