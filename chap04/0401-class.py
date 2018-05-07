#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
crawl title,body from newyorktimes and brookings
'''
import requests
from bs4 import BeautifulSoup
import re


class Content(object):
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find_all('div', {'class': re.compile('StoryBodyCompanionColumn')})
    lines = [line.find_all('div', {'class': re.compile(
        'css-')}, recursive=False) for line in lines]
    lines = [line.find_all('p') for div in lines for line in div]
    lines = [line for y in lines for line in y]
    body = '\n'.join([line.text.strip() for line in lines])
    return Content(url, title, body)


def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'post-body'}).text
    return Content(url, title, body)


url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
content = scrapeNYTimes(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)
