#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import redis

conn = redis.Redis('127.0.0.1', 6379)

run_zset_key = 'run_zset_key'
# for i in range(199, 299):
#     conn.zadd(run_zset_key, '%s%s' % (run_zset_key, i), i)

#list = conn.zrange(run_zset_key, 0, -1, withscores=True)
#print(list)

#list = conn.zrevrange(run_zset_key, 0, -1, withscores=True)
#print(list)

# val = conn.zrank(run_zset_key, 'run_zset_key296')
# print(val)


conn.zincrby(run_zset_key, 'run_zset_key296', 99999)
val = conn.zrevrank(run_zset_key, 'run_zset_key296')
print(val)


score = conn.zscore(run_zset_key, 'run_zset_key296')
print(score)

#conn.zrem(run_zset_key, 'run_zset_key199')
#conn.zremrangebyscore(run_zset_key, 200, 201)

#conn.zremrangebyrank(run_zset_key, 1, 10)

# list = conn.zrangebyscore(run_zset_key, 199, 210)
# print(list)
#
# list2 = conn.zrevrangebyscore(run_zset_key, 210, 199)
# print(list2)


