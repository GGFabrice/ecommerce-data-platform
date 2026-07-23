from pathlib import Path
from dotenv import load_dotenv
import os

# Racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Charger le fichier .env
load_dotenv(BASE_DIR / ".env")

# Paramètres PostgreSQL
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "ecommerce_dw")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")