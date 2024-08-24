from src.decorators import log_parameters

ttt = "my_log.txt"


@log_parameters(ttt)
def my_function(x, y):
    """Здесь определяем саму ту функцию, которая у нас будет делать действия"""
    return x + y


my_function(1, 3)

# создадим функцию специально для ошибки


@log_parameters(ttt)
def func_with_error(x, y):
    return x + y


def test_log_parameters():

    # передаем в функцию заведомо верный тип данных и тестируем
    assert my_function(5, 6) == 11
    # тестируем на наличие в файле вывода нужной строчки
    with open(ttt, "r") as file:
        log = file.read()
        assert "my_function ok" in log


# тестируем ошибочную функцию. Создаем специальную функцию для теста

func_with_error(7, "")


def test_log_par_error():

    with open(ttt, "r") as file:
        log = file.read()
        assert "TypeError" in log
