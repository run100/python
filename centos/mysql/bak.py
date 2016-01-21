#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'mysql bak file'
__author__ = 'Administrator'
__mtime__ = '2016/1/21'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import time
import sys
import os
import string

def is_path(pstr):
    if not os.path.exists(pstr):
        os.mkdir(pstr)

def run(cmd):
    p = os.popen(cmd)
    text = p.read()
    p.close()
    print(text)
    return text


IS_PLAYER = 0

if IS_PLAYER:
    databases = ['playerhot', 'themes']
    sql_user = 'root'
    sql_passwd = ''

    # 远程服务器
    scp_ip = '47.88.1.166'
    scp_user = 'shelton'
    scp_passwd = '6f^tlVq&7mqMf8We'
    scp_port = 65522
    scp_dir = '/home/shelton/mysql/'

else:
    databases = ['douban', 'solr']
    sql_user = 'run'
    sql_passwd = '123456'

#print(databases)

bakpath = '/home/mysqlbak'

''' 处理路径 '''
# 判断路径是否存在
is_path(bakpath)

# 当前时间
datestr = '%s%s' % ('bak', time.strftime('%Y%m%d'))
bakpathstr = '%s%s%s' % (bakpath, '/', datestr)
is_path(bakpathstr)

#run('ls -al /home | grep mysql')

''' 备份到本地目录 '''
os.chdir(bakpathstr)
for db in databases:
    #文件名
    flist = [bakpathstr, '/', db, time.strftime('%H%M%S'), '.sql']
    fname = ''.join(flist)

    #备份
    binstr = '/usr/local/webserver/mysql/bin/mysqldump'
    sql_cmd = "%s -u%s -p'%s' %s > %s " % (binstr, sql_user, sql_passwd, db, fname)
    if os.system(sql_cmd) == 0:
        print( '%s, %s' % (db, ' local is backup successfully!') )
    else:
        print( '%s, %s' % (db, ' local is backup Failed!!') )

    if IS_PLAYER:
        scp_cmd = "scp -P%s %s %s@%s:%s" % (scp_port, fname, scp_user, scp_ip, scp_dir)
        if os.system(sql_cmd) == 0:
            print( '%s, %s' % (db, ' remote is backup successfully!') )
            #删除本地
            os.remove(fname)
        else:
            print( '%s, %s' % (db, ' remote is backup Failed!!') )





time.sleep(3)


