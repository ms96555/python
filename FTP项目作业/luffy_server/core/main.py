# Author : Sky 
# @Time : 2020/2/3 16:21
# @Site : 
# @File : main.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import socket
from conf import settings
import json
import configparser
import hashlib


class FTPServer(object):
    """处理与客户端所有的交互的socket server"""

    STATUS_CODE = {
        200: 'Passed authentiction',
        201: 'Wrong username or password',
        300: 'File does not exits'
    }
    MSG_SIZE = 1024 #定义消息长度
    def __init__(self, management_instance):
        self.management_instance = management_instance
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((settings.HOST, settings.PORT))
        self.sock.listen(settings.MAX_SOCKET_LISTEN)
        self.accounts = self.load_accounts()

    def run_forever(self):
        """启动socket server"""
        print('starting LuffyFTP server on %s:%s'.center(50, '-') % (settings.HOST, settings.PORT))
        while True:
            self.request, self.addr = self.sock.accept()
            print('got a new connection from %s........' % (self.addr,))
            self.handle()

    def handle(self):
        """处理与用户的所有指令交互"""
        while True:
            raw_data = self.request.recv(1024)
            print('-------->', raw_data)
            if not raw_data:
                print('connection %s is lost....'%(self.addr,))
                del self.request,self.addr
                break
            data = json.loads(raw_data.decode('utf-8'))
            action_type = data.get('action_type')
            if action_type:
                if hasattr(self, '_%s' % action_type):
                    func = getattr(self, '_%s' % action_type)
                    func(data)
            else:
                print('invalid command')

    def load_accounts(self):
        """加载所有帐号"""
        config_obj = configparser.ConfigParser()
        config_obj.read(settings.ACCOUNT_FILE)
        print(config_obj.sections())
        return config_obj

    def authenticate(self, username, password):
        """用户认证方法"""
        if username in self.accounts:
            _password = self.accounts[username]['password']
            md5_obj = hashlib.md5()
            md5_obj.update(password.encode(encoding='utf-8'))
            md5_password = md5_obj.hexdigest()
            print('password:', _password, md5_password)
            if md5_password == _password:
                # print('passed authentication..')
                return True
            else:
                # print('wrong username or password...')
                return False
        else:
            print('wrong username .....')
            return False

    def send_response(self,status_code,*agrs,**kwargs):
        """
        打包发送消息到客户端
        :param status_code:
        :param agrs:
        :param kwargs:
        :return:
        """
        data = kwargs
        data['status_code'] = status_code
        data['status_msg'] = self.STATUS_CODE[status_code]
        data['fill'] = ''

        bytes_data = json.dumps(data).encode()
        if len(bytes_data) < self.MSG_SIZE:
            data['fill'] = data['fill'].zfill(self.MSG_SIZE - len(bytes_data))


        self.request.send(bytes_data)

    def _auth(self, data):
        """处理用户认证请求 这里以 _ 下划线区别客户端操作"""
        # print('auth',data)
        if self.authenticate(data.get('username'), data.get('password')):
            print('pass auth....')

            self.send_response(status_code=200)

        else:
            self.send_response(status_code=201)
