#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wyh
# @Date:   2018-05-21 21:38:33
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-21 21:44:08
import json
from urllib.request import urlopen


def getCountry(ipAddress):
    # freegeoip.net will be deprecated and access key is needed later
    response = urlopen('http://freegeoip.net/json/' +
        ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')


print(getCountry('50.78.253.58'))
