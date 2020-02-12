# Author : Sky 
# @Time : 2020/2/7 15:39
# @Site : 
# @File : zabbix_online.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import json
from urllib import request

# 当前zabbix环境的URL
zabbix_url = "http://zabbix.n-b-e-t.com/api_jsonrpc.php"
zabbix_header = {"Content-Type": "application/json"}

# 用户名密码
zabbix_user = "Sky"
zabbix_pass = "sky66658"

# 链接模版
Dick_status = "10305"
Docker_Monitor = "10277"
Template_OS_Linux = "10001"
nginx_status = "10263"
tcp_status_Template = "10337"
template_nginx = [Dick_status, Docker_Monitor, Template_OS_Linux, nginx_status, tcp_status_Template]
template_api = [Dick_status, Docker_Monitor, Template_OS_Linux, tcp_status_Template]



def zabbix_api_common(data):
    """获取token"""
    data = json.dumps(data).encode(encoding='utf-8')
    req = request.Request(zabbix_url, headers=zabbix_header, data=data)
    result = request.urlopen(req).read()
    return json.loads(result)


def get_token():
    """初始默认值 ，获取token"""
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


token = get_token()
# ngix 服务  和API 服务监控
nginx_template_list = []
for item in template_nginx:
    nginx_template_list.append({"templateid": item})

api_template_list = []
for item in template_api:
    api_template_list.append({"templateid": item})

# 主机信息
hostname = 'cld_20_test'
alias_name = 'cld_20_test枷真是'
hostip = '172.31.16.45'
groupid = 2
templateid = "10001"
groupname = "Linux servers"

# 接入的数据
data_nginx = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": hostname,
        "name": alias_name,
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
result = zabbix_api_common(data_nginx)
# result = zabbix_base.zabbix_api_common(data_api)
print(result)
