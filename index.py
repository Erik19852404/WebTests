import os
import time
import logging

import TestSuite
import Global

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pathForLogs = '\\Git\\WebTests\\Logs\\testLog.txt'

def Main():
    Init()
    TestSuite.Test1()

def Init():
    Global.RemoveOldLogs()
    Global.SetPathFroLogs(pathForLogs)

Main()