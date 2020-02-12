# Author : Sky 
# @Time : 2020/2/11 18:46
# @Site : 
# @File : 01 开启子进程的两种方式.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


# 方式一
# print('====>')
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running '%name)
#     time.sleep(3)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     p=Process(target=task,args=('子进程1',))
#     p.start()  # 仅仅只是给操作 系统发送一个信号
#
#     print('主')

#方式二
from multiprocessing import Process
import time
class myprocess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s is running '%self.name)
        time.sleep(3)
        print('%s is done'%self.name)
if __name__ == '__main__':
    p=myprocess('子进程1')
    p.start()

    print('主')

