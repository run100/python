#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/2'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
import redis
from bs4 import BeautifulSoup


ALL_IP_KEY = 'all:ip:key'

class IpCrawl:
    def __init__(self):
        self.init_redis()

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        }
        #proxy = '60.173.236.97:80'
        #self.proxy = urllib2.ProxyHandler({'http': proxy})

    def get_con(self, url):
        print(url)
        request = urllib2.Request(url, headers=self.header)
        #opener = urllib2.build_opener(self.proxy)

        resp = urllib2.urlopen(request)
        #resp = request.open(request)
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



    def parse_con(self, con):

        soup = BeautifulSoup(con, 'html.parser', from_encoding='utf-8')
        trs = soup.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) == 10:
                #print(tds)
                ip = tds[2].get_text().strip()
                port = tds[3].get_text().strip()
                ipstr = "%s:%s" % (ip, port)

                if not self.redis.sismember(ALL_IP_KEY, ipstr):
                    print(ipstr)
                    self.redis.sadd(ALL_IP_KEY, ipstr)

    def init_redis(self):
        self.redis = redis.StrictRedis('localhost', 6379, 0)


    def get_ips(self):
        page = 1
        for page in range(1, 50):
            url = 'http://www.xicidaili.com/nn/%s' % page
            con = self.get_con(url)
            self.parse_con(con)

if __name__ == '__main__':
    ipcrawl = IpCrawl()
    ipcrawl.get_ips()