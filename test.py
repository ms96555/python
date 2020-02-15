# Author : Sky 
# @Time : 2020/2/5 15:24
# @Site : 
# @File : test.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
zabbix_site = 'ac'
zabbix_listen_ip = '10.0.0.1'
if zabbix_site == 'ac':
    msg_zabbix = '''import redis
     import json, sys, os
     import time
     import socket
     import subprocess
     

     uname = %s
     r = redis.Redis(host=uname, port=6379, db=0, decode_responses=True)


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
                 if uname == i.split(':')[0] and r.exists(i) != 1:
                     os.system('/scripts/politeness_docker.sh' + " " + i.split(':')[1] + " " + i.split(':')[0] + " " + %s)
                     r.set(i, '1', ex=60, nx=True)
             node_id = []
     ''' % (zabbix_listen_ip, zabbix_site)

import redis
import json,sys,os
import time
import socket
import subprocess
hostName = socket.gethostname()
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
redis_ip = '172.31.36.33'
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
                os.system('/opt/zabbix_server/agentd-shell/politeness_docker.sh' +" " + i.split(':')[1] + " " + i.split(':')[0] + " " + 'cu')
                r.set(i,'1',ex=60,nx=True)
        node_id = []