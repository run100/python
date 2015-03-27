#!/usr/bin/env python
# -*- coding:utf-8 -*-


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

#写入日志
'''
file = os.path.abspath('.') + '/t.txt'
for i in range(1, 100):
    file_object = open(file, 'a+')
    file_object.write( 'assss\r\n' )
    file_object.close()
'''


# 连接数据库
dbconn = MySQLdb.connect(host="localhost", user="root", passwd="", db="scrapy",charset="utf8")
cursor = dbconn.cursor()

tags = []
tsql = "SELECT * FROM douban_tag WHERE id > 2 "
try:
    cursor.execute(tsql)
    data = cursor.fetchall()
    #print data
    for row in data:
        tags.append([row[1]])
except:
    print "Error: unable to fecth all data"

#print sys.argv[1]
def python_data(name, num):
    print name
    os.system( 'python '+ os.path.abspath('.') +'/douban_tag_list.py  '+ name )

try:
    for row in data:
        thread.start_new_thread(python_data, (row[1], 2) )
except:
    print "Error: unable to start thread"

cursor.close()
dbconn.close()