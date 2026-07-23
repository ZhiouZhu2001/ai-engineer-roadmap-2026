import pandas as pd


def clean_nulls(df):
    cleaned = df.copy()
    numeric_columns = cleaned.select_dtypes(include="number").columns
    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns

    cleaned[numeric_columns] = cleaned[numeric_columns].fillna(0)
    cleaned[text_columns] = cleaned[text_columns].fillna("Unknown")

    return cleaned
