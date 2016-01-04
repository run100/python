#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '16/1/3'
"""

from bs4 import BeautifulSoup
import urllib2

url = 'http://chuansong.me/select'

rs = urllib2.urlopen(url)

htmlcontent = rs.read()
print(htmlcontent)
soup = BeautifulSoup(htmlcontent, 'html.parser', from_encoding='utf-8')

links = soup.find_all('a')
for link in links:
    print(link.name, link['href'],  link.get_text())