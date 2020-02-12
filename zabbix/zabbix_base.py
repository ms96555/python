# Author : Sky 
# @Time : 2020/2/6 15:48
# @Site : 
# @File : zabbix_base.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import json
from urllib import request

zabbix_url = "http://zabbix.n-b-e-t.com/api_jsonrpc.php"
zabbix_header = {"Content-Type": "application/json"}

zabbix_user = "Sky"
zabbix_pass = "sky66658"


def zabbix_api_common(data):
    """获取token"""
    data = json.dumps(data).encode(encoding='utf-8')
    req = request.Request(zabbix_url, headers=zabbix_header, data=data)
    result = request.urlopen(req).read()
    return json.loads(result)


def get_token():
    """初始默认值 """
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": zabbix_user,
            "password": zabbix_pass
        },
        "id": 0
    }
    result = zabbix_api_common(data)
    return result['result']


if __name__ == '__main__':
    result = get_token()
    print(result)
