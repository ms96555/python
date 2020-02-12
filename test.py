# Author : Sky 
# @Time : 2020/2/5 15:24
# @Site : 
# @File : test.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

import hashlib
a = 'askdfj '

md5_obj = hashlib.md5()
md5_obj.update(a.encode(encoding='utf-8'))
md5_password = md5_obj.hexdigest()
print(md5_password)
