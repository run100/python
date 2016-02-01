#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/1'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re

import redis
import urllib2
import urllib
from bs4 import BeautifulSoup

ENABLE_URLS_KEY = 'enable:urls:key'

class Paidai:

    def __init__(self):
        self.redis = ''
        self.init_redis()

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        }




    def init_redis(self):
        self.redis = redis.StrictRedis('localhost', '6379', 0)

    def get_proxy_url(self):
        url = self.redis.srandmember(ENABLE_URLS_KEY)
        if url == '':
            print('没有代理ip')
            exit()
        return url

    def down_url_con(self, url):
        request = urllib2.Request(url, headers= self.header)

        #proxy_url = self.get_proxy_url()
        #print(proxy_url)
        proxy_url = '120.52.72.180:80'
        proxy = urllib2.ProxyHandler({'http': proxy_url})

        opener = urllib2.build_opener(proxy)
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

    def parse_con(self, content):

        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        lis = soup.find_all('li', style="padding-left:2px;")
        for li in lis:
            #print(li)

            #print(li.contents)
            for child in li.contents:
                print("====")
                print(child)
            # for child in li.body.contents:
            #     print(child)

            exit()


            # print(li.get_text().strip())
            # span_node = li.find('span', _class="m2-li-r-1")
            # print(span_node)
            # title = span_node.get_text()
            # print(title)
            # href = span_node['href']
            # print(title, href)



    def crawl(self, url):
        content = self.down_url_con(url)
        #print(content)
        self.parse_con(content)





if __name__ == '__main__':
    paidai = Paidai()
    url = 'http://www.paidai.com/more.php?page=1'
    paidai.crawl(url)
