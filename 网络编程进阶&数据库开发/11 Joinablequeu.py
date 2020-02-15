# Author : Sky 
# @Time : 2020/2/13 16:23
# @Site : 
# @File : 11 Joinablequeu.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from multiprocessing import Process, JoinableQueue
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
    q = JoinableQueue()
    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p1.start()

    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c1.start()

    p1.join()
    q.put(None)
    print('主')
