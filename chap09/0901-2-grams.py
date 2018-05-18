#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import re
import string
from collections import Counter
import chardet


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace)
        for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or
        word.lower() == 'a' or word.lower() == 'i']
    return sentence


def cleanInput(content):
    content = content.lower()
    content = re.sub('\n', ' ', content)
    content = bytes(content, 'utf-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    # return a two-dimension list
    return [cleanSentence(sentence) for sentence in sentences]


def isCommon(ngram):
    # https://www.wordfrequency.info/sample.asp#simple
    # https://www.wordfrequency.info/files/entriesWithoutCollocates.txt
    commonWords = ['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it', 'i',
        'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this', 'they',
        'is', 'an', 'at', 'but', 'we', 'his', 'from', 'that', 'not', 'by',
        'she', 'or', 'as', 'what', 'go', 'their', 'can', 'who', 'get', 'if',
        'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will', 'as',
        'up', 'one', 'time', 'has', 'been', 'there', 'year', 'so', 'think',
        'when', 'which', 'them', 'some', 'me', 'people', 'take', 'out', 'into',
        'just', 'see', 'him', 'your', 'come', 'could', 'now', 'than', 'like',
        'other', 'how', 'then', 'its', 'our', 'two', 'more', 'these', 'want',
        'way', 'look', 'first', 'also', 'new', 'because', 'day', 'more', 'use',
        'no', 'man', 'find', 'here', 'thing', 'give', 'many', 'well']
    for word in ngram:
        if word in commonWords:
            return True
    return False


def getNgramsFromSentence(sentence, n):
    output = []
    for i in range(len(sentence) - n + 1):
        output.append(sentence[i:i + n])
    return output


def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in
            getNgramsFromSentence(sentence, n) if not isCommon(ngram)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return ngrams


content = urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt',
    timeout=10).read()
encoding = chardet.detect(content)['encoding']
content = str(content, encoding)
ngrams = getNgrams(content, 2)
print(ngrams)
