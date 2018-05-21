#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-21 21:44:42
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-21 21:51:31
import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],'\
    '"arrayOfFruits": [{"fruit": "apple"}, {"fruit": "banana"}, {"fruit": "pear"}]}'
jsonObj = json.loads(jsonString)
print(jsonObj.get('arrayOfNums'))
print(jsonObj.get('arrayOfNums')[1])
print(jsonObj.get('arrayOfNums')[1].get('number')+
    jsonObj.get('arrayOfNums')[2].get('number'))
print(jsonObj.get('arrayOfFruits')[2].get('fruit'))
