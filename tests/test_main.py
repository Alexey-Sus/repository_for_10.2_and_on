from src.main import output_json, output_csv_excel


trans_status = "EXECUTED"
strteddate = True
srtedrev = True
RUB_tr = True
wrd_dsc = True
wrduse = "word"

result_list = [
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
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
]

result_for_xls_csv = [
    {
        "id": 154927927,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {
            "amount": "30153.72",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 7810846596785568",
        "to": "Счет 43241152692663622869",
    },
    {
        "id": 482520625,
        "state": "EXECUTED",
        "date": "2019-11-13T17:38:04.800051",
        "operationAmount": {
            "amount": "62814.53",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 38611439522855669794",
        "to": "Счет 46765464282437878125",
    },
]


def test_output_json():
    assert (
        output_json([], trans_status, strteddate, srtedrev, RUB_tr, wrd_dsc, wrduse)
        == []
    )
    assert (
        output_json(result_list, "", strteddate, srtedrev, RUB_tr, wrd_dsc, wrduse)
        == []
    )
    assert (
        output_json(
            result_list, trans_status, strteddate, srtedrev, RUB_tr, wrd_dsc, wrduse
        )
        == []
    )


def test_output_csv_excel():
    assert (
        output_csv_excel(
            [], trans_status, strteddate, srtedrev, RUB_tr, wrd_dsc, wrduse
        )
        == []
    )
    assert (
        output_json(
            result_for_xls_csv, "", strteddate, srtedrev, RUB_tr, wrd_dsc, wrduse
        )
        == []
    )
    assert (
        output_json(
            result_for_xls_csv,
            trans_status,
            strteddate,
            srtedrev,
            RUB_tr,
            wrd_dsc,
            wrduse,
        )
        == []
    )
