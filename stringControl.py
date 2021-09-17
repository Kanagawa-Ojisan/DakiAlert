from datetime import datetime

def sourceMaker(list_of_dicts):
    resultString = '<p style=\"text-align: center;\"><strong>PC환경에서 보는것을 권장합니다.</strong></p>' \
                   '<p style=\"text-align: center;\"><strong>아래 표의 내용은 예약 기한이 가까운 다키마쿠라가 위로 오게끔 정렬되어 있습니다.</strong></p>' \
                   '<p style=\"text-align: center;\"><strong>이미지를 클릭하면 상품 페이지로 이동합니다.</strong></p><p><br></p>' \
                   '<table style=\"width:100%;\"><thead><tr><th style=\"width:40%;text-align:center;background-color:rgb(71, 85, 119);\">' \
                   '<strong><span style=\"color:rgb(255, 255, 255);\">이미지</span></strong></th><th colspan=\"2\" ' \
                   'style=\"width:60%;text-align:center;background-color:rgb(71, 85, 119);\"><strong><span style=\"color:rgb(239, 239, 239);\">' \
                   '상세 정보</span></strong></th></tr></thead><tbody>'

    for dicts in list_of_dicts:

        if dicts['기한'].hour == 23 and dicts['기한'].minute == 59 :
            dicts['기한'] = dicts['기한'].strftime('%Y-%m-%d')

        tempString = '<tr><td rowspan=\"7\" style=\"padding:0px;width:40%;\"><a href=\"'\
                     + dicts['링크'] + '\" target=\"_blank\"><img src=\"'\
                     + dicts['이미지'] + '\" class=\"fr-fic fr-dii\"></a></td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>서클명</strong></td><td>' + dicts['서클명'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>제품명</strong></td><td>' + dicts['제품명'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>재질</strong></td><td>' + dicts['재질'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>주문형식</strong></td><td>' + dicts['주문형식'] + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>기한</strong></td><td>' + str(dicts['기한']) + '</td></tr>'
        tempString += '<tr><td style=\"width:15%;word-break:keep-all;background-color:rgb(239, 239, 239);\">' \
                      '<strong>비고</strong></td><td>' + str(dicts['비고']) + '</td></tr>'
        # IMG Tag
        resultString += tempString
    resultString += "</tbody></table><p><br></p><p style=\"text-align:right;\"><span style=\"font-size:11px;color:rgb(204, 204, 204);\">edited by DakiAlert</span></p>"

    return resultString

def titleMaker():
    dt = datetime.today()
    dtWeek = int(dt.strftime("%V"))

    dtFirst = datetime(dt.year, dt.month, 1)
    dtFirstWeek = int(dtFirst.strftime("%V"))

    result = str(dt.month) + '월 ' + str(dtWeek-dtFirstWeek+1) + '주차 다키 정리'

    return result