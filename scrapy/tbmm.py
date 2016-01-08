#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib
import urllib2

url = 'http://blog.chromev.com'

login_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}

request = urllib2.Request(url, headers=login_header)

proxy_url = '121.34.195.34:9999'
proxy = urllib2.ProxyHandler({'http': proxy_url})

opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

resp = urllib2.urlopen(request)

print(resp.getcode())

