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


"""Входные данные"""
inputs = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]
"""Перебор входных данных"""
for el in inputs:
    print(mask_account_card(el))


def get_data(time: str) -> str:
    """Меняем форму даты"""
    part_time = time.split("T")
    result = part_time[0].split("-")
    result.reverse()
    return ".".join(result)


print(get_data("2018-07-11T02:26:18.671407"))
