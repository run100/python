#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/29'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import global1
import redis

NEW_URLS_KEY = 'new:urls:key'
OLD_URLS_KEY = 'old:urls:key'

#集合 set
cache = redis.StrictRedis(host=global1.REDIS_HOST, port=global1.REDIS_PORT, db=global1.REDIS_DB)
cache.flushall()
print(cache.smembers(NEW_URLS_KEY))
print(cache.smembers(OLD_URLS_KEY))

class RedisUrls:

    # def __init__(self):
    #     self.new_urls = cache.smembers(NEW_URLS_KEY)
    #     self.old_urls = cache.smembers(OLD_URLS_KEY)


    def add_new_url(self, url):
        if url is None:
            return None

        if not cache.sismember(NEW_URLS_KEY, url) and not cache.sismember(NEW_URLS_KEY, url):
            cache.sadd(NEW_URLS_KEY, url)


    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return None

        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(cache.smembers(NEW_URLS_KEY)) != 0

    def get_new_url(self):
        tmp = cache.spop(NEW_URLS_KEY)
        print(tmp)
        cache.sadd(OLD_URLS_KEY, tmp)
        return tmp
