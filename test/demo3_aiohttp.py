#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: demo3_aiohttp.py
@time: 2017/5/4 15:52
"""

import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.5)
    headers = []
    header = ("content_type", "text/html")
    headers.append(header)
    text = '<h1>hello,%s</h1>' % request.match_info['name']
    # headers "{} takes either dict or list of (key, value) "
    # return web.Response(body=text.encode('UTF-8'), headers={"content_type": "text/html"},content_type='text/html')
    return web.Response(body=text.encode('UTF-8'), headers=headers, content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
