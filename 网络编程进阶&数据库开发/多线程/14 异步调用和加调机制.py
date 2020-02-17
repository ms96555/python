# Author : Sky 
# @Time : 2/17/20 3:00 下午
# @Site : 
# @File : 14 异步调用和加调机制.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-


#提交任务的两种方式
# 1.同步调用：提交完任务后，就在原地等待任务执行完毕，拿到结果，再执行下一行代码，导致程序是串行执行
# from concurrent.futures import ThreadPoolExecutor
# import time
# import random
#
# def la(name):
#     print('%s is laing'%name)
#     time.sleep(random.randint(3,5))
#     res=random.randint(7,13)*'#'
#     return {'name':name,'res':res}
#
# def weigh(shit):
#     name=shit['name']
#     size=len(shit['res'])
#     print('%s 拉了 <%s> kg'%(name,size))
#
# if __name__ == '__main__':
#     pool=ThreadPoolExecutor(4)
#     shit1=pool.submit(la,'alex').result()  #这里是执行完要拿到结果 后面要跟 .result()
#     weigh(shit1)
#
#     shit2=pool.submit(la,'wupeiqi').result()
#     weigh(shit2)
#
#     shit3=pool.submit(la,'yuanhao').result()
#     weigh(shit3)

# 2. 异步调用：提交完任务后，不地等待任务执行完毕。

from concurrent.futures import ThreadPoolExecutor
import time
import random

def la(name):
    print('%s is laing'%name)
    time.sleep(random.randint(3,5))
    res=random.randint(7,13)*'#'
    return {'name':name,'res':res}

def weigh(shit):
    name=shit['name']
    size=len(shit['res'])
    print('%s 拉了 <%s> kg'%(name,size))

if __name__ == '__main__':
    pool=ThreadPoolExecutor(4)

    pool.submit(la,'alex')

    pool.submit(la,'wupeiqi')

    pool.submit(la,'yuanhao')