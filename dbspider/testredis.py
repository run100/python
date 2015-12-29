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
import time
import global1

cache = redis.StrictRedis(host=global1.REDIS_HOST, port=global1.REDIS_PORT, db=global1.REDIS_DB)

print(u'REDIS操作')
#key1 = 'blog:title'
#get set
#cache.set(key1, u'忠旺')
#过期时间
#cache.set(key1, u'忠旺', 10)
#删除
#cache.delete(key1)
# if cache.exists(key1):
#     print(cache.get(key1))
#     #单独设置过期时间
#     #print(cache.expire(key1, 60))
#     print(cache.ttl(key1))
# else:
#     print(key1+"不存在")

# #字典操作
# key5 = 'title:k1'
# array_met = dict({'title:k1':'v1', 'title:k2':'v2', 'title:k3':'v4'})
# #排序
# array_met = sorted(array_met.iteritems(), key=lambda d:d[0])
# #cache.mset(array_met)
# print(cache.get('title:k2'))
#
# for key,val in array_met:
#     print(key, val)

#keys
# cache.flushdb()
# cache.mset(array_met)

# print(cache.keys("t*")) #返回列表
# print(cache.keys("t??")) #返回列表
# print(cache.keys("t[w]*")) #返回列表
# print(cache.keys("*")) #返回列表

# print(cache.randomkey())
# key2 = 'title:k1'
# print(cache.get(key2))
# print(cache.ttl(key2))
# print(cache.delete(key2))
# print(cache.exists(key2))
#print(cache.dbsize())

#MOVE命令

#RENAME
# key3 = 'message3'
# key4 = 'message4'
# cache.set(key3, 'hello world')
# print(cache.get(key3))
# cache.rename(key3, key4)
# print(cache.get(key3))
# print(cache.exists(key3))

#RENAMENX

#TYPE

#字符串 string
# print(cache.get(key5))
# print(cache.type(key5))
#
# # 集合set
# cache.sadd('pat', 'dog', 'cat')
# print(cache.type('pat'))
#
# # 列表 list
# cache.lpush('book_list', 'aa', 'bb')
# print(cache.type('book_list'))
#
# # zset (sorted set)
# cache.zadd('pats', 1, 'cat')
# cache.zadd('pats', 2, 'dog')
# print(cache.zrange('pats', 0, -1))
# print(cache.type('pats'))
#
# # hset hash值，键值对
# key10 = 'website'
# cache.hset(key10, 'google', 'google.com.hk')
# print(cache.hget(key10, 'google'))


#sort
# key11 = 'today_cost'
# cache.lpush(key11, 30)
# cache.lpush(key11, 1.5)
# cache.lpush(key11, 20)
# cache.lpush(key11, 8)
#
# print(cache.llen(key11))
# print(cache.lrange(key11, 0, 2))
# print(cache.sort(key11))


# 字符串 String,setnx
#setnx
#setex
# key12 = 'setex_key'
# cache.setex(key12, int(time.time())+60, 'aaa')
# print(cache.get(key12))
# print(cache.ttl(key12))

#mset 设置集合

# key13 = 'mtitle:k1'
# array_mset = dict({'mtitle:k1':'v1', 'mtitle:k2':'v2', 'mtitle:k3':'v4'})
# cache.msetnx(array_mset)
# array_mset = dict({'mtitle:k2':'v22222'})
# cache.msetnx(array_mset)
# print(cache.exists('mtitle:k2'))
# print(cache.mget('mtitle:k2'))
#
# print(cache.strlen(key13))

# #incr incrby
# key14 = 'page_view'
# cache.set(key14, 20)
# #print(cache.incr(key14))
# print(cache.incrby(key14, 20))
# print(cache.decr(key14))
# print(cache.get(key14))


#哈希表(Hash)
