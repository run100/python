#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'

import urllib
import urllib2
import re
import thread
import time
import MySQLdb
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 连接数据库
dbconn = MySQLdb.connect(host="localhost", user="root", passwd="", db="test",charset="utf8")
cursor = dbconn.cursor()

url = 'http://www.51cto.com/recommnews/list1.htm';


def get_html(url):
    headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2327.5 Safari/537.36",
       "Connection":'keep-alive',
       "Cache-Control":"max-age=0",
    }

    request = urllib2.Request(
        url = url,
        headers = headers
    )

    response = urllib2.urlopen(request)
    html = response.read()

    return  html


tmphtml = get_html(url);
print tmphtml;

