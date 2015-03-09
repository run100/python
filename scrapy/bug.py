#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import thread
import time
import MySQLdb


# 加载
class Spider_Model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
        self.DbConn()

    def DbConn(self):
        self.db = MySQLdb.connect("localhost", "root", "", "test")


    def GetPage(self, page):
        print 'GetPage Fun'
        myurl = "http://www.qiushibaike.com/hot/page=" + page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(myurl, headers = headers)
        response = urllib2.urlopen(request)
        unicodePage = response.read()
        unicodehtml = unicodePage.decode("utf-8")

        # 找出所有的class="conent"的div标记
        #print unicodehtml
        matchs = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>', unicodehtml, re.S)
        #print matchs
        contents = []
        for m in matchs:
            contents.append([m[0].replace("\n",''),m[1].replace("\n","")])

        #print contents
        return contents

    def Insert(self, data):
        dbcursor = self.db.cursor()
        print dbcursor
        for items in data:

            sql = "INSERT INTO bk(content, publish) VALUES ('%s', '%s')" % (items[1], items[0])
            print sql

            try:
                n = dbcursor.execute(sql)
                print n
                self.db.commit()
            except Exception, e:
                self.db.rollback()
                print "MySQL Error %d: %s" % (e.args[0], e.args[1])

        dbcursor.close()
        #return True

    def LoadPage(self):
        print 'LoadPage Fun'
        while self.enable:
            if len(self.pages) < 2:
                try:
                    print 'loadpage get'
                    # 获取页面并存在数组
                    content = self.GetPage(str(self.page))
                    self.page  += 1
                    self.pages.append(content)

                    #加入数据库
                    self.Insert(content)
                except:
                    print '无法访问糗事百科！'
            else:
                time.sleep(1)

    def ShowPage(self, nowPage, page):
        print 'ShowPage Fun'
        for items in nowPage:
            print u'第%d页' % page, items[0], items[1]
            myinput = raw_input()
            if myinput == "quit":
                self.enable = False
                break

    def Start(self):
        self.enable = True
        page = self.page

        print u'正在加载中...'

        # 新建一个线程在后台加载段子并存储数组pages
        thread.start_new_thread(self.LoadPage,())

        while self.enable:
            # 如果self的page数组中存有元素
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page +=1

        self.db.close()

print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
spider = Spider_Model()
spider.Start()