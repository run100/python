#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/29'
"""
#http://www.the5fire.com/python-simple-redis.html
import redis

cache = redis.StrictRedis(host='localhost', port=6379)

cache.set('blog:title', u'忠旺博客')
print(cache.get('blog:title'))

for i in range(10):
    cache.mset({
        'blog:post:%s:title' % i:u'文章%s标题' % i
    })


post_list = []
for i in range(10):
    post = cache.mget('blog:post:%s:title' % i)
    if post:
        post_list.append(post)


for title in post_list:
    print(title)