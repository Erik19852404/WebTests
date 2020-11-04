import os
import time
import logging

import Global

def Test1():
    driver = Global.GetChromeDriver()
    driver.get("https://mail.ru")
    time.sleep(3)
    driver.close()
    logging.debug("Test 01 complete...")