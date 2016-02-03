#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '使用Lock互斥锁'
__author__ = 'Administrator'
__mtime__ = '2016/2/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import threading
import time

counter = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter, mutex
        time.sleep(1)
        if mutex.acquire():
            counter += 1
            print("I am %s, set counter:%s" % (self.name, counter))
            mutex.release()

if __name__ == '__main__':
    for i in range(1, 20):
        t = MyThread()
        t.start()