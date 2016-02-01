#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/31'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')


print(chr(65))
txt= "汉语"
repr(txt)

s = """
            en: Regular expression is a powerful tool for manipulating text.
            zh: 汉语是世界上最优美的语言，正则表达式是一个很有用的工具
            jp: 正規表現は非常に役に立つツールテキストを操作することです。
            jp-char: あアいイうウえエおオ
            kr:정규 표현식은 매우 유용한 도구 텍스트를 조작하는 것입니다.
            """


pattern = re.compile(r"[\x80-\xff]+")
ms = pattern.search(s)
# print(ms)
# print(ms.group())

# matchs = pattern.findall(s)
# print(type(matchs))
# for m in matchs:
#     print(m)

s = unicode(s)
p2 = re.compile(u"[\u4e00-\u9fa5]+")
m = p2.search(s)
# print(m)
# print(m.group())

# res = re.findall(p2, s)
# if res:
#     print("match total %d " % len(res))
#     for r in res:
#         print("\t", r)
#         print("\n")


#匹配中文及英文
source = u"        数据结构模版----单链表SimpleLinkList[带头结点&&面向对象设计思想](C语言实现)"
temp = source.decode("utf8")
pattern = re.compile("[\w\W\u4e00-\u9fa5]+")
res = pattern.findall(source)
for r in res:
    print(r)
    print("\n")