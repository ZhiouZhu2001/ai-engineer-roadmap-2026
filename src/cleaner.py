import pandas as pd


NUMERIC_RANGES = {
    "age": (16, 100),
    "years_experience": (0, 60),
    "annual_salary_eur": (0, 300000),
    "remote_work_days_per_week": (0, 5),
    "job_satisfaction_score": (1, 10),
}


def clean_nulls(df):
    cleaned = df.copy()
    numeric_columns = cleaned.select_dtypes(include="number").columns
    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns

    cleaned[numeric_columns] = cleaned[numeric_columns].fillna(0)
    cleaned[text_columns] = cleaned[text_columns].fillna("Unknown")

    return cleaned


def clean_numeric_anomalies(df):
    cleaned = df.copy()

    for column, (minimum, maximum) in NUMERIC_RANGES.items():
        if column not in cleaned.columns:
            continue

        values = pd.to_numeric(cleaned[column], errors="coerce").fillna(0)
        cleaned[column] = values.where(values.between(minimum, maximum), 0)

    return cleaned
