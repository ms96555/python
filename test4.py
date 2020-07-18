# Author : Sky 
# @Time : 2020/5/23 16:34
# @Site : 
# @File : test4.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import time

timestamp = int(round(time.time() * 1000))
# print(type(timestamp))
import hashlib

MD5KEY = '9F39A0436A5F48EF'

# 平台标示
agent = 50035

# 操作类型
s = 1
# 会员帐号
account = "bb_195070"

string = str( str(agent) + str(timestamp) + MD5KEY)
# print(string)


def string_to_md5(string):
    md5_val = hashlib.md5(string.encode('utf8')).hexdigest()
    return md5_val

print(string_to_md5(string))




string1 = str( str(agent) + MD5KEY)
# print(string)

md5_val = hashlib.md5(string1.encode('utf8')).hexdigest()
print(md5_val)
