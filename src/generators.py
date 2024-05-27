from typing import Any, Dict, Generator, Iterator


def filter_by_currency(
    transactions: list[Dict[str, Any]], currency: str
) -> Iterator[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.
    """

    # Проверка, является ли transactions итератором
    if hasattr(transactions, "__iter__") and not isinstance(transactions, str):
        for transaction in transactions:
            if transaction.get("currency") == currency:
                yield transaction
    else:
        for transaction in transactions:
            if transaction["currency"] == currency:
                yield transaction


# Пример использование функции:
transactions = [
    {"id": 939719570, "currency": "USD", "amount": 100.00},
    {"id": 142264268, "currency": "USD", "amount": 50.00},
    {"id": 329871532, "currency": "EUR", "amount": 150.00},
]

usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions)["id"])


def transaction_descriptions(
    transactions: list[Dict[str, Any]]
) -> Generator[str, None, None]:
    """
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    """

    for transaction in transactions:
        operation_type = transaction.get("operation_type", "Неизвестная операция")
        description = f"{operation_type}"
        yield description


# Пример использования функции:
transactions = [
    {"operation_type": "Перевод организации"},
    {"operation_type": "Перевод со счета на счет"},
    {"operation_type": "Перевод со счета на счет"},
    {"operation_type": "Перевод с карты на карту"},
    {"operation_type": "Перевод организации"},
]

descriptions = transaction_descriptions(transactions)

for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт.
    """
    for i in range(start, end + 1):
        card_number = f"{i:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number


# Пример использования функции:
for card_number in card_number_generator(1, 5):
    print(card_number)
