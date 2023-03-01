from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    result = read_brazilian_file(path)
    assert {"title": "Maquinista",
            "salary": "2000", "type": "trainee"} in result
