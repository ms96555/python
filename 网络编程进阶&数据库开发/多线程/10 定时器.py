# Author : Sky 
# @Time : 2/16/20 9:28 下午
# @Site : 
# @File : 10 定时器.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 1. 定时器
# from threading import Timer
#
# def task(name):
#     print('hello %s'%name)
#
# t = Timer(5,task,args=('sky',))
# t.start()

# 2.验证码
import random

def make_code(n=4):
    res = ''
    for i in range(n):
        s1 = str(random.randint(0,9))
        s2 = chr(random.randint(65,90))
        res+=random.choice([s1,s2])
    return res


