#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from io import StringIO
import csv
import chardet

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv',
               timeout=10).read()
encoding = chardet.detect(data)
print(encoding)
encoding = encoding['encoding']
data = data.decode(encoding, 'ignore')

try:
    dataFile = StringIO(data)
    csvReader = csv.reader(dataFile)
    for row in csvReader:
        print(row)
finally:
    dataFile.close()
