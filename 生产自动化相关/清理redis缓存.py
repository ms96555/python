# Author : Sky 
# @Time : 2/20/20 2:02 下午
# @Site : 
# @File : 清理redis缓存.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import redis
import socket

hostname = socket.gethostname()
host = hostname.split(".")[0].split('ip-')[1].replace('-','.')
r =redis.Redis(host=host,port=6379,db=0,decode_responses=True)
list=r.keys('web_au*')
for key in list:
    print(key)