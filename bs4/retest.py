#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


import re

str = 'one1two2three3four4'
p = re.compile(r'\d+')
print(p.split(str))
# p = re.compile(r'\w+')
# print(p.findall(str))

# ms = p.finditer(str)
# for m in ms:
#     print(m.group())

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'

print p.sub(r'\2 \1', s)