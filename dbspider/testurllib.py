#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '16/1/16'
"""

import urllib
import urllib2

url = 'http://movie.douban.com/subject/11510501/?from=subject-page'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}
request = urllib2.Request(url, headers=headers)

proxy_url = '61.162.184.7:8088'
proxy = urllib2.ProxyHandler({'http': proxy_url})

opener = urllib2.build_opener(proxy)

resp = opener.open(request)

print(resp.getcode())
print(resp.read())