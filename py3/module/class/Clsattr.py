#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/24'
"""

class Student(object):

    @property
    def get_score(self):
        return self._score

    @score.setter
    def set_score(self, value):

        if not isinstance(value, int):
            raise ValueError('score must be an integer')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')

        self._score = value


s = Student()
'''
s.set_score()
l = s.get_score()
print(l)
'''

s.score = 60
print(s.score)



