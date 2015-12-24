#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


import sys;

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s' % args[1])
    else:
        print('too many args')

if __name__ == '__main__':
    test()