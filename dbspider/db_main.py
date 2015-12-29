#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from dbspider import db_url_manager,redis_url,db_url,db_url_downer,db_url_parser,db_outputer


class DbMain(object):
    def __init__(self):
        self.urls = db_url.MysqlUrls()
        self.downloader = db_url_downer.DownLoader()
        self.parser = db_url_parser.UrlParser()
        self.outputer = db_outputer.Outputer()

    def craw(self, url):

        if url == None :
            return None

        count = 0

        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            url = self.urls.get_new_url()
            print('crawl %d : %s' % (count, url))
            #下载
            html_con = self.downloader.down(url)
            #解析
            urls, condata = self.parser.parse(url, html_con)

            #新的URL加入
            self.urls.add_new_urls(urls)

            #记录数据
            self.outputer.insert_mysql(condata)

            if count > 100:
                break

            count = count + 1

        self.outputer.insert_mysql()

if __name__ == '__main__':
    base_url = 'http://movie.douban.com/subject/3077412'
    db_spider = DbMain()
    db_spider.craw(base_url)