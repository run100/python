#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2015/12/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

class Animal(object):
    def run(self):
        print('animal is runing')


class Dog(Animal):
    def run(self):
        print('dog is runing')

class Cat(Animal):
    def run(self):
        print('cat is runing')


dog = Dog()
dog.run()

a = list()
print(isinstance(a, list))
print(isinstance(dog, Animal))

print(type(a))
print(type(dog))