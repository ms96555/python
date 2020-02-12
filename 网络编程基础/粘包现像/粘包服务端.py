# Author : Sky 
# @Time : 2/1/20 12:39 下午
# @Site : 
# @File : 粘包服务端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9004))
server.listen(5)

conn, addr = server.accept()

rec1 = conn.recv(1024)
print('第一次', rec1)

rec2 = conn.recv(1024)
print('第二次', rec2)
