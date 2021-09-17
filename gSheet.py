import logging

import gspread
import configparser
from datetime import datetime

def readGSheet():
    config = configparser.ConfigParser()
    config.read('config.ini')
    logging.info('Google Information Loaded')

    gc = gspread.service_account(filename=config['GOOGLE_INFO']['JSON'])
    sh = gc.open_by_url(config['GOOGLE_INFO']['URL'])
    logging.info('Google Sheet Connected')

    worksheet = sh.get_worksheet(0)
    listOfDicts = worksheet.get_all_records()
    logging.info('All Record Loaded')
    bookListOfDicts = []
    nowListOfDicts = []

    for dicts in listOfDicts:
        if dicts['주문형식'] == '접수완료' or dicts['주문형식'] == '통상판매':
            continue
        elif dicts['주문형식'] == '재고판매':
            dicts['기한'] = datetime(1900, 1, 1)
            nowListOfDicts.append(dicts)
        else:
            try:
                dicts['기한'] = datetime.strptime(dicts['기한'], '%Y-%m-%d %H:%M')
            except ValueError:
                dicts['기한'] = datetime(1900, 1, 1)
            bookListOfDicts.append(dicts)
    logging.info('All Record Modified')


    resultOfDicts1 = sorted(bookListOfDicts, key=lambda t: (t['기한'], t['서클명'], t['제품명']))
    resultOfDicts2 = sorted(nowListOfDicts, key=lambda t: (t['서클명'], t['제품명']))
    resultOfDicts = [resultOfDicts1, resultOfDicts2]
    logging.info('All Record Arranged')

    return resultOfDicts