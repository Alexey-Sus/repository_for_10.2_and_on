from src.read_from import read_from_csv, read_from_excel_2

# 1. тестируем функцию выборки данных из файла CSV


def test_read_from_csv():
    """Тестирование функции read_from_csv из модуля read_from.py
    вводим тут (здесь) небольшую тестовую переменную из 2-х словарей и будем использовать
    тоже специальный файл CSV, который тоже содержит 2 строчки всего"""

    test_value: list = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    file_to_use: str = "../data/transactions_with_two.csv"
    assert test_value == read_from_csv(file_to_use)

    # проверка работы функции при несуществующем файле; функция должна просто выводить пустой список
    assert read_from_csv("../data/some_file.csv") == []


# 2. тестируем так же функцию выборки (получения данных из) файла excel


def test_read_from_excel_2():
    """Тестируем функцию чтения файла из файла Excel. Она принимает на вход файл и выводит
    из него список словарей. Так же вводим тестовую переменную из 2-х словарей и в качестве
    файла передаем специальный файл Excel, состоящий из 2-х строчек"""

    test_value = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    file_for_excel: str = "../data/transactions_excel_with_two.xlsx"
    assert read_from_excel_2(file_for_excel) == test_value

    # аналогично, проверяем работу функции при несуществующем файле
    assert read_from_excel_2("../data/yet_another_fake_file.xlsx") == []
