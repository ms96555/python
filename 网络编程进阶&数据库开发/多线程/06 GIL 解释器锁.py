# Author : Sky 
# @Time : 2/16/20 4:19 下午
# @Site : 
# @File : 06 GIL 解释器锁.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 1. 对于纯计算密集型的，我们要用进程方式，这样会快
# from multiprocessing import Process
# from threading import Thread
# import os,time
#
# def work():
#     res = 0
#     for i in range(100000000):
#         res *= i
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count()) # 本机cpu核心数
#     start=time.time()
#     for i in range(4):
#         # p = Process(target=work)  #这里是进程 效率 大约9秒多
#         p = Thread(target=work,)   # 这里是线程 效率 大约17秒
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop= time.time()
#     print('run time is %s'%(stop - start))

# 2. IO密集型，用多线程

from multiprocessing import Process
from threading import Thread
import os,time

def work():
    time.sleep(2)
if __name__ == '__main__':
    l = []
    # print(os.cpu_count()) # 本机cpu核心数
    start=time.time()
    for i in range(400):
        # p = Process(target=work)  #这里是进程 效率 大约2.8秒多
        p = Thread(target=work,)   # 这里是线程 效率 大约2.04秒多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop= time.time()
    print('run time is %s'%(stop - start))