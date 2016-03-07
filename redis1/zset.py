#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/7'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import redis

conn = redis.Redis('localhost', 6379)

#print(type(redis))

zsetkey = 'zset-key'

#conn.zadd(zsetkey, 'a', 1, 'b', 2, 'c', 3)

# for i in range(99, 199):
#     conn.zadd(zsetkey, '%s%s' % ('zkey', i), i)

# 数量
# print(conn.zcard(zsetkey))
# 添加 zincrby
#conn.zincrby(zsetkey, 'b', 10)

#list = conn.zrange(zsetkey, 0, -1, withscores=True)
#print(list)

