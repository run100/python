#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import re
from bs4 import BeautifulSoup


class UrlParser(object):



    def parse(self, page_url, html_con):

        if html_con is None or page_url is None:
            return None

        soup = BeautifulSoup(html_con, 'html.parser', from_encoding='utf-8')

        urls = self.get_data_urls(soup, page_url)
        content = self.get_data_content(soup, page_url)

        return urls, content

    def get_data_urls(self, soup, page_url):
        urls = set()
        links = soup.find_all('a', href=re.compile(r"http://.+?subject/\d+/\?from=subject-page", re.I))

        for link in links:
            new_url = link['href']
            urls.add(new_url)

        return urls

    def get_data_content(self, soup, page_url):
        res_data = {}

        res_data['url'] = page_url

        # 匹配标题 <span property="v:itemreviewed">寻龙诀</span>
        title_node = soup.find('span', property="v:itemreviewed")
        res_data['title'] = title_node.get_text()

        # 匹配评分 <strong class="ll rating_num" property="v:average">8.0</strong>
        average_node = soup.find('strong', property="v:average")
        res_data['average'] = average_node.get_text()

        # 匹配简介 <span property="v:summary" class=""></span>
        summary_node = soup.find('span', property="v:summary")
        if summary_node is not None:
            res_data['summary'] = summary_node.get_text()
        else:
            res_data['summary'] = ''

        return res_data

