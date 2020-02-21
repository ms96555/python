# Author : Sky 
# @Time : 2/20/20 10:09 下午
# @Site : 
# @File : 服务端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from socket import *

server = socket(AF_INET,SOCK_STREAM)

server.bind(('127.0.0.1',8080))

server.listen(5)

server.setblocking(False)   # 换成非阻塞
print('starting.......')

rlist=[]

while True:
    try:
        conn,addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        # print('干其它的活')
        pass
server.close()