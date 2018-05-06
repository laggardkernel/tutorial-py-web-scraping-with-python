#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Crawl along the external page only
'''
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
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


def getRandomExternalLink(startingPage):
    print('    urlopen(%s)' % startingPage)
    html = urlopen(startingPage, timeout=10)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme,
                                  urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        if len(internalLinks) == 0:
            print('Crawling dead with no links found at all.')
        return getRandomExternalLink(internalLinks[random.randint(0,
            len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)


if __name__ == '__main__':
    followExternalOnly('https://oreilly.com/')
    # followExternalOnly('https://wikipedia.org/')
