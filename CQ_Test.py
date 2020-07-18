# Author : Sky 
# @Time : 2020/5/23 16:54
# @Site : 
# @File : test5.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from pyDes import des, CBC, PAD_PKCS5
import binascii
import base64
import requests, json
import hashlib
import time
from django.shortcuts import render
import requests, datetime

# Create your views here.
account = 'bb_122493'


def Get_balance():
    CONFIG = {
        'url': 'https://apif.cqgame.cc/gameboy/player/balance/',
        'headers': {
            'ContentType': 'application/x-www-form-urlencoded',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI1YzdmOWIyZjZkNjhmNDAwMDE4OTM3ZjEiLCJhY2NvdW50IjoidWJldCIsIm93bmVyIjoiNWM3ZjliMmY2ZDY4ZjQwMDAxODkzN2YxIiwicGFyZW50Ijoic2VsZiIsImN1cnJlbmN5IjoiQ05ZIiwianRpIjoiMzg5NTA5MjM5IiwiaWF0IjoxNTUxODY2NjcxLCJpc3MiOiJDeXByZXNzIiwic3ViIjoiU1NUb2tlbiJ9.ehLUnJR9QDguJR3agzy4qEwMrNjn7umJmujkGuOE7JM'
        }
    }

    headers = CONFIG['headers']
    get_url = CONFIG['url'] + 'bb_122493'

    '''
    https://apif.cqgame.cc/gameboy/player/balance/bb_122493?
    :param request:
    :return:
    '''

    print(headers)
    # r = requests.get(url=get_url,headers=headers)
    # print(r.url)
    # print(r.text)


def Transfer_in():
    time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    mtcode = "cq" + time_now
    # 轉入金額
    amount = 1

    CONFIG = {
        'url': 'https://apif.cqgame.cc/gameboy/player/deposit',
        'headers': {
            # 'ContentType': 'application/x-www-form-urlencoded',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI1YzdmOWIyZjZkNjhmNDAwMDE4OTM3ZjEiLCJhY2NvdW50IjoidWJldCIsIm93bmVyIjoiNWM3ZjliMmY2ZDY4ZjQwMDAxODkzN2YxIiwicGFyZW50Ijoic2VsZiIsImN1cnJlbmN5IjoiQ05ZIiwianRpIjoiMzg5NTA5MjM5IiwiaWF0IjoxNTUxODY2NjcxLCJpc3MiOiJDeXByZXNzIiwic3ViIjoiU1NUb2tlbiJ9.ehLUnJR9QDguJR3agzy4qEwMrNjn7umJmujkGuOE7JM'
        }

    }

    cq = {
        'account': account,
        'mtcode': mtcode,
        'amount': amount,
    }

    headers = CONFIG['headers']
    get_url = CONFIG['url']
    # r = requests.post(url=get_url, data=json.dumps(cq), headers=headers)
    r = requests.post(url=get_url, data=cq, headers=headers)
    print(headers)
    print(cq)
    print(r.url)
    print(r.text)


def Transfer_out():
    time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    mtcode = "cq" + time_now
    # 轉入金額
    amount = 1

    CONFIG = {
        'url': 'https://apif.cqgame.cc/gameboy/player/withdraw',
        'headers': {
            # 'ContentType': 'application/x-www-form-urlencoded',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI1YzdmOWIyZjZkNjhmNDAwMDE4OTM3ZjEiLCJhY2NvdW50IjoidWJldCIsIm93bmVyIjoiNWM3ZjliMmY2ZDY4ZjQwMDAxODkzN2YxIiwicGFyZW50Ijoic2VsZiIsImN1cnJlbmN5IjoiQ05ZIiwianRpIjoiMzg5NTA5MjM5IiwiaWF0IjoxNTUxODY2NjcxLCJpc3MiOiJDeXByZXNzIiwic3ViIjoiU1NUb2tlbiJ9.ehLUnJR9QDguJR3agzy4qEwMrNjn7umJmujkGuOE7JM'
        }

    }

    cq = {
        'account': account,
        'mtcode': mtcode,
        'amount': amount,
    }

    headers = CONFIG['headers']
    get_url = CONFIG['url']
    # r = requests.post(url=get_url, data=json.dumps(cq), headers=headers)
    r = requests.post(url=get_url, data=cq, headers=headers)
    print(headers)
    print(cq)
    print(r.url)
    print(r.text)



print(Transfer_out())
