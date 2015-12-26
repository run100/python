#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import logging_test

def foo(s):
    return 10/int(s)


def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging_test.exception(e)




main()

print('END')