# Author : Sky 
# @Time : 2020/2/5 15:24
# @Site : 
# @File : test.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

cc = '1'
zabbix_site = 'ac'
zabbix_listen_ip = '10.0.0.1'
if zabbix_site == 'ac':
    msg_api = '''filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
setup.template.settings:
  index.number_of_shards: 3
setup.kibana:
processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/messages
  fields:
    %s: messages                                     
    fields_under_root: true
  tags: ["syslog"]
- type: log
  enabled: true
  paths:
    - /opt/logs/%s/Logs/20200209/*.txt                  
    - /opt/logs/%s_2/Logs/20200209/*.txt
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}'
  multiline.negate: true
  multiline.match: after
  fields:
    %s: %s
    fields_under_root: true
  tags: ["applog"]
output.redis:
  hosts: ["172.31.3.15"]
  port: "17788"
  key: "*"
  password: APPLE!@#++--123''' % (
    cc, cc, cc, cc, cc)
    if zabbix_listen_ip :
        if cc :
            msg_zabbix = '''import redis
import json,sys,os
import time
import socket
import subprocess
hostName = socket.gethostname()
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
redis_ip = %s
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
                os.system('/opt/zabbix_server/agentd-shell/politeness_docker.sh' +" " + i.split(':')[1] + " " + i.split(':')[0] + " " + %s)
                r.set(i,'1',ex=60,nx=True)
        node_id = []''' % (zabbix_listen_ip, zabbix_site)

print(msg_api)