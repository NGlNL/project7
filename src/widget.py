"""Импорт функий"""

from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Тип карты/счета с маскировкой"""
    parts = number.split()
    if "Счет" in parts:
        return f"{parts[0]} {get_mask_account(int(parts[1]))}"
    elif len(parts) == 2:
        return f"{parts[0]} {get_mask_card_number(int(parts[1]))}"
    else:
        return f"{parts[0]} {parts[1]} {get_mask_card_number(int(parts[2]))}"


def get_data(time: str) -> str:
    """Меняем форму даты"""
    part_time = time.split("T")
    result = part_time[0].split("-")
    result.reverse()
    return ".".join(result)
