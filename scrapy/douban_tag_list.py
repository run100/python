#!/usr/bin/env python
# -*- coding:utf-8 -*-


import urllib
import urllib2
import re1
import thread
import time
import MySQLdb
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

constDebug = False


keyword = sys.argv[1]
if not keyword:
    print 'keyword is empty'
    exit()



keywordquote = urllib.quote_plus(keyword)
perage = 20
url = 'http://movie.douban.com/tag/'+str(keywordquote) #&start=0

#print url

#解码
#print urllib.unquote_plus('%E7%A7%91%E5%B9%BB')

#加码
#print urllib.quote_plus('科幻')

#测试模式
if constDebug:
    file = os.path.abspath('.') + '/tag_list.txt'
    with open(file) as f:
        html = f.read()

    unicodehtml = html.decode("utf-8")



def url_get_html(url):
    '''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    '''

    #opener = urllib2.build_opener(urllib2.ProxyHandler({'http':'121.41.84.140:80'}), urllib2.HTTPHandler(debuglevel=1))
    #urllib2.install_opener(opener)

    headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2327.5 Safari/537.36",
               "Connection":'keep-alive',
               "Cache-Control":"max-age=0",
             }

    #request = urllib2.Request(url)
    request = urllib2.Request(
        url = url,
        headers = headers
    )

    print url

    response = urllib2.urlopen(request)
    html = response.read()
    #return  html.decode("utf-8")
    return  html

#非测试模式
if not constDebug:
    # 获取总的页数
    unicodehtml = url_get_html(url)


#print unicodehtml
#exit()

#获取总页数
totalr = re1.compile(r'data-total-page="(.*?)"', re1.S)
matchs = totalr.findall(unicodehtml)

total = 0
if matchs:
    total = int(matchs[0])


def match_content(htmls):
    #内容匹配,  匹配 详细页,标题,缩略图,简介，评分,评价人数，

    movies = []

    #先匹配整个一部电影
    patternstr = '<tr\s*class="item">\s*'
    #缩略图
    patternstr += '<td\s*width="100"\s*valign="top">\s*<a.*?>\s*<img\s*src="(.*?)".*?/>\s*</a>\s*</td>\s*'

    #详细页,标题 标题还要替换一次
    patternstr += '<td\s*valign="top">\s*<div class="pl2">\s*<a\s*href="(.*?)".*?>[\s|\r\n]*(.*?)[\s|\r\n]*</a>[\s|\r\n|\n]*'

    #简介
    patternstr += '(.*?)'
    '''
    #评分
    patternstr += '\s*<span\s*class="rating_nums">(.*?)</span>'

    #评价人数
    patternstr += '\s*<span\s*class="pl">\((.*?)\)</span>\s*</div>\s*</div>'
    '''
    patternstr += '</td>\s*'
    patternstr += '</tr>'
    all = re1.compile(r''+ patternstr +'', re1.S)
    allm = all.findall(htmls)
    #print allm
    #exit()
    for item in allm:
        #print item[0] #缩略图地址
        #print item[1] #详细页

        # 标题
        titletmp = re1.sub(re1.compile(r'[\r\n|\n|\s*]'), '', item[2])
        titletmp = re1.sub(re1.compile(r'<.*?>'), '', titletmp)
        #print titletmp

        # 内容
        introm = re1.compile(r'<p\s*class="pl">(.*?)</p>', re1.S)
        introarr = introm.findall(item[3])
        introstr = introarr[0]

        # 评分
        score = '0'
        scorem = re1.compile(r'<span\s*class="rating_nums">(.*?)</span>', re1.S)
        scorearr = scorem.findall(item[3])
        if scorearr:
            score = scorearr[0]

        # 评分人数
        score_num = '0'
        scorenumm= re1.compile('<span\s*class="pl">\((.*?)\)</span>', re1.S)
        scorenumarr = scorenumm.findall(item[3])
        if scorenumarr:
            score_num = re1.sub( re1.compile(u'[\u4e00-\u9fa5]+'), '', scorenumarr[0] )

        #print score_num
        #exit()

        # 评分
        #print item[4]

        # 评价人数
        # score_num = re.sub( re.compile(u'[\u4e00-\u9fa5]+'), '',item[5] )
        #print reviewnum

        movies.append([titletmp, item[0], item[1], introstr, score, score_num])
        #exit()
    return movies


# 连接数据库
dbconn = MySQLdb.connect(host="localhost", user="root", passwd="", db="scrapy",charset="utf8")
cursor = dbconn.cursor()

#取tagid
ksql = "SELECT * FROM douban_tag WHERE tag_name='%s'" % (keyword)
#print ksql
tagid = 0
try:
    cursor.execute(ksql)
    data = cursor.fetchone()
    tagid = data[0]
except:
    print "Error: unable to fecth data"

file = os.path.abspath('.') + '/tag_list_sql.txt'

def insert_data( ms , start = 0):
    global dbconn,cursor,tagid, tag_name
    for m in ms:
        #for i in range(0, 6):
        #    print m[i]
        #m[4] if m[4] is not None  else 0
        #m[5] if m[5] is not None  else 0

        for i in range(0, 6):
            if not m[i]:
                m[i] = 0

        '''
        if not m[4]:
            m[4] = 0
        if not m[5]:
            m[5] = 0
        '''

        sql = "INSERT INTO douban_movie( tag_id, tag_name, title, thumb_url, detail_url, intro, score, score_num, start) "
        sql += " VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d')" % ( tagid, keyword, m[0], m[1], m[2], m[3], m[4], m[5], start)

        try:
            cursor.execute(sql)
            dbconn.commit()
        except Exception, e:
            dbconn.rollback()

            #写入日志
            file_object = open(file, 'a+')
            file_object.write(sql+'\r\n')
            file_object.close()

            print "MySQL Error %s: %s" % (e.args[0], e.args[1])



#提取单页内容数组
ms = match_content(unicodehtml)

#加入数据库
insert_data( ms )


if constDebug:
    msnext = match_content(unicodehtml)
    insert_data(msnext)
    exit()


if not constDebug:
    print total
    #入口 循环页面匹配
    for i in range(1, total):
        start = i*20
        tmpurl = url + '?start=' + str(start)
        #print url
        #break
        htmlconent = url_get_html(tmpurl)
        msnext = match_content(htmlconent)
        insert_data(msnext, start)
        print i,start,tmpurl

cursor.close()
#关闭数据库连接
dbconn.close()



#print movies
'''
#标题， start
title = re.compile(r'<div class="pl2">.*?<a href="(.*?)".*?>(.*?)</a>', re.S)
titlematch = title.findall(htmls)

for item in titlematch:
    #处理\r\n及html字符
    titletmp = re.sub(re.compile(r'[\r\n|\n|\s*]'), '', item[1])
    titletmp = re.sub(re.compile(r'<.*?>'), '', titletmp)

    movies.append([item[0],titletmp])

#缩略图 start
thumb = re.compile(r'', re.S)
'''