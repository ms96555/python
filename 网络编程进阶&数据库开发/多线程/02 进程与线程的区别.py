# Author : Sky 
# @Time : 2020/2/15 13:13
# @Site : 
# @File : 02 进程与线程的区别.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 1 . 开进程的开销远大于线程
import time
from threading import Thread
from multiprocessing import Process

def piao(name):
    print('%s piaoing'%name)
    time.sleep(2)