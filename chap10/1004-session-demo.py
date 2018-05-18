# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-18 16:18:41
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-18 16:18:41
import requests
session = requests.Session()
params = {'username': 'username', 'password': 'password'}
# this post request fails cause the page is removed
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php',
                 timeout=10, data=params)
print('Cookie is set to:\n%r' % s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php',
                timeout=10)
print(s.text)
