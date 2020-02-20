# Author : Sky 
# @Time : 2/17/20 1:20 下午
# @Site : 
# @File : 客户端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from socket import *
from threading import Thread,currentThread


def more_client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8091))

    while True:
        client.send(('%s hello'%currentThread().getName()).encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))

    client.close()
# if __name__ == '__main__':
#     for i in range(500):
#         t = Thread(target=more_client)
#         t.start()

if __name__ == '__main__':
    t = Thread(target=more_client)
    t.start()