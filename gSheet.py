import gspread
from datetime import datetime

def readGSheet():
    gc = gspread.service_account(filename='daki-alert-df8cac6c666f.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1LL7OlmqJD7JUPSG9NXOnKH4O2-I1eEjLWbQIKxO35k0')

    worksheet = sh.get_worksheet(0)
    listOfDicts = worksheet.get_all_records()
    totalOfDicts = []

    for dicts in listOfDicts:
        if dicts['주문형식'] == '접수완료' or dicts['주문형식'] == '통상판매':
            continue
        else:
            try:
                dicts['기한'] = datetime.strptime(dicts['기한'], '%Y-%m-%d %H:%M')
            except ValueError:
                dicts['기한'] = datetime(2000, 1, 1)
            totalOfDicts.append(dicts)

    resultOfDicts = sorted(totalOfDicts, key=lambda t: (t['기한'], t['서클명'], t['제품명']))
    print('List of Dicts')
    for dicts in resultOfDicts:
        if dicts['기한'] == datetime(1900,1,1):
            dicts['기한'] = '-'

    return resultOfDicts
