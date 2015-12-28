#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib2


class DownLoader(object):


    def down(self, url):

        if url is None:
            return None

        resp = urllib2.urlopen(url)
        if resp.getcode() != 200:
            return None

        return resp.read()
