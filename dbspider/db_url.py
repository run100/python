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

    def get_urls_cnt(self, type='new'):
        crawls = dict({'new': 0, 'old': 1})
        try:
            sql = " SELECT COUNT(1) FROM douban_movies_url WHERE iscrawl= %d "
            param = (crawls[type])
            count = cursor.execute(sql, param)
            print('has %s row' % count)
            return count
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insert_url(self, url):


    def add_new_url(self, url):
        if url is None:
            return None

        if not cache.sismember(NEW_URLS_KEY, url) and not cache.sismember(NEW_URLS_KEY, url):
            cache.sadd(NEW_URLS_KEY, url)


    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return None

        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(cache.smembers(NEW_URLS_KEY)) != 0

    def get_new_url(self):
        tmp = cache.spop(NEW_URLS_KEY)
        print(tmp)
        cache.sadd(OLD_URLS_KEY, tmp)
        return tmp
