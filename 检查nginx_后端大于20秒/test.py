# Author : Sky
# @Time : 2020/2/15 15:23
# @Site :
# @File : 检查大于20秒.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import redis
import json, sys, os
import time
import socket
import subprocess
import requests

hostName = socket.gethostname()
# uname = hostName.split(".")
uname = hostName.split(".")[0].split('ip-')[1].replace('-', '.')
r = redis.Redis(host=uname, port=6379, db=0, decode_responses=True)
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
    popen = subprocess.Popen('tail -f ' + '/opt/lnmp/nginx/logs/webUI_' + sys.argv[1] + "_greate_10" + ".log",
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = popen.pid
    print('Popen.pid:' + str(pid))
    while True:
        line = popen.stdout.readline().strip()
        if line:
            str_line = bytes.decode(line)
            dict_line = eval(str_line)
            uri = dict_line['uri']
            kn_uri = str(uri).split('/')[-1]
            if dict_line['upstream_response_time'] != '-' and kn_uri != "CheckLoginFirstStep" and kn_uri != "RegisterUser":
                new_list = dict_line['upstream_response_time'].split(',')

                print("**************")
                print('这个不走登录和注册')
                print("new_list:",new_list)
                print("dict_line:",dict_line)
                print('uri:',uri)
                print("kn_rui:",kn_uri)
                print("**************")
                try:
                    if len(new_list) >= 1:
                        new_addr = dict_line['upstream_addr'].split(',')
                        new_dict = dict(zip(new_addr, new_list))
                        print("--------------")
                        print("new_addr:",new_addr)
                        print("nwe_dict:",new_dict)
                        print("--------------")
                        for k, v in new_dict.items():
                            if float(v) > 50:
                                f = k + ',' + uri
                                obj.public(f)
                    elif float(new_list[0]) > 50:
                        obj.public(dict_line['upstream_addr'])
                except Exception as e:
                    print(e)
                    continue
            elif dict_line['upstream_response_time'] != '-' and kn_uri == "CheckLoginFirstStep" or kn_uri == "RegisterUser":
                new_list = dict_line['upstream_response_time'].split(',')
                try:
                    if len(new_list) >= 1:
                        new_addr = dict_line['upstream_addr'].split(',')
                        new_dict = dict(zip(new_addr, new_list))
                        print("+++++++++++++++")
                        print('111111111111111111111111111')
                        print("+++++++++++++++")
                        for k, v in new_dict.items():
                            if float(v) > 20:
                                f = k + ',' + uri
                                obj.public(f)
                    elif float(new_list[0]) > 20:
                        obj.public(dict_line['upstream_addr'])
                except Exception as e:
                    print(e)
                    continue




stat_logs(sys.argv[1])
