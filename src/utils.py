import json
from typing import Any, Dict, List


def transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        print("Ошибка декодирования json")
    except TypeError:
        print("Неправильный тип данных")
    return []


transactions_from_json("operations.json")
