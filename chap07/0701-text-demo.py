#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
print('Reading chapter1.txt...')
textPage = urlopen('http://www.pythonscraping.com/'
    'pages/warandpeace/chapter1.txt', timeout=10)
print(textPage.read())

print('\nReading chapter1-ru.txt...')
textPage = urlopen('http://www.pythonscraping.com/'
    'pages/warandpeace/chapter1-ru.txt', timeout=10)
print(textPage.read())
