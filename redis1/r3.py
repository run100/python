#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/2'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
from bs4 import BeautifulSoup


url = 'http://news.cnblogs.com/'
resp = urllib2.urlopen(url)

print(resp.getcode())



