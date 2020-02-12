# Author : Sky 
# @Time : 2020/2/11 20:15
# @Site : 
# @File : 03 Process对象的其它的属性或方法.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
#
# join方法
# from multiprocessing import Process
# import time,os
#
# def task(name):
#     print('%s is running ,parnet id is <%s> '%(os.getpid(),os.getppid()))
#     time.sleep(3)
#     print('%s is done,parent id is <%s>'%(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#     p=Process(target=task,args=('子进程1',))
#     p.start()  # 仅仅只是给操作 系统发送一个信号
#
#     p.join()
#     print('主',os.getpid(),os.getppid())
#     print(p.pid)


# 程序并发执行
# from multiprocessing import Process
# import time,os
#
# def task(name,n):
#     print('%s is running  '%name)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start = time.time()
#     p1=Process(target=task,args=('子进程1',5))
#     p2=Process(target=task,args=('子进程2',3))
#     p3=Process(target=task,args=('子进程3',2))
#     p_list = [p1,p2,p3]
#     for i in p_list:
#         i.start()
#     for j in p_list:
#         j.join()
#
#     # p1.start()
#     # p2.start()
#     # p3.start()
#     # p1.join()
#     # p2.join()
#     # p3.join()
#     print('主',(time.time() - start))


# 串行执行
# from multiprocessing import Process
# import time,os
#
# def task(name,n):
#     print('%s is running  '%name)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start = time.time()
#     p1=Process(target=task,args=('子进程1',5))
#     p2=Process(target=task,args=('子进程2',3))
#     p3=Process(target=task,args=('子进程3',2))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     print('主',(time.time() - start))


# 了解知识点   print(p.is_alive()) ：判断这个进程是否死掉
# from multiprocessing import Process
# import time, os
# def task(name):
#     print('%s is running ,parnet id is <%s> ' % (os.getpid(), os.getppid()))
#     time.sleep(3)
#     print('%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))
# if __name__ == '__main__':
#     p = Process(target=task, args=('子进程1',))
#     p.start()
#     print(p.is_alive())   # 判断这个进程是否死掉
#     p.join()
#     print('主', os.getpid(), os.getppid())
#     print(p.pid)
#     print(p.is_alive())


from multiprocessing import Process
import time, os
def task(name):
    print('%s is running ,parnet id is <%s> ' % (os.getpid(), os.getppid()))
    time.sleep(3)
    print('%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))
if __name__ == '__main__':
    p = Process(target=task,)
    p.start()
    p.terminate()   #杀死进程
    time.sleep(3)
    print(p.is_alive())
    print('主')