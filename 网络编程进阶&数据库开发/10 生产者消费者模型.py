# Author : Sky 
# @Time : 2020/2/13 14:31
# @Site : 
# @File : 10 生产者消费者模型.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
# import time
# def producer():
#     for i in range(3):
#         res = '包子%s'%i
#         time.sleep(2)
#         print('生产者生产了%s'%res)
#
#         consumer(res)
#
# def consumer(res):
#     time.sleep(1)
#     print('消费者吃了%s'%res)
#
# producer()

from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(4):
        res = '包子%s' % i
        time.sleep(2)
        print('生产者生产了%s' % res)

        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        if res == None: break
        time.sleep(0.2)
        print('消费者吃了%s' % res)


if __name__ == '__main__':
    # 容器
    q = Queue()
    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p1.start()

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c1.start()

    p1.join()
    q.put(None)
    print('主')
