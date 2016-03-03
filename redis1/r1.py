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
import random

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

# 模拟投票
def article_vote(conn, user, article):

    # 计算文章到现在的投票截止时间, 一周前
    cutoff = time.time() - ONE_WEEK_IN_SECONDS

    # 检查是否还可以对文章进行投票
    #（虽然使用散列也可以获取文章的发布时间，
    # 但有序集合返回的文章发布时间为浮点数，
    # 可以不进行转换直接使用）。
    t = conn.zscore('time:', article)
    # print(t)
    if t < cutoff:
        return

    # 从article:id 标识符(identifier)里面取出文章的ID
    article_id = article.partition(':')[-1]
    print(article)

    # 如果用户是第一次为这篇文章投票，那么增加这篇文章的投票数量和评分。
    if conn.sadd('voted:'+article_id, user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)

# 模拟添加文章
def post_article(conn, user, title, link):
    # 生成一个新的文章ID
    article_id = str(conn.incr('article:'))
    #print(article_id+'title')

    # 将发布文章的用户添加到文章的已投票用户名单中
    # 并且设置过期时间为一周
    voted = "voted:" + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    # 设置文章信息,存入散列中
    now = time.time()
    article = 'article:'+article_id

    conn.hmset(article, {
        'id': article_id,
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1
    })

    # 将文章添加到 按发布时间的有序集合 和 按时间的有序集合
    conn.zadd('score:', article, now+VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id

# 取文章列表
ARTICLES_PER_PAGE = 25

def get_articles(conn, page, order='score:'):
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    ids = conn.zrevrange(order, start, end)
    articles = []
    #print(ids)
    for idstr in ids:
        article_data = conn.hgetall(idstr)
        articles.append(article_data)

    return articles

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
        num = random.randint(10, 9999)
        username = "%s%s" % ('run', num)
        article_id = str(post_article(conn, username, 'a title', 'http://www.google.com'))
        print "We posted a new article with id:", article_id
        print
        self.assertTrue(article_id)
        article_id = '10'

        print("Its HASH looks like:")
        r = conn.hgetall('article:'+article_id)
        print r
        print
        self.assertTrue(r)

        voteusername = "%s%s" % ('vote', num)
        article_vote(conn, voteusername, 'article:'+article_id)
        print "We voted for the article, it now has votes:",
        v = int(conn.hget('article:'+article_id, 'votes'))
        print v
        print
        self.assertTrue(v > 1)

        print "The currently highest-scoring articles are:"
        articles = get_articles(conn, 1)
        pprint.pprint(articles)
        print

        self.assertTrue(len(articles) > 1)


if __name__ == '__main__':
    print('hello world')
    unittest.main()
