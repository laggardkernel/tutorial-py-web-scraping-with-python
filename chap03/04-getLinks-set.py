#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
crawl along article pages from home page of wikipedia
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
