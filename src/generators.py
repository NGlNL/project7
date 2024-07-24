from typing import Iterator, List


def filter_by_currency(transaction_dictionary: List[dict], currency: str) -> Iterator[dict]:
    """Фильтрует список транзакций по заданной валюте.
    :param transaction_dictionary: список словарей с транзакциями
    :param currency: строка с кодом валюты
    :return: итератор с транзакциями в заданной валюте
    """
    return (
        element
        for element in transaction_dictionary
        if element.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )


def transaction_descriptions(transaction_dictionary: List[dict]) -> Iterator[str]:
    """Генерирует описания транзакций из списка словарей.
    :param transaction_dictionary: список словарей с транзакциями.
    Возвращает описание каждой операции по очереди.
    """
    for element in transaction_dictionary:
        yield element.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генерирует последовательность отформатированных номеров карт в заданном диапазоне.
    :param start: Начальное значение диапазона для генерации номеров карт.
    :param end: Конечное значение диапазона для генерации номеров карт.
    Возвращает отформатированные номера карт.
    """
    for element in range(start, end + 1):
        numbers = f"{element:016d}"
        formated_numbers = f"{numbers[:4]} {numbers[4:8]} {numbers[8:12]} {numbers[12:16]}"
        yield formated_numbers
