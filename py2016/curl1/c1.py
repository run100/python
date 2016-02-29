#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/16'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import re
import urllib2
import cookielib

from bs4 import BeautifulSoup

print("Hello world2016")

# request = urllib2.Request('http://baidu.com')
# request.add_header('user-agent', 'Mozilla/5.0')
# resp2 = urllib2.urlopen(request)
# print(resp2.getcode())
# print(resp2.read())

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
resp3 = urllib2.urlopen('http://a.ruansky.com')
# print(resp3.getcode())
# print(cj)
# print(resp3.read())

if resp3.getcode() == 200:
    content = resp3.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

    lis = soup.find_all('li')
    for li in lis:
        print(li)

#import urllib2
#resp = urllib2.urlopen('http://baidu.com')
#print(resp.getcode())
#print(resp.read())


# l = ['a', 'b', 'c', 'd']
# print(''.join(l))
# content = "%s%s%s%s" % tuple(l)
# print(type(content))

# s = 'ilovepython'
# s1 = s[0:2]
# print(s1)

s = 'hello persist'
# s1 = s.replace('persist', 'world')
sre = re.compile('persist')

#print(sre.sub('world', s))
#print(s.find('sfdsf'))



