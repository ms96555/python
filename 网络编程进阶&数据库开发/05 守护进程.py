# Author : Sky 
# @Time : 2020/2/12 17:14
# @Site : 
# @File : 05 守护进程.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# from multiprocessing import  Process
# import time
#
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#
# if __name__ == '__main__':
#     p = Process(target=task,args=('子进程1',))
#     p.daemon=True     #守护进程
#     p.start()
#
#     print('主')



# 练习题

from multiprocessing import  Process
import time

def foo():
    print('123')
    time.sleep(1)
    print('end 123')

def bar():
    print('456')
    time.sleep(3)
    print(' end 123')

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print(' main.........')