from unittest.mock import patch
import json
import os
from typing import Generator
import pytest
from src.utils import transactions_from_files


@pytest.fixture
def files_set() -> Generator:
    with patch("src.utils.transactions_from_files"):
        os.makedirs("data", exist_ok=True)
        yield


def test_files_set(files_set: None) -> None:
    data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-01-01T12:00:00",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Test transaction",
            "from": "Account 1",
            "to": "Account 2",
        }
    ]
    with open("data/test_operations.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

    transactions = transactions_from_files("data/test_operations.json")
    assert transactions == data


def test_files_set_empty(files_set: None) -> None:
    open("data/empty_operations.json", "a").close()
    transactions = transactions_from_files("data/empty_operations.json")
    assert transactions == []


def test_files_not_found(files_set: None) -> None:
    if os.path.exists("data/not_list_operations.json"):
        os.remove("data/not_list_operations.json")
        transactions = transactions_from_files("data/not_list_operations.json")
        assert transactions == []


def test_type_error(files_set: None) -> None:
    with open("data/not_list_operations.json", "w", encoding="utf-8") as file:
        json.dump({"key": "value"}, file)
    with patch("json.load", side_effect=TypeError):
        transactions = transactions_from_files("data/not_list_operations.json")
        assert transactions == []
