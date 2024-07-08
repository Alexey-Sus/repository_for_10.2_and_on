from src.utils import fin_oper_data
from src.read_from import read_from_csv, read_from_excel_2
from datetime import datetime as dt
from src.widget import mask_for_acc_card
import re


def main():
    """Основная функция в программе, организующая всю бизнес-хлогику"""

    # ввод пользователем выбора - считывать из JSON, CSV или XLSX - и проверка этого ввода
    list_choice: list = ["", "JSON-файл", "CSV-файл", "XLSX-файл"]

    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    first_choice = input()

    if first_choice in ["1", "2", "3"]:
        print(f"Для обработки выбран {list_choice[int(first_choice)]}")

    else:
        while True:
            print("Вы ввели недействительное значение. Введите цифры 1, 2 или 3: ")
            first_choice = input()
            if int(first_choice) in [1, 2, 3]:
                print(f"Для обработки выбран {list_choice[int(first_choice)]}")
                break
    print()

    # ввод пользователем статуса операции и проверка этого ввода, с получением переменной status_trans
    # в виде строки
    while True:
        status_trans: str = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n "
        ).upper()
        if status_trans in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status_trans}"')
            break
        else:
            print(f'Статус операции "{status_trans}" недоступен.\n')

    print()

    # ввод пользователем выбора сортировки по дате и проверка этого ввода, с получением перемею bool srt_d
    while True:
        sorted_date: str = input(
            "It's not over yet. Нужно сортировать по дате? да/нет: \n "
        )
        if sorted_date.lower() in ["да", "нет"]:
            srt_d = True if sorted_date.lower() == "да" else False
            break
        else:
            print('Вы ввели что-то не то. Вводите только "да" или "нет": ')
    print(f"Вы ввели статус сортировки по дате: {sorted_date.lower()}, {srt_d}")

    # если сортировать по дате нужно, запрашиваем у пользователя направление сортировки - по возрастанию
    # или убыванию. Получаем переменную srt_кум типа bool
    if srt_d:
        while True:
            sorted_reverse: str = input("Сортируем по возрастанию или убыванию? \n ")
            if sorted_reverse.lower() in ["по возрастанию", "по убыванию"]:
                if sorted_reverse.lower() == "по возрастанию":
                    srt_rev = False
                    break
                else:
                    srt_rev = True
                    break
            else:
                print(
                    'Вы ввели что-то не то. Вводите только "по возрастанию" или "по убыванию": '
                )
        print(
            f'Вы ввели статус сортировки по возрастанию или убыванию: "{sorted_reverse.lower()}", {srt_rev}'
        )
    else:
        srt_rev = False
        pass
    # ввод пользователем рублевых или non-рублевых транзакций и проверка этого вывода. Получаем RUB_trans bool
    while True:
        rub_or_all: str = input(
            "Stay here for a bit more. Выводить только RUB-транз или все? да/нет: \n"
        )

        if rub_or_all.lower() in ["да", "нет"]:
            RUB_trans = True if rub_or_all.lower() == "да" else False
            break

        else:
            print('Be careful with what you input. Only "да" or "нет" are accepted')

    print(
        f'Вы ввели статус транзакций: {'только рублевые' if RUB_trans else '"по всем валютам"'}'
    )

    # ввод пользователем выбора фильтрации тр-ий по слову в описании и (если да) ввод этого
    # слова и проверка этого ввода получаем сюда переменную word_in_descr строкового типа wrd_to_use и
    # wrd_descr bool
    while True:
        word_in_descr: str = input(
            "Your nightmare is still here. Wanna some word to filter trxs out? да/нет: \n"
        )

        if word_in_descr.lower() == "да":
            wrd_descr: bool = True
            wrd_to_use: str = input(
                "So please input here your lovely word(s) to filter trxs out:\n"
            )
            break

        elif word_in_descr.lower() == "нет":
            wrd_descr = False
            wrd_to_use: str = ""
            break

        else:
            print('You think it is funny? Only "да" or "нет" are accepted!')

    print(f"Ваш статус фильтрации транзакций: {word_in_descr.lower()}, {wrd_descr}")
    print(f"Слово для фильтрации: {wrd_to_use if wrd_descr else 'без слова'}")

    return first_choice, status_trans, srt_d, srt_rev, RUB_trans, wrd_descr, wrd_to_use


print()

s = main()

status_trans = s[1]
srt_d = s[2]
srt_rev = s[3]
RUB_trans = s[4]
wrd_descr = s[5]
wrd_to_use = s[6]

# делаем вызов нужной функции в зав-ти от значения переменной first_choice:
if s[0] == "1":
    result_interm = fin_oper_data("../data/operations.json")
elif s[0] == "2":
    result_interm = read_from_csv("../data/transactions.csv")
else:
    result_interm = read_from_excel_2("../data/transactions_excel.xlsx")


# прописываем функцию для работы со словарем из JSON-файла
def output_json(
    result: list, tr_st: str, srtd_date: bool, srtd_rev: bool, RUB_tr, wrd_dsc, wrduse
) -> list:
    """Функция вывода списка словарей в том же виде, что в файле JSON, но с учетом
    выбора пользователя. Эта функция работает только для файла JSON, а для CSV и Excel будет другая,
    так как там другой формат вывода словаря"""
    list_output: list = []

    if not result or not tr_st or result == [] or tr_st == "":
        return []

    else:

        # сначала извлекаем все транзакции с нужным статусом
        for i in result:
            if i.get("state") == tr_st:
                list_output.append(i)
        # код выше нормально возвращает list_output с нужным статусом транзакции

        # дальше делаем сортировку списка (у нас уже список list_output) по дате
        if srtd_date:
            list_sorted_date: list = sorted(
                list_output, key=lambda i: i.get("date"), reverse=srtd_rev
            )
            list_output = list_sorted_date
        else:
            pass
        # код выше нормально выдает новый список list_output при наличии флага sorted_d на сортировку по дате

        # дальше пишем сортировку по наличию флага RUB_trans - сортировать или не сортировать по рублевым транзакциям
        if RUB_tr:
            list_for_rub: list = []
            for i in list_output:
                if i["operationAmount"]["currency"]["code"] == "RUB":
                    # if x.get('operationAmount').get('currency').get('code') == 'RUB':
                    list_for_rub.append(i)
            list_output = list_for_rub
        else:
            pass
        # код выше успешно отфильтровывает транзакции по рублю (при наличии такого флага)

        # дальше фильтруем по опред. слову в описании. Тут есть переменные:
        #  wrd_descr: bool и wrd_to_use: str
        if wrd_dsc:
            list_for_desc: list = []
            for i in list_output:
                pattern = r"\b\w*" + wrduse + r"\w*\b"
                if re.search(pattern, i["description"]):
                    list_for_desc.append(i)
            list_output = list_for_desc
        else:
            pass
        # код выше нормально и хорошо возвращает список словарей при условии фильтрации по слову в поле description
        # то есть, дальше можем работать с этим списком и выводить строки в формате как в условиях задачи.

        return list_output


if __name__ == "__main__" and s[0] == "1":
    result = output_json(
        result_interm, status_trans, srt_d, srt_rev, RUB_trans, wrd_descr, wrd_to_use
    )
else:
    pass


# а сюда теперь пишем функцию для работы с файлами CSV и Excel - она одинаковая, но логика в ней чуть другая
# чем в функции для файлафффф JSON
def output_csv_excel(
    result: list,
    tr_st: str,
    srtd_date: bool,
    srtd_rev: bool,
    RUB_tr: bool,
    wrd_dsc: bool,
    wrduse: str,
) -> list:
    """Функция выводит список операций по параметрам от пользователя. Работает только с файлами
    CSV и Excel, так как у файла JSON там другой совсем формат вывода словаря"""
    list_output: list = []

    if not result or not tr_st or result == [] or tr_st == "":
        return []
    else:

        for i in result:
            if i.get("state") == tr_st:
                list_output.append(i)

        if srtd_date:
            list_sorted_date: list = sorted(
                list_output, key=lambda i: i.get("date"), reverse=srtd_rev
            )
            list_output = list_sorted_date
        else:
            pass

        if RUB_tr:
            list_for_RUB: list = []
            for i in list_output:
                if i.get("currency_code") == "RUB":
                    list_for_RUB.append(i)
            list_output = list_for_RUB
        else:
            pass

        if wrd_dsc:
            list_for_descr: list = []
            for i in list_output:
                pattern = r"\b\w*" + wrduse + r"\w*\b"
                if re.search(pattern, i["description"]):
                    list_for_descr.append(i)
            list_output = list_for_descr
        else:
            pass

        return list_output


if __name__ == "__main__" and s[0] in ["2", "3"]:
    result = output_csv_excel(
        result_interm, status_trans, srt_d, srt_rev, RUB_trans, wrd_descr, wrd_to_use
    )
else:
    pass

if not result:
    print("Операций по заданным критериям не найдено")

else:
    print()
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(result)}")
    print()
    # дальше обрабатываем список и делаем его вывод так, чтобы он соответствовал условиям задачи (по три строки
    # на каждую операцию)
    for i in result:
        print()

        # сначала приводим дату в каждом словаре к требуемому в задании формату
        first_date = dt.strptime(i["date"][0:10], "%Y-%m-%d")
        i["date"] = first_date.strftime("%d.%m.%Y")

        # затем вызываем функцию mask_for_acc_card для счета (карты) в поле to каждого словаря
        str_to = mask_for_acc_card(str(i.get("to")))
        i["to"] = str_to

        # затем вызываем ту же самую ф-ию mask_for_acc_card для счета/карты в поле from каждого словаря
        str_from = mask_for_acc_card(str(i.get("from")))
        i["from"] = str_from

        # и теперь уже компонуем нужные строчки так, как указано в задании
        print(f"{i['date']} {i['description']}")
        if i["description"] == "Открытие вклада":
            print(i["to"])
        else:
            print(f"{i['from']} -> {i['to']}")

        # для вывода последней строчки есть разница между словарем JSON и словарями из CSV и Excel, поэтому тут
        # есть логика выбора:

        if s[0] == "1":
            print(
                f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
            )
        elif s[0] in ["2", "3"]:
            print(f"Сумма: {i['amount']} {i['currency_name']}")
