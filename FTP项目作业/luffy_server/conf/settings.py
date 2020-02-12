# Author : Sky 
# @Time : 2020/2/3 16:25
# @Site : 
# @File : settings.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import os,sys

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = "127.0.0.1"

PORT = 7766

USER_HOME_DIR = os.path.join(BASE_DIR,'home')

ACCOUNT_FILE = '%s/conf/accounts.ini'% BASE_DIR

MAX_SOCKET_LISTEN = 5


