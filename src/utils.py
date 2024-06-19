import json
import os.path
from src.external_api import get_exch_rate
from dotenv import load_dotenv
import os

load_dotenv()
KEY_API = os.getenv("API_KEY")


def fin_oper_data(file_to_input: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых операциях. Если файла такого нет, либо он пустой или содержит
    не данные в формате list, возвращаем пустой список"""
    if os.path.isfile(file_to_input):
        with open(file_to_input, encoding="utf-8") as file:
            try:
                new_list = json.load(file)
            except ValueError:
                new_list = []
    else:
        new_list = []

    return new_list


# temp_var = fin_oper_data('../data/operations.json')
# print(temp_var)

# пишем функцию для возврата суммы транзакции в рублях
# вводим тестовую временную переменную для работы этой функции - транзакцию с типом
# данных dict, которую будем отправлять на вход функции


trans = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {"name": "USD", "code": "USD"},
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


def get_rub_amnt_for_trns(tran_n: dict) -> float:
    """Функция возвращает сумму транзакции в рублях, если транзакция в рублях, и переводит сумму
    транзакции в другой валюте (вызывая внутри себя другую функцию get_exch_rate) в сумму в рублях,
    если вызывается транзакция в валюте"""
    amnt = float(tran_n["operationAmount"]["amount"])
    curr = tran_n["operationAmount"]["currency"]["code"]
    if curr == "RUB":
        result = amnt
    else:
        result = get_exch_rate(curr, "FAYTtDvjSMHYgYj3hS6q0SVqZ1PsGsSU") * amnt
    return result


# result_amnt = get_rub_amnt_for_trns(trans)
# print(result_amnt)
