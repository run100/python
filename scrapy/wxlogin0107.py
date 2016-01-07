#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/7'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


import urllib
import urllib2
import cookielib

url = 'https://mp.weixin.qq.com/cgi-bin/login'

''' 构造Request对象 '''
data = {
    'username': 'chromev@qq.com',
    'pwd': '8dc2742b5b79797c17b3685dc7381c2a',
    'f': 'json'
}
post_data = urllib.urlencode(data)

login_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Host': 'mp.weixin.qq.com',
    'Referer': 'https://mp.weixin.qq.com/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

request = urllib2.Request(url, post_data, login_header)

''' 构造openr '''
filename = 'wxcookie0107.txt'
cookie = cookielib.MozillaCookieJar(filename)

cookiehandler = urllib2.HTTPCookieProcessor(cookie)

proxy_url = '120.195.199.92:80'
proxy = urllib2.ProxyHandler({'http': proxy_url})

opener = urllib2.build_opener(cookiehandler, proxy, urllib2.HTTPHandler)

rs = opener.open(request)

print(rs.read())

cookie.save(ignore_discard=True, ignore_expires=True)
