#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/2'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
from bs4 import BeautifulSoup


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

url = 'http://news.cnblogs.com/'
# resp = urllib2.urlopen(url)

request = urllib2.Request(url, headers=header)

resp = urllib2.urlopen(request)

#print(resp.getcode())
if resp.getcode() == 200:
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    news = soup.find_all('div', class_="news_block")

    for new in news:
        #print(new)
        title = new.h2.a.string
        print(title)
        href = new.h2.a
        print(href['href'])
        #desc = new.select('div .entry_summary')
        desc = new.find('div', class_="entry_summary")
        print(desc.get_text())

else:
    print('error read page')

