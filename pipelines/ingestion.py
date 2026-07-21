import os
import shutil
import logging
from datetime import datetime


# Configuration du logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Chemins

SOURCE_PATH = "data/sample"

RAW_PATH = "data/raw"


FILES = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "payments.csv"
]


def create_folder(path):

    """
    Création d'un dossier s'il n'existe pas
    """

    if not os.path.exists(path):

        os.makedirs(path)

        logging.info(
            f"Dossier créé : {path}"
        )



def copy_file(file):

    """
    Copie un fichier vers RAW
    """

    source = os.path.join(
        SOURCE_PATH,
        file
    )

    destination = os.path.join(
        RAW_PATH,
        file
    )


    if os.path.exists(source):

        shutil.copy(
            source,
            destination
        )

        logging.info(
            f"{file} chargé dans RAW"
        )


    else:

        logging.error(
            f"Fichier introuvable : {file}"
        )



def ingestion_pipeline():

    """
    Pipeline principal d'ingestion
    """

    start_time = datetime.now()


    logging.info(
        "Début du pipeline ingestion"
    )


    create_folder(RAW_PATH)



    for file in FILES:

        copy_file(file)



    end_time = datetime.now()


    duration = end_time - start_time


    logging.info(
        f"Pipeline terminé en {duration}"
    )



if __name__ == "__main__":

    ingestion_pipeline()