#! /bin/bash

#截取配置文件中version的值
ver=`cat ../apps_conf/release/config.properties_2016-05-17 |grep "version=" |awk -F = '{print $2}'`
#num=`echo $ver |xargs awk -F = '{print $2}' `
#去掉中间的 .
num=`echo $ver | tr -d '.'`
#自＋1 ，更新version版本
num=`expr $num + 1`
#new=`echo $num |sed -r 's/^()$/\1./g' `
#更新版本后填入. -> 888 变成 8.8.8.
new=`echo $num |sed 's/./&./g'`
#去掉最后的.
new=${new%?}

sed -i "s/${ver}/${new}/g" ../apps_conf/release/config.properties_2016-05-17
