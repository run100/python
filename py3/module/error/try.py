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
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('finally')
print('END')

