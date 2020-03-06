# Author : Sky 
# @Time : 2020/3/4 14:51
# @Site : 
# @File : SQL 注入问题.py
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

# sql = 'select * from userinfo where user= "%s" and pwd="%s"' % (user, pwd)

# 这种方法， 前面不传值 后面传值，过滤掉非法字符
sql = 'select * from userinfo where user= %s and pwd=%s'
rows = cursor.execute(sql,(user,pwd))


# 4 关闭游标，关闭连接

cursor.close()

conn.close()

# 5 进行判读
if rows:
    print('登录成功')
else:
    print('登录失败')


#  (知道用户名的情况)在输入用户名密码的时候   sky" --xxxx  这样直接登录了,
#  sky" --xxx 这里的 -- 就是后面的都注释不查只查前面的


# （不知道用户名的情况）xxxx" or 1=1 -- shf as
'''
user>>: xxxx" or 1=1 -- shf as
password>>: asdf
select * from userinfo where user= "xxxx" or 1=1 -- shf as" and pwd="asdf"
登录成功
'''