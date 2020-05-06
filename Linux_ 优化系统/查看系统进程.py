# Author : Sky 
# @Time : 2020/4/28 14:18
# @Site : 
# @File : 查看系统进程.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import os,sys
import psutil
pids = psutil.pids()
pid_list = []
for pid in pids:
    p = psutil.Process(pid)
    # print(p)
    # print('pid-%s,pname-%s' % (pid, p.name()))
    if p.name() == 'crond':
        pid_list.append(pid)
if len(pid_list) >= 2:
    print(2)
    exit()
else:
    print(1)
    exit()



#     os.system('curl -s "https://api.telegram.org/bot943824825:AAG--vAsjbOY1HZUKwZ-tfAG6z7OliZrAG8/sendMessage?chat_id=-345686437&text="---------检测到两个系统进程-------""')
# else:
#     exit()