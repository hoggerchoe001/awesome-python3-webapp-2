#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
async web application.
'''
#logging的作用 输出信息 logging.basicConfig 输出信息的等级 INFO表示普通 
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')#返回等号后的信息作为响应

async def init(loop):
    #将web对象加入消息循环，生成一个支持异步IO的对象
    app = web.Application(loop=loop)
    #将浏览器通过GET方式传过来的对根目录的请求转发给index函数处理
    app.router.add_route('GET', '/', index)
    #异步坚挺127.0.0.1得值得9000端口
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    #把监听http请求的写成返回给loop，从而持续监听http请求
    return srv
#loop的作用暂时不明确
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
