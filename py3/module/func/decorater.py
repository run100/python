#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '装饰器'
__author__ = 'Administrator'
__mtime__ = '2015/12/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

# 定义装饰器函数
def log(func):
    def wrapper(*args, **kw):
        print("name is %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

# 定义使用装饰器类函数
@log
def now():
    print('hello %s' % 'world')


# 调用装饰器函数
now()