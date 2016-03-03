#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/1'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import json
import threading
import time
import unittest
import uuid
import random

QUIT = False
LIMIT = 100

def check_token(conn, token):
    return conn.hget('login:', token)


def update_token(conn, token, user, item=None):
    # 获取当前时间戳
    timestamp = time.time()

    # 维护令牌和用户的关系 hash散列
    conn.hset('login:', token, user)
    # 记录令牌最后一次出现的时间
    conn.zadd('recent:', token, timestamp)

    if item:
        # 记录浏览过的商品
        conn.zadd('viewd:'+token, item, timestamp)
        # 移除旧的记录，只保留最新浏览过的25个商品
        #conn.zremrangebyrank('viewd:'+token, 0, -26)


class TestCh02(unittest.TestCase):
    def setUp(self):
        import redis
        self.conn = redis.Redis(db=15)

    def tearDown(self):
        pass

    def test_login_cookies(self):
        conn = self.conn

        global LIMIT, QUIT

        # 批量添加token
        # for i in range(1, 2):
        #     token = str(uuid.uuid4())
        #     randint = str(random.randint(99, 99999))
        #     username = 'cookie'+randint
        #     #print(token)
        #     #print(username)
        #     print(token)
        #     print(username)
        #     update_token(conn, token, username)

        token = '99d228e9-27fa-426d-9bfb-406bdc6b75c0'
        username = 'cookie85495'
        for i in range(1, 100):
            itemname1 = '%s%s' % ('item', i)
            update_token(conn, token, username, itemname1)

        print "We just logged-in/updated token:", token
        print "For user:", 'username'
        print




if __name__ == '__main__':
    unittest.main()