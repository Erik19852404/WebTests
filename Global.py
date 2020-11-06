import os
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def RemoveOldLogs(logPaths):
    for logPath in logPaths:
        if os.path.exists(logPath):
            os.remove(logPath)

def SetPathLogs(_path):
    logging.basicConfig(filename=_path, encoding='utf-8', level=logging.DEBUG)

def GetChromeDriver():
    return webdriver.Chrome(executable_path=r'D:\Git\WebTests\Drivers\chromedriver.exe')
