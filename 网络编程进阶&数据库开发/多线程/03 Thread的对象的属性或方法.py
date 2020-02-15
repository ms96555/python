# Author : Sky 
# @Time : 2/15/20 9:34 下午
# @Site : 
# @File : 03 Thread的对象的属性或方法.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from threading import Thread,currentThread,active_count,enumerate
import os
import time


def task():
    print('%s is running'%currentThread().getName())
    time.sleep(2)
    print('%s is done '%currentThread().getName())

if __name__ == '__main__':
    t1 = Thread(target=task,name='子线程1')
    t1.start()
    # t1.setName('儿子线程1')
    #
    # print(t1.isAlive())   #检测线程是否成活

    # t1.join()

    # print('主线程',currentThread().getName())

    # print(active_count())   # 查看进程数量
    print(enumerate())  #查看进程数的对象，