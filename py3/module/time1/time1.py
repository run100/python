#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


import time

ticks = time.time()

print "Number of ticks since 12:00am, January 1, 1970:", ticks

#获取当前时间
localtime = time.localtime(time.time())
print(localtime)

#获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print(localtime)