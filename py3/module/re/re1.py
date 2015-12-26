#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""

import re

r = re.match('^(\d{3})\-(\d{3,8})', '010-12345')
print(r.group())
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.groups())
('010', '12345')

s = 'a b   c,d;e'
# print(s.split(r'\s+'))

# r = re.split(r'\s+', s)
# print(r)

r = re.split(r'[\s\,]+', 'a,b, c, d')
print(r)

r = re.split(r'[\s\,\;]+', s)
print(r)