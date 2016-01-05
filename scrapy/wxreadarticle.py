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

url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list_card&lang=zh_CN&token=971281399'

login_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Host': 'mp.weixin.qq.com',
    'Referer': 'https://mp.weixin.qq.com/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

request = urllib2.Request(url, '', login_header)

cookie = cookielib.MozillaCookieJar()
cookie.load('wxcookie.txt', ignore_discard=True, ignore_expires=True)


opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)

print(response)

