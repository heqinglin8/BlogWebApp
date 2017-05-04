#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: server.py
@time: 2017/5/2 16:50
"""
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我编写的函数application:
from test.hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 8080, application)
print('Serving HTTP on port 8080...')
# 一直监听这http请求
httpd.serve_forever()
