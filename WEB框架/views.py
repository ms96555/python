# Author : Sky 
# @Time : 2020/3/26 9:25
# @Site : 
# @File : views.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

def login(environ):
    with open('templates\login.html','rb') as f:
        data = f.read()
    return data

def index(environ):
    with open('templates\index.html','rb') as f:
        data = f.read()
    return data
def reg(environ):
    with open('templates\reg.html','rb') as f:
        data = f.read()
    return data

def timer(environ):
    import datetime
    now=datetime.datetime.now().strftime("%y-%m-%d %X")
    return now.encode('utf-8')