#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-20 16:44:38
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-20 16:44:38
from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 10:
            print('Timing out after 10 seconds and returning')
            return
        time.sleep(0.5)
        try:
            if elem != driver.find_element_by_tag_name('html'):
                return
        except StaleElementReferenceException:
            return


driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
print(driver.page_source)
