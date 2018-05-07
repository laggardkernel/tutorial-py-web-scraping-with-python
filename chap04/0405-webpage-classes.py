#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Define different classes representing different types of page
'''


class Website(object):
    '''Common base class for all articles/pages'''

    def __init__(self, name, url, titleTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag


class Product(Website):
    '''Contains info for scraping a product page'''

    def __init__(self, name, url, titleTag, productNumber, priceTag):
        super(Product, self).__init__(name, url, titleTag)
        self.productNumber = productNumber
        self.price = priceTag


class Article(Website):
    '''Contains info for scraping a article page'''

    def __init__(self, name, url, titleTag, bodyTag, dateTag):
        super(Article, self).__init__(name, url, titleTag)
        self.bodyTag = bodyTag
        self.dateTag = dateTag
