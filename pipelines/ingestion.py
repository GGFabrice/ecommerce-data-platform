from pathlib import Path
import shutil
from datetime import datetime

from config.settings import SAMPLE_DIR, RAW_DIR, REPORT_DIR
from config.logger import logger
from utils.file_manager import get_csv_files, count_rows

REPORT_DIR.mkdir(exist_ok=True)

def ingest_files():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    csv_files = get_csv_files(SAMPLE_DIR)

    if not csv_files:
        logger.warning("Aucun fichier CSV trouvé dans data/sample")
        print("Aucun fichier CSV trouvé.")
        return

    report_lines = []

    for file in csv_files:
        destination = RAW_DIR / file.name
        shutil.copy(file, destination)

        rows = count_rows(file)

        logger.info(f"{file.name} copié vers RAW ({rows} lignes)")

        report_lines.append(f"{file.name} : {rows} lignes")

        print(f"✔ {file.name} copié ({rows} lignes)")

    report_file = REPORT_DIR / f"ingestion_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write("RAPPORT D'INGESTION\n")
        f.write("====================\n\n")
        for line in report_lines:
            f.write(line + "\n")

    print("\nIngestion terminée avec succès.")
    print(f"Rapport généré : {report_file.name}")

if __name__ == "__main__":
    ingest_files()