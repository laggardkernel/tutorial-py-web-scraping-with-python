#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
retrieve src file from http://www.pythonscraping.com,
keep the relative structure within local download dir
'''

import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

downloadDirectory = os.path.dirname(os.path.abspath(__file__)) + '/download'
baseUrl = 'http://pythonscraping.com'


def getAbsoluteURL(baseUrl, source):
    '''Regulate input source URL, return the absolute URL'''
    if source.startswith('http://www.'):  # omit www.
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    else:  # relative path
        url = '{}/{}'.format(baseUrl, source)
    if baseUrl not in url:
        return None
    return url


def getDownalodPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.find_all(src=True)  # select link source with lambda func

for item in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, item['src'])
    if fileUrl:
        print(fileUrl)
        # print(getDownalodPath(baseUrl, fileUrl, downloadDirectory))
        urlretrieve(fileUrl, getDownalodPath(baseUrl, fileUrl, downloadDirectory))
