# Author : Sky
# @Time : 2020/7/20 17:23
# @Site :
# @File : 真人转帐失败报警.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import redis
import json, sys, os
os.system('pwd')

# curl -s "https://api.telegram.org/bot945332702:AAERMRbqmjIwS5_36eMyxk4C1PugUfsTjVI/sendMessage?chat_id=-287988350&text='api_$3:$2:$1 监控发现后端处理大于50秒,超时接>口:  $4 重启Docker容器'"
# #
# #!/bin/bash
# curl -s "https://api.telegram.org/bot943824825:AAG--vAsjbOY1HZUKwZ-tfAG6z7OliZrAG8/sendMessage?chat_id=-345686437&text=' /PROBLEM:                                                                          发现转帐失败                                                                            转帐服务器IP:$1                                                                    服务器端口：$2                                                                          后台转帐单号：$3                                                                        'STATUS'：$4                                                           转放游戏类型：$5"
#
