#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""


def log(func):
    def wrapper(*args, **kw):
        print("call time is %s" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2016-01-01')


now()