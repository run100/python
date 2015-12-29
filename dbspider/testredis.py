#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import redis
import global1

cache = redis.StrictRedis(host=global1.REDIS_HOST, port=global1.REDIS_PORT, db=global1.REDIS_DB)

print(u'get和set操作')
key1 = 'blog:title'
cache.set(key1, u'忠旺')
print(cache.get(key1))
#print(cache.expire(key1, 60))
print(cache.ttl(key1))
