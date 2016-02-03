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

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setName("new"+self.name)

    def run(self):
        print("I am %s" % self.name)

if __name__ == '__main__':
    for i in range(0, 5):
        t = MyThread()
        t.run()