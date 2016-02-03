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

def func():
    print 'func() passed to thread'

t = threading.Thread(target=func)
t.start()


# 方法2: 从Thread继承, 并重写run

class MyThread(threading.Thread):
    def run(self):
        print("MyThread extended from Thread")

t = MyThread()
t.start()