#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'run'
__mtime__ = '15/12/26'
"""

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


# 输入Email地址和口令:
#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
# 输入SMTP服务器地址:
#smtp_server = raw_input('SMTP server: ')
# 输入收件人地址:
#to_addr = raw_input('To: ')

from_addr = "727271755@qq.com"
password = "1987@163.com"
smtp_server = "smtp.qq.com"
to_addr = "727271755@qq.com"


import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
