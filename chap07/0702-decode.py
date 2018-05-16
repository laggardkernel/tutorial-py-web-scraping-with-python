#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

print('Reading chapter1-ru.txt...')
textPage = urlopen('http://www.pythonscraping.com'
    '/pages/warandpeace/chapter1-ru.txt', timeout=10)
print(str(textPage.read(), 'utf-8'))

print('\nReading Python_(programming_language) with bs...')
html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)',
    timeout=10)
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id': 'mw-content-text'}).get_text()
content = bytes(content, 'UTF-8')
content = content.decode('utf-8')
print(content)
