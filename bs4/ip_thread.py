#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import threading
import time
import urllib2
import redis
from bs4 import BeautifulSoup
import random



ALL_IP_KEY = 'all:ip:key'

raw_proxy_list = []
check_proxy_list = []

targets = []
for i in range(1, 20):
    targets.append('http://www.xicidaili.com/nn/%s' % i)

class ProxyGet(threading.Thread):

    def __init__(self, target):
        threading.Thread.__init__(self)
        self.target = target
        self.init_redis()
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        }

    def init_redis(self):
        self.redis = redis.StrictRedis('localhost', 6379, 0)

    def get_con(self):
        request = urllib2.Request(self.target, headers=self.header)

        proxy_urls = ['211.143.146.230:81', '124.202.200.98:8118']
        #proxy_url = '211.143.146.230:81'
        #proxy_url = '124.202.200.98:8118'
        urlint = random.choice(range(0, 1))
        proxy_url = proxy_urls[int(urlint)]
        proxy = urllib2.ProxyHandler({'http': proxy_url})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(request)
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
                lo = tds[4].get_text().strip()
                ipstr = "%s:%s" % (ip, port)

                #raw_proxy_list.append(ipstr)
                raw_proxy_list.append([ip, port, lo])

                #if not self.redis.sismember(ALL_IP_KEY, ipstr):
                #    print(ipstr)
                    #self.redis.sadd(ALL_IP_KEY, ipstr)
                    #raw_proxy_list.append(ipstr)

    def getProxy(self):
        print "代理服务器目标网站： " + self.target
        con = self.get_con()
        self.parse_con(con)


    def run(self):
        self.getProxy()

# 验证采集的IP是否可用
class ProxyCheck(threading.Thread):

    def __init__(self, proxy_list):
        threading.Thread.__init__(self)
        self.proxy_list = proxy_list

    def checkProxy(self):

        i = 0
        for proxy in self.proxy_list:

            # if i > 20:
            #     exit()

            proxy_url = "%s:%s" % (proxy[0], proxy[1])
            print(proxy_url)
            proxy_handle = urllib2.ProxyHandler({'http': proxy_url})
            opener = urllib2.build_opener(proxy_handle)
            urllib2.install_opener(opener)

            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            }

            url = 'http://www.baidu.com/'
            request = urllib2.Request(url, headers=header)
            t1 = time.time()
            #print("正在处理代理IP %s" % str(proxy))

            i = i + 1

            try:
                resp = urllib2.urlopen(request, timeout=5)
                print("urlopen is ok")
                result = resp.read()
                print("read html ...")
                timeused = time.time() - t1
                pos = result.find('030173')
                if pos > 1:
                    print('success,add list')
                    check_proxy_list.append((proxy[0], proxy[1], proxy[2], timeused))
                else:
                    print('error2')
                    continue
            except Exception, e:
                #print e.code
                #print e.msg
                print('error1')
                continue

    def run(self):
        self.checkProxy()



if __name__ == '__main__':
    get_threads = []
    check_threads = []

    # 对每个目标网站开启一个线程抓取
    for i in range(len(targets)):
        t = ProxyGet(targets[i])
        get_threads.append(t)

    # 开启所有的线程
    for i in range(len(get_threads)):
        time.sleep(1)
        get_threads[i].start()

    # 等待所有的进程结束
    for i in range(len(get_threads)):
        get_threads[i].join()

    # 抓取的ip
    # print(len(raw_proxy_list))
    print '.'*10 + "总共抓取了%s个代理" % len(raw_proxy_list) +'.'*10

    # 校验
    #开启20个线程负责校验，将抓取到的代理分成20份，每个线程校验一份
    # 50 一个组校验
    total = len(raw_proxy_list)
    perpage = 50
    pages = total / perpage

    #每页50,共
    for page in range(1, pages + 1):

        start = (page - 1) * perpage
        end = start + perpage
        #print(page, start, end)
        list = raw_proxy_list[start:end]
        t = ProxyCheck(list)
        check_threads.append(t)
        #print(page, list[0:5], len(list))

    for i in range(len(check_threads)):
        check_threads[i].start()
        time.sleep(1)

    for i in range(len(check_threads)):
        check_threads[i].join()

    print '.'*10+"总共有%s个代理通过校验" %len(check_proxy_list) +'.'*10

    print(check_proxy_list)