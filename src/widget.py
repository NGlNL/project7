"""Импорт функий"""

from datetime import datetime

from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Тип карты/счета с маскировкой"""
    parts = number.split()
    if "Счет" in parts:
        return f"{parts[0]} {get_mask_account(int(parts[1]))}"
    elif len(parts) == 2:
        return f"{parts[0]} {get_mask_card_number(int(parts[1]))}"
    elif len(parts) == 3:
        return f"{parts[0]} {parts[1]} {get_mask_card_number(int(parts[2]))}"
    else:
        return "Неверные данные"


def get_data(date_str: str) -> datetime:
    """Меняем форму даты"""
    return datetime.fromisoformat(date_str)
