# Напишите ф-ю, кот. приним-ет на вход список словарей и возвр. новый список,
# в кот. исх. словари отсорт-ны по убыванию даты (ключ date). Принимает 2 арг-та: 2-й - необяз. поряд. сорт.

list_orig: list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
]


def list_sort_date(work_list: list, reverse_or_not: bool = True) -> list:
    """Функция принимает на вход сп-к словарей и возвр-ет новый список,
    в котором исх. словари отсортированы по убываанию даты (ключ date). Принимает 2 аргумента:
    2-й - необязательный порядок сортировки"""

    if isinstance(work_list, list):
        return sorted(work_list, key=lambda x: x["date"], reverse=reverse_or_not)
    else:
        return []


# Напишите функцию, которая принимает на вход список словарей и значение для ключа
# state (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
# содержащий только те словари, у которых ключ state содержит переданное в функцию значение.


print()


def list_for_state(work_list: list, state_val="EXECUTED") -> list:
    """Функция принимает на вход список словарей и зн-ие для ключа state (опц. параметр со зн-ием по умолчанию
    EXECUTED) и возвр-ет нов. список, содержащий только те словари, у кот. ключ state содержит
    переданное в ф-ю зн-ие"""

    list_new: list = []
    if isinstance(work_list, list):
        for i in work_list:
            if i["state"] == state_val.upper():
                list_new.append(i)
    else:
        list_new = []
    return list_new


print()
