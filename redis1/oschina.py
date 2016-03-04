#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/4'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
import urllib
import re

from bs4 import BeautifulSoup

url = 'http://www.oschina.net/news/list?show=industry'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

data = ''

request = urllib2.Request(url, data, headers=header)

resp = urllib2.urlopen(request)

if resp.getcode() == 200:
    html_doc = resp.read()
    #print(html_doc)

    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    #news = soup.find(class_=re.compile("^List$"))

    news = soup.find('div', {"class":"panel", "id":"RecentNewsList"})
    print(type(news))
    ul = news.find('ul', class_="List")
    print(type(ul))
    lis = ul.find_all('li')
    #print(lis)
    for li in lis:
        print(type(li))
        print(li.h2.a.string)
        pdate = li.find('p', class_=re.compile('date'))
        print(type(pdate))
        print(pdate.get_text())
        pdetail = li.find('p', class_=re.compile('detail'))
        print(pdetail.get_text())
        

