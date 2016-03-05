#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/5'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re
import sys
import urllib2
import urllib


reload(sys)
sys.setdefaultencoding('utf8')



from bs4 import BeautifulSoup

url = 'http://blog.jobbole.com/category/it-tech/'

header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

data = ''

request = urllib2.Request(url, data, header)

resp = urllib2.urlopen(request)

#print(resp.getcode())

if resp.getcode() == 200:
    #print(resp.read())
    html_doc = resp.read()
    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    lists = soup.find_all('div', class_=re.compile('floated-thumb'))
    #print(type(lists))
    #print(lists)
    for list in lists:
        #print(list)
        #print(type(list))
        post = list.find('div', class_=re.compile('post-meta'))
        print(post.p.a.string)

        ptext = post.p.text
        pattern = re.compile(r'\d{4}/\d{2}/\d{2}', re.M)
        pstr = ptext.encode('utf-8')
        pmatch = pattern.findall(pstr)
        print(pmatch[0])

        pa = post.find('p', class_="align-right")
        print(pa.span.a['href'])
        exit()

