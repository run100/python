#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2016/3/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

# 1 6,11,18,20 * * * /usr/local/bin/python /root/health.py >> /root/health.log

import time
import sys
import os
import sys

# 邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def run(cmd):
        p = os.popen(cmd)
        text = p.read()
        p.close()
        return text

def send_email(msg):
        from_addr = "zzw2006372@163.com"
        password = "zzw@163.com"
        smtp_server = "smtp.163.com"
        smtp_port = "25"
        to_addr = "727271755@qq.com"

        msg = MIMEText(msg, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'定时器 <%s>' % from_addr)
        msg['To'] = _format_addr(u'忠旺同学 <%s>' % to_addr)
        msg['Subject'] = Header(u'运动，饮食控制不要吃多，多思考', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

msg = '运动，饮食控制不要吃多，多思考'

send_email(msg);
