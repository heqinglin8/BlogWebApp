#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: app.py
@time: 2017/5/4 20:41
"""

import asyncio
import logging
from aiohttp import web
import www.config_default as config_default
import www.orm as orm
from www.User import User


# from www import User


async def index(request):
    text = '<h1>home</h1>'
    return web.Response(body=text.encode('UTF-8'), content_type='text/html')

async def setdata():
    user = User(id=3, name='Michael')
    await user.save()
    print(await User.findAll())

async def init(loop):
    configs = config_default.configs
    # 创建数据库连接池
    await orm.create_pool(loop=loop, **configs)
    await setdata()
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    print('server started at http://127.0.0.1:9000...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
