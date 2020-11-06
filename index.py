import os
import sys
import time
import logging
import unittest

import TestSuiteKitchen
import Global

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCaseKitchen(unittest.TestCase):
    def setUp(self):#some actions before start
        pass
    def tearDown(self):#some actions after run
        pass
    def test_OpenMainPage(self):
        self.assertTrue(TestSuiteKitchen.TestOpenStartPage(), "Can't open main page...")

if __name__ == '__main__':
    unittest.main()