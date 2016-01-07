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
import sys




page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)
login_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
request = urllib2.Request(url, headers=login_header)
try:

    content = urllib2.urlopen(request).decode('utf-8')
    # print(response1.getcode())
    # print(len(response1.read()))
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

