#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin(Administrator)
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: User.py
@time: 2017/5/5 14:49
"""
__author__ = 'heqinglin'

from www.orm import Model, StringField, IntegerField

class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()