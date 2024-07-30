from src.decorators import log
import os


def test_log_file():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    @log(filename="test_log.txt")
    def test_func_success(a, b):
        return a + b

    result = test_func_success(1, 2)
    assert result == 3

    with open("test_log.txt", "r") as f:
        line = f.readlines()
        assert len(line) == 1
        assert line[0].strip() == "test_func_success ok"


def test_log_error():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    @log(filename="test_log.txt")
    def test_func_error(a, b):
        return a / b

    test_func_error(1, 0)
    with open("test_log.txt", "r") as f:
        line = f.readlines()
        assert len(line) == 1
        assert line[0].strip() == "test_func_error error: division by zero. Inputs: (1, 0), {}"


def test_log_success_console(capsys):
    @log()
    def func_success_console(a, b):
        return a + b

    result = func_success_console(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert captured.out == "func_success_console ok\n"


def test_log_error_console(capsys):
    @log()
    def func_error_console(a, b):
        return a / b

    func_error_console(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "func_error_console error: division by zero. Inputs: (1, 0), {}\n"
