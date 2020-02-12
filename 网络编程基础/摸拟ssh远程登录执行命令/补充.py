# Author : Sky 
# @Time : 1/31/20 8:15 下午
# @Site : 
# @File : 补充.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 执行系统命令
import os

# os.system('ls /')
# res=os.system('ls /')
# print('返回的结果是：',res)   #这里的=0 代=表的是命令执行的成功于否

# 之前学到的模块
import subprocess

obj = subprocess.Popen('xxxxx/', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
print(obj)
print('stdout>>>:',obj.stdout.read().decode('utf-8'))
print('stderr>>>:',obj.stderr.read().decode('utf-8'))