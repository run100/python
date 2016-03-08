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



# 获取固定数量的分值
# item = conn.zscore(zsetkey, 'zkey99')
# print(item)

# 删除元素
# conn.zrem(zsetkey, 'zkey99')



#Reversion 反转

# score
scores = conn.zremrangebyscore(zsetkey, 197, 198)

# 元素已按score从小到大排序
list = conn.zrange(zsetkey, 0, -1, withscores=True)
#print(list)

list = conn.zrevrange(zsetkey, 0, -1, withscores=True)
print(list)

# 取单个元素分值 分值 从大到小
score = conn.zrevrank(zsetkey, 'zkey198')
print(score)

#取单个元素分值 分值 从小到大
score1 = conn.zrank(zsetkey, 'zkey198')
print(score1)




# scores = conn.zrangebyscore(zsetkey, 190, 200)
# print(scores)
#
# s = conn.zscore(zsetkey, ['zkey195'])
# print(s)

# score 从小到大
conn.zremrangebyrank(zsetkey, 0, 1)

