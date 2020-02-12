# Author : Sky 
# @Time : 1/31/20 12:13 下午
# @Site : 
# @File : ssh连接服务端server.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import socket
import subprocess

#1 买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 第一个参数，套接字的类型， 第协议  ，意思是基于网强和的tcp通信的。

#2 绑定手机卡
phone.bind(('127.0.0.1',8081))   # 必须以元组形式传进来  第一个是IP  第二个是端口  0-1024是给操作系统使用的。


#3 开机
phone.listen(5)   #括号里面的数字，表示是最大挂起连接数。

#4 等电话连接
print('starting.....')
conn,client_addr = phone.accept()
print(client_addr)
# 收，发消息
while True:
    cmd = conn.recv(1024) #这里面的1024 代表最大接收1024个bytes
    print('接收到的数据是',cmd)
    conn.send(data.upper())

    obj = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    print('stdout>>>:', obj.stdout.read().decode('utf-8'))
    print('stderr>>>:', obj.stderr.read().decode('utf-8'))

# 挂电话
conn.close()

#关机

phone.close()

