from typing import Any, Dict, Generator, Iterator, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 939719570, "currency": "USD", "amount": 100.00},
        {"id": 142264268, "currency": "USD", "amount": 50.00},
        {"id": 329871532, "currency": "EUR", "amount": 150.00},
    ]


def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    expected_ids = [939719570, 142264268]
    usd_transactions: Iterator[Dict[str, Any]] = filter_by_currency(transactions, "USD")
    assert [next(usd_transactions)["id"] for _ in range(2)] == expected_ids


@pytest.fixture
def transactions_fixture() -> List[Dict[str, Any]]:
    return [
        {"operation_type": "Перевод организации"},
        {"operation_type": "Перевод со счета на счет"},
        {"operation_type": "Перевод со счета на счет"},
        {"operation_type": "Перевод с карты на карту"},
        {"operation_type": "Перевод организации"},
    ]


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    descriptions: Generator[str, None, None] = transaction_descriptions(transactions)
    assert list(descriptions) == expected_descriptions


@pytest.fixture
def card_numbers() -> List[str]:
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator(card_numbers: List[str]) -> None:
    generated_numbers: List[str] = list(card_number_generator(1, 5))
    assert generated_numbers == card_numbers
