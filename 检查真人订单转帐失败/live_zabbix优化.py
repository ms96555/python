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
uname = hostName.split(".")[0].split('ip-')[1].replace('-', '.')
# r = redis.Redis(host=uname, port=6379, db=0, decode_responses=True)
live_pid = os.getpid()
cmd = 'ps -fe | grep tail | grep -v "grep"'
a = os.popen(cmd)
txt = a.readlines()
now_tiem = datetime.datetime.now().strftime('%Y%m%d')
if len(txt) != 0:
    for lin in txt:
        lin_ = lin.split()
        pid = lin_[1]
        cmd = 'kill -9 %d' % (int(pid))
        print('准备结束tail:', cmd)
        rc = os.system(cmd)
a.close()
live_zabbix = 'ps -fe | grep live_zabbix.py | grep -v "grep"'
b = os.popen(live_zabbix)
txt1 = b.readlines()
print(txt1)
if len(txt1) != 0:
    for lin in txt1:
        lin_ = lin.split()
        pid = lin_[1]
        print('live_zabbix_pid:', live_pid)
        print(pid)
        print('pid类型', type(pid))
        print('live_pido类型', type(live_pid))
        if int(pid) != live_pid:
            cmd1 = 'kill -9 %d' % (int(pid))
            print('准备结束live_zabbix', cmd1)
            rc = os.system(cmd1)
        else:
            continue
b.close()

file = 'TraceLog' + now_tiem + '_1.txt'


def live_1(args):
    path = '/opt/logs/live_game_api_' + args + '/Logs/'

    os.chdir(path)

    # print(os.getcwd())

    while True:
        if os.path.exists(file):
            print('------:文件存在')
            break
        else:
            print('------文件不存在等待50秒再试')
            time.sleep(60)
    cc = 'popen' + args
    cc = subprocess.Popen(
        'tail -f ' + '/opt/logs/live_game_api_' + args + '/Logs/TraceLog' + now_tiem + '_1.txt',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        line = cc.stdout.readline().strip()
        if line:
            str_line = line.decode('utf-8-sig')
            json_data = json.loads(str_line)
            status = str(json_data['CONTENT'])
            log = str(json_data['LOG']).split('(')[0]
            # print('容器1_____日志类型', log)
            T1 = uname
            T2 = 'live_game_api_' + args
            # print(args, ':---T2:', T2)

            if log == '转账接口调用失败' and status.split('->')[-1].split('","')[1][-1] == '2':
                print("********调用转帐接口失败")
                GAME_TYPE = json_data['GAME_TYPE']
                ORDER_NO_LIVE = json_data['ORDER_NO_LIVE']
                ACCOUNT = json_data['ACCOUNT']
                CREATE_DTT = str(json_data['CREATE_DTT'])
                CREATE_DTT = CREATE_DTT.replace(' ', '-')
                os.system(
                    '/opt/zabbix_server/agentd-shell/live_transfer.sh' + " " + T1 + " " + T2 + " " + ORDER_NO_LIVE + " " +
                    status.split('->')[-1].split('","')[1][
                        -1] + " " + GAME_TYPE + " " + ACCOUNT + " " + CREATE_DTT)


if __name__ == '__main__':
    threads = [threading.Thread(target=live_1, args=("91",)), threading.Thread(target=live_1, args=("92",)),
               threading.Thread(target=live_1, args=("93",)),
               threading.Thread(target=live_1, args=("94",))]
    for t in threads:
        t.start()
