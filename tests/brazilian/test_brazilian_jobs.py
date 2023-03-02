from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    error = (
        "read_brazilian_file() missing 1 required positional "
        "argument: 'path'"
    )

    # Test calling function without argument
    try:
        read_brazilian_file()
    except TypeError as e:
        assert str(e) == error

    # Test function with argument
    result = read_brazilian_file(path)
    assert {"title": "Maquinista",
            "salary": "2000", "type": "trainee"} in result
