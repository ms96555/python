# Author : Sky 
# @Time : 2/16/20 5:27 下午
# @Site : 
# @File : 07 死锁与递归锁.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 1. 死锁
# from threading import Thread,Lock
# import time
# mutexA=Lock()
# mutexB=Lock()
#
# class mythread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print('%s 拿到了A锁'%self.name)
#
#         mutexB.acquire()
#         print('%s 拿到了B锁'%self.name)
#         mutexB.release()
#
#         mutexA.release()
#     def f2(self):
#         mutexB.acquire()
#         print('%s 拿到了B锁'%self.name)
#
#         time.sleep(0.2)
#
#         mutexA.acquire()
#         print('%s 拿到了A锁'%self.name)
#         mutexB.release()
#
#         mutexB.release()
# if __name__ == '__main__':
#     for i in range(10):
#         t=mythread()
#         t.start()


# 2. 递归锁  Rlock 可以连续acquire多次， 每acquire一次计数器加1，只要计数为0时，才能被抢到acquire。
from threading import Thread,RLock
import time
mutexB=mutexA=RLock()


class mythread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁'%self.name)

        mutexB.acquire()
        print('%s 拿到了B锁'%self.name)
        mutexB.release()

        mutexA.release()
    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁'%self.name)

        time.sleep(8)

        mutexA.acquire()
        print('%s 拿到了A锁'%self.name)
        mutexB.release()

        mutexB.release()
if __name__ == '__main__':
    for i in range(10):
        t=mythread()
        t.start()