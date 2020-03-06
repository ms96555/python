# Author : Sky 
# @Time : 2020/3/4 11:44
# @Site : 
# @File : 01 连接mysql.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

'''
1,先创建远程用户
下面这条命令是创建远程用户加授权
 grant all on *.* to 'root'@'%' identified by '123';

flush privileges; #刷新一下
'''