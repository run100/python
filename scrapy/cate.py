#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import string
import MySQLdb
import os

import re1
'''
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
'''

#f=open('cate.txt', 'r')

file = os.path.abspath('.') + '/cate.txt'
with open(file, 'r') as f:
    unicodehtml = f.read()

unicodehtml = unicodehtml.decode("utf-8")
#print unicodehtml

p = re1.compile(u'<td><a\s+href="\.\/[\u4e00-\u9fa5]+">(.*?)<\/a><b>\((\d*)\)<\/b></td>', re1.S)
matchs = p.findall(unicodehtml)

# 连接数据库
dbconn = MySQLdb.connect(host="localhost", user="root", passwd="", db="scrapy",charset="utf8")
cursor = dbconn.cursor()

tags = []
for m in matchs:
    #tags.append([m[0], m[1]])
    #print m[0], m[1]
    sql = "INSERT INTO douban_tag(tag_name, tag_num) VALUES ('%s', '%s')" % (m[0], m[1])
    try:
        cursor.execute(sql)
        dbconn.commit()
    except Exception, e:
        dbconn.rollback()
        print "MySQL Error %s: %s" % (e.args[0], e.args[1])

print tags





'''
matchs = re.findall('<td><a href=".*?">(.*?)</a><b>\((\d*)\)</b></td>', unicodehtml, re.S)
print matchs
for m in matchs:
print m[0].replace("\n",''), m[1].replace("\n",'')
p = re.compile(r'<td><a\s+href=".*?">(.*)<b>')
print p.findall(unicodehtml)
'''


