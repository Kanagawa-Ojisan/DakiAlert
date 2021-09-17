import logging
from datetime import datetime


def sourceMaker(list_of_dicts):
    logging.info('Editing Context Started')
    resultString = '<table style=\"width:100%;\"><thead><tr><th style=\"width:40%;text-align:center;background-color:rgb(71, 85, 119);\">' \
                   '<strong><span style=\"color:rgb(255, 255, 255);\">이미지</span></strong></th><th colspan=\"2\" ' \
                   'style=\"width:60%;text-align:center;background-color:rgb(71, 85, 119);\"><strong><span style=\"color:rgb(239, 239, 239);\">' \
                   '상세 정보</span></strong></th></tr></thead><tbody>'

    for dicts in list_of_dicts:
        if dicts['기한'] == datetime(1900, 1, 1):
            dicts['기한'] = '-'
        elif dicts['기한'].hour == 23 and dicts['기한'].minute == 59:
            dicts['기한'] = dicts['기한'].strftime('%Y-%m-%d')
        elif dicts['기한'].second == 0:
            dicts['기한'] = dicts['기한'].strftime('%Y-%m-%d %H:%M')
        else:
            pass

        tempString = '<tr><td rowspan=\"7\" style=\"padding:0px;width:40%;\"><a href=\"' \
                     + dicts['링크'] + '\" target=\"_blank\"><img style="width:100%;" src=\"' \
                     + dicts['이미지'] + '\" class=\"fr-fic fr-dii\"></a></td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>서클명</strong></td><td style=\"text-align:center;\">' + dicts['서클명'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>제품명</strong></td><td>' + dicts['제품명'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>재질</strong></td><td style=\"text-align:center;\">' + dicts['재질'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>주문형식</strong></td><td style=\"text-align:center;\">' + dicts['주문형식'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>기한</strong></td><td style=\"text-align:center;\"><strong>' + str(
            dicts['기한']) + '</strong></td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>비고</strong></td><td>' + str(dicts['비고']) + '</td></tr>'
        # IMG Tag
        resultString += tempString
    resultString += '</tbody></table><p><br></p>'
    logging.info('Editing Context Completed')

    return resultString


def titleMaker():
    logging.info('Editing Title Started')
    dt = datetime.today()
    dtWeek = int(dt.strftime("%V"))

    dtFirst = datetime(dt.year, dt.month, 1)
    dtFirstWeek = int(dtFirst.strftime("%V"))

    result = str(dt.month) + '월 ' + str(dtWeek - dtFirstWeek + 1) + '주차 다키 정리'
    logging.info('Editing Title Completed')

    return result
