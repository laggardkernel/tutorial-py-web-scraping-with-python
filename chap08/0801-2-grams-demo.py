#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getNgrams(content, n):
    content = content.split(' ')
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i + n])
    return output


html = urlopen('https://en.wikipedia.org'
               '/wiki/Python_(programming_language)', timeout=10)
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count: ' + str(len(ngrams)))
