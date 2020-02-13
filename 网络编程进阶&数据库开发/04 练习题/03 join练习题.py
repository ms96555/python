# Author : Sky 
# @Time : 2020/2/12 16:08
# @Site : 
# @File : 03 join练习题.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time
import random


def talk(n):
    time.sleep(random.randint(1, 3))
    print('----------------%s' % n)


if __name__ == '__main__':
    p1 = Process(target=talk, args=(1,))
    p2 = Process(target=talk, args=(2,))
    p3 = Process(target=talk, args=(3,))

    p1.start()
    p2.start()
    p3.start()

    print('--------------->4')
