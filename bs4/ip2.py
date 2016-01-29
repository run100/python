#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

#http://haodailiip.com/guonei/1

import time
import sys
from bs4 import BeautifulSoup
import re
import urllib
import urllib2
import socket
import MySQLdb
import Redis

class IpCrawl:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        }
        proxy = '61.160.250.25:3128'
        self.proxy = urllib2.ProxyHandler({'http': proxy})

        self.conn = ''
        self.cursor = ''
        self.init_mysql()

    def init_mysql(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8")
        self.cursor = self.conn.cursor()

    def init_redis(self):
        


    def get_content(self, url):
        #request
        request = urllib2.Request(url, headers=self.header)
        opener = urllib2.build_opener(self.proxy)
        resp = opener.open(request)
        try:
            if resp.getcode() == 200:
                #print(resp.read())
                return resp.read()
            else:
                print(resp.getcode())

        except urllib2.HTTPError, e:
            print e.code
            print e.msg
            return None


    def html_parse(self, content):
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        trs = soup.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == 7:
                ip = tds[0].get_text().strip()
                pattern = re.compile('IP')
                m = pattern.match(ip)
                if m:
                    continue
                port = tds[1].get_text().strip()
                lo = tds[2].get_text().strip()
                n = self.in_douban_queue(ip, port, lo)

                if n == 0:
                    str = "%s 入库,待验证".decode('utf-8') % ip
                    print(str)
                else:
                    if n == 1:
                        print("%s 已加入过".decode('utf-8') % ip)
                    else:
                        print("%s 入库出错".decode('utf-8') % ip)

    def in_redis_queue(self, ip, port):


    def in_douban_queue(self, ip, port, lo):

        #判断是否存在
        sqlif = "SELECT COUNT(1) as cnt FROM douban_ip_queue WHERE ip=%s "
        param = [ip]

        try:
            self.cursor.execute(sqlif, param)
            n = self.cursor.fetchone()
            if int(n[0]) > 0:
                return 1
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

        try:
            sql = "INSERT INTO douban_ip_queue(ip, port, lo, addtime) VALUES(%s, %s, %s, %s)"
            param = [ip, port, lo, time.strftime("%Y-%m-%d %H-%M-%S")]
            n = self.cursor.execute(sql, param)
            self.conn.commit()
            return 0
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            self.conn.rollback()
            return 2



    def crawl(self, url):
        content = self.get_content(url)
        self.html_parse(content)




if __name__ == '__main__':
    crawl = IpCrawl()
    url = 'http://haodailiip.com/guonei/1'
    crawl.crawl(url)


