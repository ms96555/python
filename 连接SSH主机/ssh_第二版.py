# Author : Sky
# @Time : 2020/4/24 19:08
# @Site :
# @File : ssh_第二版.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

import os, sys
import hashlib
import time
import paramiko

Server_ip = {
    'HK': "10.0.0.103",
    'TEST': "10.0.0.102"
}
path_dir = os.getcwd()

str1 = "======准备上传文件"
str2 = "======上传完成"
str3 = "======准备删除文件"
str4 = "======删除成功"


def Connect(item):
    os.chdir(path_dir)
    pkey1 = paramiko.RSAKey.from_private_key_file('id_rsa')
    # print(item)
    # 建立连接
    # 判读服务器
    for i in Server_ip.items():
        if i[0] == item.split('-')[0].upper():
            cmd = i[1]
            # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            trans = paramiko.Transport((cmd, 22))
            trans.connect(username='root', pkey=pkey1)
            # 将sshclient的对象的transport指定为以上的trans
            ssh = paramiko.SSHClient()
            ssh._transport = trans
            # 实例化一个 sftp对象,指定连接的通道
            sftp = paramiko.SFTPClient.from_transport(trans)
            # 发送文件
            if i[0] == 'HK':
                sftp.put(localpath='D:/home/%s' % item, remotepath='/etc/nginx/html/%s' % item.split('-')[0] + '.rar')
                # 列出Linux目录中的文件，以便检查是否传送成功
                print('上传完成！' + 'home' + ' 下有如下文件：')
                # lscmd = 'ls -l ' + '/home/'
                lscmd = 'md5sum ' + '/etc/nginx/html/%s' % item.split('-')[0] + '.rar'
                stdin, stdout, stderr = ssh.exec_command(lscmd)
                # 计算远和计算机的MD5值
                arr = str(stdout.read().decode('utf-8')).strip().split()
                # 进行对比
                md5_l = hashlib.md5()
                with open("D:/home/%s" % item, mode="rb") as f:
                    by = f.read()
                md5_l.update(by)
                ret = md5_l.hexdigest()
                # print(arr)
                if arr[0] != ret:
                    count = 1
                    while count <= 3:
                        print('文件传输过程中数据不一致， 准备第%s次上传' % count)
                        sftp.put(localpath='D:/home/%s' % item,
                                 remotepath='/etc/nginx/html/%s' % item.split('-')[0] + '.rar')
                        print('上传完成！' + 'home' + ' 下有如下文件：')
                        # lscmd = 'ls -l ' + '/home/'
                        lscmd = 'md5sum ' + '/etc/nginx/html/%s' % item.split('-')[0] + '.rar'
                        stdin, stdout, stderr = ssh.exec_command(lscmd)
                        # 计算远和计算机的MD5值
                        arr = str(stdout.read().decode('utf-8')).strip().split()
                        # 进行对比
                        md5_l = hashlib.md5()
                        with open("D:/home/%s" % item, mode="rb") as f:
                            by = f.read()
                        md5_l.update(by)
                        ret = md5_l.hexdigest()
                        count += 1
                    if count == 3:
                        os.system(
                            'curl -s "https://api.telegram.org/bot680232824:AAFF-5HNgrgc33JG1TdtjAdSwIDhNtW47VE/sendMessage?chat_id=-287988350&text="---54.222.184.206---上传到"HK"服务器3次传输不完整请,请手动检查""')
                else:
                    print('远端MD5 : ', arr[0])
                    print('本地MD5 : ', ret)
                filePath = '/etc/nginx/html/%s' % item.split('-')[0] + '.rar'
                rar_x = 'rar ' + 'x ' + filePath + ' -y'
                rar_x = 'cd /etc/nginx/html/ ;' + rar_x
                stdin, stdout, stderr = ssh.exec_command(rar_x)
                stdout.read()
                stdin, stdout, stderr = ssh.exec_command("rm -rf " + filePath)
                stdout.read()
                ssh.close()
                # delete_File(item)

                print('----------------------------------------------------')
            elif i[0] == 'TEST':
                sftp.put(localpath='D:/home/%s' % item,
                         remotepath='/opt/lnmp/nginx/html/%s' % item.split('-')[0] + '.rar')
                # 列出Linux目录中的文件，以便检查是否传送成功
                print('上传完成！' + '/opt/lnmp/nginx/html/' + ' 下有如下文件：')
                # lscmd = 'ls -l ' + '/home/'
                lscmd = 'md5sum ' + '/opt/lnmp/nginx/html/%s' % item.split('-')[0] + '.rar'
                stdin, stdout, stderr = ssh.exec_command(lscmd)
                # 计算远和计算机的MD5值
                arr = str(stdout.read().decode('utf-8')).strip().split()
                # 进行对比
                md5_l = hashlib.md5()
                with open("D:/home/%s" % item, mode="rb") as f:
                    by = f.read()
                md5_l.update(by)
                ret = md5_l.hexdigest()
                # print(arr)
                if arr[0] != ret:
                    count = 1
                    while count <= 3:
                        print('文件传输过程中数据不一致， 准备第%s次上传' % count)
                        sftp.put(localpath='D:/home/%s' % item,
                                 remotepath='/opt/lnmp/nginx/html/%s' % item.split('-')[0] + '.rar')
                        # 列出Linux目录中的文件，以便检查是否传送成功
                        print('上传完成！' + '/opt/lnmp/nginx/html/' + ' 下有如下文件：')
                        # lscmd = 'ls -l ' + '/home/'
                        lscmd = 'md5sum ' + '/opt/lnmp/nginx/html/%s' % item.split('-')[0] + '.rar'
                        stdin, stdout, stderr = ssh.exec_command(lscmd)
                        # 计算远和计算机的MD5值
                        arr = str(stdout.read().decode('utf-8')).strip().split()
                        # 进行对比
                        md5_l = hashlib.md5()
                        with open("D:/home/%s" % item, mode="rb") as f:
                            by = f.read()
                        md5_l.update(by)
                        ret = md5_l.hexdigest()
                        count += 1
                    if count == 3:
                        os.system(
                            'curl -s "https://api.telegram.org/bot680232824:AAFF-5HNgrgc33JG1TdtjAdSwIDhNtW47VE/sendMessage?chat_id=-287988350&text="---54.222.184.206---上传到"TEST"服务器3次传输不完整请,请手动检查""')

                else:
                    print('远端MD5 : ', arr[0])
                    print('本地MD5 : ', ret)
                filePath = '/opt/lnmp/nginx/html/%s' % item.split('-')[0] + '.rar'
                rar_x = 'rar ' + 'x ' + filePath + ' -y'
                rar_x = 'cd /opt/lnmp/nginx/html/ ;' + rar_x
                stdin, stdout, stderr = ssh.exec_command(rar_x)
                stdout.read()
                stdin, stdout, stderr = ssh.exec_command("rm -rf " + filePath)
                stdout.read()
                ssh.close()
                # delete_File(item)


def Run(path):
    item_list = []
    os.chdir(path)
    content = os.listdir(os.curdir)
    print(content)
    if len(content) == 0:
        print('内容为空')
        exit()
    elif len(content) > 2:
        print('里面的包大于两个请检查版本包------》要发到小飞机')
        os.system(
            'curl -s "https://api.telegram.org/bot680232824:AAFF-5HNgrgc33JG1TdtjAdSwIDhNtW47VE/sendMessage?chat_id=-287988350&text="---54.222.184.206---国内北京这台服务器上传的版本包超过限制制""')
        exit()
    # print(content[0])
    for item in content:
        head_name = item.split('-')[0].upper()
        # print(head_name)
        if head_name == 'HK' or 'TEST':
            print("-----正在检查上传的文件是否正确-----")
            old_filesize = -1
            diff_success = 0;
            while True:
                filesize = get_Filesize(path, item)
                if old_filesize == -1:
                    old_filesize = filesize;
                    continue
                if filesize != old_filesize:
                    print("发现" + item + "文件不同：" + str(old_filesize) + "===>" + str(filesize))
                    old_filesize = filesize
                    diff_success = 0;
                else:
                    diff_success = diff_success + 1
                    print("发现" + item + "相同：第" + str(diff_success) + "次")
                if diff_success == 5:
                    break;
                time.sleep(3)

        else:
            print('----上传的版本包不是正确的命名规则--------》发小飞机')
            os.system(
                'curl -s "https://api.telegram.org/bot680232824:AAFF-5HNgrgc33JG1TdtjAdSwIDhNtW47VE/sendMessage?chat_id=-287988350&text="---54.222.184.206---国内北京这台服务器上传的版本包不是正确的命名规则,请手动检查""')
            continue
        item_list.append(item)
    return item_list


def get_Filesize(path, filename):
    os.chdir(path)
    # content = os.listdir(os.curdir)
    time_list = []
    fsize = os.path.getsize(path + filename)
    # for item in content:
    #     file_name = path + item
    #     fsize = os.path.getsize(file_name)
    #     # fsize = fsize / float(1024*1024)
    #     # fsize = round(fsize,2)
    #     time_list.append(fsize)
    return fsize
    # print("%s---文件大小：%sMB" %(item,fsize))


def delete_File(item):
    # 删除原文件
    print(str3)
    if os.path.exists('D:/home/%s' % item):
        os.remove('D:/home/%s' % item)
        print(str4)


if __name__ == "__main__":
    print(path_dir)
    os.chdir(path_dir)
    if os.path.exists("lock"):
        print("检测到有未执行完成任务")
        exit()
    os.makedirs("lock")
    # 先比对上传的文件大小是否完整，10秒检查一次
    # get_Filesize("D:/home/")
    # print()
    for item in Run("D:/home/"):
        print(item)
        Connect(item)

    os.chdir(path_dir)
    os.rmdir("lock")
