# Author : Sky 
# @Time : 2020/2/13 13:15
# @Site : 
# @File : 07 模拟抢票.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from multiprocessing import Process,Lock
import json
import time
def searche(name):
    time.sleep(1)
    dic = json.load(open('db.txt','r',encoding='utf-8'))
    print('<%s> 剩于的票数%s'%(name,dic['count']))

def get(name):
    time.sleep(1)
    dic = json.load(open('db.txt','r',encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(3)
        json.dump(dic,open('db.txt','w',encoding='utf-8'))
        print('<%s> 购票成功'%name)
def task(name,mutex):
    searche(name)
    mutex.acquire()
    get(name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = Process(target=task,args=('路人%s'%i,mutex))
        p.start()

