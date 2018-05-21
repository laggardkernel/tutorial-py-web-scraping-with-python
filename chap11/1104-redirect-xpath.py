#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-20 16:59:11
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-20 17:05:07
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
try:
    bodyElement = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH,
        '//body[contains(text(),"This is the page you are looking for!")]')))
    print(bodyElement.text)
except TimeoutException:
    print('Did not find the element')
