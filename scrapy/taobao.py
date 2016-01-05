#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/5'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib
import urllib2
import cookielib

url = 'https://mp.weixin.qq.com/cgi-bin/loginpage?t=wxm2-login&lang=zh_CN'
login_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Host': 'mp.weixin.qq.com',
    'Connection': 'Keep-Alive'
}
data = {
    'a': 1
}

#提交数据
post_data = urllib.urlencode(data)
request = urllib2.Request(url, post_data, login_header)

#代理服务器
proxyURL = '120.195.199.92:80'
proxy = urllib2.ProxyHandler({'http': proxyURL})

#cookie
cookie = cookielib.LWPCookieJar()
cookieHandler = urllib2.HTTPCookieProcessor(cookie)

#opener
opener = urllib2.build_opener(cookieHandler, proxy, urllib2.HTTPHandler)

respone = opener.open(request)

print(respone.read())


#urllib2.urlopen()
