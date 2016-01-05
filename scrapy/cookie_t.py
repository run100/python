#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/5'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
import cookielib

#声明一个cookieJar对象保存cookie
cookie = cookielib.CookieJar()

#利用urllib2库的HTTPCookieProcessor对象来处理cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
##此处的open方法同urllib2的urlopen方法，也可以传入request
respone = opener.open('http://www.baidu.com')

for item in cookie:
    print("name: %s, value: %s" % (item.name, item.value) )

