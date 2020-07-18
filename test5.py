# Author : Sky 
# @Time : 2020/5/23 16:54
# @Site : 
# @File : test5.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import base64
import requests, json
import hashlib
import time

timestamp = int(round(time.time() * 1000))
print(timestamp)
# 平台标示
agent = 50035

# 操作类型
s = 1
# 会员帐号
# account = "bb_195070"
account = "bb_122493"
# KEY 密钥文件
DESKEY = '56A168B84F35B70E'
MD5KEY = '9F39A0436A5F48EF'

# param 的值
param = str('s=' + str(s) + '&' + 'account=' + account)
url = 'https://api.ky012.com:189/channelHandle'


# Encrypt.AESEncrypt(param,DESKey);
def aes_cipher(key, aes_str):
    # 使用key,选择加密方式
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(pad_pkcs7)
    # 加密结果
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    encrypted_text_str = encrypted_text.replace("\n", "")

    return encrypted_text_str


# KEY 的值
string = str(str(agent) + str(timestamp) + MD5KEY)
md5_val = hashlib.md5(string.encode('utf8')).hexdigest()

if __name__ == '__main__':


    e = aes_cipher(DESKEY, param)  # 加密
    # print("加密:", e)
    # kyqb = json.dumps({'agent': '50035', 'timestamp': '%s', 'param': '%s', 'key': '%s'}) % (timestamp, e, md5_val)
    # kyqb = {'agent': agent, 'timestamp': timestamp, 'param': e, 'key': md5_val}
    # r = requests.get(url, params=kyqb)
    # print(kyqb)
    # print(r.url)
    # print(r.text)
    print(e)

