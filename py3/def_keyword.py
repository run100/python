#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def person(name, age, **kw):
    print('name',name,'age',age,'kw',kw)



person('shelton', 30)
person('shelton', 30, city='dc')
person('shelton', 30, city='dc', height='180')


