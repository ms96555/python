# Author : Sky 
# @Time : 2020/2/6 20:00
# @Site : 
# @File : zabbix_create.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import zabbix_base

token = zabbix_base.get_token()
Dick_status = "10305"
Docker_Monitor = "10277"
Template_OS_Linux = "10001"
nginx_status = "10263"
tcp_status_Template = "10337"
template_nginx = [Dick_status, Docker_Monitor, Template_OS_Linux, nginx_status, tcp_status_Template]
template_api = [Dick_status, Docker_Monitor, Template_OS_Linux, tcp_status_Template]

nginx_template_list = [];
for item in template_nginx:
    nginx_template_list.append({"templateid": item})

api_template_list = [];
for item in template_api:
    api_template_list.append({"templateid": item})

hostname = 'cld_20_test'
hostip = '172.31.16.45'
groupid = 2
templateid = "10001"

groupname = "Linux servers"
data_nginx = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": hostname,
        "interfaces": [{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": hostip,
            "dns": "",
            "port": "10050"
        }],
        "groups": [{
            "groupid": groupid
        }],
        "templates": nginx_template_list,
    },
    "auth": token,
    "id": 1
}

data_api = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": hostname,
        "interfaces": [{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": hostip,
            "dns": "",
            "port": "10050"
        }],
        "groups": [{
            "groupid": groupid
        }],
        "templates": api_template_list,
    },
    "auth": token,
    "id": 1
}

# print(data)
result = zabbix_base.zabbix_api_common(data_nginx)
result = zabbix_base.zabbix_api_common(data_api)
print(result)
