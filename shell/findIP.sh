#! /bin/bash

invok_tar (){
tar -xzvf jdk7u13-linux-x64.tar.gz -C /usr/local/ > /dev/null 2>&1

echo 'JAVA_HOME=/usr/local/jdk1.7.0_13' >> /etc/profile
echo 'CLASSPATH=.:$JAVA_HOME/lib/tools.jar' >> /etc/profile
echo 'PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile
echo 'export JAVA_HOME CLASSPATH PATH' >> /etc/profile

source /etc/profile
}

#invok_tar
JDK_V=`java -version > a 2>&1` 
java_flag=`awk '{print $1}' a` 
java_flag=`echo ${java_flag} | awk '{print $1}'` 
echo $java_flag
  if [ $java_flag = "java" ] ; then
IP=`ifconfig  |grep "inet addr:" |grep -v "127"|sed 's/^.*addr://g' |sed 's/Bcast.*$//g' |tr -d ' '`
#IP=`ifconfig  |grep "inet addr:" |grep -v "127"|sed 's/^.*addr://g' |sed 's/Bcast.*$//g' |sed 's/[[:space:]]//g'`
echo "${IP}-"
#sed  's/1.22.1.154/`$IP`/g' config.txt
sed  -i "s/1.22.1.1/$IP/g" config_TEST.xml
  else 
echo "Java JDK is error!"
  fi

rm  -f a 
