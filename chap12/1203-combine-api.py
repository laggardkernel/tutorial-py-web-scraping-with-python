#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-21 21:52:28
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-21 22:05:28
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re
from urllib.error import HTTPError

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org{}'.format(articleUrl), timeout=5)
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
        href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'https://en.wikipedia.org/w/index.php?title='\
        '{}&action=history'.format(pageUrl)
    print('history url is: {}'.format(historyUrl))
    html = urlopen(historyUrl, timeout=5)
    bs = BeautifulSoup(html, 'html.parser')
    ipAddresses = bs.find_all('a', {'class': 'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    try:
        response = urlopen('http://freegeoip.net/json/{}'.format(ipAddress)).\
            read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')


links = getLinks('/wiki/Python_(programming_language)')
while len(links) > 0:
    for link in links:
        print('-' * 20)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print('{} is from {}'.format(historyIP, country))
    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)
