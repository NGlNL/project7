import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.utils import transactions_from_json

load_dotenv()
API_KEY = os.getenv("API_KEY")
api_url = "https://api.exchangeratesapi.io/convert"


def convert_amount_to_rub(convert: Dict[str, Any]) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях.Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли."""
    amount = float(convert["operationAmount"]["amount"])
    currency = convert["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    params = {"to": "RUB", "from": currency, "amount": str(amount)}
    headers = {"API_KEY": API_KEY}
    response = requests.get(api_url, params=params, headers=headers)
    response_data = response.json()
    if response.status_code == 200:
        return float(response_data["result"])
    else:
        error = response_data.get("Error", "API error")
        raise ValueError(f"Error in API request: {error}")
