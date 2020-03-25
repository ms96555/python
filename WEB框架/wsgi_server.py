# Author : Sky 
# @Time : 2020/3/22 11:23
# @Site : 
# @File : wsgi_server.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ,start_response):
    # 按着http协议解析数据：environ
    # 按着http协议组装数据：start_response
    # print(environ)
    # print(type(environ))

    path = environ.get('PATH_INFO')    #当前的请求路径

    start_response('200 OK',[])  # 响应状态码

    if path == '/login':
        with open('login.html','r',encoding='utf-8') as f :
            data = f.read()
            return [data.encode('utf-8')]
    elif path == '/index':
        with open('D:\python\WEB框架\index.html','r',encoding='utf-8')  as f :
            data = f.read()
            return [data.encode('utf-8')]

httped= make_server("",8060,application) #封装socket

httped.serve_forever() #  等待用户连接


