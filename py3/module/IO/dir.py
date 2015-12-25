#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


import os
#print(os.name)

#print(os.uname())
#print(os.environ.get('PATH'))


#print(os.path.abspath('.'))
#print(os.path.join('F:\python\py3\module\IO', 'test'))
#os.mkdir('F:/python/py3/module/IO/test')
#os.rmdir('F:/python/py3/module/IO/test')

#print(os.path.split('r1.txt'))
#os.rename('r.txt', 'r1.txt')


l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l)
