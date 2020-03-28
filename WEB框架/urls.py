# Author : Sky 
# @Time : 2020/3/26 9:26
# @Site : 
# @File : urls.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

from views import *

# 视图函数
url_patterns = [
    ('/login', login),
    ('/index', index),
    ('/reg', reg),
    ('/timer',timer),
]
