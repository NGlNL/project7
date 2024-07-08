from typing import Any, Dict, List, Optional

from src.widget import get_data


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция сортировки по статусу"""
    return [element for element in list_of_dicts if element.get("state") == state]


def sort_by_date(list_of_dicts: List[Dict[str, Any]], is_ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки по дате"""
    return sorted(list_of_dicts, key=lambda el: get_data(el["date"]), reverse=is_ascending)


# Входные данные
example_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
# Вызов функии по дате в убывающем порядке
sorted_data = sort_by_date(example_data)
print("Сортировка в убывающем порядке:")
for record in sorted_data:
    print(record)

# Вызов функии по дате в возрастающем порядке
sorted_data_asc = sort_by_date(example_data, False)
print("\nСортировка в возрастающем порядке:")
for record in sorted_data_asc:
    print(record)

# Вызов функии по статусу
filtered_data = filter_by_state(example_data)
print("\nФильтрация по статусу (EXECUTED):")
for record in filtered_data:
    print(record)
