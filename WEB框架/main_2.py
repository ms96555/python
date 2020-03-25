# Author : Sky 
# @Time : 2020/3/25 10:10
# @Site : 
# @File : main_2.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    path = environ.get('PATH_INFO')


httpd = make_server('',8090,application)
print('Server HTTP on prot 8080')

httpd.serve_forever()