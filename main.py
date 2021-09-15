# import time
# import logging
# import smtplib

import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
import chromedriver_autoinstaller
import subprocess
import os


import clipboard
# from win10toast import ToastNotifier



def arca():

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

    # driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
    driver.get("https://arca.live/u/login")
    driver.implicitly_wait(3)

    driver.find_element_by_css_selector('#idInput').send_keys(config['USER_INFO']['ID'])
    driver.find_element_by_css_selector('#idPassword').send_keys(config['USER_INFO']['PW'])
    driver.find_element_by_css_selector('article > div > div.col-sm-12.col-lg-10 > div > div > form > div.btns > button').click()
    driver.implicitly_wait(3)


    driver.get('https://arca.live/b/dakimakura/write')

    time.sleep(2)
    driver.find_element_by_css_selector('button.btn.btn-primary').click()
    driver.implicitly_wait(3)

    driver.find_element_by_css_selector('#inputTitle').send_keys('테스트')
    driver.find_element_by_css_selector('#html-1').click()

    time.sleep(2)
    context = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # print(context)
    driver.find_element_by_css_selector('#article_write_form > div.write-body > div > div.fr-wrapper.show-placeholder > textarea').send_keys(context)
    driver.implicitly_wait(3)

    driver.find_element_by_css_selector('#submitBtn').click()
    # da = Alert(driver)
    # da.accept()

    # driver.get(url)
    # driver.implicitly_wait(3)
    # driver.save_screenshot('screenshot.png')

    # Text = driver.find_element_by_css_selector(
    #     "#novel_drawing"
    # ).text

    driver.quit()

    # return Text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arca()
    # novel = refresher("https://novelpia.com/viewer/265792")
    # clipboard.copy(novel)

