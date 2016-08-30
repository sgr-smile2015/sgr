#! /bin/bash
# the scripts is usefull auto link to something
#author by lol

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
#find the locat dir link file such as test.war
LN_FILE=`find -type l |awk -F / '{print $2}'`

#if the link file use .war end , rm the test dir
FLAG=`echo $LN_FILE |awk -F . '{print $2}'`
DIR_WAR=`echo $LN_FILE |awk -F . '{print $1}'`

if [ ${FLAG} = 'war' ]
    then
    echo "stop the server--> $DIR_WAR"
    ../bin/shutdown.sh 
    echo "Delete --> ${DIR_WAR}"
    rm -r ${DIR_WAR}
else
    ../bin/server.sh stop
    fi


#LA_FILE=`find  test/ -type f -mmin -2 |awk -F / '{print $2}'` 
LA_FILE=`find  release/ -type f -mmin -30`

if [ ! -z $LA_FILE ]
    then
    echo "link ${LA_FILE} --> ${LN_FILE}"
    ln -sf ${LA_FILE} ${LN_FILE}
fi

sleep 2s

if [ ${FLAG} = 'war' ]
    then
    ../bin/start.sh 
else
    ../bin/server.sh start
    fi
