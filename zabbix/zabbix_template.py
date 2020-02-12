# Author : Sky 
# @Time : 2020/2/6 17:39
# @Site : 
# @File : zabbix_template.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import zabbix_base

token = zabbix_base.get_token()
data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": ['host'],
        "filter": {
            "host": [
                "Dick_status",
                "Docker Monitor",
                "tcp_status_Template",
                "nginx_status",
                "Template OS Linux"]}
    },
    "auth": token,
    "id": 1
}
result = zabbix_base.zabbix_api_common(data)
for i in result['result']:
    print(i)
