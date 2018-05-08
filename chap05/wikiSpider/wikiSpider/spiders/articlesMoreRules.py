#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
    name = 'artitlesRules'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items',
    follow=True, cb_kwargs={'is_aritcle': True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items',
             cb_kwargs={'is_aritcle': False})
    ]

    def parse_items(self, response, is_aritcle):
        print('URL is: {}'.format(response.url))
        title = response.css('h1::text').extract_first()
        if is_aritcle:
            title = response.css('h1::text').extract_first()
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css(
                'li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace('This page was last edited on ', '')
            print('Title is: {}'.format(title))
            print('Text is: {}'.format(text))
            print('Last updated: {}\n'.format(lastUpdated))
        else:
            print('This is not an article: {}'.format(title))
