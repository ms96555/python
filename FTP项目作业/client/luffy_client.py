# Author : Sky 
# @Time : 2020/2/3 17:09
# @Site : 
# @File : luffy_client.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
'''
客户端的格式：
python luffy.py -h 192.168.22.33 -p 3333
user:
passwd:
'''
import optparse
import socket
import json


# 第三方的传参库

class FtpClient(object):
    """ftp客户端"""
    MSG_SIZE = 1024  # 定义消息长度

    def __init__(self):
        self.username = None
        parser = optparse.OptionParser()
        parser.add_option('-s', '--server', dest='server', help='ftp server ip_addr')
        parser.add_option('-P', '--port', type='int', dest='port', help='ftp server prot')
        parser.add_option('-u', '--username', dest='username', help='username info')
        parser.add_option('-p', '--password', dest='password', help='password info')
        self.options, self.args = parser.parse_args()

        # print(self.options,self.args,type(self.options),self.options.server)
        self.argv_verification()

        self.make_connection()

    def argv_verification(self):
        """检查参数合法性"""
        if not self.options.server or not self.options.port:
            print('Error: muster suupy server and port parameters')

    def make_connection(self):
        """建立socket连接"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.options.server, self.options.port))

    def get_response(self):
        """获取服务器返回"""
        data = self.sock.recv(self.MSG_SIZE)
        return json.loads(data.decode())

    def auth(self):
        """用户认证"""
        count = 0
        while count < 3:
            username = input('username:').strip()
            if not username: continue
            password = input('password:').strip()

            cmd = {
                'action_type': 'auth',
                'username': username,
                'password': password
            }
            self.sock.send(json.dumps(cmd).encode('utf-8'))

            response = self.get_response()
            print('response', response)
            if response.get('status_code') == 200:
                self.username = username
                return True
            else:
                print(response.get('status_msg'))
            count += 1

    def interactive(self):
        """处理与ftpserver的所有交互"""
        if self.auth():
            while True:
                user_input = input('[%s]>>:' % self.username).strip()
                if not user_input:
                    continue
                cmd_list = user_input.split()
                if hasattr(self, '_%s' % cmd_list[0]):
                    func = getattr(self, '_%s' % cmd_list[0])
                    func(cmd_list[1:])

    def parameter_check(self, agrs, min_agrs=None, max_agrs=None, exact_args=None):
        """判断参数个数是否合法"""
        if min_agrs:
            if len(args) < min_agrs:
                print('must provide at least %s parameters but %s received.'%(min_agrs,len(args)))
                return False
        if max_agrs:
            if len(args) > max_agrs:
                print('need at most %s paraemters but %S received.'%(max_agrs,len(args)))
                return False
        if exact_args:
            if len(args) != exact_args:
                print('need exactly %s parameters but %s received'%(exact_args,len(args)))
                return False
        return True




    def _get(self, cmd_args):
        """download file from ftp server"""
        if self.parameter_check(cmd_args,min_agrs=1):
            filename = cmd_args[0]

    def _put(self):
        pass


if __name__ == '__main__':
    client = FtpClient()
    client.interactive()  # 交互
