#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time

print time.time()
print time.localtime()
print time.strftime('%d/%b/%Y:%X')

print time.gmtime()

print time.mktime(time.localtime())

print time.asctime()

print time.strptime('28/Jul/2013:04:33:29', '%d/%b/%Y:%X')

'''
import datetime
print datetime.time()
t = datetime.time(1, 3, 5, 25)
print datetime.time.max
'''

#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
#print dt
