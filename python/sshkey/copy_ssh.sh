#! /bin/bash

cat ip.txt |while read line ; do
    ip=`echo $line | awk '{print $1}'` #提取ip
    password=`echo $line | awk '{print $2}'` #提取password
	#echo $ip $password
    python sendkey.py $ip $password
done
