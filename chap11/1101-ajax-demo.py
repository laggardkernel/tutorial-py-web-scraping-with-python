#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wyh
# @Date:   2018-05-20 16:33:09
# @Last Modified by:   wyh
# @Last Modified time: 2018-05-20 16:33:09
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
