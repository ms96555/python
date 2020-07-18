from pyDes import des, CBC, PAD_PKCS5
import binascii


# 秘钥
KEY = 'iJTZb06o'


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

if __name__ == '__main__':
    str="74a106ff5b7a54896bce0ebfd46b430df058a9c727eff5114ccce881b868951a9d3349a68a0a5f659c1875bc4c8c25aa9f836861bf07a9e272b08c40fb526f1dbbb6afa51d0daa4c897295da98180434f7b4ef0170089dbe904dbfe020b5130a5c07085874f15cbd8fe67d6faeee7c28"
    str=des_descrypt(str)
    print(str)