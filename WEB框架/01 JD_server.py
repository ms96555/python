# Author : Sky 
# @Time : 2020/3/16 13:44
# @Site : 
# @File : 01 JD_server.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import socket
sock=socket.socket()
sock.bind(('127.0.0.1',8800))
sock.listen(5)

while True:
    print('server waiting......')
    conn,addr=sock.accept()
    data=conn.recv(1024)
    print('data',data)
    # 读取html文件
    with open('login.html','rb') as f :
        data= f.read()
    conn.send((b"HTTP/1.1 200 OK\r\n\r\n%s"%data))
    conn.close()




