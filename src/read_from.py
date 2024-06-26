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

#
# print(read_from_csv(file_to_use))


# запускаем функцию и выводим на печать:
# print(read_from_csv(file_to_use))


# это здесь пишем функцию чтения из файла excel и создания из данных списка словарей;
# это самый удобный и простой способ
def read_from_excel_2(file_name: str) -> list:
    """Функция чтения данных из файла Excel и вывода их в виде списка словарей транзакций"""
    # это самый изящный способ сделать быстро из dataframe список словарей, и самый короткий и быстрый способ
    try:
        from_excel = pd.read_excel(file_name)
        from_excel_dict: dict = from_excel.to_dict(orient="records")
        return from_excel_dict

    except FileNotFoundError as exp:
        print(f"{exp} Файл, видимо, не найден...")
        return []


# запустим эту функцию для проверки
# print(read_from_excel_2('../data/transactions_excel.xlsx'))

# чисто для справки сделаем еще одну функцию, получающую такой же список -
# более долгий способ, но заставляющий подумать
# def read_from_excel(file_name: str) -> None:
#     '''Функция чтения данных из файла Excel и вывода их в виде списка словарей транзакций'''
#     try:
#         with open(file_name, 'rb') as file:
#             from_excel = pd.read_excel(file)
#             list_interm: list = from_excel.values.tolist()
#
#             list_result: list = []
#             for i in list_interm:
#                 # это первый способ сделать словарь из каждой строки, который потом помещать в конец списка
#                 # dict_new: dict = {}
#                 # dict_new['id'] = i[0]
#                 # dict_new['state'] = i[1]
#                 # dict_new['date'] = i[2]
#                 # dict_new['amount'] = i[3]
#                 # dict_new['currency_name'] = i[4]
#                 # dict_new['currency_code'] = i[5]
#                 # dict_new['from'] = i[6]
#                 # dict_new['to'] = i[7]
#                 # dict_new['description'] = i[8]
#                 # list_result.append(dict_new)
#
#                 # а это второй способ, более изящный и элегантный
#                 dict_new: dict = {}
#                 counter = 0
#                 for j in ['id', 'state', 'date', 'amount', 'currency_name',
#                 'currency_code', 'from', 'to', 'description']:
#                     dict_new[j] = i[counter]
#                     counter += 1
#                 list_result.append(dict_new)
#
#             return list_result
#     except FileNotFoundError as exp:
#             print(f'{exp} Файл, видимо, не найден...')
#             return []
#
# # запустим эту функцию для проверки
# read_from_excel('../data/transactions_excel.xlsx')
# print(read_from_excel('../data/transactions_excel.xlsx'))
