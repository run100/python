#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/22'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
import urllib

import time

from bs4 import BeautifulSoup
import random

# 把str编码由ascii改为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file_name = 'book_list.txt'
file_content = ''
file_content += '生成时间：' + time.asctime()

headers = [
       {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
       {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
       {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
       {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
       {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
]

#print(time.asctime())
#print( random.choice(headers) )

def do_spider(tag):
    global file_content, headers
    url = "http://www.douban.com/tag/%s/book" % tag
    #print(url)
    request = urllib2.Request(url, headers=random.choice(headers))
    resp = urllib2.urlopen(request)
    #print(resp.read())
    #exit

    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
    books = soup.find('div', {'class':'mod book-list'})

    count = 1
    for book in books.find_all('dd'):
        title = book.find('a', {'class': 'title'}).string.strip()
        print(title)
        desc = book.find('div', {'class': 'desc'}).string.strip()
        desc_list = desc.split('/')
        author = '/'.join(desc_list[0:-3])
        author = "作者:%s" % author
        pub_info = '/'.join(desc_list[-3:])
        pub_info = "出版:%s" % pub_info
        try:
            rating = book.find('span', {'class': 'rating_nums'}).string.strip()
        except AttributeError:
            rating = '无'

        file_content += "%d\t《%s》\t评分：%s\n\t%s\n\t%s\n\n" % (
            count, title, rating, author.strip(), pub_info.strip())
        count += 1

        #print(rate)


def do_tags(tags):
    for tag in tags:
        #print(tag)
        do_spider(tag)


if __name__ == '__main__':
    tags = ['PHP', 'javascript', 'linux', 'ios']
    do_tags(tags)

    f = open(file_name, 'w')
    f.write(file_content)
    f.close()
    