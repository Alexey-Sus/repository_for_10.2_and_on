from collections import Counter

# пример списка словарей:

dict_example: list = [
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

str_example: str = 'с карты на карту'


# Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
# а возвращать список словарей, у которых в описании есть данная строка. При реализации этой функции можно
# использовать библиотеку re для работы с регулярными выражениями. Расположение новой функции в структуре проекта
# определите самостоятельно.
# пишем функцию


def dict_descr_string(list_to_use: list, str_to_use: str) -> dict:
    list_for_output: list = []

    for i in list_to_use:
        if str_to_use in i['description']:
            list_for_output.append(i)

    return list_for_output


# print(dict_descr_string(dict_example, str_example))

# Напишите функцию, которая будет принимать список словарей с данными о
# банковских операциях и список категорий операций, а возвращать словарь,
# в котором ключи — это названия категорий, а значения — это количество операций
# в каждой категории. Категории операций хранятся в поле description. Расположение
# новой функции в структуре проекта определите самостоятельно.

categ_names: list = ['Перевод организации']


def dict_categ_amount(input_list: list, list_categ: list) -> dict:
    list_count: list = []
    for i in input_list:
        if i['description'] in list_categ:
            list_count.append(i['description'])

    # выводим именно словарь, чтобы соответствовало условию задачи. И выводим его на вывод

    dict_for_output = dict(Counter(list_count))
    print("Словарь с названиями категорий и количеством операций по данным категориям:")
    return dict_for_output


print(dict_categ_amount(dict_example, categ_names))

# {'Перевод со счета на счет': 0, 'Перевод организации': 0, 'Перевод с карты на карту': 0}
