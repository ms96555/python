# Author : Sky 
# @Time : 2/20/20 10:26 下午
# @Site : 
# @File : 并发版本服务端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from socket import *
from threading import Thread

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

def communicate(conn):
    while True:
        try:
            data = server.recv(1024)
            if not data: break
            server.send(data.upper())

        except ConnectionError:
            break
    conn.close()

while True:
    print('starting.....')
    conn,addr = server.accept()
    print(addr)

    t = Thread(target=communicate,args=(conn,))
    t.start()

server.close()
