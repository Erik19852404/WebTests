import os
import time
import unittest
import logging
from datetime import datetime

import Global
import TestCases


def TestSuite1():
    suite = unittest.TestSuite()
    suite.addTest(TestCases.TestCaseKitchenAuthorization('test_LoginFormOpen'))
    suite.addTest(TestCases.TestCaseKitchenAuthorization('test_OpenMainPage'))
    return suite

def TestSuite2():
    suite = unittest.TestSuite()
    suite.addTest(TestCases.TestCaseKitchenAuthorization('test_LoginFormOpen'))
    suite.addTest(TestCases.TestCaseKitchenAuthorization('test_OpenMainPage'))
    return suite

if __name__ == '__main__':
    # простой способ запустить тесты без группировки в комплекты
    #unittest.main()
    #запуск тест-комплектов
    runner = unittest.TextTestRunner()
    runner.run(TestSuite1())
    runner.run(TestSuite2())

