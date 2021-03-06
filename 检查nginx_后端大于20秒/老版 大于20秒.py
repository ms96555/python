# Author : Sky 
# @Time : 2020/2/15 15:37
# @Site : 
# @File : 监听nginx服务器大于20秒.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import redis
import json,sys,os
import time
import socket
import subprocess
hostName = socket.gethostname()
#uname = hostName.split(".")
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
print(uname)
# conn = redis.Redis(host="192.168.30.101", port=6379,password="youbottest!@#")
r = redis.Redis(host='172.31.36.33', port=6379,db=0,decode_responses=True)
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host="172.31.36.33", port=6379,db=0,decode_responses=True)
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub


obj = RedisHelper()
redis_sub = obj.subscribe()
node_id = []
while True:
    msg = redis_sub.parse_response()
    if msg:
        node_id.append(msg[2])
        tuple_list = list(set(node_id))
        for i in tuple_list:
            if uname == i.split(':')[0] and r.exists(i) != 1:
                #os.system('/scripts/politeness_docker.sh' +" " + i.split(':')[1] + " " + i.split(':')[0] + " " + 'cu')
                r.set(i,'1',ex=60,nx=True)
        node_id = []