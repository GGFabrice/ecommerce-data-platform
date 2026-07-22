from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
print("DB_HOST =", repr(DB_HOST))
print("DB_PORT =", repr(DB_PORT))
print("DB_NAME =", repr(DB_NAME))
print("DB_USER =", repr(DB_USER))
print("DB_PASSWORD =", repr(DB_PASSWORD))