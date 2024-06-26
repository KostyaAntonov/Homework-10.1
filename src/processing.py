from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.
    """
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: List[Dict], order: str = "desc") -> List[Dict]:
    """
    Функция сортирует список словарей по дате
    """
    if order not in ["desc", "asc"]:
        raise ValueError("order должен быть 'desc' или 'asc'")

    return sorted(data, key=lambda item: item["date"], reverse=(order == "desc"))


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sorted_data = sort_by_date(data)
print(sorted_data)
