# Author : Sky
# @Time : 9/1/20 3:34 下午
# @Site :
# @File : 20200901-test.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import redis
import json,sys,os
import time
import socket
import subprocess
import requests
hostName = socket.gethostname()
#uname = hostName.split(".")
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
r = redis.Redis(host=uname, port=6379,db=0,decode_responses=True)
cmd = 'ps -fe | grep tail | grep -v "grep"'
a = os.popen(cmd)  # 返回一个对象
txt = a.readlines()
if len(txt) != 0:
    for lin in txt:
        lin_ = lin.split()
        pid = lin_[1]
        cmd = 'kill -9 %d' % (int(pid))
        rc = os.system(cmd)
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

def stat_logs(*args):
    bad_list = []
    ip_list = []
    local_time = time.time()
    popen = subprocess.Popen('tail -f ' + '/opt/lnmp/nginx/logs/webUI_'+sys.argv[1]+"_greate_10"+".log", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = popen.pid
    print('Popen.pid:' + str(pid))
    while True:
        line = popen.stdout.readline().strip()
        if line:
            str_line = bytes.decode(line)
            dict_line = eval(str_line)
            #print(dict_line)
            if dict_line['upstream_response_time'] != '-':
                new_list = dict_line['upstream_response_time'].split(',')
                # print(new_list)
                # print(int(float(new_list[0])))
                try:
                    if len(new_list) > 1:
                        new_addr = dict_line['upstream_addr'].split(',')
                        new_dict = dict(zip(new_addr,new_list))
                        print(new_list)
                        for k,v in new_dict.items():
                            if float(v) > 50:
                                obj.public(k)
                                time.sleep(50)
                                continue
                    elif float(new_list[0]) > 50:
                        obj.public(dict_line['upstream_addr'])
                        time.sleep(50)
                        continue
                except Exception as e:
                    print(e)
                    continue
stat_logs(sys.argv[1])
