#!/bin/bash/env python3
# -*- coding:utf-8 -*-


def my_abs(x):
    # 判断数据类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if (x>0) :
        return x;
    else:
        return -x;


x=my_abs('a');
print(x)
