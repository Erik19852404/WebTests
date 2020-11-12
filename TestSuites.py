import os
import time
import unittest
import logging
from datetime import datetime

import Global
import TestCases


def TestSuiteKitchen():
    suite = unittest.TestSuite()
    suite.addTest(TestCases.TestCaseKitchenAuthorization('test_LoginFormOpen'))
    suite.addTest(TestCases.TestCaseKitchenAuthorization('test_OpenMainPage'))
    return suite

if __name__ == '__main__':#запуск тест-комплектов
    Global.InitDriver()
    runner = unittest.TextTestRunner()
    runner.run(TestSuiteKitchen())
    Global.CloseDriver()