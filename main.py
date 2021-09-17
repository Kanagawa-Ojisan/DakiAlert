import chromeControl
import gSheet
import stringControl
import logging

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    fileHandler = logging.FileHandler('history.log','a','utf-8')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    logging.info('Logging Started')
    dic = gSheet.readGSheet()
    dic1 = dic[0] #예약중
    dic2 = dic[1] #재고판매

    print(dic1)
    print(dic2)

    logging.info('All Google Sheet Read - len(dic1) : ' + str(len(dic1)) + ' | len(dic2) : ' + str(len(dic2)))
    print(dic)
    title = stringControl.titleMaker()
    logging.info('Making Title Complete - title : ' + title)
    context1 = stringControl.sourceMaker(dic1)
    context2 = stringControl.sourceMaker(dic2)
    context = '<p style=\"text-align: center;\"><strong>PC환경에서 보는것을 권장합니다.</strong></p>' \
              '<p style=\"text-align: center;\"><strong>아래 표의 내용은 예약 기한이 가까운 다키마쿠라가 위로 오게끔 정렬되어 있습니다.</strong></p>' \
              '<p style=\"text-align: center;\"><strong>이미지를 클릭하면 상품 페이지로 이동합니다.</strong></p><p><br></p>'\
              '<hr><p style=\"text-align: center;\"><strong><span style=\"font-size: 30px;\">예약 판매분</span></strong></p><p><br></p>' + context1 \
              + '<p><br></p><hr><p style=\"text-align: center;\"><strong><span style=\"font-size: 30px;\">재고 판매분</span></strong></p><p><br></p>' + context2 + \
              '<p style=\"text-align:right;\"><span style=\"font-size:11px;color:rgb(204, 204, 204);\">edited by DakiAlert</span></p>'

    logging.info('Making Context Complete - len(Context) : ' + str(len(context)))

    # title = '테스트'
    # context = '섹스보지자지털'
    print(title)
    print(context)

    # logging.info('Start Webdriver Control')
    # chromeControl.writeArca(title, context)
    # logging.info('Logging Completed')