# Author : Sky 
# @Time : 7/20/20 7:32 下午
# @Site : 
# @File : test.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import re
import datetime
import json
import os
def happy(arg,*args,**kwargs):

    print(arg,args,kwargs,type(arg),type(args),type(kwargs))

if __name__ == '__main__':

    happy(3,3,3,3,a=8,c=9)