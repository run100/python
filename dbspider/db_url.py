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
import base64
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
        tips = ''

        if 'url' in kw:
            where += " AND urlbase64='%s'" % base64.b64encode(kw['url'])
            tips = 'url '

        if 'iscrawl' in kw:
            where += " AND iscrawl=%s " % kw['iscrawl']
            tips = 'crawled '

        try:
            sql = r" SELECT COUNT(1) as cnt FROM douban_movies_url WHERE 1 " + where
            n = cursor.execute(sql)
            cnt = cursor.fetchone()
            print(tips + 'result has %s row' % cnt)
            return int('%d' % cnt)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def insert_url(self, url):
        # cnt = self.get_urls_cnt(url=base64.b64encode(url))
        # if cnt > 0:
        #     return None
        #print('insert %s' % url)
        try:
            sql = "INSERT INTO douban_movies_url(url, urlbase64, addtime) VALUES(%s, %s, %s) "
            param = [url, base64.b64encode(url), int(time.time())]
            n = cursor.execute(sql, param)
            conn.commit()
            #print('insert %s row' % n)
            return n
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.rollback()

    def update_url(self, url):
        # cnt = self.get_urls_cnt(url=base64.b64encode(url))
        # if cnt < 1:
        #     return None

        try:
            sql = "update douban_movies_url set iscrawl=1 where urlbase64=%s"
            param = [base64.b64encode(url)]
            n = cursor.execute(sql, param)
            conn.commit()
            #print('update %s row' % n)
            return n
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.rollback()

    def add_new_url(self, url):
        if url is None:
            return None

        cnt = self.get_urls_cnt(url=url)
        if not cnt:
            self.insert_url(url)


    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return None

        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        cnt = self.get_urls_cnt(iscrawl=0)
        return cnt

    def get_new_url(self):
        sql = "SELECT url FROM douban_movies_url WHERE iscrawl=0 LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        url = result[0]
        self.update_url(url)
        return url

#mtest = MysqlUrls()
#url = 'http://movie.douban.com/subject/25798448/?from=subject-page'
#mtest.add_new_url(url)
#print(mtest.has_new_url())
#print(mtest.get_new_url())
#mtest.insert_url(url)
#cnt = mtest.get_urls_cnt(url=base64.b64encode(url), iscrawl="0")
# cnt = mtest.update_url(url)
# print(cnt)