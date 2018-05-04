#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    html = urlopen('https://pythonscrappingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be reached!')
else:
    print('It Worked!')
