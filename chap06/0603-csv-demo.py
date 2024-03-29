#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

csvFile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    # pass list/tuple into .writerow()
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i + 2, i * 2))
finally:
    csvFile.close()
