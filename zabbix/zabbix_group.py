# Author : Sky 
# @Time : 2020/2/6 16:42
# @Site : 
# @File : zabbix_group.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import zabbix_base

token = zabbix_base.get_token()
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter":{
                "name":['Linux servers'],
                 },
    },
    "auth": token,
    "id": 0
    }
result = zabbix_base.zabbix_api_common(data)
for i in result['result']:
    print(i)