#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='bob', age=20, score=88)

#print pickle.dumps(d)
'''
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

print d
'''

print json.dumps(d)


