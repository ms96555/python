# Author : Sky
# @Time : 2020/6/8 15:48
# @Site :
# @File : winds_filebeat.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import os, sys
import psutil
import time

pids = psutil.pids()
pid_list = []
for pid in pids:
    p = psutil.Process(pid)
    # print(p.name())
    print('pid-%s,pname-%s' % (pid, p.name()))
    if p.name() == 'filebeat.exe':
        print("这里是程序文件")
        process = ('taskkill -f /pid %s' % pid)
        os.system(process)

        print("杀死了filebeat进程")
time.sleep(3)
os.chdir('D:\elk')
os.system('run.bat')
