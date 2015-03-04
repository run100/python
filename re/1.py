#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
#help(re.findall)
line = "Cats are smarter than dogs"
#match =  re.match(r'dogs', line, re.M|re.I)
#print match.group()
#print help(re.search)

'''
name="Hello,My name is kuangl,nice to meet you..."
k = re.match(r"(\H....)",name)
print k.group(0)
'''
#print '111'
'''
mail='<user01@mail.com> <user02@mail.com> user04@mail.com'
matchs=re.findall(r'(\w+@m....[a-z]{3})', mail)
print matchs

var_for_arr_dict k,v in enumerate(matchs):
    print k,',',v
'''

#help(re.sub)
'''
test="Hi,nice to meet you where are you from?"
matchssub = re.sub(r'\s', '-', test)
print matchssub

msub2 = re.sub(r'\s', '-', test, 2)
print msub2
'''

#help(re.split)
'''
testSplit="Hi, nice to meet you where are you from?"
print re.split(r'\s+', testSplit)

print re.split(r'\s+', testSplit, 2)
'''

#help(re.compile)
testCompile="Hi, nice to meet you where are you from?"
k=re.compile(r'\w*o\w*') #匹配带o的字符串
print dir(k)
print k.findall(testCompile)  #显示所有包涵o的字符串
# 将字符串中含有o的单词用[]括起来
print k.sub(lambda m: '[' + m.group(0) + ']', testCompile)

