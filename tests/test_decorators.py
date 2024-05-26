import os
from typing import Generator

import pytest

from src.decorators import log


@pytest.fixture
def log_file() -> Generator[str, None, None]:
    """
    Фикстура для создания временного файла для записи логов.
    """
    filename = "test_log.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_log_decorator_success(log_file: str) -> None:
    """
    Проверяет, что декоратор записывает сообщение об успехе в файл.
    """

    @log(filename=log_file)
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(2, 3)
    assert result == 5

    with open(log_file, "r") as f:
        log_content = f.read().strip()
        assert log_content == "my_function ok"


def test_log_decorator_error(log_file: str) -> None:
    """
    Проверяет, что декоратор записывает сообщение об ошибке в файл.
    """

    @log(filename=log_file)
    def my_function(x: int, y: int) -> int:
        raise ValueError("Error!")

    with pytest.raises(ValueError):
        my_function(2, 3)

    with open(log_file, "r") as f:
        log_content = f.read().strip()
        assert log_content == "my_function error: ValueError. Inputs: (2, 3), {}"


def test_log_decorator_no_filename(log_file: str) -> None:
    """
    Проверяет, что декоратор выводит сообщение в консоль, если filename не задан.
    """

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(2, 3)
    assert result == 5
