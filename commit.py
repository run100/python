#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/1/19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import os
import re
import time
import sys


def main():

    # 取add后的文件
    l1 = run('/usr/local/bin/git diff --cached --name-only HEAD').splitlines()
    if (len(l1) == 0):
        exit(0)

    # 取  之前commit后，本次没有add的文件
    l2 = run('/usr/local/bin/git diff --name-only').splitlines()
    l3 = list(set(l1).intersection(set(l2)))

    if ( len(l3) > 0):
        print "\n"
        print "以下文件在git add后又有修改, 请重新add到暂存区后再提交"
        print "\n".join(l3)
        print "\n"
        exit(1)


    # 解析文件
    ret = parse_diff(l1)
    print(ret)

    #不可更改的文件，检查
    ban_check(ret)

    #php,yml,xml 语法检查
    syntax_check(ret)




def ban_check(lists):
    ret = lists

    if( is_super() ):
        return

    if( len(ret) == 0 ):
        return

    print "\n警告: 以下代码不允许修改。"
    print "\n"
    print "\n".join(ret['ban_files'])
    print "\n"
    exit(1)


def is_super():
    users = ['persist8']
    user_name = run('/usr/local/bin/git config --get user.name')
    return user_name in users


def run(cmd):
    p = os.popen(cmd)
    text = p.read()
    p.close()
    return text.strip()


def parse_diff(files):
    # 返回 对象{}
    ret = {}

    if(len(files) == 0):
        return ret

    # 取php文件
    ret['php_files'] = filter(filter_php, files)
    ret['php_files'].sort()
    ret['yml_files'] = filter(filter_yml, files)
    ret['yml_files'].sort()
    ret['xml_files'] = filter(filter_xml, files)
    ret['xml_files'].sort()

    ret['danger_files'] = filter(filter_danger, files)
    ret['danger_files'].sort()

    ret['ban_files'] = filter(filter_ban, files)
    ret['ban_files'].sort()

    return ret



def filter_php(file):
    return re.search(r'php$', file)

def filter_yml(file):
    return re.search(r'yml$', file)

def filter_xml(file):
    return re.search(r'xml$', file)

def filter_danger(file):
    return re.search(r'(^plugins/)|(^config/)|(^bin/)|(^lib/)|(/cron/)', file) \
        and not re.search(r'^lib/model', file) \
        or re.search(r'^lib/model/(news|user|common)', file) \
        or re.search(r'^apps/www/templates/', file) \
        or re.search(r'/(config|data)/', file) \
        or re.search(r'^web/[^/]+[.]php$', file);

def filter_ban(file):
    return re.search(r'(^symfony-stable/)|(^utils/)|(^pear/)|(^openads/)', file)


def syntax_check(lists):
    ret = lists

    # 验证php语法
    i = 0
    while( i<len(ret['php_files'])):
        file = ret['php_files'][i]
        i = i+1

        # 非文件，继续执行
        if not os.path.isfile(file):
            continue

        #利用php -l 查看语法
        p = os.popen("/usr/local/bin/git show :'%s'|php -l 2>&1" % file)
        err = p.read()
        if (p.close() != None):
            print "\n警告: PHP语法错误!不允许提交!"
            print file
            print "\n"
            print err
            exit(1)




main()
