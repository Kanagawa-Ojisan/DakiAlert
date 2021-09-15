import time

import gspread
from operator import itemgetter
import chromeControl


def gSheet():
    gc = gspread.service_account(filename='daki-alert-df8cac6c666f.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1LL7OlmqJD7JUPSG9NXOnKH4O2-I1eEjLWbQIKxO35k0')

    worksheet = sh.get_worksheet(0)
    list_of_dicts = worksheet.get_all_records()
    result_of_dicts = []

    for dicts in list_of_dicts:
        if dicts['주문형식'] == '접수완료' or dicts['주문형식'] == '통상판매':
            continue
        else:
            result_of_dicts.append(dicts)
        # result_of_dicts.append(dicts)

    result_of_dicts.sort(key=itemgetter('기한'))

    return result_of_dicts


def sourceMaker(list_of_dicts):
    resultString = "<table width=\"100%\"><thead><tr><th style=\"text-align:center;width:30%;\"><strong>샘플</strong></th><th style=\"text-align:center;width:24%;\"><strong>제품명</strong></th><th style=\"text-align:center;width:15%;\"><strong>재질</strong></th><th style=\"text-align:center;width:12%;\"><strong>주문형식</strong></th><th style=\"text-align:center;width:12%;\"><strong>기한</strong></th><th style=\"text-align:center;width:7%;\"><strong>링크</strong></th></tr></thead><tbody>"

    for dicts in list_of_dicts:
        tempString = "<tr><td style=\"padding:0px;\"><img src=\""+ dicts['이미지'] +"\" class=\"fr-fic fr-dii\"></td>"
        # IMG Tag
        tempString += "<td>" + dicts['이름'] + "</td>"
        tempString += "<td>" + dicts['재질'] + "</td>"
        tempString += "<td>" + dicts['주문형식'] + "</td>"
        tempString += "<td>" + dicts['기한'] + "</td>"
        tempString += "<td><a href=\"" + dicts['링크'] + "\" target=\"_blank\"><u><span style=\"color:rgb(65, 168, 95);\">URL</span></u></a></td></tr>"
        resultString += tempString
    resultString += "</tbody></table>"

    return resultString


if __name__ == '__main__':
    dic = gSheet()
    print(dic)
    context = sourceMaker(dic)
    # context = \
    #     '<table width=\'100%\'><tbody><tr><td>샘플</td><td>상품명</td><td>재질</td><td>주문형식</td><td>기한</td><td>링크</td></tr><tr><td><img src=\'https://booth.pximg.net/8b143a1d-a2e5-4d80-a7a6-8a3d15c7a171/i/3255495/1c51b4c6-8c9d-4c08-b0df-0efe5bba6aef.jpg\' class=\'fr-fic fr-dii\'></td><td>あーちゃん抱き枕カバー</td><td>사쿠라모찌</td><td>수주생산</td><td>2021-09-19</td><td><a herf=\'https://unagiyasan.booth.pm/items/3255495\'>URL</a></td></tr></tbody></table>'

    print(context)

    chromeControl.writeArca(context)
