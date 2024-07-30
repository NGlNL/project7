import json
from typing import Any, Dict, List

from src.logger_config import logger


def transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.debug("Читаем файл и переводим его в JSON")
            if isinstance(data, list):
                return data
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except json.decoder.JSONDecodeError:
        logger.error("Ошибка декодирования json")
    except TypeError:
        logger.error("Неправильный тип данных")
    return []


transactions_from_json("operations.json")
