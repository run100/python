#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


from baike_spider import url_manager,html_downloader,html_parser,html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print("craw %d:%s" % (count, new_url))
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)

            self.outputer.collect_data(new_data)
            self.outputer.output_html()

            if ( count == 1000 ) :
                break

            count = count+1

        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)