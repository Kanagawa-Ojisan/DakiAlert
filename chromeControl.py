import time
import configparser
import chromedriver_autoinstaller
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def writeArca(context):
    chromeVer = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    chrome_options = Options()
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument('window-size=1920x1080')
    # chrome_options.add_argument("disable-gpu")

    try:
        driver = webdriver.Chrome(f'./{chromeVer}/chromedriver.exe', chrome_options=chrome_options)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chromeVer}/chromedriver.exe', chrome_options=chrome_options)

    config = configparser.ConfigParser()
    config.read('config.ini')

    driver.get("https://arca.live/u/login")
    driver.implicitly_wait(3)

    driver.find_element_by_css_selector('#idInput').send_keys(config['USER_INFO']['ID'])
    driver.find_element_by_css_selector('#idPassword').send_keys(config['USER_INFO']['PW'])
    driver.find_element_by_css_selector(
        'article > div > div.col-sm-12.col-lg-10 > div > div > form > div.btns > button').click()
    driver.implicitly_wait(3)

    driver.get('https://arca.live/b/dakimakura/write')

    time.sleep(3)
    driver.find_element_by_css_selector('button.btn.btn-outline-danger.mr-auto').click()
    driver.implicitly_wait(3)

    # driver.find_element_by_xpath('//*[@id="category-성인"]').click()
    driver.find_element_by_css_selector('#inputTitle').send_keys('테스트')
    driver.find_element_by_css_selector('#html-1').click()

    time.sleep(2)

    driver.execute_script('')
    driver.find_element_by_css_selector(
        '#article_write_form > div.write-body > div > div.fr-wrapper.show-placeholder > textarea.fr-code').send_keys(context)
    driver.implicitly_wait(100)

    driver.find_element_by_css_selector('#submitBtn').click()

    driver.quit()

