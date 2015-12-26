#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""


import re

#编译
tel = re.compile(r'^(\d{3})-(\d{3,8})$')

#使用
rs = tel.match('010-12345').groups()
print(type(rs))
print(rs)