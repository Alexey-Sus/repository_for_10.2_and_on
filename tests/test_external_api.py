import json
import os
from unittest.mock import MagicMock, patch
import requests
from dotenv import load_dotenv
from src.external_api import get_exch_rate

load_dotenv()
KEY_API = os.getenv("API_KEY")


# тестируем тут функцию обращения к API, которая написана в модуле external_api.py


@patch("requests.get")
def test_get_exch_rate(mock_get):
    # создаем фиктивный ответ с нужной структурой
    mock_response = MagicMock()
    mock_response.text = json.dumps({"info": {"rate": 88.833612}})

    # настраиваем mock_get чтобы он возвращал наш фиктивный ответ
    mock_get.return_value = mock_response

    # создаем из mock python-объект, чтобы потом в assertion сравнить одно из его значений с выводом функции:
    for_assertion = json.loads(mock_response.text)

    # вызываем тестируемую функцию и проверяем результат
    assert get_exch_rate("USD", KEY_API) == 88.833612
    assert get_exch_rate("USD", KEY_API) == for_assertion["info"]["rate"]
