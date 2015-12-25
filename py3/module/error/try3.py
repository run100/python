#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10/n


def main():
    foo('0')


main()