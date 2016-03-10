#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/10'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re

import urllib2
from bs4 import BeautifulSoup
import redis

redis_conn = redis.Redis('localhost', 6379)

#redis_conn.incr('')


url = 'https://segmentfault.com/blogs/hottest/monthly?page='



def get_content(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
    }
    request = urllib2.Request(url, headers=header)
    resp = urllib2.urlopen(request)
    if resp.getcode() == 200:
        return resp.read()

def get_lists(html_doc):

    #global redis_conn

    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
    sections = soup.find_all('section', class_="stream-list__item")
    #print(type(sections))
    for section in sections:
        #print(section.div.h2.a.string)
        summary = section.find('div', class_= re.compile("summary"))
        anode = summary.h2.a

        title = anode.string
        detail = summary.p.string
        print(title)
        print(detail)

        data = {}
        data['title'] = title
        data['url'] = anode['href']
        data['summary'] = detail
        # print(data)

def add_redis(data):
    global redis_conn


def init_page(page):
    html = get_content(url + str(page))
    get_lists(html)


for i in range(1, 50):
    init_page(i)