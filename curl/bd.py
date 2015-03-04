# -*- coding:utf-8 -*-

import urllib2
import re

url='http://tieba.baidu.com/p/3295185529?see_lz=1'

#打开页面并进行转码
page=urllib2.urlopen(url).read()
print 'Open %s'%url

#去掉超链接和图片
none_re=re.compile('<a href=.*?>|</a>|<img.*?>')

#换行符转换
br_re=re.compile('<br>')

#标题
title_re=re.compile('<h1 class="core_title_txt  " title="(.*?)"')
#帖子内容
content_re=re.compile('<div id="post_content_\d*" class="d_post_content j_d_post_content ">(.*?)</div>')

#搜索文章标题，并去掉文件标题可能含有的特殊符号
title=re.search(title_re,page)
title=title.group(1).replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')  

#搜索文本内容
content=re.findall(content_re,page)

with open('%s.txt'%title,'w') as f:
    print 'Writing %s.txt now...'%title
    for i in content:
        
        #对html特殊符号进行替换处理
        i=re.sub(none_re, '', i)
        i=re.sub(br_re, '\n', i)
        
        #写入文本文件
        f.write(i.encode('utf-8').strip()+'\n')
    print 'Done!'
