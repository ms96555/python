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


    from urls import url_patterns

    func = None
    for item in url_patterns:
        if path == item[0]:
            func=item[1]
            break
    if func:
        return [func()]
    else:
        return [b'404']






httpd = make_server('',8080,application)   # 封装socket
print('Server HTTP on prot 8080')
#开始监听HTTP请求：
httpd.serve_forever()