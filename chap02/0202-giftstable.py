#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

print('----------children----------')
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)  # outpur <tr> blocks

print('----------next siblings----------')
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)  # jump the <th>

print('----------parents----------')
print(bs.find('img', {'src': '../img/gifts/img1.jpg'})
    .parent  # td
    .previous_sibling.get_text())  # text in previous td

print('----------images----------')
images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])

print('----------tags whose length is 2----------')
for item in bs.find_all(lambda tag: len(tag.attrs) == 2):
    print(item)
