from typing import Any, Callable
from unittest.mock import MagicMock
import pytest
from src.widget import mask_card_or_account, reformat_date


@pytest.fixture
def mock_input(monkeypatch: pytest.MonkeyPatch) -> Callable[[Any], Any]:
    """Фикстура для замены input() мок-объектом."""
    mock = MagicMock()
    monkeypatch.setattr("builtins.input", mock)
    return mock


def test_mask_card_or_account_card(mock_input: MagicMock) -> None:
    """Тест маскировки номера карты."""
    mock_input.return_value = "Platinum Visa 4111111111111111"
    result: str = mask_card_or_account(mock_input.return_value)
    assert result == "Platinum Visa 4111 11** **** 1111"


def test_mask_card_or_account_account(mock_input: MagicMock) -> None:
    """Тест маскировки номера счета."""
    mock_input.return_value = "Счет 12345678901234567890"
    result: str = mask_card_or_account(mock_input.return_value)
    assert result == "Счет **7890"


def test_reformat_date() -> None:
    """Тест форматирования даты."""
    date_string: str = "2023-10-26T12:34:56.789Z"
    result: str = reformat_date(date_string)
    assert result == "26.10.2023"
