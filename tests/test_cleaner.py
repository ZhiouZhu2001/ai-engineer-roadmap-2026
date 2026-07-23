import pandas as pd

from src.cleaner import clean_nulls, clean_numeric_anomalies


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


def test_clean_numeric_anomalies_converts_valid_numeric_strings():
    df = pd.DataFrame(
        {
            "age": ["29"],
            "annual_salary_eur": ["37000"],
            "job_satisfaction_score": ["8"],
        }
    )

    result = clean_numeric_anomalies(df)

    assert result.loc[0, "age"] == 29
    assert result.loc[0, "annual_salary_eur"] == 37000
    assert result.loc[0, "job_satisfaction_score"] == 8


def test_clean_numeric_anomalies_replaces_invalid_text_with_zero():
    df = pd.DataFrame(
        {
            "age": ["twenty-nine"],
            "annual_salary_eur": ["not-a-salary"],
        }
    )

    result = clean_numeric_anomalies(df)

    assert result.loc[0, "age"] == 0
    assert result.loc[0, "annual_salary_eur"] == 0


def test_clean_numeric_anomalies_replaces_outliers_with_zero():
    df = pd.DataFrame(
        {
            "age": [12],
            "years_experience": [80],
            "annual_salary_eur": [-1],
            "remote_work_days_per_week": [9],
            "job_satisfaction_score": [11],
        }
    )

    result = clean_numeric_anomalies(df)

    assert result.loc[0, "age"] == 0
    assert result.loc[0, "years_experience"] == 0
    assert result.loc[0, "annual_salary_eur"] == 0
    assert result.loc[0, "remote_work_days_per_week"] == 0
    assert result.loc[0, "job_satisfaction_score"] == 0
