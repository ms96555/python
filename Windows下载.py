# Author : Sky 
# @Time : 9/30/20 3:24 下午
# @Site : 
# @File : Windows下载.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
# from ftplib import FTP
#
# ftp = FTP()
# timeout = 100
# port = 21
# ftp.connect('13.230.125.116', port, timeout)  # 连接FTP服务器
# ftp.login('ftp001', 'QWE123qwe')  # 登录
# # ftp.cwd('file/test')  # 设置FTP路径
# list = ftp.nlst()  # 获得目录列表
# for name in list:
#     print(name)  # 打印文件名字
# # path = 'd:/data/' + name  # 文件保存路径
# # f = open(path, 'wb')  # 打开要保存文件
# # filename = 'RETR ' + name  # 保存FTP文件
# # ftp.retrbinary(filename, f.write)  # 保存FTP上的文件
# # ftp.delete(name)  # 删除FTP文件
# # ftp.storbinary('STOR ' + filename, open(path, 'rb'))  # 上传FTP文件
# ftp.quit()  # 退出FTP服务器
#

str1='''
{\x22id\x22:null,\x22retCode\x22:\x22fail\x22,\x22retMsg\x22:\x22IP\xE7\x99\xBD\xE5\x90\x8D\xE5\x8D\x95\xE9\x99\x90\xE5\x88\xB6(CloudPayApi)_61.158.134.216\x22,\x22data\x22:null,\x22sign\x22:null}
'''
print(str1.encode('raw_unicode_escape').decode('utf-8'))