# Author : Sky 
# @Time : 2020/2/12 14:44
# @Site : 
# @File : 服务端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    conn,addr = server.accept()

