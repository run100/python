#!/usr/bin/env python

import urllib2
import re1
import os


URL = 'http://image.baidu.com/channel/wallpaper'
read=urllib2.urlopen(URL).read()
pat = re1.compile(r'src="http://.+?.js">')
urls = re1.findall(pat, read)
print urls
for i in urls:
    url = i.replace('src="','').replace('">', '')
    print url
    try:
        iread=urllib2.urlopen(url).read()
        name=os.path.basename(url)
        #with open(name, 'wb') as jsname:
        #    jsname.write(iread)
    except:
        print url,"url error"



