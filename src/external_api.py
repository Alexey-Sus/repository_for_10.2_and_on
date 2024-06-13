import requests
import json

# здесь напишем (пишем) функцию, обращающуюся ко внешнему API и возвращающую
# курс заданной валюты по отношению к рублю

# # url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
# url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=15000"
#
# # payload = {}
# headers= {"apikey": "FAYTtDvjSMHYgYj3hS6q0SVqZ1PsGsSU"}
#
# # response = requests.request("GET", url, headers=headers, data = payload)
#
# response = requests.get(url, headers=headers)
#
# # status_code = response.status_code
#
# result = response.text
# result_pyth = json.loads(result)
# rate = result_pyth['info']['rate']
#
# print(rate)
# print(result)
# print(result_pyth)
# print('Это разделительная строка')

def get_exch_rate(curr: str) -> float:
    headers:dict = {"apikey": "FAYTtDvjSMHYgYj3hS6q0SVqZ1PsGsSU"}
    url_frmtted = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=" + curr + "&amount=15000"

    response = requests.get(url_frmtted, headers=headers)
    result_pyth = json.loads(response.text)

    return result_pyth['info']['rate']

print(get_exch_rate(input('Введите сюда, сюда введите, свою валюту: ')))






