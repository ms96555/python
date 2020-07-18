# Author : Sky 
# @Time : 2020/5/23 16:04
# @Site : 
# @File : test3.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from Crypto.Util.Padding import pad
"""
ECB没有偏移量
"""

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
# 操作类型
s = 1
# 会员帐号
account = "bb_195070"


param = str('s='+ str(s) +'&'+'account='+ account)
print(param)


def aes_cipher(key, aes_str):
    # 使用key,选择加密方式
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
    encrypt_aes = aes.encrypt(pad_pkcs7)
    # 加密结果
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 解码
    encrypted_text_str = encrypted_text.replace("\n", "")
    # 此处我的输出结果老有换行符，所以用了临时方法将它剔除

    return encrypted_text_str

print(aes_cipher('56A168B84F35B70E','s=1&account=bb_195070'))