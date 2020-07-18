from django.shortcuts import render, HttpResponse

# Create your views here.
import base64
import requests, json
import hashlib, base64
import uuid
from hashlib import sha1
import time, datetime

'''

'''

'''
字段名称	类型	长度	必选	说明
random	string	64	是	随机字符串，建议使用UUID
digest	string	64	是	签名摘要digest=md5(random+sn+loginId+secretCode)
sn	string	4	是	厅代码
loginId	string	24	是	用户登录ID
{"SN":"he06","Sha1SignKey":"JsbsR3W5","Md5SignKey":"7A7DA0EE92CC45208B655F5F480B9580"}
'''

# 随机字符串
random = uuid.uuid1().hex
# random = 'c18d8124aedf11ea9260b42e99443bbe'
print('random:'+random)

# 13711331327  aa123456
# 用户名密码
loginId = 'bb_122493'
# password = '123888bbb'
password = 'JsbsR3W5'

# SN
sn = 'he06'

sha_1 = hashlib.sha1(password.encode('utf8')).hexdigest()
print('sha_1:'+ sha_1)
secretCode = str(base64.encodebytes(hashlib.sha1(password.encode('utf8')).digest()), 'utf-8').strip()
print('secretCode:'+secretCode)

# 定义ULR  POST  传数字典
CONFIG = {
    'url': 'http://n1api.trarot.com/open-cloud/api/',
    'headers': {'Content-Type': 'application/json'}
}
url = CONFIG['url']
headers = CONFIG['headers']

# ID
id = uuid.uuid1().hex

# digest=md5(random+sn+loginId+secretCode)
print("**************************************************************")
print("random:"+str(random))
print("sn:"+str(sn))
print("loginId:"+str(loginId))
print("secretCode:"+str(secretCode))
digest_str = str(str(random) + str(sn) + str(loginId) + str(secretCode))
print("digest_str:"+ digest_str.strip())

digest = hashlib.md5(digest_str.encode('utf8')).hexdigest()
print('digest_MD5:'+digest)
print("**************************************************************")

time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
print(type(time_now))
print(time_now)
#  查询余额请求URL
'''
http://n1api.trarot.com/open-cloud/api/?{"params":{"random":"fb6acc1230624a52b1b42f3d026942ca","digest":"0c0b0a08c370306e8d47640b0a5e29fe","sn":"he06","loginId":"bb_122493"},"id":"9cc7cdf8e3384efaac6d297ec1a82ace","method":"open.balance.get","jsonrpc":"2.0"}
:return:
'''

# bg = {'params':
#     {
#         'random': random,
#         'digest': digest,
#         'sn': sn,
#         'loginId': loginId,
#     },
#     'id': id,
#     'method': "open.balance.get",
#     'jsonrpc': '2.0'
# }
#
# print(type(bg))
# print(bg)
# # r = requests.post(url=url, data=json.dumps(bg), headers=headers)
# r = requests.post(url=url, data=json.dumps(bg))
# print(r)
# print(r.url)
# print(r.text)

'''
字段名称	类型	长度	必选	说明
random	string	64	是	随机字符串，建议使用UUID
digest	string	64	是	签名摘要digest=md5(random+sn+loginId+amount+secretCode)
sn	string	4	是	厅代码
loginId	string	24	是	用户登录ID
amount	string	32	是	转账金额(负数表示从BG 转出，正数转入)，支持2位小数
bizId	long	64	否	转账业务ID，由调用方提供
checkBizId	string	1	否	是否检查转账业务ID的唯一性. 1: 检查; 0: 不检查(默认)

响应参数
字段名称	类型	长度	说明
result	float	32	账户余额
http://n1api.trarot.com/open-cloud/api/?{"params":{"random":"b80405e3fd794b9e822d284ae92ce0ee","digest":"eabe4e4fc79229107a59f044c3bbab4d","sn":"he06","loginId":"bb_122493","amount":"1","bizId":2020061515162292402},"id":"80109497e27c4b64bff15fcebfa58514","method":"open.balance.transfer","jsonrpc":"2.0"}
:param request:
:return:
'''

amount = 1
# digest
digest_str = str(str(random) + str(sn) + str(loginId) + str(amount) + str(secretCode))
digest = hashlib.md5(digest_str.encode('utf8')).hexdigest()

# BIZID
time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
bg = {'params':
    {
        'random': random,
        'digest': digest,
        'sn': sn,
        'loginId': loginId,
        'amount': amount,
        'bizId': int(time_now),
    },
    'id': id,
    'method': "open.balance.transfer",
    'jsonrpc': '2.0'
}

print(type(bg))
print(bg)
# r = requests.post(url=url, data=json.dumps(bg), headers=headers)
r = requests.post(url=url, data=json.dumps(bg))
print(r.text)