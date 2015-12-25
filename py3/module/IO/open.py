#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

try:
    f = open('r.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('r.txt', 'r') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())


with open('t.jpg', 'rb') as f:
    print(f.read())


f = open('r.txt', 'w+')
f.write('python study')
f.close()