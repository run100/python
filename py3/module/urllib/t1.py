#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '16/1/3'
"""
import cookielib

import urllib2

url = 'http://chuansong.me/select'

rs = urllib2.urlopen(url)
print(rs.getcode())
print(len(rs.read()))

request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
rs = urllib2.urlopen(request)
print(rs.getcode())
print(len(rs.read()))

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
rs = urllib2.urlopen(url)
print(rs.getcode())
print(cj)
#print(rs.read())