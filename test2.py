# Author : laobai
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
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
redis_ip = '172.31.41.93'
r = redis.Redis(host=redis_ip, port=6379,db=0,decode_responses=True)
class RedisHelper:
    def __init__(self):
        self.__conn = r
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
            print( i.split(':')[0])
            if uname == i.split(':')[0] and r.exists(i) != 1:
                os.system('/opt/zabbix_server/agentd-shell/politeness_docker.sh' +" " + i.split(':')[1] + " " + i.split(':')[0] + " " + 'de')
                r.set(i,'1',ex=60,nx=True)
        node_id = []
