# Author : Sky 
# @Time : 2/16/20 5:52 下午
# @Site : 
# @File : 08 信号量.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from threading import Thread, Semaphore, currentThread
import time, random

sm = Semaphore(3)


def task():
    # print('%s in '%currentThread().getName())
    # sm.acquire()
    with sm:
        print('%s in ' % currentThread().getName())
        time.sleep(random.randint(1,3))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()



