# Author : Sky 
# @Time : 2020/5/23 16:54
# @Site : 
# @File : test5.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from pyDes import des, CBC, PAD_PKCS5
import binascii
import base64
import requests, json
import hashlib
import time

timestamp = int(round(time.time() * 1000))

# 请求头
headers = {
    'User-Agent': 'WEB_LIB_GI_M49_AGIN'
}

# 平台标示
cagent = "M49_AGIN"
# 操作类型
s = 1
# 会员帐号

loginname = "bb_122493"

# 查询余额常量
method = "gb"

# 代表真假钱帐号 1 是直实用户 0 是试玩
actype = 1

#  password 这里的密码理论是后台一样的
password = '123888bbb'

# cur=CNY  币种

cur = 'CNY'

# KEY 密钥文件
DESKEY = 'iJTZb06o'

MD5KEY = 'xIWeLnnp7mDs'

# 加密方式   params=des.encrypt(“cagent=XXXXXXXXX/\\\\/loginname=XXXXXX/\\\\/method=lg/\\\\/actype=0/\\\\/password=XXXXXXXX/\\\\/oddtype=XXX/\\\\/cur=XXX”)


# param 的值
# param = str(
#     'cagent=' + cagent + '/\\\\\\\/' +
#     'loginname=' + loginname + '/\\\\\\\/' +
#     'method=' + method + '/\\\\\\\/' +
#     'actype=' + str(actype) + '/\\\\\\\/' +
#     'password=' + password + '/\\\\\\\/' +
#     'cur=' + cur)
# url = 'http://gi.gameagzrsx.com:81/doBusiness.do'
param = str(
    'cagent=' + cagent + '/\\\\/' +
    'loginname=' + loginname + '/\\\\/' +
    'method=' + method + '/\\\\/' +
    'actype=' + str(actype) + '/\\\\/' +
    'password=' + password + '/\\\\/' +
    'cur=' + cur)
url = 'http://gi.gameagzrsx.com:81/doBusiness.do'

# print(param)


# Encrypt.DESEncrypt(param,DESKey);
def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = DESKEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


# KEY 的值
string = str(param + MD5KEY)
md5_val = hashlib.md5(string.encode('utf8')).hexdigest()

if __name__ == '__main__':
    print(param)
    str_txt = param
    e = des_encrypt(str_txt)  # 加密
    # print("加密:", e)

    ag = {'param': e, 'key': md5_val}
    r = requests.get(url, params=ag, headers=headers)
    print(r)
    print(ag)
    print(r.url)
    print(r.text)
