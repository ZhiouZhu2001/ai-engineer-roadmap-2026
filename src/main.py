import json
from pathlib import Path

from analyzer import (
    average_salary,
    average_salary_by_age,
    average_salary_by_english_level,
    average_salary_by_industry,
    average_salary_by_occupation,
    average_salary_by_skills,
    choose_salary_average_option,
)
from cleaner import clean_nulls, clean_numeric_anomalies
from reader import read_csv


SALARY_AVERAGE_FUNCTIONS = {
    "occupation": average_salary_by_occupation,
    "age": average_salary_by_age,
    "industry": average_salary_by_industry,
    "skills": average_salary_by_skills,
    "english_level": average_salary_by_english_level,
    "all": average_salary,
}


def save_result_to_json(result, output_path="output/result.json"):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    return path


def run_salary_analysis(csv_path="data/Professional_data.csv", output_path="output/result.json"):
    df = read_csv(csv_path)
    df = clean_nulls(df)
    df = clean_numeric_anomalies(df)

    option = choose_salary_average_option()
    result = {
        "calculation": "average_salary",
        "option": option,
        "result": SALARY_AVERAGE_FUNCTIONS[option](df),
    }

    saved_path = save_result_to_json(result, output_path)
    print(f"Result saved to {saved_path}")
    return saved_path


if __name__ == "__main__":
    run_salary_analysis()
