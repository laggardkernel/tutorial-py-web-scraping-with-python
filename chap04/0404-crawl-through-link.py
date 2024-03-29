#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
crawl title,body through inner links
'''
import requests
from bs4 import BeautifulSoup
import re


class Content(object):
    '''Common base class for all articles/pages'''

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        '''
        Flexible printing function controls output
        '''
        print('URL: {}'.format(self.url))
        print('Title: {}'.format(self.title))
        print('Body:\n{}\n'.format(self.body))


class Website(object):
    '''Contains info about website structure'''

    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler(object):
    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url, timeout=10)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
        if title != '' and body != '':
            content = Content(url, title, body)
            content.print()

    def crawl(self):
        '''
        Get pages from website home page
        '''
        bs = self.getPage(self.site.url)
        targetPages = bs.find_all('a', href=re.compile(self.site.targetPattern))
        print('Length of articles: %d' % len(targetPages))
        i = 1
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                print('No.%d' % i)
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = '{}{}'.format(self.site.url, targetPage)
                self.parse(targetPage)
                i = i + 1


reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)', False,
    'h1', 'div.body_1gnLA')
crawler = Crawler(reuters)
crawler.crawl()
