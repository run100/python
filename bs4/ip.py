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
import MySQLdb

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWD = "root"
MYSQL_DB = "douban"
MYSQL_CHARSET = "utf8"

conn = MySQLdb.connect(host=MYSQL_HOST
                       , user=MYSQL_USER
                       , passwd=MYSQL_PASSWD
                       , db=MYSQL_DB
                       , charset=MYSQL_CHARSET)
cursor = conn.cursor()


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

    def insert_data(self, ip, port, lo):
        try:
            sql = "INSERT INTO douban_ip(ip, port, lo, addtime) VALUES(%s, %s, %s, %s)"
            param = [ip, port, lo, time.strftime("%Y-%m-%d %H-%M-%S")]
            n = cursor.execute(sql, param)
            conn.commit()
            return n
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.rollback()

    def verify(self):

        socket.setdefaulttimeout(3)

        f = open("ips.txt")
        lines = f.readlines()
        #print(lines)

        visiturl = 'http://ip.chinaz.com/getip.aspx'
        for line in lines:
            l = line.strip("\n").split(":")
            proxy_url = "http://%s:%s" % (l[0], l[1])

            try:
                resp = urllib.urlopen(visiturl, proxies={'http': proxy_url})
                # proxy = urllib2.ProxyHandler({'http': proxy_url})
                # opener = urllib2.build_opener(proxy)
                # resp = opener.open(self.request)
                if resp.getcode() == 200:
                    pattern = re.compile(r"address:'(.*?)'", re.S)
                    str = ''
                    m = re.findall(pattern, resp.read())
                    if m:
                        str = m[0].strip()

                    self.insert_data(l[0], l[1], str)
                    #print(resp.read())

            except Exception, e:
                print proxy_url
                print e
                continue



#print(__name__)
if __name__ == '__main__':

    for i in range(1, 100):
        url = 'http://www.xicidaili.com/nn/' + str(i)
        clsip = ProxyIp(url)
        clsip.parse()
        print(clsip.verify())
        time.sleep(3)