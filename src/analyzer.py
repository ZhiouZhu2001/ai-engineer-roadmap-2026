import pandas as pd


def count_professionals(df):
    occupations = sorted(df["occupation"].dropna().unique().tolist())
    return {"count": len(occupations), "occupations": occupations}


def average_salary(df):
    salaries = pd.to_numeric(df["annual_salary_eur"], errors="coerce").dropna()
    if salaries.empty:
        return 0

    return float(salaries.mean())


def _average_salary_by_column(df, column):
    data = df[[column, "annual_salary_eur"]].copy()
    data["annual_salary_eur"] = pd.to_numeric(data["annual_salary_eur"], errors="coerce")
    data = data.dropna(subset=[column, "annual_salary_eur"])

    if data.empty:
        return {}

    return data.groupby(column)["annual_salary_eur"].mean().sort_index().to_dict()


def average_salary_by_occupation(df):
    return _average_salary_by_column(df, "occupation")


def average_salary_by_age(df):
    data = df[["age", "annual_salary_eur"]].copy()
    data["age"] = pd.to_numeric(data["age"], errors="coerce")
    data["annual_salary_eur"] = pd.to_numeric(data["annual_salary_eur"], errors="coerce")
    data = data.dropna(subset=["age", "annual_salary_eur"])

    if data.empty:
        return {}

    result = data.groupby("age")["annual_salary_eur"].mean().sort_index().to_dict()
    return {int(age): salary for age, salary in result.items()}


def average_salary_by_industry(df):
    return _average_salary_by_column(df, "industry")


def average_salary_by_skills(df):
    data = df[["skills", "annual_salary_eur"]].copy()
    data["annual_salary_eur"] = pd.to_numeric(data["annual_salary_eur"], errors="coerce")
    data = data.dropna(subset=["skills", "annual_salary_eur"])

    rows = []
    for _, row in data.iterrows():
        for skill in str(row["skills"]).split(";"):
            skill = skill.strip()
            if skill:
                rows.append({"skill": skill, "salary": row["annual_salary_eur"]})

    if not rows:
        return {}

    skill_data = pd.DataFrame(rows)
    return skill_data.groupby("skill")["salary"].mean().sort_index().to_dict()


def average_salary_by_english_level(df):
    return _average_salary_by_column(df, "english_level")


def choose_salary_average_option():
    options = {
        "1": "occupation",
        "2": "age",
        "3": "industry",
        "4": "skills",
        "5": "english_level",
        "6": "all",
    }
    choice = input(
        "Choose salary average option: 1. occupation, 2. age, 3. industry, "
        "4. skills, 5. english_level, 6. all: "
    ).strip()

    if choice not in options:
        raise ValueError(f"Invalid option: {choice}")

    return options[choice]
