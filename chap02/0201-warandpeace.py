#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')
nameList = bs.find_all('span', {'class': 'green'})
# nameList=bs.find_all(text='the prince') # 返回结果只为文本，无标签
for name in nameList:
    print(name.get_text())
