#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


print(Student)

bart = Student('zhangzw', 100)
bart.__name = 'persist'
bart.print_score()