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
#  awk -F 'upstream_response_time":"|","request_time' '{if($2>60) print $0}'


# 查看nginx返回的时间，也可以加 | 符号进行多条件匹配
# tail -f  apiApi_de.log|grep -E "[0-9].[0-9]{1,3}[0-9]{1,3}}"


# 查看返回时间
#time cat webUI_de.log| grep -E '14/Mar/2020:16:[3-6][0-1]:[0-9][0-9]'| grep -E 'request_time":[6-9][0-9].[0-9][0-9][0-9]}'
