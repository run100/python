#! /usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

import smtplib

from_addr = 'zzw2006372@163.com'
to_addr = '727271755@qq.com'
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是2
server.set_debuglevel(1)
server.login(from_addr, 'zzw20063721')
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

print 'success'
