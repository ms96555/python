import requests
import uuid
import base64

# Create your views here.

# !!! 所有请求要先获取TOKN

'''
Basic 验证资讯范例
Auth username(API 应用登入帐号): testauthuser
Auth Password(API 应用登入密码): testsecret
$ echo "testauthuser:testsecret" | base64
dGVzdGF1dGh1c2VyOnRlc3RzZWNyZXQK
您也可以透过此网站 https://www.base64encode.org/ 对资讯做 64 编码
范例请求
POST /oauth/token
Authorization: Basic dGVzdGF1dGh1c2VyOnRlc3RzZWNyZXQK
Accept: application/json ;charset=UTF-8 X-DAS-TX-ID: 123e4567-e89b-12d3-a456-426655440000
X-DAS-CURRENCY: USD
X-DAS-TZ: UTC+9
X-DAS-LANG: en
grant_type=password&username=apiusername&password=apipassword
'''


def Tocken():
    testauthuser = "YobetCNY_auth"
    testsecret = 'Gx7M555bsr3KspgLJx8V'
    authorizon = testauthuser + ':' + testsecret
    print(authorizon)
    base64_authorizon = base64.b64encode(authorizon.encode('utf-8'))
    print(str(base64_authorizon, 'utf-8'))


    # random 隨機數
    random = uuid.uuid1().hex
    print(random)

    CONFIG = {
        'url': 'https://api.adminserv88.com',
        'headers': {
            'Authorization': 'Basic WW9iZXRDTllfYXV0aDpHeDdNNTU1YnNyM0tzcGdMSng4Vg==',
            'X-DAS-TZ': 'UTC+8',
            'X-DAS-CURRENCY': 'CNY',
            'X-DAS-TX-ID': random,
            'X-DAS-LANG': 'zh-CN',

        }
    }
    data = {
        'grant_type': 'password',
        'username': 'YobetCNY_api',
        'password': 'x6529w9Yrnd3KphBfVKG',

    }
    headers = CONFIG['headers']
    get_url = CONFIG['url'] + '/oauth/token'
    r = requests.post(url=get_url, headers=headers,data=data)



    print('**********************')
    print('請求RUL:',r.url)
    print('請求headers:',headers)
    print('請求數據:',data)
    print('返回值:',r.text)
    print(r.content)
    print('**********************')





def Get_balance(request):
    '''
    Headers:Authorization=Basic WW9iZXRDTllfYXV0aDpHeDdNNTU1YnNyM0tzcGdMSng4Vg==; X-DAS-TZ=UTC+8; X-DAS-CURRENCY=CNY; X-DAS-TX-ID=4d5e4f3cc84944328d507dafaf9ddcc9; X-DAS-LANG=zh-CN] https://api.adminserv88.com/oauth/token?grant_type=password&username=YobetCNY_api&password=x6529w9Yrnd3KphBfVKG
    :param request:
    :return:
    '''

    headers = CONFIG['headers']
    get_url = CONFIG['url'] + 'bb_122493'

    '''
    https://apif.cqgame.cc/gameboy/player/balance/bb_122493?
    :param request:
    :return:
    '''

    r = requests.get(url=get_url, headers=headers)


def Transfer_in(request):
    pass


def Transfer_out(request):
    pass


def Login_game(request):
    pass


def Get_game(request):
    pass


def Check_game(request):
    pass


def Create_game(request):
    pass


print(Tocken())
