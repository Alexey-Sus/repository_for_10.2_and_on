from src.widget import get_date, mask_for_acc_card
import pytest


def test_mask_for_acc_card():
    """Тестовая для проверки функции по нахождению маски счета (карты) с разными входными данными"""
    str_new: str = "Visa Gold 8976700079228958"
    assert mask_for_acc_card(str_new) == "Карта Visa Gold 8976 70** **** 8958"
    assert mask_for_acc_card("") == ""


# определяем фикстуру для функции test_get_date:


def test_get_date():
    """Тестовая для проверки функции по форматированию даты с разными входными данными"""
    date_for_ex: str = "2018-12-11T02:26:18.671407"
    assert get_date(date_for_ex) == "11.12.18"
    assert get_date("") == ""
    assert get_date([]) == ""
    assert get_date({}) == ""


# тестируем функцию get_date с помощью параметризации:
@pytest.mark.parametrize(
    "input_date, expected_date",
    [
        ("2034-07-15T02:26:18.671407", "15.07.34"),
        ("1977-01-02T02:26:18.671407", "02.01.77"),
        (3434343, ""),
        ("", ""),
        ([], ""),
        ({}, ""),
    ],
)
def test_get_date_1(input_date, expected_date):
    """Тестовая функция для проверки функции формата даты при помощи параметризации"""
    assert get_date(input_date) == expected_date

print()
