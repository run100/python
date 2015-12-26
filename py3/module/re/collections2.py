#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""

from collections import namedtuple


point = namedtuple('point', ['x', 'y'])
p = point(1, 2)
print(p.x)
print(p.y)

print( isinstance(p, point))
print( isinstance(p, tuple))

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print(q)


from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'persist'
print(dd['key1'])
print(dd['key2'])


from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


from collections import Counter

c = Counter()

for ch in "Counter":
    c[ch] = c[ch] +  1

print(c)