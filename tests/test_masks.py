import pytest

from src.masks import mask_account_number, mask_card_number


@pytest.fixture
def card_number() -> str:
    return "1234567890123456"


@pytest.fixture
def account_number() -> str:
    return "1234567890"


def test_mask_card_number(card_number: str) -> None:
    assert mask_card_number(card_number) == "1234 56** **** 3456"


def test_mask_account_number(account_number: str) -> None:
    assert mask_account_number(account_number) == "**90"
