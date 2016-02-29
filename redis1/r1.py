#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import time
import unittest

def post_article(conn, user, title, link):
    return 1

# 发布文章
class TestCh01(unittest.TestCase):
    def setUp(self):
        import redis
        self.conn = redis.Redis(db=15)

    def tearDown(self):
        del self.conn
        print
        print

    def test_article_functionality(self):
        conn = self.conn
        import pprint
        article_id = str(post_article(conn, 'username', 'a title', 'http://www.google.com'))
        print "We posted a new article with id:", article_id
        print
        self.assertTrue(article_id)


if __name__ == '__main__':
    print('hello world')
    unittest.main()
