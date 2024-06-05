# Напишите декоратор log, который будет логировать вызов функции и ее результат в файл
# или в консоль. Декоратор log принимает один необязательный аргумент filename,
# который определяет путь к файлу, в который будут записываться логи. Если filename
# не задан, логи будут выводиться в консоль. Если вызов функции закончился ошибкой,
# то записывается сообщение об ошибке и входные параметры функции.

# успешное выполнение функции: запись в файл фразы my_function ok и результата работы функции, например, 1 + 2 = 3

# неуспешное выполнение функции: my_function error: <тип ошибки>. Inputs: (1, 2), {}
# где <тип ошибки> заменяется на текст ошибки, а (1, 2) и {} – на значения позиционных и именованных
# аргументов функции соответственно.

# Function multiply called with args: (2, 3) and kwargs: {}. Result: 6


def log_parameters(ppp):
    """Декоратор для вызова функции и записи результатов в файл либо в консоль. Если задан файл, то результат выводится
    в файл, а если не задан, то просто выводится в консоль"""

    def log(function):
        def inner(*args, **kwargs):
            message = ""
            try:
                result = function(*args, **kwargs)
                message = f"{function.__name__} ok Result: {result}\n"
                return result
            except Exception as exc:
                message = (
                    f"{function.__name__} {type(exc).__name__}. Inputs: {args} {kwargs}"
                )

            finally:
                if ppp:
                    with open(ppp, "at") as file:
                        file.write(message + "\n")
                else:
                    print(message)
            return message

        return inner

    return log


ttt = "my_log.txt"


@log_parameters(ttt)
def my_function(x, y):
    """Здесь определяем саму ту функцию, которая у нас будет делать действия"""
    return x + y


my_function(1, 2)
