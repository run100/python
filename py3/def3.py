#!/usr/bin/env python3
# -*- coding:utf-8  -*-

def calc(*numbers):
    sum=0
    for n in numbers:
        sum = n*n;
    return sum


l=calc(1, 2, 3, 4)
print(l)

l=calc(1, 2)
print(l)
