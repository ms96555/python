# -*- coding: UTF-8 -*-
# ! /usr/bin/env python
import Crypto
import base64
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

import Crypto
import time

# 使用 rsa库进行RSA签名和加解密


class RsaUtil(object):
    PUBLIC_KEY_PATH = 'company_rsa_public_key.pem'  # 公钥
    PRIVATE_KEY_PATH = 'ompany_rsa_private_key.pem'  # 私钥

    # 初始化key
    def __init__(self,
                 company_pub_file=PUBLIC_KEY_PATH,
                 company_pri_file=PRIVATE_KEY_PATH):

        if company_pub_file:
            self.company_public_key = RSA.importKey(open(company_pub_file).read())
        if company_pri_file:
            self.company_private_key = RSA.importKey(open(company_pri_file).read())



    def sign_by_private_key(self, message):
        """私钥签名.
            :param message: 需要签名的内容.
            签名之后，需要转义后输出
        """
        cipher = PKCS1_v1_5.new(self.company_private_key)  # 用公钥签名，会报错 raise TypeError("No private key") 如下
        # if not self.has_private():
        #   raise TypeError("No private key")
        hs = SHA.new(message)
        signature = cipher.sign(hs)
        return base64.b64encode(signature)

    def verify_by_public_key(self, message, signature):
        """公钥验签.
            :param message: 验签的内容.
            :param signature: 对验签内容签名的值（签名之后，会进行b64encode转码，所以验签前也需转码）.
        """
        signature = base64.b64decode(signature)
        cipher = PKCS1_v1_5.new(self.company_public_key)
        hs = SHA.new(message)

        # digest = hashlib.sha1(message).digest()  # 内容摘要的生成方法有很多种，只要签名和解签用的是一样的就可以

        return cipher.verify(hs, signature)

now_time = str(int(time.time()))


message = 'hellworldhellworldhellworldhell'
print("明文内容：>>> ")
print(message)
rsaUtil = RsaUtil()
sign = rsaUtil.sign_by_private_key(bytearray(message.encode(encoding='utf-8')))
print("签名结果：>>> ")
sign_val = (str(sign,'utf-8'))
print(sign)
print("验签结果：>>> ")
print(rsaUtil.verify_by_public_key(bytearray(message.encode(encoding='utf-8')), sign))


a = {
    'timestamp':now_time,
    'sign': sign_val
}