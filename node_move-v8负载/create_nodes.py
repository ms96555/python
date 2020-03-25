import getpass, requests
import jenkins, sys, os, json, paramiko
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import time, threading
import gitlab
import socket
import json
import socket
from urllib import request

hostName = socket.gethostname()
uname = hostName.split(".")
with open('/scripts/conf.json', 'r', encoding='utf-8')as f:
    load_dict = json.load(f)
config_name = load_dict["initialize"]["b,站点配置"]
name = load_dict["initialize"]["a,站点标识"]
key = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAq5YRYowMHDJsvo3dlchOTwbfLsgczPa01tQDJ2vrVz/2TCQNAEdElLrFH2sf\n4tGJV/krP1tpfgFDiGcoRDDFz72LACd6s0uW6A5QepkhDM/0m29FxqFl3nO+2/XY1YeS0pe01+ws\nunS0sGT/Do+A9jW7d77+fnOxD1Bj6GWHy6ae0bLMoCpOJ+hnPiooigjCaj3FYapPgsGjLFMuBE+Z\nH1whknLvcarJFNaJQRN9ctNNZlQJBtVH+M+XAeMHRBHUzChTAN2Tm5tjenv35GspcqUdnL7mc0Wu\nt4U+kquDuJT8jfdX8tAXNusg8EyjLhXC/cs+HhtS3qg79OURbwFAlQIDAQABAoIBACmtA3/6IB7h\nKISIFKACzPJo6uCD/mrSKU5cpH94uOqyQHJx9y5wIPo2+xYMgOwolMFnZde3rkHKsMp6s88MQZ+Z\nnB9nd2gBHiAzCd0dQGfKQtFWD46VORb06hCnAAmtKj44VtZzKNII8rI9da3lsR8cIfKN02aHVyQv\nFHUn4/nUkQcQcMmiI8/Cdbz0Poy6hh26miqFViEDmP/AQKDHNoKPxt4PSW9UsphW3+kgNiyBbPEM\nHjtBfTtuz3/th8Ecl8UXQXOR6gjx/ryLlkAwadjbc3bqiCHwnyjjq6WjUrMPE6b2qcLyqqTq7wxD\nz4CIwg9qG1jgFKAeqyE368O+hikCgYEA+/5yWr5+dq0uoQp4b7AgKHpjfsDkVJMvxLuZzw4EDSJs\nZlHv4T7avb/bj/A6i9IqotgqdIJHINudsq2OwhbZuBFBZnP5KB6yDoaD8z6yLUcBtsx9hWvPM/Wb\nqHy5vMKCRwLNBKANtxB9hvNq2P93nchRd1TD253M3tFfD/KK5UMCgYEArlBhrGucgg0agIKYSaRF\nxO/wBWExA63USgKSURUckMCGuPBSjxrxuNg4sbeEAfzqAH3/phcBneJM5TfYwyfwRiGevMW0oRfI\n4fR6bw1hE/O3BFnbTZgQVqTrJ1pwoUIEk81SxvZPhYAL0ikYR+Bz97mbLvwbY9KTMq7YPEn1eUcC\ngYEAlt1rETDi/aIJPJjMKfHEDvfXAVfyW0ATZTD7kJ7Phh2J0GhVuQCsbNWkWbR1GKimpf/MyxwE\nAYP6EbMeuMx9ZFnQUco07PQTneaisMpkWf8c45fhvjMhRfZRTrn9aSj6XhErNQ2tqF/TByxMV8X6\nkxgOzeaNq7n5oZyv0RhgV4kCgYAlsyDMx6FbxzW6IYSKOMsWIsaIg1K0dv3428GFY8l/zQPWL7PL\nW4p37dulJAma3HZHkPiflU42NWFoGcH5w0OGB3NrZF8CkEBUDioEpqIeTJGCkWSKzZ6K/rQVGMxP\nNBYFWVzTxyW/u8fStiyYLwUlyLC1YrURy9MmHQaLU3uRtQKBgFI2QKYeQKC1S72UehnBOiARwecT\niW7aSw2oL1gQCXw6xw52x6uVKOFAk6JJHpEiSQTWzcxpvyzoLTaeG9BVF62JpWznhKGeSv6+IK8d\nE77wGN7/3xDg6f0eH+B7ghdIeWloAshhr8dFjKWOlUql/zzDzEI7w/zIwO4AVuCXmv5x\n-----END RSA PRIVATE KEY-----"
a, b = name.upper()
name_ascii = str(1) + str(ord(a)) + str(ord(b))
name_ascii_2 = str(2) + str(ord(a)) + str(ord(b))
balance_a = load_dict["initialize"]["balance_a"]
balance_b = load_dict["initialize"]["balance_b"]
balance_c = load_dict["initialize"]["balance_c"]
jenkins_name = "laobai"
jenkins_passwd = "laobai*((!"
with open('/scripts/key.pem', 'w', encoding='utf-8')as f:
    f.write(key)


def nginx_gitlab():
    url = 'http://172.31.37.14'
    token = 'Ji2yGiPs4mYWA7zU_8yL'
    login = gitlab.Gitlab(url, token)
    projects = login.projects.list(all=True)  # 获取所有的projects
    # print(projects)
    name = load_dict["initialize"]["a,站点标识"]
    nodes = load_dict["initialize"]["nodes"]
    app_path_dir = '/tmp/appApi_move_' + nodes + '.conf'
    web_path_dir = '/tmp/webUI_' + nodes + '.conf'
    with open(app_path_dir, 'r', encoding='utf-8')as f1:
        with open('appApi' + "_" + name + '.conf', 'w', encoding='utf-8')as f3:
            for line in f1.readlines():
                if 'server_name' in line:
                    line = line.replace('server_name', 'server_name' + " " + load_dict["domain"]["appApi"] + ";")
                elif 'access_log' in line:
                    line = line.replace('access_log',
                                        'access_log /opt/lnmp/nginx/logs/apiApi' + "_" + name + ".log main buffer=32k flush=1m;")
                elif 'set $pwd' in line:
                    line = line.replace('set $pwd', 'set $pwd "/opt/project/code/' + name + '/webUI";')
                elif 'alias  /opt/project/code' in line:
                    line = line.replace('alias  /opt/project/code',
                                        'alias  /opt/project/code/' + name + "/webUI/appTemp")
                elif 'server a_1' in line:
                    line = line.replace('server a_1',
                                        'server' + " " + balance_a + ":" + name_ascii + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server a_2' in line:
                    line = line.replace('server a_2',
                                        'server' + " " + balance_a + ":" + name_ascii_2 + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server b_1' in line:
                    line = line.replace('server b_1',
                                        'server' + " " + balance_b + ":" + name_ascii + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server b_2' in line:
                    line = line.replace('server b_2',
                                        'server' + " " + balance_b + ":" + name_ascii_2 + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server c_1' in line:
                    line = line.replace('server c_1',
                                        'server' + " " + balance_c + ":" + name_ascii + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server c_2' in line:
                    line = line.replace('server c_2',
                                        'server' + " " + balance_c + ":" + name_ascii_2 + " " + "max_fails=3 fail_timeout=30s;")
                f3.write(line)
        with open('appApi_' + name + '.conf', 'r', encoding='utf-8')as f4:
            appApi_conf = f4.read()
    with open(web_path_dir, 'r', encoding='utf-8')as f:
        with open('webUI' + "_" + name + '.conf', 'w', encoding='utf-8')as f5:
            for line in f.readlines():
                # if "server_name" in line:
                #     print(line)
                if 'server_name' in line:
                    line = line.replace('server_name', 'server_name' + " " + load_dict["domain"]["webUI"] + ";")
                elif 'access_log' in line:
                    line = line.replace('access_log',
                                        'access_log /opt/lnmp/nginx/logs/webUI' + "_" + name + ".log main buffer=32k flush=1m;")
                elif 'access_kkk' in line:
                    line = line.replace('access_kkk',
                                        'access_log /opt/lnmp/nginx/logs/webUI' + "_" + name + "_" + "greate" + "_" + "10" + '.log main_greater_10 buffer=32k flush=1m;')
                elif 'set $pwd' in line:
                    line = line.replace('set $pwd', 'set $pwd "/opt/project/code/' + name + '/webUI";')
                elif 'server a_1' in line:
                    line = line.replace('server a_1',
                                        'server' + " " + balance_a + ":" + name_ascii + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server a_2' in line:
                    line = line.replace('server a_2',
                                        'server' + " " + balance_a + ":" + name_ascii_2 + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server b_1' in line:
                    line = line.replace('server b_1',
                                        'server' + " " + balance_b + ":" + name_ascii + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server b_2' in line:
                    line = line.replace('server b_2',
                                        'server' + " " + balance_b + ":" + name_ascii_2 + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server c_1' in line:
                    line = line.replace('server c_1',
                                        'server' + " " + balance_c + ":" + name_ascii + " " + "max_fails=3 fail_timeout=30s;")
                elif 'server c_2' in line:
                    line = line.replace('server c_2',
                                        'server' + " " + balance_c + ":" + name_ascii_2 + " " + "max_fails=3 fail_timeout=30s;")
                f5.write(line)
        with open('webUI' + "_" + name + '.conf', 'r', encoding='utf-8')as f6:
            webUI_conf = f6.read()
    data = {
        'branch': name,  # v3
        'commit_message': name,
        'actions': [
            {
                'action': 'create',
                'file_path': 'appApi' + "_" + name + '.conf',
                'content': appApi_conf,
            },
            {
                'action': 'create',
                'file_path': 'webUI' + "_" + name + '.conf',
                'content': webUI_conf,
            }
        ]
    }
    branch_list = []
    for p in projects:  # 获取所有的project的name，id
        # print(p.name, p.id)
        if p.name == 'cloud_site_nginx_config' + "_" + load_dict["initialize"]["cloud"]:
            num = p.id
            result = login.projects.get(num)
    if result:
        for p1 in result.branches.list():
            branch_list.append(p1.name)
        if name in branch_list:
            branch = result.branches.delete(name)
            branch = result.branches.create({'branch': name, 'ref': 'master'})
            commit = result.commits.create(data)
            print("%s has existed...pls create node..." % name)
        else:
            branch = result.branches.create({'branch': name,
                                             'ref': 'master'})
            commit = result.commits.create(data)
            print("%s has created...pls create node..." % name)
    else:
        print('can not find cloud_site_nginx_config' + "_" + load_dict["initialize"]["cloud"] + "pls check...")


def initialize():
    private_key = paramiko.RSAKey.from_private_key_file('/scripts/key.pem', '888999')
    # 创建SSH对
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='172.31.32.88', port=22, username='centos', pkey=private_key)
    # 执行命令
    localpath = "/tmp/"  # 需要上传的文件(源)
    remotepath = "/scripts/"  # 远程路径(目标)
    t = paramiko.Transport(('172.31.32.88', int(22)))
    t.connect(username='centos', password='888999', pkey=private_key)
    sftp = paramiko.SFTPClient.from_transport(t)
    list = sftp.listdir(remotepath)
    # 创建一个已经连通的SFTP客户端通道
    for filename in list:
        # 上传本地文件到规程SFTP服务端
        real_remotepath = remotepath + "/" + filename
        print(real_remotepath, '文件下载中。。。。')
        sftp.get(os.path.join(remotepath, filename), os.path.join(localpath, filename))  # 上传文件
        # 下载文件
        print(filename, '文件下载完毕。。。')
    t.close()
    for i in sys.argv:
        if i == 'nginx':
            os.system("sh /tmp/initialize_nginx.sh")
        elif i == 'api':
            os.system("sh /tmp/initialize.sh")
        else:
            continue

    # stdin, stdout, stderr = ssh.exec_command('sudo su -l root -c "sh /tmp/initialize.sh|tee -a /opt/initialize.log"'+';',get_pty=True)
    # cmd_result=stdout.read(),stderr.read()
    # print(cmd_result)
    ssh.close()


def api():
    cloud_job_name = "api_more_" + load_dict["initialize"]["cloud"]
    create_api = jenkins.Jenkins('http://172.31.10.229', username=jenkins_name, password=jenkins_passwd)
    conf = create_api.get_job_config(cloud_job_name)
    cloud_job_rollback_name = cloud_job_name.replace("more", "more_rollback")
    conf_bak = create_api.get_job_config(cloud_job_rollback_name)
    with open("/tmp/" + cloud_job_name + ".xml", 'w', encoding='utf-8') as f1:
        with open("/tmp/" + cloud_job_rollback_name + ".xml", 'w', encoding='utf-8') as f_bak:
            f1.write(conf)
            f_bak.write(conf_bak)
    tree = ET.parse('/tmp/conf_api.xml')
    root = tree.getroot()
    root_url = root.getchildren()[4].getchildren()[1].getchildren()[0][0]
    root_description = root.getchildren()[1]
    root_branch = root.getchildren()[4].getchildren()[2].getchildren()[0].getchildren()[0]
    root = root.getchildren()[12]
    root_dir = root.getchildren()[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[2]
    root_path = root_dir.getchildren()[0].getchildren()[0]
    root_cmd = root_dir.getchildren()[0].getchildren()[10]
    root_ssh = root.getchildren()[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[0]
    api_name = name + "_api_start_" + load_dict["initialize"]["cloud"]
    new_api_path = "/opt/project/code/" + name + "/api"
    # new_api_url = "http://git.nbet-group.com/preproduct/sb-cloud/sb_cloud_site_api"
    new_api_description = name + "前端api部署"
    new_api_ssh_name = load_dict["initialize"]["d,zabbix-agent-hostname"]
    new_api_cmd = "cd /opt/project/code/" + name + "/api\nsh ./docker_start.sh api api_" + name + " " + name_ascii + " " + config_name + "\nsh ./docker_start.sh api api_" + name + "_2" + " " + name_ascii_2 + " " + config_name
    # root_url.text = str(new_api_url)
    root_description.text = str(new_api_description)
    root_path.text = str(new_api_path)
    root_ssh.text = str(new_api_ssh_name)
    root_cmd.text = str(new_api_cmd)
    tree.write('/tmp/conf_api_update.xml')
    with open('/tmp/conf_api_update.xml', 'r', encoding='utf-8') as api_xml:
        conf_api_xml = api_xml.read()
    if create_api.job_exists(api_name) != None:
        if create_api.job_exists(name + "_api_start_B_" + load_dict["initialize"]["cloud"]) != None:
            api_name = name + "_api_start_C_" + load_dict["initialize"]["cloud"]
        else:
            api_name = name + "_api_start_B_" + load_dict["initialize"]["cloud"]
    create_api.create_job(name=api_name, config_xml=conf_api_xml)
    new_name_rollbak = api_name.replace('api_start', "api_rollback")
    # print(new_name_rollbak)
    # print(api_name)
    new_api_cmd_rollback = new_api_cmd.replace('docker_start', 'second')
    root_cmd.text = str(new_api_cmd_rollback)
    tree.write('/tmp/conf_api_update_rollbak.xml')
    with open('/tmp/conf_api_update_rollbak.xml', 'r', encoding='utf-8') as api_rollbak_xml:
        conf_api_rollbak_xml = api_rollbak_xml.read()
    create_api.create_job(name=new_name_rollbak, config_xml=conf_api_rollbak_xml)
    cloud_api_conf = create_api.get_job_config(cloud_job_name)
    with  open('/tmp/' + cloud_job_name + ".xml", 'r', encoding='utf-8') as f2:
        date_xml = f2.read()
        root_all = ET.parse('/tmp/' + cloud_job_name + ".xml")
        old_config = root_all.findall('publishers')[0].getchildren()[0][1][0]
        # print(old_config)
    with open('/tmp/conf_api_update.xml', 'r', encoding='utf-8') as f3:
        conf_api_data_root = ET.parse('/tmp/conf_api_update.xml')
        tree_api_update = conf_api_data_root.getroot()
        add_config = tree_api_update.getchildren()[12][0][1].getchildren()[0].getchildren()[0]
        old_config.append(add_config)
        root_all.write('/tmp/' + cloud_job_name + "_update.xml")
    with open('/tmp/' + cloud_job_name + "_update.xml", 'r', encoding='utf-8') as cloud_xml:
        conf_cloud_xml = cloud_xml.read()
    create_api.reconfig_job(name=cloud_job_name, config_xml=conf_cloud_xml)
    root_all_rollback = ET.parse('/tmp/' + cloud_job_rollback_name + ".xml")
    old_config_rollback = root_all_rollback.findall('publishers')[0].getchildren()[0][1][0]
    # print(old_config_rollback)
    with open('/tmp/conf_api_update_rollbak.xml', 'r', encoding='utf-8') as f4:
        conf_api_data = f4.read()
        conf_api_data_root = ET.parse('/tmp/conf_api_update_rollbak.xml')
        tree_rollback = conf_api_data_root.getroot()
        add_rollback_config = tree_rollback.getchildren()[12][0][1].getchildren()[0].getchildren()[0]
        # print(add_rollback_config)
        cloud_rollbak_name = cloud_job_name.replace("more", "more_rollback")
        old_config_rollback.append(add_rollback_config)
        root_all_rollback.write('/tmp/' + cloud_job_rollback_name + "_update.xml")
    with open('/tmp/' + cloud_job_rollback_name + "_update.xml", 'r', encoding='utf-8') as cloud_rollbak_xml:
        conf_cloud_rollbak_xml = cloud_rollbak_xml.read()
    create_api.reconfig_job(name=cloud_rollbak_name, config_xml=conf_cloud_rollbak_xml)
    build_job = jenkins.Jenkins('http://172.31.10.229', username=jenkins_name, password=jenkins_passwd)
    lastnum = build_job.build_job(api_name)


def webUI():
    create_webUI = jenkins.Jenkins('http://172.31.10.229', username=jenkins_name, password=jenkins_passwd)
    tree = ET.parse('/tmp/conf_webUI.xml')
    root = tree.getroot()
    root_url = root.getchildren()[4].getchildren()[1].getchildren()[0][0]
    root_description = root.getchildren()[1]
    root_branch = root.getchildren()[4].getchildren()[2].getchildren()[0].getchildren()[0]
    root = root.getchildren()[12]
    root_dir = root.getchildren()[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[2]
    root_path = root_dir.getchildren()[0].getchildren()[0]
    root_cmd = root_dir.getchildren()[0].getchildren()[10]
    root_ssh = root.getchildren()[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[0]
    webUI_name = name + "_webUI" + "_" + load_dict["initialize"]["cloud"]
    if create_webUI.job_exists(webUI_name) == None:
        new_webUI_path = "/opt/project/code/"
        new_webUI_description = name + "-webUI"
        new_webUI_ssh_name = load_dict["initialize"]["d,zabbix-agent-hostname"]
        new_webUI_branch = "*/master"
        new_webUI_cmd = 'cd /opt/project/code\nsudo sh git.sh webUI' + " " + name
        root_cmd.text = str(new_webUI_cmd)
        # new_webUI_url = load_dict["webUI"]["webUI_url"]
        root_description.text = str(new_webUI_description)
        root_path.text = str(new_webUI_path)
        # root_url.text = str(new_webUI_url)
        root_ssh.text = str(new_webUI_ssh_name)
        root_branch.text = str(new_webUI_branch)
        tree.write('/tmp/conf_webUI_update.xml')
        with open('/tmp/conf_webUI_update.xml', 'r', encoding='utf-8') as webUI_xml:
            conf_webUI_xml = webUI_xml.read()
        create_webUI.create_job(name=webUI_name, config_xml=conf_webUI_xml)
        build_job = jenkins.Jenkins('http://172.31.10.229', username=jenkins_name, password=jenkins_passwd)
        lastnum = build_job.build_job(webUI_name)
        time.sleep(90)
    else:
        print("%s was existed pls check web job and del it , run again scripts" % webUI_name)


def nginx():
    nginx_gitlab()
    create_nginx_job = jenkins.Jenkins('http://172.31.10.229', username=jenkins_name, password=jenkins_passwd)
    tree = ET.parse('/tmp/conf_nginx.xml')
    root = tree.getroot()
    root_description = root.getchildren()[1]
    root_url = root.getchildren()[4].getchildren()[1].getchildren()[0][0]
    root_branch = root.getchildren()[4].getchildren()[2].getchildren()[0].getchildren()[0]
    root = root.getchildren()[12]
    root_dir = root.getchildren()[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[2]
    root_path = root_dir.getchildren()[0].getchildren()[0]
    root_cmd = root_dir.getchildren()[0].getchildren()[10]
    root_ssh = root.getchildren()[0].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[0]
    nginx_name = name + "-nginx" + "_" + load_dict["initialize"]["cloud"]
    if create_nginx_job.job_exists(nginx_name) == None:
        new_nginx_path = "/opt/lnmp/nginx/conf/vhost/" + name + "/"
        new_nginx_description = name + "-nginx"
        new_nginx_ssh_name = load_dict["initialize"]["d,zabbix-agent-hostname"]
        new_nginx_branch = "*/" + name
        new_nginx_url = "http://git.nbet-group.com/yun/cloud_site_nginx_config_" + load_dict["initialize"][
            "cloud"] + ".git"
        root_url.text = str(new_nginx_url)
        root_description.text = str(new_nginx_description)
        root_path.text = str(new_nginx_path)
        root_ssh.text = str(new_nginx_ssh_name)
        root_cmd.text = "sudo /etc/init.d/nginx reload"
        root_branch.text = str(new_nginx_branch)
        tree.write('/tmp/conf_nginx_update.xml')
        with open('/tmp/conf_nginx_update.xml', 'r', encoding='utf-8') as nginx_xml:
            conf_nginx_xml = nginx_xml.read()
        create_nginx_job.create_job(name=nginx_name, config_xml=conf_nginx_xml)
        build_job = jenkins.Jenkins('http://172.31.10.229', username=jenkins_name, password=jenkins_passwd)
        lastnum = build_job.build_job(nginx_name)
    else:
        print("%s was existed pls check web job and del it, run again scripts" % nginx_name)


def zabbix():
    zabbix_site = load_dict["initialize"]["a,站点标识"]
    zabbix_listen_ip = load_dict["initialize"]["h,nginx_ip"]
    # 当前zabbix环境的URL
    zabbix_url = "http://172.31.14.24/api_jsonrpc.php"
    zabbix_header = {"Content-Type": "application/json"}

    # 用户名密码
    zabbix_user = "Sky"
    zabbix_pass = "sky66658"

    # 链接模版
    Dick_status = "10305"
    Docker_Monitor = "10277"
    Template_OS_Linux = "10001"
    nginx_status = "10263"
    tcp_status_Template = "10337"
    template_nginx = [Dick_status, Docker_Monitor, Template_OS_Linux, nginx_status, tcp_status_Template]
    template_api = [Dick_status, Docker_Monitor, Template_OS_Linux, tcp_status_Template]

    def zabbix_api_common(data):
        """获取token"""
        data = json.dumps(data).encode(encoding='utf-8')
        req = request.Request(zabbix_url, headers=zabbix_header, data=data)
        result = request.urlopen(req).read()
        return json.loads(result)

    def get_token():
        """初始默认值 ，获取token"""
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": zabbix_user,
                "password": zabbix_pass
            },
            "id": 0
        }
        result = zabbix_api_common(data)
        return result['result']

    token = get_token()
    # ngix 服务  和API 服务监控
    nginx_template_list = []
    for item in template_nginx:
        nginx_template_list.append({"templateid": item})

    api_template_list = []
    for item in template_api:
        api_template_list.append({"templateid": item})

    # 主机信息
    hostname = load_dict["initialize"]["c,zabbix-agent配置"]
    alias_name = load_dict["initialize"]["d,zabbix-agent-hostname"]
    hostip = uname[0].split('-')[1:]
    zabbix_ip = '.'.join(hostip)
    groupid = 2
    templateid = "10001"
    groupname = "Linux servers"

    # 接入的数据
    data_nginx = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": hostname,
            "name": alias_name,
            "interfaces": [{
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": zabbix_ip,
                "dns": "",
                "port": "10050"
            }],
            "groups": [{
                "groupid": groupid
            }],
            "templates": nginx_template_list,
        },
        "auth": token,
        "id": 1
    }
    data_api = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": hostname,
            "name": alias_name,
            "interfaces": [{
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": zabbix_ip,
                "dns": "",
                "port": "10050"
            }],
            "groups": [{
                "groupid": groupid
            }],
            "templates": api_template_list,
        },
        "auth": token,
        "id": 1
    }

    # print(data)
    for i in sys.argv:
        if i == 'nginx':
            result = zabbix_api_common(data_nginx)
            print(result)
            msg = '''
# Author : laobai
# @Time : 2020/2/15 15:37
# @Site :
# @File : 监听nginx服务器大于20秒.py
# @Software: PyCharm
# -*- coding: utf-8 -*-              
import redis
import json,sys,os
import time
import socket
import subprocess
hostName = socket.gethostname()
#uname = hostName.split(".")
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
# conn = redis.Redis(host="192.168.30.101", port=6379,password="youbottest!@#")
r = redis.Redis(host=uname, port=6379,db=0,decode_responses=True)
class RedisHelper:
    def __init__(self):
        self.__conn = r
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub


obj = RedisHelper()
redis_sub = obj.subscribe()
node_id = []
while True:
    msg = redis_sub.parse_response()
    if msg:
        node_id.append(msg[2])
        tuple_list = list(set(node_id))
        for i in tuple_list:
            if uname == i.split(':')[0] and r.exists(i) != 1:
                os.system('/opt/zabbix_server/agentd-shell/politeness_docker.sh' +" " + i.split(':')[1] + " " + i.split(':')[0] + " " + '%s')
                r.set(i,'1',ex=60,nx=True)
        node_id = []''' % zabbix_site
            with open('/opt/zabbix_server/agentd-shell/listen_greater_10.py', 'w', encoding='utf-8') as f:
                for line in msg:
                    f.write(line)
            f.close()
        elif i == 'api':
            result = zabbix_api_common(data_api)
            print(result)
            msg_zabbix = '''
# Author : laobai
# @Time : 2020/2/15 15:37
# @Site :
# @File : 监听nginx服务器大于20秒.py
# @Software: PyCharm
# -*- coding: utf-8 -*-            
import redis
import json, sys, os
import time
import socket
import subprocess
hostName = socket.gethostname()
uname = hostName.split(".")[0].split('ip-')[1].replace('-','.')
redis_ip = "%s"
r = redis.Redis(host=redis_ip, port=6379, db=0, decode_responses=True)
class RedisHelper:
    def __init__(self):
        self.__conn = r
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub


obj = RedisHelper()
redis_sub = obj.subscribe()
node_id = []
while True:
    msg = redis_sub.parse_response()
    if msg:
        node_id.append(msg[2])
        tuple_list = list(set(node_id))
        for i in tuple_list:
            if uname == i.split(':')[0] and r.exists(i) != 1:
                os.system('/scripts/politeness_docker.sh' + " " + i.split(':')[1] + " " + i.split(':')[0] + " " + %s)
                r.set(i, '1', ex=60, nx=True)
        node_id = []
''' % (zabbix_listen_ip, zabbix_site)
            with open('/opt/zabbix_server/agentd-shell/listen_greater_10.py', 'w', encoding='utf-8') as f:
                for line in msg_zabbix:
                    f.write(line)
            f.close()
        else:
            continue
    os.system("./opt/zabbix_server/sbin/zabbix_agentd")


def elk():
    filebeat_site = load_dict["initialize"]["a,站点标识"]
    filebeat_api_name = load_dict["initialize"]["d,zabbix-agent-hostname"]
    filebeat_cld = load_dict["initialize"]["cloud"]
    filebeat_site_api = load_dict["initialize"]["b,站点配置"]

    msg_nginx = '''
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
setup.template.settings:
  index.number_of_shards: 3
setup.kibana:
processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/messages
  fields:
    %s: messages
    fields_under_root: true
  tags: ["syslog"]
- type: log
  enabled: true
  paths:
    - /opt/lnmp/nginx/logs/apiApi_%s.log
    - /opt/lnmp/nginx/logs/webUI_%s.log
  json.keys_under_root: true
  json.overwrite_keys: true
  fields:
    %s: nginx-access
    fields_under_root: true
  tags: ["nginx-access_cld_%s"]
- type: log
  enabled: true
  paths:
    - /opt/lnmp/nginx/logs/nginx_error.log
    - /opt/lnmp/nginx/logs/error.log*
  fields:
    %s: nginx-error
    fields_under_root: true
  tags: ["nginx-error"]
output.redis:
  hosts: ["172.31.3.15"]
  port: "17788"
  key: "*"
  password: APPLE!@#++--123''' % (filebeat_api_name, filebeat_site, filebeat_site, filebeat_api_name, filebeat_cld, filebeat_api_name)
    msg_api = '''
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
setup.template.settings:
  index.number_of_shards: 3
setup.kibana:
processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/messages
  fields:
    %s: messages                                     
    fields_under_root: true
  tags: ["syslog"]
- type: log
  enabled: true
  paths:
    - /opt/logs/%s/Logs/20200209/*.txt                  
    - /opt/logs/%s_2/Logs/20200209/*.txt
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}'
  multiline.negate: true
  multiline.match: after
  fields:
    %s: %s
    fields_under_root: true
  tags: ["applog"]
output.redis:
  hosts: ["172.31.3.15"]
  port: "17788"
  key: "*"
  password: APPLE!@#++--123''' % (filebeat_api_name, filebeat_site_api, filebeat_site_api, filebeat_api_name, filebeat_site_api)
    for i in sys.argv:
        if i == 'nginx':
            with open('/opt/elk/filebeat-6.5.4/filebeat.yml', 'w', encoding='utf-8') as f:
                for line in msg_nginx:
                    f.write(line)
        elif i == 'api':
            with open('/opt/elk/filebeat-6.5.4/filebeat.yml', 'w', encoding='utf-8') as f:
                for line in msg_api:
                    f.write(line)
        else:
            continue
        f.close()
    os.system("sh /opt/elk/filebeat-6.5.4/date.sh")


cmd = ['initialize', 'nginx', 'webUI', 'settlement', 'api', 'zabbix', 'elk']
build_job = ['nginx', 'webUI', 'settlement', 'api', 'zabbix', 'elk']
if __name__ == '__main__':
    initialize()
    for i in sys.argv:
        if i != sys.argv[0]:
            if i in cmd:
                print('starting create job %s' % i)
                eval(i)()
                print('end create job %s' % i)
            else:
                print('invaild input pls check')