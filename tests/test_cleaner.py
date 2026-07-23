import pandas as pd

from src.cleaner import clean_nulls


def test_clean_nulls_fills_numeric_values_with_zero():
    df = pd.DataFrame(
        {
            "age": [25, None],
            "annual_salary_eur": [50000, None],
            "occupation": ["Engineer", "Designer"],
        }
    )

    result = clean_nulls(df)

    assert result.loc[1, "age"] == 0
    assert result.loc[1, "annual_salary_eur"] == 0


def test_clean_nulls_fills_text_values_with_unknown():
    df = pd.DataFrame(
        {
            "full_name": ["Ana", None],
            "occupation": [None, "Designer"],
        }
    )

    result = clean_nulls(df)

    assert result.loc[1, "full_name"] == "Unknown"
    assert result.loc[0, "occupation"] == "Unknown"


def test_clean_nulls_does_not_modify_original_dataframe():
    df = pd.DataFrame({"age": [None], "occupation": [None]})

    clean_nulls(df)

    assert pd.isna(df.loc[0, "age"])
    assert pd.isna(df.loc[0, "occupation"])
