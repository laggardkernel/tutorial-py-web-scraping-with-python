#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-05-31 22:36:45
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-05-31 22:44:50
import _thread
import time


def print_time(threadName, delay, iterations):
    start = int(time.time())
    for i in range(0, iterations):
        time.sleep(delay)
        seconds_elapsed = str(int(time.time()) - start)
        print('{} {}'.format(seconds_elapsed, threadName))


try:
    _thread.start_new_thread(print_time, ('Fizz', 3, 33))
    _thread.start_new_thread(print_time, ('Buzz', 5, 20))
    _thread.start_new_thread(print_time, ('Counter', 1, 100))
except Exception as e:
    print('Error: unable to start thread')

while 1:
    pass
