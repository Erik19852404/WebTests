import os
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='\\Git\\WebTests\\Logs\\testLog.txt', level=logging.DEBUG)

def GetChromeDriver():
    return webdriver.Chrome(executable_path=r'D:\Git\WebTests\Drivers\chromedriver.exe')

driver = GetChromeDriver()
driver.get("https://mail.ru")
time.sleep(3)
driver.close()
logging.debug("Test 01 complete...")