from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрация словарей по значению ключа state"""

    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict]) -> List[Dict]:
    """Сортировка словарей"""

    return sorted(operations, key=lambda item: item["date"], reverse=True)
