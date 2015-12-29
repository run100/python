#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import sys
import time

import global1
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

conn = MySQLdb.connect(host=global1.MYSQL_HOST
                       , user=global1.MYSQL_USER
                       , passwd=global1.MYSQL_PASSWD
                       , db=global1.MYSQL_DB
                       , charset=global1.MYSQL_CHARSET)
cursor = conn.cursor()



class MysqlUrls:

    # def __init__(self):
    #     self.new_urls = cache.smembers(NEW_URLS_KEY)
    #     self.old_urls = cache.smembers(OLD_URLS_KEY)

    def get_urls_cnt(self, **kw):
        crawls = dict({'new': 0, 'old': 1})

        where = ''

        if 'url' in kw:
            where = " AND url='%s'" % kw['url']

        if 'iscrawl' in kw:
            where = " AND iscrawl=%s " % kw['iscrawl']

        try:
            sql = r" SELECT COUNT(1) FROM douban_movies_url WHERE 1 " + where
            count = cursor.execute(sql)
            print('has %s row' % count)
            return count
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insert_url(self, url):
        try:
            sql = "INSERT INTO douban_movies_url(url, addtime) VALUES(%s, %s) "
            param = [url, int(time.time())]
            n = cursor.execute(sql, param)
            conn.commit()
            print('insert %s row' % n)
            return n
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.rollback()


    def add_new_url(self, url):
        if url is None:
            return None

        cnt = self.get_urls_cnt(url)
        if not cnt:
            self.insert_url(url)


    # def add_new_urls(self, urls):
    #     if urls is None or len(urls) == 0:
    #         return None
    #
    #     for url in urls:
    #         self.add_new_url(url)
    #
    # def has_new_url(self):
    #     return len(cache.smembers(NEW_URLS_KEY)) != 0
    #
    # def get_new_url(self):
    #     tmp = cache.spop(NEW_URLS_KEY)
    #     print(tmp)
    #     cache.sadd(OLD_URLS_KEY, tmp)
    #     return tmp

mtest = MysqlUrls()
#mtest.insert_url('http://movie.douban.com/subject/3077412')
cnt = mtest.get_urls_cnt(url='http://movie.douban.com/subject/3077412')
print(cnt)