import pytest
from data.ss import SpreadsheetAPI


SPREDSHEET_ID = '12zzJdPU5IHvYFOIevTLAP7aj1caPEfV0MpbVFUIUzSo'
CREDENTIALS_FILE = 'credentials.json'
APIS =  ['https://www.googleapis.com/auth/spreadsheets']



spredsheet = SpreadsheetAPI(SPREDSHEET_ID, "Лист1", 0, CREDENTIALS_FILE, APIS)


def test_get_sheet():
    result = {'majorDimension': 'ROWS',
            'range': "'Лист1'!A1:Z1000",
            'values': [['1', '2', '3'],
                        ['ALex', '5', '6'],
                        ['7', '8', 'Test'],
                        ['10', '11', '12']]}
    assert spredsheet.get_sheet() == result


def test_get():
    result = {'majorDimension': 'ROWS',
            'range': "'Лист1'!A1:C5",
            'values': [['1', '2', '3'],
                        ['ALex', '5', '6'],
                        ['7', '8', 'Test'],
                        ['10', '11', '12']]}

    result2 = {'majorDimension': 'ROWS',
            'range': "'Лист1'!A1:Z5",
            'values': [['1', '2', '3'],
                        ['ALex', '5', '6'],
                        ['7', '8', 'Test'],
                        ['10', '11', '12']]}
    
    result3 = {'majorDimension': 'ROWS',
            'range': "'Лист2'!A1:C5",
            'values': [['1', '2', '3'],
                        ['ALex', '5', '6'],
                        ['7', '8', 'Test'],
                        ['10', '11', '12']]}

    assert spredsheet.get("'Лист1'!A1:C5") == result
    assert spredsheet.get("A1:C5") == result
    assert spredsheet.get("1:5") == result2
    assert spredsheet.get("'Лист2'!A1:C5") == result3

    with pytest.raises(ValueError):
        spredsheet.get('1:5')
        spredsheet.get([2, 6])
        spredsheet.get("1:C5")


def test_insert():

    # Создаём тестовый лист
    test_sheet_id = 123456
    test_sheet_title = "TestSheet"
    try:
        spredsheet.service.spreadsheets().batchUpdate(spreadsheetId = SPREDSHEET_ID, 
            body = {
                "requests": [
                    {
                        "addSheet": {
                            "properties": {
                                "sheetId": test_sheet_id,
                                "title": test_sheet_title,
                                "index": 1
                            }
                        }
                    }
                ]
            }
        ).execute()
    except Exception as e:
        print('TestSheet is already created')

    # Делаем необходимые тесты
    test_sheet_title='Лист3'
    insert_result = spredsheet.insert([[1, 2, 3]], 'A', 'C', test_sheet_title)
    insert_result2 = spredsheet.insert([[1, 2, 3]], sheet_name=test_sheet_title)
    insert_result3 = spredsheet.insert([[1, 2, 3]], 'D1', 'F1', test_sheet_title)
    insert_result4 = spredsheet.insert([[1, 2, 3],[4, 5, 6]], 'D1', 'F2', test_sheet_title)
    
        
    # Удаляем тестовый лист
    spredsheet.service.spreadsheets().batchUpdate(spreadsheetId = SPREDSHEET_ID, 
        body = {
            "requests": [
                {
                    "deleteSheet": {
                        "sheetId": test_sheet_id
                    }
                }
            ]
        }
    ).execute()

    assert insert_result == True
    assert insert_result2 == True
    assert insert_result3 == True
    assert insert_result4 == True


def test_clear():

    max_range = 'A1:E10'
    test_ranges = {
        'A2:D5': [  ['1', '2', '3', '4', '5'], 
                    ['', '', '', '', '5'], 
                    ['', '', '', '', '5'], 
                    ['', '', '', '', '5'], 
                    ['', '', '', '', '5']
                ],
        'A1': [  ['', '2', '3', '4', '5'], 
                    ['1', '2', '3', '4', '5'], 
                    ['1', '2', '3', '4', '5'], 
                    ['1', '2', '3', '4', '5'], 
                    ['1', '2', '3', '4', '5']
                ],
        'C3:F7': [  ['1', '2', '3', '4', '5'], 
                    ['1', '2', '3', '4', '5'], 
                    ['1', '2'], 
                    ['1', '2'], 
                    ['1', '2']
                ]
    }

    for t_range in test_ranges:

        # Создаём тестовый лист
        test_sheet_id = 123456
        test_sheet_title = "TestSheet"
        try:
            spredsheet.service.spreadsheets().batchUpdate(spreadsheetId = SPREDSHEET_ID, 
                body = {"requests": [{"addSheet": {"properties": {
                                    "sheetId": test_sheet_id,
                                    "title": test_sheet_title,
                                    "index": 1
                        }}}]}
            ).execute()
        except Exception as e:
            print('TestSheet is already created')
        
        # Заполняем лист данными
        body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"'{test_sheet_title}'!{max_range}",
                "values": [[1, 2, 3, 4, 5]] * 5}
            ]}
        spredsheet.service.spreadsheets().values().batchUpdate(spreadsheetId=SPREDSHEET_ID,
                                                                body=body).execute()

        # Проводим необходимые тесты

        spredsheet.clear(f"'{test_sheet_title}'!{t_range}") 
        expected_result = test_ranges[t_range]

        # Получаем результат
        response = spredsheet.service.spreadsheets().values().get(
                spreadsheetId=spredsheet.spreadsheet_id,
                range=f"'{test_sheet_title}'!{max_range}"
            ).execute()

        # Удаляем тестовый лист
        spredsheet.service.spreadsheets().batchUpdate(spreadsheetId = SPREDSHEET_ID, 
            body = {"requests": [{"deleteSheet": {"sheetId": test_sheet_id}}]}).execute()

        assert response['values'] == expected_result


def test_get_sheet_url():

    expected_result = 'https://docs.google.com/spreadsheets/d/' + SPREDSHEET_ID + '/edit#gid=0'
    assert spredsheet.get_sheet_url() == expected_result
