#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/5'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import cookielib
import urllib2


#保留cookie
filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)

#处理cookie
handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

#response = opener.open("http://www.baidu.com")
response = opener.open("https://mp.weixin.qq.com")

cookie.save(ignore_discard=True, ignore_expires=True)
