import logging
import time
import configparser
import chromedriver_autoinstaller
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def writeArca(title, context):
    chromeVer = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")

    try:
        driver = webdriver.Chrome(f'./{chromeVer}/chromedriver.exe', chrome_options=chrome_options)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chromeVer}/chromedriver.exe', chrome_options=chrome_options)
    logging.info('WebDriver Started up')

    config = configparser.ConfigParser()
    config.read('config.ini')
    logging.info('Login Information Loaded')

    driver.get("https://arca.live/u/login")
    driver.implicitly_wait(3)
    logging.info('Arcalive Login Started')

    driver.find_element_by_css_selector('#idInput').send_keys(config['USER_INFO']['ID'])
    driver.find_element_by_css_selector('#idPassword').send_keys(config['USER_INFO']['PW'])
    driver.find_element_by_css_selector(
        'article > div > div.col-sm-12.col-lg-10 > div > div > form > div.btns > button').click()
    driver.implicitly_wait(3)
    logging.info('Arcalive Loginned')

    driver.get('https://arca.live/b/dakimakura/write')
    logging.info('Go to Write page')

    time.sleep(3)
    driver.find_element_by_css_selector('button.btn.btn-outline-danger.mr-auto').click()
    driver.implicitly_wait(3)
    logging.info('Popup Closed')

    inputRadio = driver.find_element_by_xpath('//*[@id="category-성인"]')
    driver.execute_script("arguments[0].checked = true", inputRadio)
    logging.info('Radio Button Selected')

    driver.find_element_by_css_selector('#inputTitle').send_keys(title)
    driver.find_element_by_css_selector('#html-1').click()
    logging.info('Title Inputed')

    time.sleep(2)

    # driver.execute_script('')
    inputField = driver.find_element_by_css_selector(
        '#article_write_form > div.write-body > div > div.fr-wrapper.show-placeholder > textarea.fr-code')
    driver.execute_script("arguments[0].value = arguments[1];", inputField, context)
    driver.implicitly_wait(10)
    logging.info('Detail Inputed')

    driver.find_element_by_css_selector('#submitBtn').click()
    logging.info('Submitted')

    driver.quit()
    logging.info('Webdriver Closed')