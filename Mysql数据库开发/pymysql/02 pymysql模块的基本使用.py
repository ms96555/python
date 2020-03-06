# Author : Sky 
# @Time : 2020/3/4 11:49
# @Site : 
# @File : 02 pymysql模块的基本使用.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# pip3 install pymysql

import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 1 建立链接
conn = pymysql.connect(
    host='10.10.15.51',
    port=3306,
    user='root',
    password='123',
    db='db10',
    charset='utf8'
)

# 2 拿到游标
cursor = conn.cursor()

# 3 执行sql语句

sql = 'select * from userinfo where user= "%s" and pwd="%s"' % (user, pwd)

rows = cursor.execute(sql)


# 4 关闭游标，关闭连接

cursor.close()

conn.close()

# 5 进行判读
if rows:
    print('登录成功')
else:
    print('登录失败')


