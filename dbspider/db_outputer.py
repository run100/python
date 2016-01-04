#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/28'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import MySQLdb
import time
import sys
import global1

reload(sys)
sys.setdefaultencoding('utf-8')


class Outputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, condata):
        if condata is None:
            return None

        #self.datas.append(condata)


    def insert_mysql(self, data):

        conn = MySQLdb.connect(host=global1.MYSQL_HOST
                       , user=global1.MYSQL_USER
                       , passwd=global1.MYSQL_PASSWD
                       , db=global1.MYSQL_DB
                       , charset=global1.MYSQL_CHARSET)
        cursor = conn.cursor()

        try:
            #for data in self.datas:
            sql = "INSERT INTO douban_movies(title, url, average, summary)"
            sql = sql + " VALUES(%s, %s, %s, %s) "
            #print(sql)
            param = (data['title'].encode('utf-8')
                     , data['url']
                     , data['average']
                     , data['summary'].encode('utf-8')
                    )
            #print(param)
            n = cursor.execute(sql, param)
            print("insert tbl_movies is %d" % n)
            conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.rollback()



    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        #acsii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
