# Author : Sky
# @Time : 2/16/20 2:45 下午
# @Site : 
# @File : 05 互斥锁.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from threading import Thread,Lock
import time
n = 100

def task():
    global n
    mutex.acquire()
    tmep= n
    time.sleep(0.1)
    n=tmep -1
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    t_l =[]
    for i in range(100):
        t=Thread(target=task,)
        t_l.append(t)
        t.start()
    for t in t_l :
        t.join()

    print('主',n)