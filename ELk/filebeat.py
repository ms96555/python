# Author : Sky 
# @Time : 2020/2/7 17:44
# @Site : 
# @File : filebeat.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import os
import sys
# filebeat_site = load_dict["initialize"]["a,站点标识"]
# filebeat_api_name = load_dict["initialize"]["d,zabbix-agent-hostname"]
# filebeat_cld = load_dict["initialize"]["cloud"]
#filebeat_site_api = load_dict["initialize"]["b,站点配置"]
filebeat_site = "cc"
filebeat_api_name = 'cld_20_ui_cc_nginx'
filebeat_cld = 20
filebeat_site_api = 'api_cc'


msg_nginx = '''filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
setup.template.settings:
  index.number_of_shards: 3
setup.kibana:
processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/messages
  fields:
    %s: messages
    fields_under_root: true
  tags: ["syslog"]
- type: log
  enabled: true
  paths:
    - /opt/lnmp/nginx/logs/apiApi_%s.log
    - /opt/lnmp/nginx/logs/webUI_%s.log
  json.keys_under_root: true
  json.overwrite_keys: true
  fields:
    %s: nginx-access
    fields_under_root: true
  tags: ["nginx-access_cld_%s"]
- type: log
  enabled: true
  paths:
    - /opt/lnmp/nginx/logs/nginx_error.log
    - /opt/lnmp/nginx/logs/error.log*
  fields:
    %s: nginx-error
    fields_under_root: true
  tags: ["nginx-error"]
output.redis:
  hosts: ["172.31.3.15"]
  port: "17788"
  key: "*"
  password: APPLE!@#++--123'''%(filebeat_api_name,filebeat_site,filebeat_site,filebeat_api_name,filebeat_cld,filebeat_api_name)
msg_api = '''filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
setup.template.settings:
  index.number_of_shards: 3
setup.kibana:
processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/messages
  fields:
    %s: messages                                     
    fields_under_root: true
  tags: ["syslog"]
- type: log
  enabled: true
  paths:
    - /opt/logs/%s/Logs/20200209/*.txt                  
    - /opt/logs/%s_2/Logs/20200209/*.txt
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}'
  multiline.negate: true
  multiline.match: after
  fields:
    %s: %s
    fields_under_root: true
  tags: ["applog"]
output.redis:
  hosts: ["172.31.3.15"]
  port: "17788"
  key: "*"
  password: APPLE!@#++--123'''%(filebeat_api_name,filebeat_site_api,filebeat_site_api,filebeat_api_name,filebeat_site_api)
with open('filebeat.yml', 'w', encoding='utf-8') as f:
    for line in msg_nginx:
        f.write(line)

