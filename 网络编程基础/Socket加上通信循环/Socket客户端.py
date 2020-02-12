# Author : Sky 
# @Time : 1/31/20 12:14 下午
# @Site : 
# @File : ssh连接客户端.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


import socket

# 1 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 第一个参数，套接字的类型， 第协议  ，意思是基于网强和的tcp通信的。

# 2 拨号
phone.connect(('127.0.0.1',8081))

# 3 发，收消息
while True:
    msg = input('>>>:').strip()
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data)

# 4.关闭

phone.close()