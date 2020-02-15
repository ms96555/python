# Author : Sky 
# @Time : 2020/2/13 14:14
# @Site : 
# @File : 08 互斥锁与join的区别.py
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
    else:
        print('%s 购票失败'%name)
def task(name):
    searche(name)
    # mutex.acquire()
    get(name)
    # mutex.release()

if __name__ == '__main__':
    # mutex = Lock()
    for i in range(10):
        p = Process(target=task,args=('路人%s'%i,))
        p.start()
        p.join()

