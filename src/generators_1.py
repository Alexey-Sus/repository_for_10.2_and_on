# Реализуйте функцию, которая принимает список словарей с банковскими операциями
# (или объект-генератор, который выдает по одной банковской операции) и возвращает итератор,
# который выдает по очереди операции, в которых указана заданная валюта. Yield – генератор написать
# тоже, тоже написать.

# Пример вызова функции:
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions)["id"])
#
# Пример вывода:
# 939719570
# 142264268 Должны выводиться только id транзакций и всё

# Пример словаря, для которого должны работать функции:
# это список словарей, в которых есть "ключ-значения" одинарные и плюс есть
# ключ operationAmount со значением в виде словаря, в котором есть 1 ключ-значение простое и 1 ключ-значение с ключом
# сurrency и значением в виде словаря с 2 ключами-значениями: name и code.

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

# напишем эту функцию:

def filter_currency(list_curr: list, currency: str):
    for i in list_curr:
        if i['operationAmount']['currency']['code'] == currency:
            yield i.get('id')

#присваиваем новой переменной генератор:
transact_gen = filter_currency(transactions, 'RUB')

#напишем функцию для определения количества транзакций с заданной валютой
def number_of_trans(list_curr: list, currency: str):
    list_count_trans: list = []
    count = 0
    for j in list_curr:
        if j['operationAmount']['currency']['code'] == currency:
            if j['operationAmount']['currency']['code'] not in list_count_trans:
                list_count_trans.append(j)
                count += 1
            else:
                pass
        else:
            pass
    list_count_trans = []
    return count

print(f'Количество транзакций с такой валютой: {number_of_trans(transactions, 'RUB')}')

#выводим на печать результат расчета функции с помощью цикла for и аргумента кол-ва
#транзакций, полученных с помощью доп. функции number_of_trans()
# сразу скажу: этот цикл - вспомогательный, и его можно было и не писать вовсе, поэтому он
# и требует изменения вручную валюты в трех местах. Но вообще конечно можно просто запрашивать
# от пользователя ввод валюты и передавать этот ввод во все функции

for i in range(number_of_trans(transactions, 'RUB')):
    print(next(transact_gen))



