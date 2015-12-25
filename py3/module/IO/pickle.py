#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


# import pickle
# d = dict(name="bob", age=20, score=88)
# pickle.dumps(d)

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))