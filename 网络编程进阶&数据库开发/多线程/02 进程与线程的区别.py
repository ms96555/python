# Author : Sky 
# @Time : 2020/2/15 13:13
# @Site : 
# @File : 02 进程与线程的区别.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 1 . 开进程的开销远大于线程
# import time
# from threading import Thread
# from multiprocessing import Process
#
# def piao(name):
#     print('%s piaoing'%name)
#     time.sleep(2)
#


# 瞅一瞅PID
from multiprocessing import Process
from threading import Thread
import os

def task():
    # 进程
    # print('子进程PID%s  父进程的PID%s'%(os.getpid(),os.getppid()))

    # 线程
    print('子线程PID：%s'%os.getpid())



if __name__ == '__main__':
    # 进和
    # p1=Process(target=task,)
    # p1.start()

    # 线程
    t1 = Thread(target=task,)
    t1.start()
    print('主线程',os.getpid())