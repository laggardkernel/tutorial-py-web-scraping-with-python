#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-31 23:16:29
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-06-03 17:39:22
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import _thread
from queue import Queue
import time
import pymysql


def storage(queue):
    conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
        user='root', passwd='password', db='mysql', charset='utf8mb4')
    cur = conn.cursor()
    try:
        cur.execute('CREATE database if not exists wiki_threads')
        cur.execute('USE wiki_threads')

        col1 = '''create table if not exists `wiki_threads`.`pages` (
  `id` int not null auto_increment,
  `title` varchar(50) not null,
  `path` varchar(255) not null,
  `created` timestamp not null default current_timestamp,
  primary key (`id`)
) engine=InnoDB;'''
        cur.execute(col1)

        while 1:
            if not queue.empty():
                article = queue.get()
                cur.execute('select * from pages where path=%s', (article['path']))
                if cur.rowcount == 0:
                    print('Storing article {}'.format(article['title']))
                    cur.execute('insert into pages(title,path) values(%s,%s)',
                                (article['title'], article['path']))
                    conn.commit()
                else:
                    print('Article already exists: {}'.format(article['title']))
    finally:
        cur.close()
        conn.close()


visited = []


def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    links = bs.find('div', {'id': 'bodyContent'}).find_all('a',
        href=re.compile('^(/wiki/)((?!:).)*$'))
    return [link for link in links if link not in visited]


def scrape_article(thread_name, path, queue):
    visited.append(path)
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    time.sleep(5)
    bs = BeautifulSoup(html, 'lxml')
    title = bs.find('h1').get_text()
    print('Added {} for storage in thread {}'.format(title, thread_name))
    queue.put({"title": title, "path": path})
    links = get_links(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        scrape_article(thread_name, newArticle, queue)


queue = Queue()
try:
    _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon', queue))
    _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python', queue))
    _thread.start_new_thread(storage, (queue,))
except Exception as e:
    print('Error: unable to start threads')

while 1:
    pass
