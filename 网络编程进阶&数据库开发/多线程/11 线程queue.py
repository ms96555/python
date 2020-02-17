# Author : Sky 
# @Time : 2/17/20 11:49 上午
# @Site : 
# @File : 11 线程queue.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import queue

# q=queue.Queue(3)    # 先进先出  --》队列
# q.put('first')
# q.put(2)
# q.put('thiird')
#
# print(q.get())

# q= queue.LifoQueue(3)  #后进先也  --》堆栈
# q.put('first')
# q.put(2)
# q.put('third')
#
# print(q.get())
# print(q.get())
# print(q.get())

q=queue.PriorityQueue(3)  # 优先级队列 --》

q.put((10,'first'))
q.put((40,'tow'))
q.put((30,'three'))

print(q.get())
print(q.get())
print(q.get())

