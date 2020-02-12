# Author : Sky 
# @Time : 2020/2/12 11:49
# @Site : 
# @File : 01 练习题.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 这个例子告诉我们   进程进程之间是隔离的
from multiprocessing import Process
n = 100

def work():
    global n
    n =0
    print('子进程：',n)

if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    p.join()
    print('主进程',n)


