#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-06-03 18:06:50
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-06-03 18:36:45

'''
Communicating info between processes using Queue,
multi-process handle tasks from the same Queue
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
from multiprocessing import Process, Queue
import os
import time


def task_delegator(taskQueue, urlsQueue):
    '''
    transmit task from urlsQueue -> taskQueue,
    filter duplicate task during the procedure
    '''
    # Initialize with a task for each process
    visited = ['/wiki/Kevin_Bacon', '/wiki/Monty_Python']
    taskQueue.put('/wiki/Kevin_Bacon')
    taskQueue.put('/wiki/Monty_Python')

    while 1:
        # Check to see if there're new links in the urlsQueue for processing
        if not urlsQueue.empty():
            links = [link for link in urlsQueue.get() if link not in visited]
            for link in links:
                taskQueue.put(link)
                visited.append(link)


def get_links(bs):
    links = bs.find('div', {'id': 'bodyContent'}).find_all('a',
        href=re.compile('^/wiki/((?!:).)*$'))
    return [link.attrs['href'] for link in links]


def scrape_article(taskQueue, urlsQueue):
    while 1:
        while taskQueue.empty():
            time.sleep(0.1)
        path = taskQueue.get()
        html = urlopen('https://en.wikipedia.org{}'.format(path))
        time.sleep(3)
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.find('h1').get_text()
        print('Scraping {} in process {}'.format(title, os.getpid()))
        links = get_links(bs)
        urlsQueue.put(links)


processes = []
taskQueue = Queue()
urlsQueue = Queue()
processes.append(Process(target=task_delegator, args=(taskQueue, urlsQueue)))
processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue)))
processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue)))

for p in processes:
    p.start()
