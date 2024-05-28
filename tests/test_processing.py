from src.processing import list_sort_date, list_for_state

# вводим переменную для проверки функций

list_orig: list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
]


def test_list_sort_date():
    """Тестовая для проверки функции по сортировке элементов списка по дате, с разными входными данными"""
    # переменная, которая должна быть возвращена:
    var_for_output: list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert list_sort_date(list_orig, False) == var_for_output
    assert list_sort_date([]) == []
    assert list_sort_date("343434") == []
    assert list_sort_date({}) == []


def test_list_for_state():
    """Тестовая для проверки функции по сортировке элементов списка по EXECUTED/CANCELLED,
    с разными входными данными"""
    # переменная, которая должна быть возвращена:
    var_for_output: list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert list_for_state(list_orig) == var_for_output
    assert list_for_state([]) == []
    assert list_for_state("") == []
    assert list_for_state({}) == []


# тестируем обе функции с помощью их фикстуры из файла conftest.py


def test_list_sort_date_1(fixt_for_lists):
    """Тестовая для проверки функции по сортировке элементов списка по дате, с помощью фикстуры из файла
    conftest.py"""
    var_for_output: list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert list_sort_date(fixt_for_lists, False) == var_for_output


def test_list_for_state_1(fixt_for_lists):
    """Тестовая для проверки функции по сортировке элементов списка по EXECUTED/CANCELLED, с помощью фикстуры
    из файла conftest.py"""
    var_for_output: list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert list_for_state(fixt_for_lists) == var_for_output

print()
