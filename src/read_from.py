import pandas as pd
import csv

file_to_use = "../data/transactions.csv"  # определяем переменную с названием файла для вызова в функции


def read_from_csv(file_name: str) -> str:
    """Функция чтения данных из CSV-файла и вывода транзакций в виде списка словарей"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            rdr_from_csv: dict = csv.DictReader(file, delimiter=";")
            list_trans: list = []

            for item in rdr_from_csv:
                list_trans.append(item)

            return list_trans

    except FileNotFoundError as exp:
        print(f"{exp}: Файл не найден")
        return []


if __name__ == "__main__":
    read_from_csv(file_to_use)


# здесь пишем функцию чтения из файла excel и создания из данных списка словарей

def read_from_excel_2(file_name: str) -> list:
    """Функция чтения данных из файла Excel и вывода их в виде списка словарей транзакций"""
    try:
        from_excel = pd.read_excel(file_name)
        from_excel_dict: dict = from_excel.to_dict(orient="records")
        return from_excel_dict

    except FileNotFoundError as exp:
        print(f"{exp} Файл, видимо, не найден...")
        return []


if __name__ == "__main__":
    read_from_excel_2(file_to_use)
