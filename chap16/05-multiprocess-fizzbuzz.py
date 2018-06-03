#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-06-03 17:52:42
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-06-03 17:57:23
from multiprocessing import Process
import time
import os


def print_time(threadName, delay, iterations):
    start = int(time.time())
    for i in range(0, iterations):
        time.sleep(delay)
        seconds_elapsed = int(time.time()) - start
        print('{} {} {}'.format(seconds_elapsed, threadName, os.getpid()))


processes = []
processes.append(Process(target=print_time, args=('Fizz', 3, 33)))
processes.append(Process(target=print_time, args=('Buzz', 5, 20)))
processes.append(Process(target=print_time, args=('Counter', 1, 100)))

for p in processes:
    p.start()
for p in processes:
    p.join
