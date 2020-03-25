# Author : Sky 
# @Time : 2020/3/24 10:26
# @Site : 
# @File : main.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


from wsgiref.simple_server import make_server

def application(environ,start_response):

    start_response('200 OK',[('Content-Type','text/html')])
    print('PATH',environ.get('PATH_INFO')) # 打印当前的请求的路径
    path = environ.get('PATH_INFO')

    # 方案一
    # if path == '/favicon.ico':
    #     return [b'hello favicon.ico']
    #
    # return [b'<h1>hello ,web</h1>']

     # 方案二


    url_patterns=[
         ('/login',login),
         ('/index',index),
         ('/favicon.ico',fav)
     ]

httpd = make_server('',8080,application)   # 封装socket
print('Server HTTP on prot 8080')
#开始监听HTTP请求：
httpd.serve_forever()