#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib
import urllib2


class DownLoader(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }

        self.proxy_url = '120.192.92.188:80'
        self.proxy = urllib2.ProxyHandler({'http': self.proxy_url})
        self.opener = urllib2.build_opener(self.proxy)


    def down(self, url):

        if url is None:
            return None

        try:
            #resp = urllib2.urlopen(url)
            request = urllib2.Request(url, headers = self.headers)
            resp = self.opener.open(request)
        except urllib2.HTTPError, e:
            print e.code
            print e.msg
            return None

        if resp.getcode() != 200:
            return None

        return resp.read()
