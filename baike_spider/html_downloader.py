#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url == None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
