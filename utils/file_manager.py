from pathlib import Path
import pandas as pd

def get_csv_files(folder: Path):
    return list(folder.glob("*.csv"))

def read_csv(file_path: Path):
    return pd.read_csv(file_path)