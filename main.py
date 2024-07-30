import pprint

from src.utils import transactions_from_files


def main() -> None:
    transaction = transactions_from_files("data/transactions.csv")
    pprint.pp(transaction)


if __name__ == "__main__":
    main()
