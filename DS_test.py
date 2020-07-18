# Author : Sky 
# @Time : 2020/5/23 16:54
# @Site : 
# @File : test5.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from pyDes import des, CBC, PAD_PKCS5
import binascii, datetime
import base64
import requests, json
import hashlib
import time

'''

lao bai, [11.06.20 16:21]
额度查询。额度转换。获取第三方游戏地址。


获取余额
命令: GET_BALANCE
请求参数:　
•　username: 合作伙伴平台的用户ID,字符串长度少于或者等于20位, 由字母和数字组成
•　password: 合作伙伴平台的用户新密码，要求ＭＤ５加密, 长度为32位

响应参数:　
•　request: 原请求
•　logId:  API日志ID
•　errorCode: 
○0:　没有错误，获取余额成功
○6001:  hashcode错误
○6002:  IP未授权
○6600:  Json参数格式错误
○6605:  无此用户
○6606:  用户存在，但密码错误
○6609:  用户名为空, 字符长度不正确, 格式不正确
○6610:  密码为空, 字符长度不正确, 格式不正确
○6656:  接口访问频率，不得低于3秒，如果同一位玩家获取余额间隔时间低于3秒的重复访问将返回此错误码
•　errorMessage:　如果错误代码为0,　errorMessage为空
•　params: 　
		balance:余额

'''

# 13711331327  aa123456
# 用户名密码
username = 'bb_122493'
password = '123888bbb'

# MD5 计算密码
md5_val = hashlib.md5(password.encode('utf8')).hexdigest()

# 第三方给个KEY
MD5KEY = 'ubet888_a5cfe97e-c238-4f58-9f0c-73bd'

# 唯一交易号,由合作伙伴平台提供,以备查验,长度范围为1到32位  例如 ds202006131107580296641
time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
ref = "ds" + time_now

# 定义ULR  POST  传数字典
CONFIG = {
    'url': 'http://dsapi.dsbet88.com/dsapi/app/api.do',
    'headers': {'Content-Type': 'application/json'}
}
url = CONFIG['url']
headers = CONFIG['headers']


def Login_game():
    pass


def Get_balance():
    #  查询余额请求URL
    '''
    http://dsapi.dsbet88.com/dsapi/app/api.do?{"params":{"username":"bb_122493","password":"3a150ca32e381b4ca83fd50298e0333f"},"hashCode":"ubet888_a5cfe97e-c238-4f58-9f0c-73bd","command":"GET_BALANCE"}

    '''
    ds = {'params':
        {
            'username': username,
            'password': md5_val,
        },
        'hashCode': MD5KEY,
        'command': "GET_BALANCE"
    }
    r = requests.post(url=url, data=json.dumps(ds), headers=headers)
    get_blance = r.text
    return get_blance


def Transfer_in():
    '''
    http://dsapi.dsbet88.com/dsapi/app/api.do?{"params":{"username":"bb_122493","password":"3a150ca32e381b4ca83fd50298e0333f","ref":"ds202006131107580296641","desc":"充值 1","amount":"1"},"hashCode":"ubet888_a5cfe97e-c238-4f58-9f0c-73bd","command":"DEPOSIT"}

    :return:
    '''


    ds = {'params':
        {
            'username': username,
            'password': md5_val,
            'ref': ref,
            'desc': '',
            'amount': '1'
        },
        'hashCode': MD5KEY,
        'command': "DEPOSIT"
    }
    r = requests.post(url=url, data=json.dumps(ds), headers=headers)
    get_blance = r.text
    return get_blance



def Transfer_out():
    '''
    http://dsapi.dsbet88.com/dsapi/app/api.do?{"params":{"username":"bb_122493","password":"3a150ca32e381b4ca83fd50298e0333f","ref":"ds202006131107580296641","desc":"充值 1","amount":"1"},"hashCode":"ubet888_a5cfe97e-c238-4f58-9f0c-73bd","command":"DEPOSIT"}

    :return:
    '''

    ds = {'params':
        {
            'username': username,
            'password': md5_val,
            'ref': ref,
            'desc': '',
            'amount': '1'
        },
        'hashCode': MD5KEY,
        'command': "WITHDRAW"
    }
    r = requests.post(url=url, data=json.dumps(ds), headers=headers)
    get_blance = r.text
    return get_blance




if __name__ == '__main__':
    print(Get_balance())
