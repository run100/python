#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""


import hashlib

md5 = hashlib.md5()

md5.update('how to use md5 in python hashlib?')
print(md5.hexdigest())


sha1 = hashlib.sha1()
sha1.update('run')
sha1.update('com')
print(sha1.hexdigest())