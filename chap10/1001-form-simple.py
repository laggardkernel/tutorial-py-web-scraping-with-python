#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

params = {'firstname': 'Requests', 'lastname': 'Module'}
r = requests.post('http://pythonscraping.com/pages/processing.php',
    timeout=10, data=params)
print(r.text)
