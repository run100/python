#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import thread
import time


def func():

    for i in range(5):
        print('func')
        time.sleep(1)

    thread.exit()

#thread.start_new_thread()
thread.start_new(func, ())

lock = thread.allocate()
print(lock.locked())
count = 0
if lock.acquire():
    count += 1
    lock.release()

time.sleep(6)
