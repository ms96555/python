# Author : Sky 
# @Time : 2/17/20 1:20 下午
# @Site : 
# @File : 服务端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from socket import *
from gevent import monkey,spawn
monkey.patch_all()


def communicate(conn):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionRefusedError:
            break
    conn.close()

def server(ip,port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        spawn(communicate,conn)
    server.close()

if __name__ == '__main__':
    g=spawn(server,'127.0.0.1',8091)
    g.join()