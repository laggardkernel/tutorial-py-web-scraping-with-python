#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.request import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())


def getInternalLinks(bs, includeUrl):
    '''retrieve a list of all internal links'''
    # clean the url, strip queries
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
        urlparse(includeUrl).netloc)
    internalLinks = []
    # finds all links begining with '/', or inclue current location
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startwith('/'):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    for link in bs.find_all('a',
            href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


allExtLinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
        urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html)
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, urlparse(domain).netloc)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print(link)
            getAllExternalLinks(link)


allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')
