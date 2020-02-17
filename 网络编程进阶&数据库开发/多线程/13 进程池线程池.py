# Author : Sky 
# @Time : 2/17/20 2:14 下午
# @Site : 
# @File : 13 进程池线程池.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 1 . 进程池
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import os,time,random
#
# def task(name):
#     print('name:%s pid:%s run'%(name,os.getpid()))
#     time.sleep(random.randint(1,3))
#
# if __name__ == '__main__':
#     pool= ProcessPoolExecutor(4)
#     for i in range(10):
#         pool.submit(task,'sky%s'%i)
#
#     pool.shutdown(wait=True)  # 这里 想当于join 就是等上面全部执行完了，才会打印下面的 print('主')
#
#     print('主')


# 2. 线程池
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, time, random
from threading import currentThread

def task():
    print('name:%s pid:%s run' % (currentThread().getName(), os.getpid()))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(4)
    for i in range(10):
        pool.submit(task,)

    pool.shutdown(wait=True)  # 这里 想当于join 就是等上面全部执行完了，才会打印下面的 print('主')

    print('主')