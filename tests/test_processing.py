from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date

TEST_DATA: List[Dict[str, Any]] = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-25"},
    {"id": 2, "state": "CANCELED", "date": "2023-10-26"},
    {"id": 3, "state": "EXECUTED", "date": "2023-10-27"},
]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("RUNNING", []),
    ],
)
def test_filter_by_state(state: str, expected_ids: List[int]) -> None:
    filtered_data: List[Dict[str, Any]] = filter_by_state(TEST_DATA, state)
    result_ids: List[int] = []
    for item in filtered_data:
        result_ids.append(item["id"])
    assert result_ids == expected_ids


@pytest.mark.parametrize(
    "order, expected_ids",
    [
        ("desc", [3, 2, 1]),
        ("asc", [1, 2, 3]),
    ],
)
def test_sort_by_date(order: str, expected_ids: List[int]) -> None:
    sorted_data: List[Dict[str, Any]] = sort_by_date(TEST_DATA, order)
    result_ids: List[int] = []
    for item in sorted_data:
        result_ids.append(item["id"])
    assert result_ids == expected_ids


def test_sort_by_date_invalid_order() -> None:
    with pytest.raises(ValueError) as excinfo:
        sort_by_date(TEST_DATA, "invalid")
    assert "order должен быть 'desc' или 'asc'" in str(excinfo.value)
