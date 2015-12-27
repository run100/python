#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/28'
"""
import cookielib

import urllib2

url = "http://baidu.com"

rs1 = urllib2.urlopen(url)
print(rs1.getcode())
print(len(rs1.read()))

request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
rs1 = urllib2.urlopen(url)

print(rs1.getcode())
print(len(rs1.read()))



cj = cookielib.CookieJar()
opener = urllib2.build_opener( urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

rs1 = urllib2.urlopen(url)
print(rs1.getcode())
print(cj)
print(len(rs1.read()))