#!/usr/bin/env python
# -*- conding:utf-8 -*-

import string, urllib2
'''
response = urllib2.urlopen('http://www.baidu.com')
html = response.read()
print html
req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req)
print res.read()
'''

from urllib2 import Request,urlopen,URLError,HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)

print response.geturl()
print response.info()

