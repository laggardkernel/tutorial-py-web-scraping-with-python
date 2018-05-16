#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import chardet

print('Reading chapter1-ru.txt with chardet...')
textPage = urlopen('http://www.pythonscraping.com'
    '/pages/warandpeace/chapter1-ru.txt', timeout=10)
content = textPage.read()
encoding = chardet.detect(content)
print(encoding)
encoding=encoding['encoding']
print(str(content, encoding))
