import json
import os
from typing import Any, Hashable

import pandas as pd

from src.logger_config import logger


def transactions_from_files(file_path: str) -> list[Any] | list | list[dict[Hashable, Any]]:
    """Функция принимает на вход путь до JSON-файла, CSV- и XLSX-файлов и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    if not os.path.exists(file_path):
        return []
    try:
        if file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                logger.debug("Читаем файл и переводим его в JSON")
                if isinstance(data, list):
                    return data
        elif file_path.endswith(".csv"):
            data = pd.read_csv(file_path, delimiter=";")
            return data.to_dict(orient="records")
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path)
            return data.to_dict(orient="records")
        else:
            logger.error("Неподдерживаемый формат файла")
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except json.decoder.JSONDecodeError:
        logger.error("Ошибка декодирования json")
    except TypeError:
        logger.error("Неправильный тип данных")
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
    return []
