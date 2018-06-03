#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-06-03 17:57:56
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-06-03 18:06:04
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
from multiprocessing import Process
import os
import time

visited = []


def get_links(bs):
    print('Getting links in process {}'.format(os.getpid()))
    links = bs.find('div', {'id': 'bodyContent'}).find_all('a',
        href=re.compile('^/wiki/((?!:).)*$'))
    return [link for link in links if link not in visited]


def scrape_article(path):
    visited.append(path)
    html = urlopen('https://en.wikipedia.org{}'.format(path))
    time.sleep(5)
    bs = BeautifulSoup(html, 'lxml')
    title = bs.find('h1').get_text()
    print('Scraping {} in process {}'.format(title, os.getpid()))
    links = get_links(bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        scrape_article(newArticle)


processes = []
processes.append(Process(target=scrape_article, args=('/wiki/Kevin_Bacon',)))
processes.append(Process(target=scrape_article, args=('/wiki/Monty_Python',)))

for p in processes:
    p.start()
