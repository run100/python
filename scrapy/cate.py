#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import string
import MySQLdb

import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

url = 'http://movie.douban.com/tag/'
#request = urllib2.Request(url)
request = urllib2.Request(
    url = url,
    headers = headers
)

response = urllib2.urlopen(request)
html = response.read()
unicodehtml = html.decode("utf-8")
#print unicodehtml

# 写入文件


#matchs = re.findall('<td><a href="./美国">(.*?)</a><b>(14329915)</b></td>', unicodehtml, re.S)
#print matchs

#matchs = re.findall('<td><a href=".*?">(.*?)</a><b>\((\d*)\)</b></td>', unicodehtml, re.S)
#print matchs
#for m in matchs:
#    print m[0].replace("\n",''), m[1].replace("\n",'')



