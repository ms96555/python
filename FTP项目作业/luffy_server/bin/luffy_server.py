# Author : Sky 
# @Time : 2020/2/3 13:41
# @Site : 
# @File : luffy_server.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import os,sys

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
if __name__ == '__main__':
    from core import management

    argv_parser = management.ManagementTool(sys.argv)
    argv_parser.execute()