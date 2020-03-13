# Author : Sky 
# @Time : 2020/3/12 19:43
# @Site : 
# @File : Tcpdump抓包.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import datetime
import time
import sys, os
import psutil

os.system('pip install --upgrade pip')
os.system('pip install psutil')

net = sys.argv[1]
def tcpdump(net):
    count = 0
    while count < 10:
        now_time = datetime.datetime.now().strftime('%d日:%H:%M:%S')
        os.system("nohup tcpdump -i %s -w %s.cap &" %( net,now_time))
        time.sleep(1800)
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name() == 'tcpdump':
                print(pid,p.name())
                os.system("kill %s" % pid)
                os.system("mv *.cap /tmp/")
        count += 1
        continue

tcpdump(net)
exit()