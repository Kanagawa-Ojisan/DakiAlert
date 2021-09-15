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

import chromeControl


if __name__ == '__main__':

    context = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    chromeControl.writeArca(context)
