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

# 使得 sys.getdefaultencoding() 的值为 'utf-8'
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'


page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)
login_header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
request = urllib2.Request(url, headers=login_header)
try:

    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # print(response1.getcode())
    # print(len(response1.read()))
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason


pattern = re.compile('<a.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?>(.*?)<!--(.*?)-->.*?</div>.*?<div.*?<i.*?class="number">(.*?)</i>.*?</div>', re.S)

items = re.findall(pattern, content)

for item in items:
    #print(item[0], item[1], item[2], item[3])
    print(item[0].strip())
    print(item[1].strip())
    print(item[2].strip())
    print(item[3].strip())
    print('===========')