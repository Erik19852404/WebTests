import os
import sys
import time
import logging
import unittest
from datetime import datetime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Global

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pathLog = 'D:\\Git\\WebTests\\Logs\\LogDebug.txt'

def ConfigLogs():
    Global.SetPathLogs(pathLog[0:len(pathLog) - 4] + datetime.now().strftime("%d_%m_%H_%M_%S") + pathLog[len(pathLog) - 4:])

class TestCaseKitchenAuthorization(unittest.TestCase):
    def setUp(self):#some actions before start test
        ConfigLogs()
        self.driver = Global.GetChromeDriver()

    def tearDown(self):#some actions after test run
        self.driver.close()

    def test_OpenMainPage(self):
        logging.debug('test_OpenMainPage started...')
        driver = self.driver
        testResult = True
        try:
            driver.get('http://kitchen/')
        except Exception as ex:
            logging.error(ex)
            testResult = False
        finally:
            logging.debug('test_OpenMainPage finished...')                                                                                    
        self.assertTrue(testResult, "Can't open main page...")
        
    def test_LoginFormOpen(self):
        logging.debug('test_LoginFormOpen started...')
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        testResult = True
        try:
            driver.get('http://kitchen/')
            btnEnter = driver.find_element_by_partial_link_text('ход')
            btnEnter.click()
            loginForm = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="myModal"]/div')))
            ActionChains(driver).move_to_element(loginForm).perform()
        except Exception as ex:
            logging.error(ex)
            testResult = False
        finally:
            logging.debug('test_LoginFormOpen finished...')  
        self.assertTrue(testResult, "Can't open login form...")