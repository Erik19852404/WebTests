import os
import sys
import time
import logging
import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import TestSuiteKitchen
import Global

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCaseKitchenAuthorization(unittest.TestCase):
    driverChrome = Global.GetChromeDriver()
    def setUp(self):#some actions before start test
        pass
    def tearDown(self):#some actions after test run
        pass
    def test_OpenMainPage(self):
        self.assertTrue(TestSuiteKitchen.TestOpenStartPage(), "Can't open main page...")
    def test_LoginFormOpen(self):
        driver = self.driverChrome
        wait = WebDriverWait(driver, 5)
        testResult = True
        errText = ''
        try:
            driver.get('http://kitchen/')
            btnEnter = driver.find_element_by_partial_link_text('ход')
            btnEnter.click()
            loginForm = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="myModal"]/div')))
            ActionChains(driver).move_to_element(loginForm).perform()
        except Exception as ex:
            testResult = False
            errText = ex
        finally:
            driver.close()
        self.assertTrue(testResult, str(errText))

if __name__ == '__main__':
    unittest.main()