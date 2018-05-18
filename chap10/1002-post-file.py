#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import requests
files = {'uploadFile': open('./python-logo.png', 'rb')}
r = requests.post('http://pythonscraping.com/pages/processing2.php',
    timeout=10, files=files)
print('%r' % r)
print(r.text)
