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

while True:
    print('starting.......')
    conn,addr = server.accept()
    print(addr)

    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionError:
            break
    conn.close()

server.close()