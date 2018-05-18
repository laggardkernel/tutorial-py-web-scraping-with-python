# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-18 16:23:00
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-18 16:23:00
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('Requests', 'password')
r = requests.post(url='http://pythonscraping.com/pages/auth/login.php',
    timeout=10, auth=auth)
print(r.text)
