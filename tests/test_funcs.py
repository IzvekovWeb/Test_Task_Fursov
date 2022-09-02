import pytest
from funcs import *


def test_get_range():

    assert get_range() == None
    assert get_range('A1') == 'A1'
    assert get_range('A1', 'C5') == 'A1:C5'
    assert get_range('B2', 'E4', 'Лист1') == 'Лист1!B2:E4'
    assert get_range(start='C4', sheet_name='Лист1') == 'Лист1!C4:Z'
    assert get_range(end='B3') == 'A:B3'


def test_get_body_insert():

    expected_result = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": 'A1:B4',
             "values": [[1, 2, 3]]}
        ]}

    assert get_body_insert('A1:B4', [[1, 2, 3]]) == expected_result

    with pytest.raises(ValueError):
        get_body_insert('A2:C5', [1, 2, 3])
        get_body_insert('None!A3:E6', [[1, 2, 3]])