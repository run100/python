#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/2'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import thread
import time

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s => %s: %s" % (count, thread_name, time.ctime(time.time()))

    thread.exit_thread()

try:
    thread.start_new_thread( print_time, ("Thread-1", 2) )
    thread.start_new_thread( print_time, ("Thread-2", 4) )
except:
    print("Error: unable to start thread")


while 1:
    pass