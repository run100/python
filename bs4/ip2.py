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
import redis

NEW_URLS_KEY='new:urls:key'


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

        self.redis = ''
        self.init_redis()


    def init_mysql(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8")
        self.cursor = self.conn.cursor()

    def init_redis(self):
        self.redis = redis.StrictRedis('localhost', '6379', 0)


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
                n = self.in_redis_queue(ip, port)

                str = "%s 入库,待验证".decode('utf-8') % ip
                print(str)

                # n = self.in_douban_queue(ip, port, lo)
                #
                # if n == 0:
                #     str = "%s 入库,待验证".decode('utf-8') % ip
                #     print(str)
                # else:
                #     if n == 1:
                #         print("%s 已加入过".decode('utf-8') % ip)
                #     else:
                #         print("%s 入库出错".decode('utf-8') % ip)

    def veritfy(self, ipstr):
        iparr = ipstr.split(':')
        #print(iparr[0], iparr[1])
        visiturl = 'http://ip.chinaz.com/getip.aspx'
        proxy_url = "http://%s" % (ipstr)
        try:
            resp = urllib.urlopen(visiturl, proxies={'http': proxy_url})
            if resp.getcode() == 200:
                pattern = re.compile(r"address:'(.*?)'", re.S)
                str = ''
                m = re.findall(pattern, resp.read())
                if m:
                    str = m[0].strip()
                    print(str)

        except Exception, e:
            print proxy_url
            print e



    def in_redis_queue(self, ip, port):

        ipstr = '%s:%s' % (ip, port)
        if not self.redis.sismember(NEW_URLS_KEY, ipstr):
            self.redis.sadd(NEW_URLS_KEY, ipstr)

    def do_redis_queue(self):
        ips = self.redis.smembers(NEW_URLS_KEY)
        ipslen = len(ips)

        i = 0
        while i<ipslen:
            ipstr = self.redis.spop(NEW_URLS_KEY)
            self.veritfy(ipstr)
            i = i+1

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

    crawl.do_redis_queue()


