# Author : Sky 
# @Time : 2/1/20 12:43 下午
# @Site : 
# @File : 粘包客户端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import socket
import time

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',9004))

client.send('hello'.encode('utf-8'))
time.sleep(5)
client.send('word'.encode('utf-8'))
