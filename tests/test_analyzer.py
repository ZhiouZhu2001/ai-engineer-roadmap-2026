import pandas as pd
import pytest

from src.analyzer import (
    average_salary,
    average_salary_by_age,
    average_salary_by_english_level,
    average_salary_by_industry,
    average_salary_by_occupation,
    average_salary_by_skills,
    choose_salary_average_option,
    count_professionals,
)


def test_count_professionals_returns_number_of_rows():
    df = pd.DataFrame(
        {
            "full_name": ["Ana", "Luis", "Marta"],
            "occupation": ["Engineer", "Designer", "Engineer"],
        }
    )

    result = count_professionals(df)

    assert result == {"count": 2, "occupations": ["Designer", "Engineer"]}


def test_count_professionals_returns_zero_for_empty_dataframe():
    df = pd.DataFrame(columns=["full_name", "occupation"])

    result = count_professionals(df)

    assert result == {"count": 0, "occupations": []}


def test_count_professionals_ignores_null_occupations():
    df = pd.DataFrame({"occupation": ["Teacher", None, "Teacher"]})

    result = count_professionals(df)

    assert result == {"count": 1, "occupations": ["Teacher"]}


def test_choose_salary_average_option_returns_valid_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: " 1 ")

    result = choose_salary_average_option()

    assert result == "occupation"


def test_choose_salary_average_option_raises_for_invalid_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "city")

    with pytest.raises(ValueError):
        choose_salary_average_option()


def test_choose_salary_average_option_returns_all_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "6")

    result = choose_salary_average_option()

    assert result == "all"


def test_average_salary_returns_overall_average():
    df = pd.DataFrame({"annual_salary_eur": [30000, 50000, 70000]})

    result = average_salary(df)

    assert result == 50000.0


def test_average_salary_ignores_invalid_and_missing_values():
    df = pd.DataFrame({"annual_salary_eur": ["30000", "bad-value", None, "60000"]})

    result = average_salary(df)

    assert result == 45000.0


def test_average_salary_returns_zero_without_valid_salaries():
    df = pd.DataFrame({"annual_salary_eur": ["bad-value", None]})

    result = average_salary(df)

    assert result == 0


def test_average_salary_by_occupation():
    df = pd.DataFrame(
        {
            "occupation": ["Engineer", "Designer", "Engineer"],
            "annual_salary_eur": [60000, 40000, 80000],
        }
    )

    result = average_salary_by_occupation(df)

    assert result == {"Designer": 40000.0, "Engineer": 70000.0}


def test_average_salary_by_age():
    df = pd.DataFrame(
        {
            "age": ["25", "30", "25", "unknown"],
            "annual_salary_eur": [30000, 50000, 50000, 90000],
        }
    )

    result = average_salary_by_age(df)

    assert result == {25: 40000.0, 30: 50000.0}


def test_average_salary_by_industry():
    df = pd.DataFrame(
        {
            "industry": ["Tech", "Education", "Tech"],
            "annual_salary_eur": [70000, 30000, "bad-value"],
        }
    )

    result = average_salary_by_industry(df)

    assert result == {"Education": 30000.0, "Tech": 70000.0}


def test_average_salary_by_skills():
    df = pd.DataFrame(
        {
            "skills": ["Python; SQL", "Python; Excel", None],
            "annual_salary_eur": [60000, 40000, 100000],
        }
    )

    result = average_salary_by_skills(df)

    assert result == {"Excel": 40000.0, "Python": 50000.0, "SQL": 60000.0}


def test_average_salary_by_english_level():
    df = pd.DataFrame(
        {
            "english_level": ["B2", "C1", "B2"],
            "annual_salary_eur": [50000, 70000, 60000],
        }
    )

    result = average_salary_by_english_level(df)

    assert result == {"B2": 55000.0, "C1": 70000.0}
