#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '获取免费的IP'
__author__ = 'Administrator'
__mtime__ = '2016/1/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import time
import sys
from bs4 import BeautifulSoup
import re
import urllib
import urllib2
import socket

class ProxyIp(object):

    def __init__(self, url):
        print(url)

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        }
        self.request = urllib2.Request(url, headers=self.header)

        self.proxy_url = '221.211.121.110:9000'
        self.proxy = urllib2.ProxyHandler({'http': self.proxy_url})
        self.opener = urllib2.build_opener(self.proxy)







    def down(self):

        try:
            #resp = self.opener.open(self.request)
            resp = urllib2.urlopen(self.request)
            if resp.getcode() == 200:
                return resp.read()
            else:
                print(resp.getcode())

        except urllib2.HTTPError, e:
            print e.code
            print e.msg
            return None


    def parse(self):
        html_doc = self.down()
        #print(html_con)

        soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')


        f = open('ips.txt', "w")
        trs = soup.find_all('tr')

        for tr in trs:
            tds = tr.findAll("td")
            if len(tds) == 10:
                tmp = {}
                # tmp['ip'] = tds[2].get_text()
                # tmp['port'] = tds[3].get_text()
                # tmp['lo'] = tds[4].get_text()
                # print(tmp)
                str = "%s:%s\n" % (tds[2].get_text(), tds[3].get_text())
                print(str)
                f.write(str)

    def verify(self):

        socket.setdefaulttimeout(3)

        f = open("ips.txt")
        lines = f.readlines()
        #print(lines)

        visiturl = 'http://ip.chinaz.com/getip.aspx'
        for line in lines:
            l = line.replace("\n", "").split(":")
            proxy_url = "%s:%s" % (l[0], l[1])

            try:
                #resp = urllib2.urlopen(visiturl, proxies=proxy_url)
                urllib2.ProxyHandler({'http'})
                if resp.getcode() == 200:
                    print(resp.read())
            except Exception, e:
                print proxy_url
                print e
                continue



#print(__name__)
if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/1'
    clsip = ProxyIp(url)
    #clsip.parse()
    print(clsip.verify())