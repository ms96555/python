# Author : Sky 
# @Time : 2/17/20 1:20 下午
# @Site : 
# @File : 客户端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from socket import *

client=socket(AF_INET,SOCK_STREAM)

client.connect(('127.0.0.1',8080))

while True:
    msg = input('>>: ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data =client.recv(1024)
    print(data.decode('utf-8'))

client.close()