# Author : Sky 
# @Time : 2020/2/11 19:15
# @Site : 
# @File : 02 查看进程的pid 和ppid.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

#方式一
print('====>')
from multiprocessing import Process
import time,os

def task(name):
    print('%s is running ,parnet id is <%s> '%(os.getpid(),os.getppid()))
    time.sleep(3)
    print('%s is done,parent id is <%s>'%(os.getpid(),os.getppid()))

if __name__ == '__main__':
    p=Process(target=task,args=('子进程1',))
    p.start()  # 仅仅只是给操作 系统发送一个信号

    print('主',os.getpid(),os.getppid())

