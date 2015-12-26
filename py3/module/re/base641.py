#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""


import base64

a = base64.b64encode('binary\x00string')
print(a)
b = base64.b64decode('YmluYXJ5AHN0cmluZw==')
print(b)


c = base64.b64encode('i\xb7\x1d\xfb\xef\xff')

print(c)

d = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print(d)

e = base64.urlsafe_b64decode('abcd--__')
print(e)