#!/bin/bash
curl -o 86 "http://home.ustc.edu.cn/~mmmwhy/86"
chmod 777 86
echo "请输入jetbains激活服务器的端口 [1-65535]:"
read -p "(默认端口: 104):" httpport
[ -z "$httpport" ] && httpport="104"
echo "请输入jetbains用户名(仅英文):"
read -p "(默认用户名: feiyang):" name
[ -z "$name" ] && name="feiyang"
ip=`curl -m 10 -s http://members.3322.org/dyndns/getip`
echo "您选择的端口是：${httpport},用户名是：${name}"
echo -e "本地 IP : \033[41;37m ${ip} \033[0m"
echo "————————————————————————————————————————————————————————————————————"
echo "                                                  "
echo  -e "  License sever地址填写为 \033[41;37m  http://${ip}:${httpport} \033[0m"
echo "                                                  "
echo "————————————————————————————————————————————————————————————————————"
echo "                                                  "
echo "                                                  "
echo "                                                  "
screen -dmS IntelliJIDEALicenseServer -d -m ./86 -p ${httpport} -u ${name}
exit 1
