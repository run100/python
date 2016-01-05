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
import urllib
import urllib2

url = 'https://mp.weixin.qq.com/cgi-bin/login'
data = {
    'username': 'chromev@qq.com',
    'pwd': '8dc2742b5b79797c17b3685dc7381c2a',
    'f': 'json'
}
login_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Host': 'mp.weixin.qq.com',
    'Referer': 'https://mp.weixin.qq.com/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

post_data = urllib.urlencode(data)

request = urllib2.Request(url, post_data, login_header)


proxy_url = '120.195.199.92:80'
proxy = urllib2.ProxyHandler({'http': proxy_url})

#cookie处理
filename = 'wxcookie.txt'
cookie = cookielib.MozillaCookieJar(filename)

cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler, proxy, urllib2.HTTPHandler)

respone = opener.open(request)

print(respone.read())

cookie.save(ignore_discard=True, ignore_expires=True)

url_list = 'https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list_card&lang=zh_CN&token=971281399'

result = opener.open(url_list)
print(result.read())
