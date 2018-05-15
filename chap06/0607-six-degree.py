#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from time import sleep
import random

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
    user='root', passwd='password', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute('use wikipedia')


def insertPageIfNotExists(url):
    cur.execute('select * from pages where url=%s', (url))
    if cur.rowcount == 0:
        cur.execute('insert into pages (url) values (%s)', (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]  # return the page id


def loadPages():
    cur.execute('select * from pages where visited=true')
    pages = [row[0] for row in cur.fetchall()]
    return pages


def insertLink(fromPageId, toPageId):
    cur.execute('select * from links where fromPageId=%s and toPageId=%s',
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('insert into links (fromPageId,toPageId) values (%s,%s)',
                    (int(fromPageId), int(toPageId)))
        conn.commit()


def visit(pageId):
    # use pageId since pageId is generated after an item being inserted into db
    cur.execute('update pages set visited=true where id=%s', (int(pageId)))
    conn.commit()


def getLinks(pageUrl, recursionLevel, pages):
    print(pageUrl)
    if len(pages) % 20 == 0:
        sleep(5)
        # sleep(random.randint(5,60))
    if recursionLevel > 4:  # 5, starts with 0
        return None
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl), timeout=20)
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]
    for link in links:
        insertLink(pageId, insertPageIfNotExists(link))
        if link not in pages:
            pages.append(link)
            getLinks(link, recursionLevel + 1, pages)
    visit(pageId)


try:
    getLinks('/wiki/Kevin_Bacon', 0, loadPages())
finally:
    cur.close()
    conn.close()
