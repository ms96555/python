#!/bin/bash
yum install wget gcc zlib* bzip2 bzip2-devel  ncurses ncurses-devel  readline readline-devel  openssl openssl-devel  openssl-static  xz lzma xz-devel  sqlite sqlite-devel  gdbm gdbm-devel  tk tk-devel -y
echo "starting download python3...pls wait..."
mkdir -p /scripts
cd /scripts
wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz 2>/opt/res.txt 1>&2
echo "python3 tar has download in node|starting download openssl-1.1.1a..."
echo "starting make install python"
tar xf /scripts/Python-3.6.6.tgz
sleep 10
cd /scripts/Python-3.6.6
./configure --prefix=/usr/local/python/
make && make install
if [ $? -eq 0 ];then
  echo "make install finished..."
  ln -s /usr/local/python/bin/python3 /usr/bin/python3
  ln -s /usr/local/python/bin/pip3 /usr/bin/pip
  pip install --upgrade pip
  pip install paramiko
  pip install requests
  pip install python-jenkins
  pip install jenkins
  pip install gitlab
  pip install python-gitlab
  pip install psutil
   if [ $? -eq 0 ];then
     python3 /scripts/create_nodes.py $1 $2 $3 $4 $5
   else
     echo "something wrong pls check..."
  fi
else
  echo "something wrong pls check..."
  exit 1
fi 
