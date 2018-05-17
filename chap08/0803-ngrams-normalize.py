#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import re
import string


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or
                word.lower() == 'a' or word.lower == 'i']
    return sentence


def cleanInput(content):
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'utf-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    # return a list with depth 2
    return [cleanSentence(sentence) for sentence in sentences]


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i + n])
    return output


def getNgrams(content, n):
    content = cleanInput(content.lower())
    ngrams = Counter()
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentence(sentence, n)]
        ngrams.update(newNgrams)
    return ngrams


html = urlopen('https://en.wikipedia.org'
               '/wiki/Python_(programming_language)', timeout=10)
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count: ' + str(len(ngrams)))
