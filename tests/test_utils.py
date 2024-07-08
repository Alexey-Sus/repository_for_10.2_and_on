import json
from unittest.mock import patch, mock_open, MagicMock
from src.utils import fin_oper_data
from src.utils import get_rub_amnt_for_trns
from dotenv import load_dotenv
import os

load_dotenv()
KEY_API = os.getenv("API_KEY")

# сначала тестируем функцию fin_oper_data, которая загружает из json-файла список словарей
# с транзакциями и переводит его в python-совместимый формат (тип данных dict)


def test_fin_oper_data():
    """Функция тестирования функции, которая извлекает данные из JSON-файла и возвращает python-объект (список)"""
    # вводим тестовое значение переменной для mock; только один элемент списка
    mock_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    mock_file = json.dumps(mock_data)
    with patch("builtins.open", mock_open(read_data=mock_file)):
        result = fin_oper_data("../src/new_json.json")
        result_no_file = fin_oper_data("../data/some_nonexistent_file.json")
        assert result == mock_data
        assert result_no_file == []

