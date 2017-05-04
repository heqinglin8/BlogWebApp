#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: hello.py
@time: 2017/5/2 16:37
"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, web! my first blog web </h1> <BR/> <h4>welcome! %s</h4>' % (environ['PATH_INFO'][1:])
    print('environ:',environ)
    return [body.encode('UTF-8')]
