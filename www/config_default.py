#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin(Administrator)
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: config_default.py
@time: 2017/5/5 10:36
"""
__author__ = 'heqinglin'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'admin',
        'db_name': 'blog'
    },
    'session': {
        'secret': 'Blog'
    },
    'maxsize':10,
    'minsize':1
}
