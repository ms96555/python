# Author : Sky 
# @Time : 2020/2/15 11:05
# @Site : 
# @File : 01 开启线程的两种方式.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 第一种起线程方式
# import time
# import random
# from threading import Thread
#
# def piao(name):
#     print('%s piaoing'%name)
#     time.sleep(random.randrange(1,5))
#     print('%s piao end '% name)
#
# if __name__ == '__main__':
#     t1 = Thread(target=piao,args=('egon',))
#     t1.start()
#     print('主')

#第二种方式
import time
import random
from threading import Thread

class mythread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s piaoing '%self.name)

        time.sleep(random.randrange(1,5))
        print('%s piao end'%self.name)

if __name__ == '__main__':
    t1 =mythread('sky')

    t1.start()

    print('主')
