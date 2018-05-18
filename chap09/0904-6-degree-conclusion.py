#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql


def getUrl(pageId):
    cur.execute('select url from pages where id = %s', int(pageId))
    return cur.fetchone()[0]


def getId(url):
    cur.execute('select * from pages where url=%s', url)
    if cur.rowcount == 0:
        return None
    else:
        return cur.fetchone()[0]


def getLinks(fromPageId):
    cur.execute('select toPageId from links where fromPageId=%s', int(fromPageId))
    if cur.rowcount == 0:
        return []
    else:
        return [x[0] for x in cur.fetchall()]


def searchBreadth(targetPageId, paths=[[1]]):
    newPaths = []
    for path in paths:
        links = getLinks(path[-1])
        for link in links:
            print(path + [link])
            if link == targetPageId:
                return path + [link]
            else:
                newPaths.append(path + [link])
    return searchBreadth(targetPageId, newPaths)


conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
    user='root', passwd='password', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute('use wikipedia')

targetPage = '/wiki/Eric_Idle'

try:
    targetPageId = getId(targetPage)
    if targetPageId is None:
        print('%s is not found, more links need to be scrawled.' % targetPage)
    else:
        print('Searching route from /wiki/Kevin_Bacon, id=1 to '
            '/wiki/Eric_Idle, id=%s...' % targetPageId)
        pageIds = searchBreadth(targetPageId)
        print('\nGot route: %s' % pageIds)
        for pageId in pageIds:
            print(getUrl(pageId))
finally:
    cur.close()
    conn.close()

# [1, 109714, 111023, 111027]
