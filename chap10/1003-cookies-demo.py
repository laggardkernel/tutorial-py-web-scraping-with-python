# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-18 16:06:32
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-18 16:18:10
import requests
params = {'username': 'Requests', 'password': 'password'}
# this post request fails cause the page is removed
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php',
                  timeout=10, data=params)
print(r.text)
print('Cookie is set to:\n%r' % r.cookies.get_dict())
print('Going to profile page...')
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',
                 timeout=10, cookies=r.cookies)
print(r.text)
