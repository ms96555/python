# Author : Sky 
# @Time : 2/20/20 3:13 下午
# @Site : 
# @File : 17 greenlet模块.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 注意点， 无法在遇到IO 时切换。

from greenlet import greenlet

def eat(name):
    print('%s eat 1'%name)
    g2.switch('xiaohei')
    print('%s eat 2'%name)
    g2.switch()

def play(name):
    print('%s play 1'%name)
    g1.switch()
    print('%s play 2'%name)

g1=greenlet(eat)
g2=greenlet(play)

g1.switch('sky')