import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
KEY_API = os.getenv("API_KEY")

# здесь напишем (пишем) функцию, обращающуюся ко внешнему API и возвращающую
# курс заданной валюты по отношению к рублю


def get_exch_rate(curr: str, my_api: str) -> float:
    """Функция возвращает курс валюты по отношению к рублю, обращаясь к АПИ apilayer.com"""
    headers: dict = {"apikey": my_api}
    url_frmtted = (
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
        + curr
        + "&amount=15000"
    )

    response = requests.get(url_frmtted, headers=headers)
    result_pyth = json.loads(response.text)
    result = result_pyth["info"]["rate"]
    return result


# пишем строчки для проверки работы функции
s_curr = input("Введите аббревиатуру своей валюты: ")
new_api: str = KEY_API
print(get_exch_rate(s_curr, new_api))
