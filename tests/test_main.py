import json
from pathlib import Path

from src.main import run_salary_analysis, save_result_to_json


def test_save_result_to_json_writes_result():
    output_path = Path("output/test_result.json")
    output_path.unlink(missing_ok=True)

    result = {"average_salary": 50000.0}

    saved_path = save_result_to_json(result, output_path)

    assert saved_path == output_path
    assert json.loads(output_path.read_text(encoding="utf-8")) == result

    output_path.unlink()


def test_run_salary_analysis_saves_selected_calculation(monkeypatch):
    csv_path = Path("output/test_salary_input.csv")
    output_path = Path("output/test_salary_result.json")
    csv_path.write_text(
        "occupation,annual_salary_eur\nEngineer,60000\nDesigner,40000\nEngineer,80000\n",
        encoding="utf-8",
    )
    output_path.unlink(missing_ok=True)
    monkeypatch.setattr("src.main.choose_salary_average_option", lambda: "occupation")

    saved_path = run_salary_analysis(csv_path, output_path)

    result = json.loads(output_path.read_text(encoding="utf-8"))
    assert saved_path == output_path
    assert result == {
        "calculation": "average_salary",
        "option": "occupation",
        "result": {"Designer": 40000.0, "Engineer": 70000.0},
    }

    csv_path.unlink()
    output_path.unlink()
