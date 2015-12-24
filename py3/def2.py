#!/bin/bash/env python3
# -*- coding:utf-8 -*-

def add_end(L=None):
    if L is None:
        L = [];
    L.append('END')
    return L

L=add_end([1, 2, 3])
print(L)

L=add_end(['x', 'y', 'z'])
print(L)




L=add_end()
print(L)

L=add_end()
print(L)
