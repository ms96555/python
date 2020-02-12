#!/bin/bash
# 先把elk的安装tar包 和zabbix 安装tar包 移到tmp下
n=$(cat /scripts/conf.json |grep 'a,'|awk -F ':' '{print $2}'|awk -F '"' '{print $2}')
config=$(cat /scripts/conf.json |grep 'b,'|awk -F ':' '{print $2}'|awk -F '"' '{print $2}')
z=$(cat /scripts/conf.json |grep 'c,'|awk -F ':' '{print $2}'|awk -F '"' '{print $2}')
zn=$(cat /scripts/conf.json |grep 'd,'|awk -F ':' '{print $2}'|awk -F '"' '{print $2}')
oracle=$(cat /scripts/conf.json |grep 'e,oracle'|awk -F ':' '{print $2}'|awk -F '"' '{print $2}')
redis=$(cat /scripts/conf.json |grep 'f,'|awk -F ': "' '{print $2}'|awk -F '"' '{print $1}')
redisbak=$(cat /scripts/conf.json |grep 'g,'|awk -F ': "' '{print $2}'|awk -F '"' '{print $1}')
redis_ip=$(cat /scripts/conf.json |grep 'h,'|awk -F ': "' '{print $2}'|awk -F '"' '{print $1}')
echo "exclude=kernel centos-release*" >>/etc/yum.conf
yum -y update
#设置市区
rm -rf /etc/localtime
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#安装日常软件包
yum install -y wget net-tools vim telnet curl unzip lvm2

#安装redis
yum install epel-release -y 
yum install -y  redis
sed -i "s/bind 127.0.0.1/bind $redis_ip/g" /etc/redis.conf
cd /tmp
nohup redis-server /etc/redis.conf &

#安装ntp并执行时间同步
yum install -y ntp crontabs ntpdate
ntpdate -u pool.ntp.org
#echo -e "#定时同步时间\n /30 * root ntpdate -u 172.31.42.116 >> /dev/null" >> /etc/crontab
systemctl restart crond.service
systemctl enable crond.service
#修改系统限制
cat >> /etc/security/limits.conf<<eof
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
eof
echo "fs.file-max=65535" >> /etc/sysctl.conf
echo 'vm.overcommit_memory=1' >> /etc/sysctl.conf
echo 'ulimit -SHn 65535' >> /etc/rc.local
sysctl -p

#添加到开机启动
echo "echo 'never' > /sys/kernel/mm/transparent_hugepage/enabled && echo 'never' > /sys/kernel/mm/transparent_hugepage/defrag" >> /etc/rc.local
echo "echo '2048' > /proc/sys/net/core/somaxconn" >> /etc/rc.local
chmod +x /etc/rc.local

#对TCP／IP网络参数进行调整
echo 'net.ipv4.tcp_syncookies = 1' >> /etc/sysctl.conf
sudo tee -a /etc/sysctl.conf <<-EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
cat >> /etc/sysctl.conf <<EOF
net.ipv4.tcp_fin_timeout = 2
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_keepalive_time =600
net.ipv4.ip_local_port_range = 4000 65000
net.ipv4.tcp_max_syn_backlog = 16384
net.ipv4.tcp_max_tw_buckets = 36000
net.ipv4.route.gc_timeout = 100
net.ipv4.tcp_syn_retries = 1
net.ipv4.tcp_synack_retries = 1
net.core.somaxconn = 16384
net.core.netdev_max_backlog = 16384
net.ipv4.tcp_max_orphans = 16384
net.nf_conntrack_max = 25000000
EOF
sysctl -p

#关闭SElinux
sed -i.bak 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config
setenforce 0

#关闭邮件You have new mail in /var/spool/mail/root提示
echo "unset MAILCHECK" >> /etc/profile

#关闭邮件服务
systemctl stop postfix.service
systemctl disable postfix.service

#卸载无用干扰程序
sudo yum -y remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine

#启用内核转发IPtables
sudo tee -a /etc/sysctl.conf <<-EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl -p

#安装基础环境
yum install -y yum-utils device-mapper-persistent-data

#安装yum源
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

#安装DockerCE
yum -y install docker-ce

#启动Docker守护进程
systemctl start docker
systemctl enable docker

#获取appsvc/dotnetcore镜像到本地
docker pull appsvc/dotnetcore


mkdir -p /opt/project/code/$n/api/publish
mkdir -p /opt/project/code/$n/appDownload	
mkdir -p /opt/project/code/$n/webUI
mkdir -p /opt/lnmp/nginx/conf/vhost/$n
mkdir -p /opt/project/code/config
cat >/opt/project/code/config/$config.config<< EOF
<configuration>
  <connectionStrings>
    <$oracle/>
  </connectionStrings>

  <appSettings>
    <!--平台类型(前端接口=Api，云后台=Web，云平台=Platform)-->
    <add key="ProjectType" value="Api"/>
    <!-- 平台标识配置 -->
    <add key="PlatformIdent" value="$n" />
    <!-- ================== 1：开发系统相关配置 ================== -->
    <!-- 登陆提供者模式：Session、Cookie-->
    <add key="LoginProvider" value="Cookie" />
    <!-- 启用系统日志-->
    <add key="IsLog" value="true" />
    <!-- 数据库超时间-->
    <add key="CommandTimeout" value="180" />
    <!--启用IP过滤 -->
    <add key="IsIPFilter" value="false" />
    <!-- ================== 2：系统软件参数配置 ================== -->
    <!-- 联系我们 -->
    <add key="Contact" value="www.niupeng.co" />
    <!-- 软件名称 -->
    <add key="SoftName" value="天天發財快速开发框架" />
    <!-- 软件版本 -->
    <add key="Version" value="1.0" />
    <!-- 软件授权码 测试备用 -->
    <add key="LicenceKey" value="vcLREOoScamURS2eTDePUA==" />
    <!--同步数据操作 授权码-->
    <add key="DataSyncKey" value="LEEMbkimEPSaWdUv01Xh7LYvU1gSistb4tFJCCiROWg=" />
    <!-- ================== 3：外部邮件参数 ================== -->
    <!-- 设置邮箱名称 -->
    <add key="MailName" value="邮件中心" />
    <!-- 设置邮箱地址 -->
    <add key="MailUserName" value="sendbug@niupeng.co" />
    <!-- 设置邮箱密码 -->
    <add key="MailPassword" value="123456" />
    <!-- 设置邮箱主机 -->
    <add key="MailHost" value="smtp.ym.163.com" />
    <!-- ================== 4：消息推送配置 ================== -->
    <!--AppID-->
    <add key="MessagePushAppID" value="aSTtkVpJDI90Zxt0ThRZL" />
    <!--AppKey-->
    <add key="MessagePushAppKey" value="y0G3VsGVLq6uKdcXcz9Ie3" />
    <!--MasterSecret-->
    <add key="MessagePushMasterSecret" value="J3EFqYfPuYAsq0grULW4i2" />
    <!--HOST-->
    <add key="MessagePushHost" value="" />
    <!--redis配置101.102.225.156-->
    <add key="RedisHost" value="rd_b.x-y-l.com" />
    <add key="RedisPort" value="6379" />
    <add key="RedisPwd" value="np!QAZ" />
    <add key="RedisDefaultdatabase" value="5" />
    <add key="ExpireMinutes" value="30" />
    <!--redis配置  END-->
    <!--定时收集在线人数   -->
    <add key="cronExpr" value="0 0/20 * * * ?" />
    <!--开彩网彩票接口-->
    <add key="apiplusLottery" value="http://zddd.apiplus.net" />
    <add key="tokenLottery" value="d50f47440dc9b586" />
    <!--星彩网彩票接口-->
    <add key="apiLottery" value="http://aaaa.apilottery.com/api/2053966777b1ed6bda74dad8cac6274d/{0}/json" />
    <!--博易网彩票接口  -->
    <add key="apib1cpLottery" value="http://api.b1cp.com" />
    <add key="apib1cpToken" value="599f19fc9e7efc2b" />
    <!--六合彩当年生肖-->
    <add key="hk6CurrAnimals" value="猪" />
    <!--真人彩票池地址：-->
    <add key="LiveApiUrl" value="http://dzqpzrhgapigame004.com" />
    <!-- 彩票池地址：-->
    <add key="LotteyApiUrl" value="http://ubetliveapi.com" />
    <!--彩票手动开奖接数来源类型（live/web）：-->
    <add key="getdataType" value="live" />
    <!-- 默认为现金盘,代理信用盘部署时需修改credit [ money、credit]-->
    <add key="webType" value="credit" />
    <!--跨域配置-->
    <add key="AllowUrl" value="http://127.0.0.1:8020,http://localhost:5000,10.8.15.188" />
    <!--是否开启账号替换-->
    <!--add key="UserIdKeyEnable" value="false"/-->
    <!--替换账号KEY只能是字母不能有重复字母-->
    <!--add key="UserIdKey" value="AOPGHTCGWQ"/-->
    <add key ="LotteryApiType" value=""/>
    <add key="UserLogInEnable" value=""/>
    <!--redis配置101.102.225.156  defaultdatabase存储库 connectTimeout 超时间（毫秒） PoolSize（池）-->
    <$redis/>
    <!--新增限流配置Redis defaultdatabase存储库 connectTimeout 超时时间（毫秒-->
    <$redisbak/>
    <!-- 是否开启登录验证码  true为开启-->
    <add key="UserLoginVerify" value="true" />
    <!-- 验证码验证模式:[1:简单;2:中等;3:复杂] -->
    <add key="VerifyMode" value="0" />
    <!--真人加密密钥-->
    <add key="LiveRsaKey" value="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQEhUty/iC5TwCGaZNzfGJ6ihyq3pzp8w1NZA3thEJjS3vNm/ovfpyImkngkImDKEIpEu85TP4Jq9p50LlJtgDM8LrtrflU97+vDUQN3aLYQ/EOYFCLed3tkRFS9llCeEO8c2M63+/KJngYv0/sDDCoakd2jhWwiKzgmn/2+G1yQIDAQAB" />
    <!--真人签名-->
    <add key="LiveSignKey" value="1234567890ABCabc"/>
    <!--真人新开关-->
    <add key="LiveAPiVerify" value="true"/>
    <!--真人新请求地址-->
    <add key="LiveAPiCoreURL" value="http://live-api-1255110395.ap-northeast-1.elb.amazonaws.com"/>
    <!--IP地址解析-->
    <add key="ProvinceURL" value="http://192.168.16.188:9999"/>
    <!--IP地址解析开关，关闭默认走百度IP翻译接口-->
    <add key="Province" value="false"/>
    <!--开启真人图片-->
    <add key="LiveImgCheck" value="false"/>
    <!-- 是否开启试玩账号 true为开启-->
    <add key="UserPlay" value="false" />
    <!--进入真人是否验证秘钥-->
    <add key="LivePloginKey" value="true"/>
  </appSettings>
</configuration>
EOF
chown -R centos.centos /opt/project/code/
chown -R centos.centos /opt/lnmp/nginx/conf/vhost/$n

cat >/opt/lnmp/nginx/conf/nginx.conf<<EOF
user  www www;
worker_processes auto;
error_log  /opt/lnmp/nginx/logs/nginx_error.log  crit;
pid        /opt/lnmp/nginx/logs/nginx.pid;
worker_rlimit_nofile 51200;

events{
        use epoll;
        worker_connections 51200;
        multi_accept on;
}

http
    {
        include       mime.types;
        default_type  application/octet-stream;

       log_format main '{'
'"host": "\$host",'
'"server_addr": "\$server_addr",'
'"http_x_forwarded_for":"\$http_x_forwarded_for",'
'"remote_addr":"\$remote_addr",'
'"time_local":"\$time_local",'
'"request_method":"\$request_method",'
'"uri":"\$uri",'
'"status":\$status,'
'"body_bytes_sent":\$body_bytes_sent,'
'"http_referer":"\$http_referer",'
'"http_user_agent":"\$http_user_agent",'
'"upstream_addr":"\$upstream_addr",'
'"upstream_status":"\$upstream_status",'
'"upstream_response_time":"\$upstream_response_time",'
'"request_time":\$request_time'
'}';
        log_format main_greater_10 '{'
        '"upstream_addr":\"$upstream_addr",'
        '"upstream_response_time":"\$upstream_response_time",'
        '}';

        server_names_hash_bucket_size 512;
        client_header_buffer_size 32k;
        large_client_header_buffers 4 32k;
        client_max_body_size 50m;

        tcp_nodelay on;
        tcp_nopush on;
        keepalive_timeout 120;

        sendfile on;

        fastcgi_connect_timeout 300;
        fastcgi_send_timeout 300;
        fastcgi_read_timeout 300;
        fastcgi_buffer_size 64k;
        fastcgi_buffers 4 64k;
        fastcgi_busy_buffers_size 128k;
        fastcgi_temp_file_write_size 256k;
       
        map \$sent_http_content_type \$expires {
        default         off;
        application/pdf 42d;
        ~image/         max;
        application/javascript 365d;
        text/css        365d;
        }

        limit_req_zone \$http_x_forwarded_for zone=one:10m rate=10r/m;

        gzip on;
        gzip_min_length  1k;
        gzip_buffers     4 16k;
        gzip_http_version 1.1;
        gzip_comp_level 2;
        gzip_types     text/plain application/javascript application/x-javascript text/javascript text/css application/xml application/xml+rss;
        gzip_vary on;
        gzip_proxied   expired no-cache no-store private auth;
        gzip_disable   "MSIE [1-6]\.";

        server_tokens off;
        access_log off;

#        req_status_zone server_name \$server_name 256k;
#       req_status_zone server_addr \$server_addr 256k;
#        req_status_zone server_url  \$server_name$uri 512k;
#        req_status server_name server_addr server_url;

        server{
        listen 800 default_server;
        server_name 127.0.0.1;

        location /nginx_status{
            stub_status on;
            access_log   off;
            allow 172.31.39.211;
            allow 127.0.0.1;
            deny all;
        }

#        location /ttlsa_req_status{
#           req_status_show on;
#           access_log   off;
#           allow 127.0.0.1;
#           allow 172.31.39.211;
#           deny all;
#        }
    }
    include vhost/*.conf;
    include vhost/*/*.conf;
}
EOF

cat >/opt/lnmp/nginx/conf/proxy_set.conf<<EOF
proxy_redirect off;

if ( \$uri ~* /api/User/ ) {
     expires off;
}
if ( \$uri ~* /User/ ) {
     expires off;
}
proxy_set_header Host \$host;
proxy_set_header X-Real-IP \$remote_addr;
proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;

proxy_set_header Connection "";
proxy_http_version 1.1;
proxy_set_header Cookie \$http_cookie;
client_max_body_size 10m;
client_body_buffer_size 128k;
proxy_connect_timeout 90;
proxy_send_timeout 90;
proxy_read_timeout 90;
proxy_buffer_size 4k;
proxy_buffers 4 32k;
proxy_busy_buffers_size 64k;
proxy_temp_file_write_size 64k;
EOF

cat >/opt/lnmp/nginx/logs/nginx_log.sh<<EOF
#!/bin/bash
#初始化
echo \$(date +%Y%m%d-%T) >> /tmp/nginx.txt
LOGS_PATH=/opt/lnmp/nginx/logs
YESTERDAY=\$(date -d "yesterday" +%Y%m%d)

#获取日志个数
lognumber=\$(ls \$LOGS_PATH/*.log|wc -l)

#循环按天切割日志
for((i=1;i<=\$lognumber;i++));
do
logspath=\$(ls \$LOGS_PATH/*.log|sed 's/ /\n/g'|sed -n '1p');
mv "\${logspath}" "\${logspath}-\${YESTERDAY}"
done

#向nginx主进程发送USR1信号，重新打开日志文件，否则会继续往mv后的文件写数据的。原因在于：linux系统中，内核是根据文件描述符来找文件的。如果不这样操作导致日志切割失败。
kill -USR1 \`ps axu | grep "nginx: master process" | grep -v grep | awk '{print \$2}'\`

#删除7天前的日志
cd \${LOGS_PATH}
find . -mtime +2 -name "*20[1-9][1-9]*" | xargs rm -f
#定义删除两天前日志的函数
LOGS=/opt/logs/
function logs () {
a=\$(ls \$LOGS);
for b in \$a;
do
if [ -d \$b ];then
cd \$b/Logs/ ;
find . -mtime +2 -name "*20[1-9][3-9]*" | xargs rm -rf
cd ../..;
else
echo "\$LOGS 不是目录"
fi
done
}
#应用函数
cd \$LOGS
logs
exit 0
EOF
chown -R centos.centos /opt/lnmp/nginx/logs/nginx_log.sh
chmod +x /opt/lnmp/nginx/logs/nginx_log.sh

cat >/opt/project/docker_img_del.sh<<EOF
#!/bin/bash
dockernamenumber=\$(docker images | awk '{print \$1}' |sort -u|sed '/appsvc\/dotnetcore/d' |sed '/REPOSITORY/d'|wc -l);
echo \$(date +%Y%m%d-%T) >> /tmp/docker.txt

for((i=1;i<=\$dockernamenumber;i++));
do
name=\$(docker images | awk '{print \$1}' |sort -u|sed '/appsvc\/dotnetcore/d' |sed '/REPOSITORY/d' |sed -n \$i'p')
sudo docker images \$name|awk '{print \$1":"\$2}'|sed -n '7,\$p'|xargs -i docker rmi {}
done
docker image prune -f
EOF
chown -R centos.centos /opt/project/docker_img_del.sh
chmod +x /opt/project/docker_img_del.sh

sudo cat >/var/spool/cron/root<<EOF
0 0 * * 7 /bin/bash /opt/project/docker_img_del.sh >> /dev/null
0 0 * * * /bin/bash /opt/lnmp/nginx/logs/nginx_log.sh >> /dev/null
0 0 * * * /bin/bash /opt/zabbix_server/agentd-shell/check_nginx_start.sh >> /dev/null
1 0 * * * /bin/bash /opt/elk/filebeat-6.5.4/date.sh >> /dev/null
*/30 * * * * ntpdate -u 172.31.42.116 >> /dev/null
EOF

#sed -i '$d' /etc/crontab
#echo " /30 * root ntpdate -u 172.31.42.116 >> /dev/null" >>/etc/crontab
yum install epel-release -y
yum install htop -y
wget https://github.com/bcicen/ctop/releases/download/v0.5/ctop-0.5-linux-amd64 -O ctop
sudo mv ctop /usr/local/bin/
sudo chmod +x /usr/local/bin/ctop
cd /tmp/
tar xf zabbix_server.tar.gz -C /opt/
rm -rf zabbix_server.tar.gz 
cd

sed -i 's/^Hostname.*/Hostname='$z'/g' /opt/zabbix_server/etc/zabbix_agentd.conf

echo "$zn" >/opt/zabbix_server/agentd-shell/name.txt
/etc/init.d/zabbix_agent restart

cat >/root/oracle-paping.sh<<EOF
#!/bin/bash
paping -p 1521 or_b.x-y-l.com
EOF
cat >/root/redis-paping.sh<<EOF
#!/bin/bash
paping -p 6379 rd_b.x-y-l.com
EOF
chmod +x oracle-paping.sh
chmod +x redis-paping.sh

wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/paping/paping_1.5.5_x86_linux.tar.gz
yum install glibc.i686 libstdc++.so.6 -y
tar xf paping_1.5.5_x86_linux.tar.gz -C /usr/bin/
chown -R root:root /usr/bin/paping
chmod 775 /usr/bin/paping
rm -rf paping_1.5.5_x86_linux.tar.gz
cat >/etc/docker/daemon.json<<EOF
{"insecure-registries":["http://dk-img.n-b-e-t.com:7777"]}
EOF
sudo systemctl restart docker
docker login dk-img.n-b-e-t.com:7777 -u admin -p UYi9vYAtqMhW1g^*NcoudPecpg6OGwBJ
docker=`sudo docker search dk-img.n-b-e-t.com:7777/api |awk '{if (NR>1) {print $1}}' |awk -F: '{print $3}' |sort -r`
version=`echo "$docker" |sed -n 1p`
sudo docker pull dk-img.n-b-e-t.com:7777/api:$version
docker_2=`sudo docker search dk-img.n-b-e-t.com:7777/pay_site_api |awk '{if (NR>1) {print $1}}' |awk -F: '{print $3}' |sort -r`
version_2=`echo "$docker_2" |sed -n 1p`
sudo docker pull dk-img.n-b-e-t.com:7777/pay_site_api:$version_2
cd /tmp/
tar xf elk.tar.gz -C /opt
rm -rf elk.tar.gz
echo 'it is ok'>>/opt/last.log
date=$(date +%Y%m%d)
cat >/opt/elk/filebeat-6.5.4/filebeat.yml<<EOF
###################### Filebeat Configuration Example #########################

# This file is an example configuration file highlighting only the most common
# options. The filebeat.reference.yml file from the same directory contains all the
# supported options with more comments. You can use it as a reference.
#
# You can find the full configuration reference here:
# https://www.elastic.co/guide/en/beats/filebeat/index.html

# For more available modules and options, please see the filebeat.reference.yml sample
# configuration file.

#=========================== Filebeat inputs =============================

#filebeat.inputs:

# Each - is an input. Most options can be set at the input level, so
# you can use different inputs for various configurations.
# Below are the input specific configurations.

#- type: log

  # Change to true to enable this input configuration.
#  enabled: false

  # Paths that should be crawled and fetched. Glob based paths.
#  paths:
#    - /var/log/*.log
    #- c:\programdata\elasticsearch\logs\*

  # Exclude lines. A list of regular expressions to match. It drops the lines that are
  # matching any regular expression from the list.
  #exclude_lines: ['^DBG']

  # Include lines. A list of regular expressions to match. It exports the lines that are
  # matching any regular expression from the list.
  #include_lines: ['^ERR', '^WARN']

  # Exclude files. A list of regular expressions to match. Filebeat drops the files that
  # are matching any regular expression from the list. By default, no files are dropped.
  #exclude_files: ['.gz\$']

  # Optional additional fields. These fields can be freely picked
  # to add additional information to the crawled log files for filtering
  #fields:
  #  level: debug
  #  review: 1

  ### Multiline options

  # Multiline can be used for log messages spanning multiple lines. This is common
  # for Java Stack Traces or C-Line Continuation

  # The regexp Pattern that has to be matched. The example pattern matches all lines starting with [
  #multiline.pattern: ^\[

  # Defines if the pattern set under pattern should be negated or not. Default is false.
  #multiline.negate: false

  # Match can be set to "after" or "before". It is used to define if lines should be append to a pattern
  # that was (not) matched before or after or as long as a pattern is not matched based on negate.
  # Note: After is the equivalent to previous and before is the equivalent to to next in Logstash
  #multiline.match: after


#============================= Filebeat modules ===============================

filebeat.config.modules:
  # Glob pattern for configuration loading
  path: \${path.config}/modules.d/*.yml

  # Set to true to enable config reloading
  reload.enabled: false

  # Period on which files under path should be checked for changes
  #reload.period: 10s

#==================== Elasticsearch template setting ==========================

setup.template.settings:
  index.number_of_shards: 3
  #index.codec: best_compression
  #_source.enabled: false

#================================ General =====================================

# The name of the shipper that publishes the network data. It can be used to group
# all the transactions sent by a single shipper in the web interface.
#name:

# The tags of the shipper are included in their own field with each
# transaction published.
#tags: ["service-X", "web-tier"]

# Optional fields that you can specify to add additional information to the
# output.
#fields:
#  env: staging


#============================== Dashboards =====================================
# These settings control loading the sample dashboards to the Kibana index. Loading
# the dashboards is disabled by default and can be enabled either by setting the
# options here, or by using the -setup CLI flag or the setup command.
#setup.dashboards.enabled: false

# The URL from where to download the dashboards archive. By default this URL
# has a value which is computed based on the Beat name and version. For released
# versions, this URL points to the dashboard archive on the artifacts.elastic.co
# website.
#setup.dashboards.url:

#============================== Kibana =====================================

# Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
# This requires a Kibana endpoint configuration.
setup.kibana:

  # Kibana Host
  # Scheme and port can be left out and will be set to the default (http and 5601)
  # In case you specify and additional path, the scheme is required: http://localhost:5601/path
  # IPv6 addresses should always be defined as: https://[2001:db8::1]:5601
  #host: "localhost:5601"

  # Kibana Space ID
  # ID of the Kibana Space into which the dashboards should be loaded. By default,
  # the Default Space will be used.
  #space.id:

#============================= Elastic Cloud ==================================

# These settings simplify using filebeat with the Elastic Cloud (https://cloud.elastic.co/).

# The cloud.id setting overwrites the output.elasticsearch.hosts and
# setup.kibana.host options.
# You can find the cloud.id in the Elastic Cloud web UI.
#cloud.id:

# The cloud.auth setting overwrites the output.elasticsearch.username and
# output.elasticsearch.password settings. The format is <user>:<pass>.
#cloud.auth:

#================================ Outputs =====================================

# Configure what output to use when sending the data collected by the beat.

#-------------------------- Elasticsearch output ------------------------------
#output.elasticsearch:
  # Array of hosts to connect to.
#  hosts: ["localhost:9200"]

  # Optional protocol and basic auth credentials.
  #protocol: "https"
  #username: "elastic"
  #password: "changeme"

#----------------------------- Logstash output --------------------------------
#output.logstash:
  # The Logstash hosts
  #hosts: ["localhost:5044"]

  # Optional SSL. By default is off.
  # List of root certificates for HTTPS server verifications
  #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]

  # Certificate for SSL client authentication
  #ssl.certificate: "/etc/pki/client/cert.pem"

  # Client Certificate Key
  #ssl.key: "/etc/pki/client/cert.key"

#================================ Procesors =====================================

# Configure processors to enhance or manipulate events generated by the beat.

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~

#================================ Logging =====================================

# Sets log level. The default log level is info.
# Available log levels are: error, warning, info, debug
#logging.level: debug

# At debug level, you can selectively enable logging only for some components.
# To enable all selectors use ["*"]. Examples of other selectors are "beat",
# "publish", "service".
#logging.selectors: ["*"]

#============================== Xpack Monitoring ===============================
# filebeat can export internal metrics to a central Elasticsearch monitoring
# cluster.  This requires xpack monitoring to be enabled in Elasticsearch.  The
# reporting is disabled by default.

# Set to true to enable the monitoring reporter.
#xpack.monitoring.enabled: false

# Uncomment to send the metrics to Elasticsearch. Most settings from the
# Elasticsearch output are accepted here as well. Any setting that is not set is
# automatically inherited from the Elasticsearch output configuration, so if you
# have the Elasticsearch output configured, you can simply uncomment the
# following line.
#xpack.monitoring.elasticsearch:
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/messages
  fields:
    $zn: messages
    fields_under_root: true
  tags: ["syslog"]
- type: log
  enabled: true
  paths:
    - /opt/lnmp/nginx/logs/apiApi_$n.log
    - /opt/lnmp/nginx/logs/webUI_$n.log
  json.keys_under_root: true
  json.overwrite_keys: true
  fields:
    $zn: nginx-access
    fields_under_root: true
  tags: ["nginx-access"]
- type: log
  enabled: true
  paths:
    - /opt/lnmp/nginx/logs/nginx_error.log
    - /opt/lnmp/nginx/logs/error.log*
  fields:
    $zn: nginx-error
    fields_under_root: true
  tags: ["nginx-error"]
- type: log
  enabled: true
  paths:
    - /opt/logs/api_$n/Logs/$date/*.txt
    - /opt/logs/api_${n}_2/Logs/$date/*.txt
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}\ [0-9]{2}:[0-9]{2}:[0-9]{2}'
  multiline.negate: true
  multiline.match: after
  fields:
    $zn: api_$n
    fields_under_root: true
  tags: ["applog"]
output.logstash:
  hosts: ["172.31.29.145:5044"]
EOF
echo 'test ok ' >>/opt/last.log
chmod +x /opt/elk/filebeat-6.5.4/date.sh
sh /opt/elk/filebeat-6.5.4/date.sh
