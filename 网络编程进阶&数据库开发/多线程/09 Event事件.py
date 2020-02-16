# Author : Sky 
# @Time : 2/16/20 7:43 下午
# @Site : 
# @File : 09 Event事件.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 1.Event事件
# from threading import Thread,Event
# import time
#
# event= Event()
# # event.wait() 一直等着
# # event.set()  下发信号
#
# def student(name):
#     print('学生%s 正在听课'%name)
#     event.wait(3)   #wait 是可以设超时间的
#     print('学生%s 课间活动'%name)
#
# def teacher(name):
#     print('老师%s 正在授课'%name)
#     time.sleep(7)
#     event.set()
#
#
# if __name__ == '__main__':
#     stu1 = Thread(target=student, args=('alex',))
#     stu2 = Thread(target=student, args=('wxx',))
#     stu3 = Thread(target=student, args=('yxx',))
#     t1 = Thread(target=teacher, args=('sky', ))
#
#     stu1.start()
#     stu2.start()
#     stu3.start()
#     t1.start()

# 2.
from threading import Thread,Event,currentThread
import time

event= Event()
# event.wait() 一直等着
# event.set()  下发信号

def conn():
    n=0
    while not event.is_set():
        if n == 3:
            print('%s try too many times'%currentThread().getName())
            return
        print('%s try %s'%(currentThread().getName(),n))
        event.wait(0.5)
        n+=1
    print('%s is connected'%currentThread().getName())


def check():
    print('%s is checking'%currentThread().getName())
    time.sleep(5)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t=Thread(target=conn,)
        t.start()
    t=Thread(target=check,)
    t.start()