# Author : Sky
# @Time : 2020/7/20 17:23
# @Site :
# @File : 真人转帐失败报警.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import redis
import json, sys, os
import time, datetime
import socket
import subprocess
import threading

hostName = socket.gethostname()
# uname = hostName.split(".")
uname = hostName.split(".")[0].split('ip-')[1].replace('-', '.')
r = redis.Redis(host=uname, port=6379, db=0, decode_responses=True)
cmd = 'ps -fe | grep tail | grep -v "grep"'
a = os.popen(cmd)  # 返回一个对象
txt = a.readlines()
now_tiem = datetime.datetime.now().strftime('%Y%m%d')
if len(txt) != 0:
    for lin in txt:
        lin_ = lin.split()
        pid = lin_[1]
        cmd = 'kill -9 %d' % (int(pid))
        rc = os.system(cmd)


def stat_logs():
    # bad_list = []
    # ip_list = []
    # local_time = time.time()
    popen = subprocess.Popen('tail -f ' + '/opt/logs/live_game_api_91/Logs/TraceLog' + now_tiem + '_1.txt',
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        line = popen.stdout.readline().strip()
        if line:
            str_line = bytes.decode(line)
            json_data = json.loads(str_line)
            status = str(json_data['CONTENT'])
            log = str(json_data['LOG']).split('(')[0]
            print('容器1_____日志类型', log)
            T1 = uname
            T2 = 'live_game_api_91'

            if log == '转账接口调用失败' and status.split('->')[-1].split('","')[1][-1] == '0':
                print("********调用转帐接口失败")
                GAME_TYPE = json_data['GAME_TYPE']
                ORDER_NO_LIVE = json_data['ORDER_NO_LIVE']
                os.system(
                    '/opt/zabbix_server/agentd-shell/live_transfer.sh' + " " + T1 + " " + T2 + " " + ORDER_NO_LIVE + " " +
                    status.split('->')[-1].split('","')[1][-1] + " " + GAME_TYPE)
def live_2():
    # bad_list = []
    # ip_list = []
    # local_time = time.time()
    popen = subprocess.Popen('tail -f ' + '/opt/logs/live_game_api_92/Logs/TraceLog' + now_tiem + '_1.txt',
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        line = popen.stdout.readline().strip()
        if line:
            str_line = bytes.decode(line)
            json_data = json.loads(str_line)
            status = str(json_data['CONTENT'])
            log = str(json_data['LOG']).split('(')[0]
            print('容器2_____日志类型', log)
            T1 = uname
            T2 = 'live_game_api_92'

            if log == '转账接口调用失败' and status.split('->')[-1].split('","')[1][-1] == '0':
                print("********调用转帐接口失败")
                GAME_TYPE = json_data['GAME_TYPE']
                ORDER_NO_LIVE = json_data['ORDER_NO_LIVE']
                os.system(
                    '/opt/zabbix_server/agentd-shell/live_transfer.sh' + " " + T1 + " " + T2 + " " + ORDER_NO_LIVE + " " +
                    status.split('->')[-1].split('","')[1][-1] + " " + GAME_TYPE)
def live_3():
    # bad_list = []
    # ip_list = []
    # local_time = time.time()
    popen = subprocess.Popen('tail -f ' + '/opt/logs/live_game_api_93/Logs/TraceLog' + now_tiem + '_1.txt',
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        line = popen.stdout.readline().strip()
        if line:
            str_line = bytes.decode(line)
            json_data = json.loads(str_line)
            status = str(json_data['CONTENT'])
            log = str(json_data['LOG']).split('(')[0]
            print('容器3_____日志类型', log)
            T1 = uname
            T2 = 'live_game_api_93'

            if log == '转账接口调用失败' and status.split('->')[-1].split('","')[1][-1] == '0':
                print("********调用转帐接口失败")
                GAME_TYPE = json_data['GAME_TYPE']
                ORDER_NO_LIVE = json_data['ORDER_NO_LIVE']
                os.system(
                    '/opt/zabbix_server/agentd-shell/live_transfer.sh' + " " + T1 + " " + T2 + " " + ORDER_NO_LIVE + " " +
                    status.split('->')[-1].split('","')[1][-1] + " " + GAME_TYPE)
def live_4():
    # bad_list = []
    # ip_list = []
    # local_time = time.time()
    popen = subprocess.Popen('tail -f ' + '/opt/logs/live_game_api_94/Logs/TraceLog' + now_tiem + '_1.txt',
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        line = popen.stdout.readline().strip()
        if line:
            str_line = bytes.decode(line)
            json_data = json.loads(str_line)
            status = str(json_data['CONTENT'])
            log = str(json_data['LOG']).split('(')[0]
            print('容器4_____日志类型', log)
            T1 = uname
            T2 = 'live_game_api_94'

            if log == '转账接口调用失败' and status.split('->')[-1].split('","')[1][-1] == '0':
                print("********调用转帐接口失败")
                GAME_TYPE = json_data['GAME_TYPE']
                ORDER_NO_LIVE = json_data['ORDER_NO_LIVE']
                os.system(
                    '/opt/zabbix_server/agentd-shell/live_transfer.sh' + " " + T1 + " " + T2 + " " + ORDER_NO_LIVE + " " +
                    status.split('->')[-1].split('","')[1][-1] + " " + GAME_TYPE)



if __name__ == '__main__':
    # 使用threading模块，threading.Thread()创建线程，其中target参数值为需要调用的方法，同样将其他多个线程放在一个列表中，遍历这个列表就能同时执行里面的函数了
    threads = [threading.Thread(target=stat_logs),threading.Thread(target=live_4),threading.Thread(target=live_3),threading.Thread(target=live_2)]
    for t in threads:
        # 启动线程
        t.start()


