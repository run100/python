#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import redis
import urllib2
from bs4 import BeautifulSoup
import time

redis_conn = redis.Redis('localhost', 6379)
redis_smem_key = 'smembers:category:href'
redis_smem_letters = 'smembers:letter:href'

header = {
    'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
}

def get_url_content(url):
    global header

    request = urllib2.Request(url, headers=header)
    resp = urllib2.urlopen(request)
    if resp.getcode() == 200:
        return resp.read()

def add_redis_content(title, url, summary):
    global redis_conn

    # 生成新的ID
    article_id = redis_conn.incr("article:")
    print(article_id)

    now = time.time()

    artkey = "%s%s" % ("article:", article_id)
    redis_conn.zadd('article:ids', article_id, now)


    redis_conn.hmset(artkey, {
        'title': title,
        'link': url,
        'time': now,
        'summary': summary
    })

    redis_conn.zadd('score:', artkey, now)
    redis_conn.zadd('time:', artkey, now)


arts = redis_conn.hgetall('article*')
print(arts)

htmls = redis_conn.smembers(redis_smem_key)
for url in htmls:
    urlstr = '%s%s' % ('http://www.cnbeta.com', url)

    content = get_url_content(urlstr)
    #print(content)

    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    items = soup.find_all('div', class_="item")
    for item in items:
        #print(item)
        #break;
        divtitle = item.find('div', class_="title")
        atitle = divtitle.a
        #print(atitle['href'])
        #print(atitle.string)
        spansummary = item.find('span', class_="newsinfo")
        #print(spansummary.p.string)

        add_redis_content(atitle.string, atitle['href'], spansummary)



        break

    exit()


