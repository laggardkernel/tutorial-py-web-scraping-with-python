#!/usr/bin/env pythpn3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-06-03 17:42:20
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-06-03 17:45:17
import threading
import time


def print_time(threadName, delay, iterations):
    start = int(time.time())
    for i in range(0, iterations):
        time.sleep(delay)
        seconds_elapsed = str(int(time.time()) - start)
        print('{} {}'.format(seconds_elapsed, threadName))


threading.Thread(target=print_time, args=('Fizz', 3, 33)).start()
threading.Thread(target=print_time, args=('Buzz', 5, 20)).start()
threading.Thread(target=print_time, args=('Counter', 1, 100)).start()
