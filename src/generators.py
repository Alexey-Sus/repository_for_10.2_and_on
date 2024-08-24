# Реализуйте функцию, которая принимает список словарей с банковскими операциями
# (или объект-генератор, который выдает по одной банковской операции) и возвращает итератор,
# который выдает по очереди операции, в которых указана заданная валюта. Yield – генератор написать
# тоже, тоже написать.

# Пример вызова функции:
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions)["id"])

# Пример вывода:
# 939719570
# 142264268 Должны выводиться только id транзакций и всё

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

# напишем эту функцию:


def filter_currency(list_curr: list, currency: str):
    """Функция-генератор для выдачи по запросу id транзакций с заданной валютой"""
    for i in list_curr:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i.get("id")


# присваиваем новой переменной генератор:
transact_gen = filter_currency(transactions, "USD")


# напишем функцию для определения количества транзакций с заданной валютой
def number_of_trans(list_curr: list, currency: str):
    """Вспомогательная функция для расчета количества транзакций с заданной валютой в исходном списке"""
    list_count_trans: list = []
    count = 0
    for j in list_curr:
        if j["operationAmount"]["currency"]["code"] == currency:
            if j["operationAmount"]["currency"]["code"] not in list_count_trans:
                list_count_trans.append(j)
                count += 1
            else:
                pass
        else:
            pass
    list_count_trans = []
    return count


print(f"Количество транзакций с такой валютой: {number_of_trans(transactions, 'USD')}")

# выводим на печать результат расчета функции с помощью цикла for и аргумента кол-ва
# транзакций, полученных с помощью доп. функции number_of_trans()
# этот цикл - вспомогательный, и его можно было и не писать вовсе. Но вообще конечно можно
# просто запрашивать от пользователя ввод валюты и передавать этот ввод во все функции

# проверка работы функции с выводом на печать
for i in range(number_of_trans(transactions, "USD")):
    print(next(transact_gen))

print()
# вторая функция

# Напишите генератор, который принимает список словарей и
# возвращает описание каждой операции по очереди. То есть, тут надо будет бы
# написать генераторное выражение – это уже от меня.
# Пример вызова функции:
# descriptions = transaction_descriptions(transactions):
# for _ in range(5):
#     print(next(descriptions))
# Пример вывода:
# Перевод организации
# Перевод со счета на счет
# Перевод со счета на счет
# Перевод с карты на карту
# Перевод организации


# пишем саму функцию:
def trans_descr(list_curr):
    """Функция для вывода списка описаний транзакций"""
    for i in list_curr:
        yield i["description"]

# проверяем работу этой функции с помощью генератора
gen_descr_trans = trans_descr(transactions)
print(next(gen_descr_trans))
print(next(gen_descr_trans))
print(next(gen_descr_trans))
print(next(gen_descr_trans))
print(next(gen_descr_trans))

# третья функция

# Напишите генератор номеров банковских карт, который должен генерировать номера
# карт в формате XXXX XXXX XXXX XXXX, где X — цифра. Должны быть сгенерированы номера
# карт в заданном диапазоне, например от 0000 0000 0000 0001 до 9999 9999 9999 9999
# (диапазоны передаются как параметры генератора).

# for card_number in card_number_generator(1, 5):
#     print(card_number)

# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005

print()

start = input("Ввод начала диапазона номеров карт: ")
stop = int(input("...и окончания диапазона: "))

# start = "20"
# stop = 25 - это для случая, когда мы хотим просто проверить функцию с жестко заданными значениями


def card_number_gen(start: str, stop: int):
    """Функция-генератор для вывода номеров карт в формате XXXX XXXX XXXX XXXX с заданным от пользователя
    диапазоном, от и до"""

    # вычисляем формат для первой карты, для первого вывода в yield
    xs = 16 - len(start)
    str_interm = "X" * xs + start
    str_for_output = (
        str_interm[0:4]
        + " "
        + str_interm[4:8]
        + " "
        + str_interm[8:12]
        + " "
        + str_interm[12:]
    )
    count = int(start)
    while True:
        yield str_for_output
        # увеличиваем счетчик и инкрементируем номер следующей карты на 1
        count += 1
        frmt_str = str_for_output.replace(" ", "")
        for i in frmt_str:
            if i.isdigit():
                int_aux = int(frmt_str[frmt_str.find(i) :])
                int_aux += 1
                str_aux = str(int_aux)
                nmr_of_x = 16 - len(str_aux)
                s_w_s = "X" * nmr_of_x + str_aux
                str_for_output = (
                    s_w_s[0:4] + " " + s_w_s[4:8] + " " + s_w_s[8:12] + " " + s_w_s[12:]
                )
                break
        if count > stop:
            break


# проверка работы функции с заданным диапазоном карт (от и до)
for card_number in card_number_gen(start, stop):
    print(card_number)
