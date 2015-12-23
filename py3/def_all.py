#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def f1(a,b,c=0,*args,**kw):
    print('a',a,'b',b,'c',c,'args',args,'kw',kw)


l=f1(1, 2)
print(l)

l=f1(1, 2, 3)
print(l)

l=f1(1, 2, 3, 'a', 'b')
print(l)

l=f1(1, 2, 3, 'a', 'b', x=9)
print(l)


args=(1, 2, 3, 4)
kw={'d':99, 'x':'#'}
f1(*args, **kw)
