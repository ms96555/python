# Author : Sky 
# @Time : 2020/2/13 14:22
# @Site : 
# @File : 09 队列的使用.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from multiprocessing import Queue
q = Queue(3)
q.put('hello')
q.put({'a':1})
q.put([3,3,3])
print(q.full())

print(q.get())
print(q.get())
print(q.get())

print(q.empty())  # 队列清空，
print(q.get())
