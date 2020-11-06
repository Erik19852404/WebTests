import os
import time
import unittest
import logging

import Global

pathLog = 'D:\\Git\\WebTests\\Logs\\LogDebug.txt'

def ConfigLogs():
    Global.RemoveOldLogs([pathLog])
    Global.SetPathLogs(pathLog)

def TestOpenStartPage():
    ConfigLogs()
    logging.debug('TestOpenStartPage started...')
    driver = Global.GetChromeDriver()
    result = True
    try:
        driver.get('http://kitchen/')
    except Exception as ex:
        logging.error(ex)
        result = False
    finally:
        driver.close()
        logging.debug('TestOpenStartPage finished...')
    return result