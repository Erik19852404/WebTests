import os
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='\\WebTests\\Logs\\testLog.txt', level=logging.DEBUG)

driver = webdriver.Chrome(executable_path=r'C:\Users\erik\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://mail.ru")
time.sleep(3)
driver.close()
logging.debug("Test 01 complete...")