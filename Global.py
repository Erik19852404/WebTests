import os
import time
import logging
import unittest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pathLog = 'D:\\Git\\WebTests\\Logs\\LogDebug.txt'
pathChromeDriver = r'D:\Git\WebTests\Drivers\chromedriver.exe'
driver = None

def RemoveOldLogs(logPaths):
    for logPath in logPaths:
        if os.path.exists(logPath):
            os.remove(logPath)

def SetPathLogs(_path):
    logging.basicConfig(filename=_path, encoding='utf-8', level=logging.DEBUG)

def ConfigLogs():
    SetPathLogs(pathLog[0:len(pathLog) - 4] + datetime.now().strftime("%d_%m_%H_%M_%S") + pathLog[len(pathLog) - 4:])

def GetChromeDriver():
    return webdriver.Chrome(executable_path=pathChromeDriver)

def GetFirefoxDriver():
    return webdriver.Firefox()

def InitDriver():
    global driver
    driver = GetChromeDriver()

def CloseDriver():
    driver.close()
