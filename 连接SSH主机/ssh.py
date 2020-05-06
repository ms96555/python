# Author : Sky 
# @Time : 2020/4/23 12:28
# @Site : 
# @File : ssh.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import paramiko
import sys, os

# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
# pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa',password='')
pkey1 = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

# 多命令执行
# def Myssh():
#     cmd = input("要执行的命令->>:").strip()
#     return cmd

# 建立连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.0.0.102',
            port=22,
            username='root',
            pkey=pkey1
            )
# 执行命令，
stdint,stdout,stderr = ssh.exec_command('cd /home/h5ftp/ ;ls')

# cmd = Myssh()
# stdint,stdout,stderr = ssh.exec_command(cmd)
content = stdout.read().decode()
# print(content)
# 将文件转成数组
arr=str(content).strip().split('\n')

# 当文件为空的时候直接退出程序
if content.strip()=='':
    ssh.close()

# 当大于两个的时候报错退出程序
if len(arr) >2 :
    stdint,stdout,stderr = ssh.exec_command('curl -s "https://api.telegram.org/bot680232824:AAFF-5HNgrgc33JG1TdtjAdSwIDhNtW47VE/sendMessage?chat_id=-287988350&text="18.163.239.198，这台服务器里面有两个RAR包，请手动更新查验""')
    ssh.close()
# print(arr)
for item in arr:
    # print(item)
    a= item.upper()
    # print(item)
    head_name = a.split('-')[0]
    # print(head_name)
    if  head_name == 'HK':
        ssh.close()
        cmd = "scp root@10.0.0.102:/home/h5ftp/%s /home/" % (item)
        os.system(cmd)


# 关闭连接

ssh.close()


