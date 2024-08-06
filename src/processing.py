import re
from typing import Any, Dict, List, Optional

from src.widget import get_data


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция сортировки по статусу"""
    return [element for element in list_of_dicts if element.get("state") == state]


def sort_by_date(list_of_dicts: List[Dict[str, Any]], is_ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки по дате"""
    return sorted(list_of_dicts, key=lambda el: get_data(el["date"]), reverse=is_ascending)


def filter_transactions_on_search(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict]:
    """Фильтрует данные банковских операций по ключевому слову"""
    filtered_transactions = []
    pattern = re.compile(search_string, re.IGNORECASE)
    for transaction in transactions:
        descriptions = transaction.get("description", "")
        if not transaction or not transaction.get("description"):
            continue
        if pattern.search(descriptions):
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> dict[Any, int]:
    """Считает операии по категориям"""
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        descriptions = transaction.get("description")
        for category in categories:
            if category in descriptions:
                category_count[category] += 1
                break
    return category_count


def filter_rub_transactions(transaction):
    """Фильтрует по валюте 'RUB'"""
    return [el for el in transaction if el["currency_code"] == "RUB"]
