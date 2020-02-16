# Author : Sky 
# @Time : 2/16/20 2:10 下午
# @Site : 
# @File : 04 守护线程.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 1.一个进程内没有开启非守护
# from threading import Thread
# import time
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello'%name)
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi,args=('sky',))
#
#     t.setDaemon(True)    #这是一种方式还有一种
#     # t.daemon=True      #这是别一种开启守护
#
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())


# 2.
from threading import Thread
import time

def foo():
    print(123)
    time.sleep(2)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    t1 = Thread(target=foo,)
    t2 = Thread(target=bar,)
    t1.daemon=True
    t1.start()
    t2.start()
    print('main.......')