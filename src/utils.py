import json
import os.path

def fin_oper_data(file_to_input: str) -> list:
    '''Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых операциях'''
    if os.path.isfile(file_to_input):
        with open(file_to_input, encoding="utf-8") as file:
            try:
                new_list = json.load(file)
            except ValueError:
                new_list = [' ', 'данные не являются объектом или массивом, либо файл пустой']
    else:
        new_list = [' ', 'такой файл не найден']
    return new_list

print(fin_oper_data('../data/operations.json'))
temp_var = fin_oper_data('../data/operations.json')

# Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
# тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API
# для получения текущего курса валют и конвертации суммы операции в рубли.
# Для конвертации валюты воспользуйтесь Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модуль external_api.

# пишем функцию для возврата суммы транзакции в рублях

def get_rub_amnt_for_trns(list_trans: list, id_trans: int) -> float:
    amnt: float = 0.0
    for i in list_trans:
        if i['id'] == id_trans:
            amnt = i['operationAmount']['amount']
            curr = i['operationAmount']['currency']['code']
            if curr == 'RUB':
                result = amnt
                break
            else:
                result = curr
                break
    return result

result_amnt = get_rub_amnt_for_trns(temp_var, int(input('Введите свою транзакцию: ')))
print(result_amnt)
