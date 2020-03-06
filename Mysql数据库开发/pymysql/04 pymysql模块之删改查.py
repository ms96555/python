# Author : Sky 
# @Time : 2020/3/4 15:04
# @Site : 
# @File : 04 pymysql模块之删改查.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import pymysql

# 增删改

# # 建立链接
# conn = pymysql.connect(
#     host='10.10.15.51',
#     port=3306,
#     user='root',
#     password='123',
#     db='db10',
#     charset='utf8'
# )
# # 拿游标
# cursor=conn.cursor()
#
# # 执行SQL
# # 增、删、改
#
# sql = 'insert into userinfo(user,pwd) values(%s,%s)'
# #rows= cursor.execute(sql,('wxx','333'))   # 这种是插一条记录
# #print(rows)
#
# rows=cursor.executemany(sql,[('xiaoming','444'),('lishi','777'),('k1','admin')])   # 以列表的形式插入多条
# print(rows)
# conn.commit() # 提交修改内容
#
# # 关游标，关链接
# cursor.close()
# conn.close()


# 查

# 建立链接
conn = pymysql.connect(
    host='10.10.15.51',
    port=3306,
    user='root',
    password='123',
    db='db10',
    charset='utf8'
)
# 拿游标
cursor=conn.cursor(pymysql.cursors.DictCursor)

# 执行SQL
# 查询

# rows 只能看到影响行数
rows=cursor.execute('select * from userinfo;')
print(rows)

cursor.scroll(3,mode='absolute') #相对绝对位置移动
#cursor.scroll(3,mode='relative') #相对当前位置移动


print(cursor.fetchall())
print(cursor.fetchall())
conn.commit() # 提交修改内容

# 关游标，关链接
cursor.close()
conn.close()