#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
f = open('1.txt', 'r')
print f.read()
f.close()
'''

'''
try:
    f = open('2.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
with open('2.txt', 'r') as f:
    print f.read()
with open('1.txt', 'r') as f:
    for line in f.readlines():
        print line.strip()

'''


f = open('1.jpeg', 'rb')
print f.read()

