from src.generators import filter_by_currency
from src.logger_config import logger
from src.processing import filter_by_state, filter_rub_transactions, filter_transactions_on_search, sort_by_date
from src.utils import transactions_from_files
from src.widget import get_data, mask_account_card


def user_input(pattern, options) -> str:
    """Получаем входные данные от пользователя"""
    while True:
        u_input = input(pattern).strip().upper()
        if options and u_input not in options:
            print(f'Неверный ввод. Доступные опции: {", ".join(options)}')
        else:
            return u_input


def main() -> None:
    """Главная функия"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    file_option = user_input("", ["1", "2", "3"])
    file_pass = ""
    if file_option == "1":
        print("Для обработки выбран JSON-файл.")
        file_pass = "data/operations.json"
    elif file_option == "2":
        print("Для обработки выбран CSV-файл.")
        file_pass = "data/transactions.csv"
    elif file_option == "3":
        print("Для обработки выбран XLSX-файл")
        file_pass = "data/transactions_excel.xlsx"
    try:
        transactions = transactions_from_files(file_pass)
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {e}.")
        return
    while True:
        status = user_input(
            "Введите статус, по которому необходимо выполнить фильтрацию.(EXECUTED, CANCELED, PENDING): ",
            ["EXECUTED", "CANCELED", "PENDING"],
        )
        filter_transactions = filter_by_state(transactions, status)
        if filter_transactions:
            print(f"Операции отфильтрованы по статусу {status}")
        sort_op = user_input("Отсортировать операции по дате? Да/Нет", ["ДА", "НЕТ"])
        if sort_op == "ДА":
            sort_order = user_input("Отсортировать по возрастанию или по убыванию?", ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"])
            ascending = sort_order == "ПО ВОЗРАСТАНИЮ"
            filter_transactions = sort_by_date(filter_transactions, ascending)
        transaction_rub = user_input("Выводить только рублевые тразакции? Да/Нет", ["ДА", "НЕТ"])
        if transaction_rub == "ДА":
            if file_option == "1":
                filtered_json = filter_by_currency(filter_transactions, "RUB")
                filter_transactions = list(filtered_json)
            else:
                filter_transactions = filter_rub_transactions(filter_transactions)
        description_op = user_input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет", ["ДА", "НЕТ"]
        )
        if description_op == "ДА":
            search = input("Введите строку для поиска: ".strip())
            filter_transactions = filter_transactions_on_search(filter_transactions, search)
        print("Распечатываю итоговый список транзакций...\n")
        if not filter_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
            break
        else:
            print(f"Всего банковских операций в выборке: {len(filter_transactions)}\n")
            for transaction in filter_transactions:
                date = get_data(transaction["date"])
                description = transaction["description"]
                if file_option == "1":
                    amount = transaction["operationAmount"]["amount"]
                    currency = transaction["operationAmount"]["currency"]["code"]
                else:
                    amount = transaction["amount"]
                    currency = transaction["currency_code"]
                from_account = mask_account_card(transaction.get("from", ""))
                to_account = mask_account_card(transaction["to"])
                print(f"{date}{description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n")
            break


if __name__ == "__main__":
    main()
