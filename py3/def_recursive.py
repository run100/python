#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


l=fact(5);
print(l)
