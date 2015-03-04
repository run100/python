#  -*-  conding:utf-8 -*-

import urllib2
import re

url = 'http://tieba.baidu.com/p/3295185529?see_lz=1'

page=urllib2.urlopen(url).read()
print 'url is %s'%url


