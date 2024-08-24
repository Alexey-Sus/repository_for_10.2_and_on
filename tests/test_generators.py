from src.generators import filter_currency, trans_descr, card_number_gen

# в первой функции в качестве аргументов передаются список транзакций и валюта
# во второй функции в качестве аргумента передается только список транзакций
# в третьей функции в качестве аргумента передаются только начало и конец диапазона

# укажем переменную списка транзакций для проверки функций

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

# тестируем генератор первой функции


def test_transact_gen():
    """Тестовая функция для проверки функции выдачи id транзакций по запросу"""
    transact_gen = filter_currency(transactions, "USD")
    assert next(transact_gen) == 939719570
    assert next(transact_gen) == 142264268
    assert next(transact_gen) == 895315941


# тестируем генератор второй функции
def test_gen_descr_trans():
    '''Тестовая функция для тестирования функции-генератора, которая выводит описание транзакций по запросу'''
    gen_descr_trans = trans_descr(transactions)
    assert next(gen_descr_trans) == "Перевод организации"
    assert next(gen_descr_trans) == "Перевод со счета на счет"
    assert next(gen_descr_trans) == "Перевод со счета на счет"
    assert next(gen_descr_trans) == "Перевод с карты на карту"


# тестируем третью функцию, которая выводит маски для номеров карт по заданному диапазону

# эта функция называется card_number_gen; для нее в теле тестовой функции создадим специальный генератор


def test_card_number_gen():
    '''Тестовая функция для тестирования функции, генерирующей номера карт'''
    # определяем специальный генератор для этой функции
    gen_for_card_number_gen = card_number_gen("20", 25)
    assert next(gen_for_card_number_gen) == "XXXX XXXX XXXX XX20"
    assert next(gen_for_card_number_gen) == "XXXX XXXX XXXX XX21"
    assert next(gen_for_card_number_gen) == "XXXX XXXX XXXX XX22"
    assert next(gen_for_card_number_gen) == "XXXX XXXX XXXX XX23"
