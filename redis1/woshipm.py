#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2
import urllib
from   bs4 import BeautifulSoup
import re

class Pm(object):
    def __init__(self):
        pass

    def get_request(self, url):
        header = {
            'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
        }
        return urllib2.Request(url, headers=header)

    def get_content(self, url):
        request = self.get_request(url)
        resp = urllib2.urlopen(request)
        if resp.getcode() == 200:
            return resp.read()

    def parser_content(self, url):
        print(url)
        html_doc = self.get_content(url)
        print(html_doc)
        soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
        ftdivs = soup.find_all('div', class_="ft")
        print(ftdivs)

    def do_list(self, url):
        #print('do_list')
        page = 1
        url = url + str(page)
        self.parser_content(url)
        #print(url)

if __name__ == '__main__':
    print('start')
    pm = Pm()
    url = 'http://www.woshipm.com/page/'
    pm.do_list(url)

