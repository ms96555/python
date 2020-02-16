# Author : Sky 
# @Time : 2020/2/16 11:12
# @Site : 
# @File : nginx日志格式.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 过滤时间格式
# cat webUI_dh.log | grep '16/Feb/2020:10:1[5-6]:[0-9][0-9]'


# 感觉是模糊匹配，同一时间的日志在这种方式里面不显示要用上面的方法
# cat webUI_dh.log| sed -n '/2020:10:16:00/,/2020:10:17:00/p'

#  查看大于20秒的
#  awk -F 'upstream_response_time":"|","request_time' '{if($2>20) print $0}'
