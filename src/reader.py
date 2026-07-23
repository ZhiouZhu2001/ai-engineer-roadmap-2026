from pathlib import Path

import pandas as pd


def read_csv(csv_path):
    path = Path(csv_path)
    if path.suffix.lower() != ".csv":
        raise ValueError("File must be a CSV.")
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    return pd.read_csv(path)
