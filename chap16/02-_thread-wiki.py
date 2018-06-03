#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-31 22:48:20
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-31 23:03:30
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import _thread
import time


def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    return bs.find('div', {'id': 'bodyContent'}).find_all('a',
        href=re.compile('^(/wiki/)((?!:).)*$'))


def scrape_article(thread_name, path):
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    time.sleep(3)
    bs = BeautifulSoup(html, 'lxml')
    title = bs.find('h1').get_text()
    print('Scraping {} in thread {}'.format(title, thread_name))
    links = get_links(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        scrape_article(thread_name, newArticle)


try:
    _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon'))
    _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python'))
except Exception as e:
    print('Error: unable to start threads')

while 1:
    pass
