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
