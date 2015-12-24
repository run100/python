#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '处理图片'
__author__ = 'Administrator'
__mtime__ = '2015/12/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


from PIL import Image


im = Image.open('img.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('img2.jpg', 'JPEG')

