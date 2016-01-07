#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/7'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


import re

import urllib
import urllib2
import cookielib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #控制程序是否继续运行
        self.enable = False

    #获取分页段子内容
    def getPageContent(self, page):
        url = "http://www.qiushibaike.com/hot/page/" + str(page)
        login_header = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        request = urllib2.Request(url, headers=login_header)
        try:

            response = urllib2.urlopen(request)
            if response.getcode() == 200:
                return response.read().decode('utf-8')
            else:
                print('获取失败')
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    #提取段子内容
    def parsePageContent(self, page):
        #提取内容
        content = self.getPageContent(page)
        #正则
        pattern = re.compile('<a.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?>(.*?)<!--(.*?)-->.*?</div>.*?<div.*?<i.*?class="number">(.*?)</i>.*?</div>', re.S)

        items = re.findall(pattern, content)

        pageStories = []
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, '', item[1])
            pageStories.append([item[0].strip(), text, item[2].strip(), item[3].strip()])
        return pageStories

    #加载页面内容
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.parsePageContent(self.pageIndex)
                #print(pageStories)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    #显示内容
    def getOneStroy(self, story, page):

        for item in story:
            inputstr = raw_input()
            self.loadPage()
            if inputstr == 'Q':
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,item[0],item[2],item[3],item[1])


    def start(self):
        print(u"正在读取糗事百科,按回车查看新段子，Q退出")
        #程序运行
        self.enable = True
        self.loadPage()

        nowpage = 0
        while self.enable:
            if len(self.stories) > 0:
                story = self.stories[0]
                nowpage += 1
                del self.stories[0]
                self.getOneStroy(story, nowpage)




spider = QSBK()
spider.start()