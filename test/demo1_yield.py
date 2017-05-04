#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: demo1_yield.py
@time: 2017/5/4 13:40
"""


def h():
    print('Wen Chuan')
    m = yield 5  # Fighting!
    print(m)
    d = yield 12
    print('We are together!', d)
    yield 18


c = h()
print('out:', next(c))  # 相当于c.send(None)
print('out:', c.send('Fighting!'))  # (yield 5)表达式被赋予了'Fighting!'


def getlistNum(n):
    for i in range(n):
        yield i * 2


f = getlistNum(8)
for num in f:
    print(num)

f1 = (x * 2 for x in range(8))
for num in f1:
    print(num)
