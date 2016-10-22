#! /bin/bash
# the scripts is usefull auto link to something
#author by lol

#base_dir=`echo ${PWD%/*}`

#获取脚本所在的绝对路径，其他机器使用ansible能调用该脚本
base_dir=$(cd `dirname $0`; pwd)
cd $base_dir
config_dir=$(echo ${base_dir/webapps})

#获取链接文件的真实文件地址
config_file=`readlink -f ${config_dir}/apps_conf/config.properties`
#截取配置文件中version的值
ver=`cat ${config_file} |grep "version=" |awk -F = '{print $2}'`
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

sed -i "s/${ver}/${new}/g" ${config_file}

#find the locat dir link file such as test.war
LN_FILE=`find ${base_dir} -type l |awk -F / '{print $8}'`

#if the link file use .war end , rm the test dir
FLAG=`echo $LN_FILE |awk -F . '{print $2}'`
DIR_WAR=`echo $LN_FILE |awk -F . '{print $1}'`

if [ ${FLAG} = 'war' ]
    then
    echo "关闭服务：$DIR_WAR"
    ../bin/shutdown.sh 
    echo "删除缓存文件夹: ${DIR_WAR}"
    rm -r ${base_dir}/${DIR_WAR}
    fi

#LA_FILE=`find  test/ -type f -mmin -2 |awk -F / '{print $2}'` 
#LA_FILE=`ls -t release/*.war | head -1`
LA_FILE=`find  release/ -type f -mmin -30`


if [ ! -z $LA_FILE ]
    then
    echo "链接新文件：${LA_FILE} --> ${LN_FILE}"
    ln -sf ${LA_FILE} ${LN_FILE}
fi

sleep 2s

if [ ${FLAG} = 'war' ]
    then
    echo "重启服务：$DIR_WAR"
    ../bin/start.sh 
    fi
