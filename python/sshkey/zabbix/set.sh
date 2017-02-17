#!/bin/bash

#SHELL_Env
LIB=`dpkg -l |grep libcurl3`

  if [ -z "${LIB}" ]; then
	  sudo apt-get  -y install libcurl3 
  fi 

# install zabbix-agent

sudo dpkg -i zabbix-agent_3.0.0-1+trusty_amd64.deb

sudo sed -i 's/Server=127.0.0.1/Server=192.168.1.8/g' /etc/zabbix/zabbix_agentd.conf

sudo sed -i 's/# ListenPort=10050/ListenPort=10050/g' /etc/zabbix/zabbix_agentd.conf

sudo service zabbix-agent restart
