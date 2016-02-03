#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/2/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import threading
import time

def thread_fun(num):
    for n in range(0, int(num)):
        print("i come from %s, num is %s" % (threading.currentThread().getName(), n))

def main(num):

    thread_list = []
    #创建线程
    for i in range(0, num):
        thread_name = "thread_%s" % i
        thread_list.append(threading.Thread(target=thread_fun, name=thread_name, args=(20, )))

    # 启动所有线程
    for thread in thread_list:
        thread.start()

    # 主线程等待所有的子线程退出
    for thread in thread_list:
        thread.join()


if __name__ == '__main__':
    main(3)
