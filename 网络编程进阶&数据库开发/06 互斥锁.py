# Author : Sky 
# @Time : 2020/2/13 11:15
# @Site : 
# @File : 06 互斥锁.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from multiprocessing import Process,Lock
import time

def task(name,mutex):
    mutex.acquire()     #这里加锁
    print('%s 1'%name)
    time.sleep(1)
    print('%s 2'%name)
    time.sleep(1)
    print('%s 3'%name)
    mutex.release()        #运行完了把锁释放
if __name__ == '__main__':
    mutex=Lock()
    for i in range(3):
        p = Process(target=task,args=('进程%s'%i,mutex))
        p.start()
