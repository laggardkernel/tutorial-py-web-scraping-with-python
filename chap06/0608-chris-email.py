#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'christmas_alerts@pythonscraping.com'
    msg['To'] = 'ryan@pythonscraping.com'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


bs = BeautifulSoup(urlopen('https://isitchristmas.com/', timeout=10),
                   'html.parser')
while bs.find('a', {'id': 'answer'}).attrs['title'] == 'NO':
    print('It is not Christmas yet.')
    time.sleep(3600)
    bs = BeautifulSoup(urlopen('https://isitchristmas.com/', timeout=10),
                       'html.parser')

sendMail('It\'s Christmas!',
         'According to https://itischristmas.com, it is Christmas!')
