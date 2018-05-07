#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
simple demo to get all links from wiki page Kevin_Bacon
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
