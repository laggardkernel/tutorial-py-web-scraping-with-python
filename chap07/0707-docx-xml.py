#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

wordFile = urlopen('http://pythonscraping.com'
                   '/pages/AWordDocument.docx', timeout=10).read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))
