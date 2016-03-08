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

redis_conn = redis.Redis('localhost', 6379)
redis_smem_letters = 'smembers:letter:href'
redis_smem_key = 'smembers:category:href'


url = 'http://www.cnbeta.com/topics.htm'

header = {
    'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
}



request = urllib2.Request(url, headers=header)
resp = urllib2.urlopen(request)


def get_cate_url(soup):
    letters = soup.find('div', class_="letter")
    #print(type(letters))
    lis = letters.find_all('li')
    for li in lis:
        ahrefs = li.a
        #print(ahrefs['href'])
        redis_conn.sadd(redis_smem_letters, ahrefs['href'])

def get_url_content():
    global redis_conn, header
    #soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
    lists = redis_conn.smembers(redis_smem_letters)

    for url in lists:
        urlstr = '%s%s' % ('http://www.cnbeta.com', url)
        request = urllib2.Request(urlstr, headers=header)
        resp = urllib2.urlopen(request)

        if resp.getcode() == 200:
            soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='utf-8')
            divs = soup.find_all('div', class_="imgbox100x100")
            for div in divs:
                diva = div.a
                print(diva['href'])

                redis_conn.sadd(redis_smem_key, diva['href'])



def do_href_cate(soup):
    global redis_conn

    #print(redis_conn.scard(redis_smem_letters))
    lists = redis_conn.smembers(redis_smem_letters)
    #print(lists)
    for list in lists:
        print(list)



if resp.getcode() == 200:
    html_doc = resp.read()

    #get_url_content()

    #print(html_doc)

    #soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    #get_cate_url(soup)
    #do_href_cate(soup)

    # divs = soup.find_all('div', class_="imgbox100x100")
    # for div in divs:
    #     diva = div.a
    #     print(diva['href'])
    #
    #     redis_conn.sadd(redis_smem_key, diva['href'])




#members = redis_conn.smembers(redis_smem_key)
#print(members)


#print(redis_conn.scard(redis_smem_key))

