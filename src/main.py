from src.widget import get_date, mask_for_acc_card
# from src.widget_addit import get_max_product, get_similar_char
from src.processing import list_for_state, list_sort_date

# переменные для проверки основного задания
date_for_ex = "2018-12-11T02:26:18.671407"
str_new: str = "Visa Gold 8976700079228960"

# переменные для проверки дополнительного задания
list_for_list_char: list = ["helloh", "worldw", "apple", "pear", "banana", "pop"]
list_for_product = [2, 3, 5, -7, 11, -345]

# вызываем функции из основного задания
print(f"Маскированныый номер сущности: {mask_for_acc_card(str_new)}")
print(f"Дата в формате ДД.ММ.ГГГГ: {get_date(date_for_ex)}")

# вызываем функции из дополнительного задания
# print(f"Нов. сп-к один. 1-й и посл. бкв.: {get_similar_char(list_for_list_char)}")
# print(f"Макс. произв. эл-ов списка равно {get_max_product(list_for_product)}")

# вводим тестовую переменную для функций из основногоо задания урока 10.1
# и вызываем функции из основного задания урока 10.1

list_orig: list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
]

# проверка работы функций (для функции сортировки передаем значение 'cancelled')

for i in list_sort_date((list_orig), False):
    print(i)

print()
print()

for i in list_for_state(list_orig):
    print(i)
