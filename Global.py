import os
import time
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def RemoveOldLogs():
    os.remove('\\Git\\WebTests\\Logs\\testLog.txt')

def SetPathFroLogs(_path):
    logging.basicConfig(filename=_path, level=logging.DEBUG)

def GetChromeDriver():
    return webdriver.Chrome(executable_path=r'D:\Git\WebTests\Drivers\chromedriver.exe')
