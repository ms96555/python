# Author : Sky 
# @Time : 2/20/20 7:33 下午
# @Site : 
# @File : 18 gevent模块.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# # 这个可以监测IO 自动切换
# import gevent
# import time
#
# # 如果说 换成 time.sleep(3)  ，那程序就不会说切换到别一个操作，这里就要用到下面的方法如下
# from gevent import monkey;monkey.patch_all()    # 这个要加在所有程序开头，这个方法会把阻塞IO换成非阻塞切换到另一个线程。
#
#
# def eat(name):
#     print('%s eat 1'%name)
#     gevent.sleep(3)
#     print('%s eat 2'%name)
#
#
# def play(name):
#     print('%s play 1'%name)
#     gevent.sleep(4)
#     print('%s play 2'%name)
# start_time=time.time()
# g1=gevent.spawn(eat,'sky')
# g2=gevent.spawn(play,'xiaoming')
#
#
# g1.join()
# g2.join()
# stop_time=time.time()
# print(stop_time-start_time)


# 这个可以监测IO 自动切换
import gevent
import time
from gevent import monkey

monkey.patch_all()


def eat(name):
    print('%s eat 1' % name)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(4)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'sky')
g2 = gevent.spawn(play, 'xiaoming')

# time.sleep(5) # 这种方法虽然可以但是不能这样用也不确定程序多少秒

# g1.join()
# g2.join()  # 也可以说用join 等两个join 完了和序自动结速

gevent.joinall([g1,g2]) # 也可以说用  gevent模块里面有一个joinall 里面加一个列表，等同于上面一个方法




