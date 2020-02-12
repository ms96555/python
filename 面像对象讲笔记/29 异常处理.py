# Author : Sky
# @Time : 1/25/20 3:06 下午
# @Site :
# @File : 29 异常处理.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# 一：错误一般分两钟
# 语法错误：在程序执行前就要立刻改正过来
# print('sk fk s'

# 二：逻辑错误

# 3 . 异常
# 强调一： 错误发生的条件如果是可以预知的，此时应该用if判断去预防异常
# AGE = 10
# age = input('>>: ').strip()
# # 这样如输入的是数字是没有问题，如果输入是字符串就会报错，针对这样，可以加一个if判断。如下
# if age.isdigit():
#     age = int(age)
#     if age > AGE:
#         print('太大了')

# 强调二：如果错误发生条件是不可预知的，此时应该用异常机制， try ......except
# 打印一个文件的时候不知道它会有几行，超过这个文件内容的时候就会报错。此时加try 如下
# try:
#     f = open('29_a.txt','r',encoding='utf-8')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     f.close()
# except StopIteration:   #这样我们把这个异常传入 后面的就不会终止。
#     print('出错了')
#
# print('======>1')
# print('======>2')
# print('======>3')

