#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time, MySQLdb

#import MySQLdb.cursors

conn = MySQLdb.connect(host="192.168.148.132", user="root", passwd="", db="test")
print(conn)

cursor = conn.cursor()
print(cursor)

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

print "Database version : %s " % data

# 创建表
# sql = "create table  user(id int(4) not null primary key auto_increment,name varchar(128) not null, created int(10))"
# cursor.execute(sql)

# # 写入
# try:
#     sql = "insert into user(name,created) values(%s, %d)"
#     param = ("aaa",int(time().time))
#     n = cursor.execute(sql)
#     conn.commit()
#     print('insert',n)
# except:
#     conn.rollback()
#
# # 更新
# try:
#     sql = "UPDATE user SET name=%s where id=7"
#     param = ("cc")
#     n = cursor.execute(sql, param)
#     conn.commit()
# except:
#     conn.rollback()

# cursor.execute("SELECT * FROM documents")
# for row in cursor.fetchall():
#     print(row)


sql = "SELECT * FROM user where id>%d" % (7)

try:
    cursor.execute(sql)
    rs = cursor.fetchone()
    for row in rs:
        print(row)
except:
    print "Error: unable to fecth data"

cursor.close()
conn.close()