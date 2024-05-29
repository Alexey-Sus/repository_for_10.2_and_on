# Напишите генератор номеров банковских карт, который должен генерировать номера
# карт в формате XXXX XXXX XXXX XXXX, где X — цифра. Должны быть сгенерированы номера
# карт в заданном диапазоне, например от 0000 0000 0000 0001 до 9999 9999 9999 9999
# (диапазоны передаются как параметры генератора).

# for card_number in card_number_generator(1, 5):
#     print(card_number)
#
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005

start = input("Ввод начала диапазона номеров карт: ")
stop = int(input("...и окончания диапазона: "))


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
