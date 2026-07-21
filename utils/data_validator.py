import pandas as pd

def validate_dataframe(df: pd.DataFrame):
    """
    Retourne quelques indicateurs de qualité.
    """

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
    }

    return report