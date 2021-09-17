import chromeControl
import gSheet
import stringControl

if __name__ == '__main__':
    dic = gSheet.readGSheet()
    print('All Google Sheet Read')
    print(dic)
    title = stringControl.titleMaker()
    print('Making Title Complete')
    context = stringControl.sourceMaker(dic)
    print('Making Context Complete')

    # title = '테스트'
    # context = '섹스보지자지털'
    print(title)
    # print(context)

    chromeControl.writeArca(title, context)
