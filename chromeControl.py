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
    print('ChromeDriver Started up')

    config = configparser.ConfigParser()
    config.read('config.ini')

    driver.get("https://arca.live/u/login")
    driver.implicitly_wait(3)

    driver.find_element_by_css_selector('#idInput').send_keys(config['USER_INFO']['ID'])
    driver.find_element_by_css_selector('#idPassword').send_keys(config['USER_INFO']['PW'])
    driver.find_element_by_css_selector(
        'article > div > div.col-sm-12.col-lg-10 > div > div > form > div.btns > button').click()
    driver.implicitly_wait(3)
    print('Loginned')

    driver.get('https://arca.live/b/dakimakura/write')

    time.sleep(3)
    driver.find_element_by_css_selector('button.btn.btn-outline-danger.mr-auto').click()
    driver.implicitly_wait(3)
    print('Popup Closed')

    inputRadio = driver.find_element_by_xpath('//*[@id="category-성인"]')
    driver.execute_script("arguments[0].checked = true", inputRadio)
    print('Radio Button Selected')

    driver.find_element_by_css_selector('#inputTitle').send_keys(title)
    driver.find_element_by_css_selector('#html-1').click()
    print('Title Inputed')

    time.sleep(2)

    # driver.execute_script('')
    inputField = driver.find_element_by_css_selector(
        '#article_write_form > div.write-body > div > div.fr-wrapper.show-placeholder > textarea.fr-code')
    driver.execute_script("arguments[0].value = arguments[1];", inputField, context)
    driver.implicitly_wait(10)
    print('Detail Inputed')

    driver.find_element_by_css_selector('#submitBtn').click()
    print('Submitted')

    driver.quit()

