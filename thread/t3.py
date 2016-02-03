#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import threading
import time

data = 0
lock = threading.Lock()

def func():
    global data

    print("%s acquire lock ... " % threading.currentThread().getName())

    if lock.acquire():
        print("%s get the lock " % threading.currentThread().getName())
        data += 1
        print("%s data is %s " %(threading.currentThread().getName(), data) )
        time.sleep(1)
        print("%s release lock " % threading.currentThread().getName())
        lock.release()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)

t1.start()
t2.start()
t3.start()