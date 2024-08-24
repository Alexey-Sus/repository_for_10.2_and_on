import json
import os.path
from src.external_api import get_exch_rate
from dotenv import load_dotenv
import os
import logging

load_dotenv()
KEY_API = os.getenv("API_KEY")

# создаем логгер с уровнем логирования, например, INFO

utils_logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../data/utils_log_file.log",  # записываем логи в файл
    filemode="w",
)  # метка 'w' означает перезапись лога в файл при каждом запуске
utils_handler = logging.FileHandler("../data/utils_log_file.log")
utils_logger.addHandler(utils_handler)


def fin_oper_data(file_to_input: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых операциях. Если файла такого нет, либо он пустой или содержит
    не данные в формате list, возвращаем пустой список"""
    utils_logger.info("Function started working")
    if os.path.isfile(file_to_input):
        with open(file_to_input, encoding="utf-8") as file:
            try:
                new_list: list = json.load(file)
                s: int = len(new_list)
                utils_logger.info(
                    f"The function has finished working and returned a list of {s} elements"
                )
            except ValueError:
                utils_logger.warning(
                    "There is no such file, or the file is empty, or the data is incompatible"
                )
                new_list = []

    else:
        new_list = []
        utils_logger.warning(
            "There is no such file, or the file is empty, or the data is incompatible"
        )

    return new_list


# temp_var = fin_oper_data('../data/operations.json')
# temp_var = fin_oper_data("../data/operations.json")
# print(temp_var)

# пишем функцию для возврата суммы транзакции в рублях
# вводим тестовую временную переменную для работы этой функции - транзакцию с типом
# данных dict, которую будем отправлять на вход функции


trans = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


def get_rub_amnt_for_trns(tran_n: dict) -> float:
    """Функция возвращает сумму транзакции в рублях, если транзакция в рублях, и переводит сумму
    транзакции в другой валюте (вызывая внутри себя другую функцию get_exch_rate) в сумму в рублях,
    если вызывается транзакция в валюте"""
    utils_logger.info("get_rub_amnt_for_trns has started working")
    amnt = float(tran_n["operationAmount"]["amount"])
    curr = tran_n["operationAmount"]["currency"]["code"]
    if curr == "RUB":
        utils_logger.info(
            f"get_rub_amnt_for_trns has started working and returned a RUB amnt {amnt}"
        )
        result = amnt
    else:
        result = get_exch_rate(curr, "aBIrncn56FEd5ZTlZY0WzRQuD9cZ0XNz") * amnt
        utils_logger.info(
            f"get_rub_amnt_for_trns has finished working with a currency transaction, returned {result}"
        )
    return result


# result_amnt = get_rub_amnt_for_trns(trans)
# print(result_amnt)
