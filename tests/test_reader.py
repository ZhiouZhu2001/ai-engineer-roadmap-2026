import pandas as pd
import pytest

from src.reader import read_csv


def test_read_csv_returns_dataframe():
    result = read_csv("data/Professional_data.csv")

    assert isinstance(result, pd.DataFrame)
    assert "occupation" in result.columns
    assert "annual_salary_eur" in result.columns
    assert not result.empty


def test_read_csv_requires_csv_extension():
    with pytest.raises(ValueError):
        read_csv("README.md")


def test_read_csv_requires_existing_file():
    with pytest.raises(FileNotFoundError):
        read_csv("data/missing.csv")
