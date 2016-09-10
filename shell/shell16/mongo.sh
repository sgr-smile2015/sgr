#!/bin/bash   
#program   
# this shell is mongodb bat   
#history   
#2014/09/17 11:53   
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin   
export PATH   
targetpath='/home/muse68'   
nowtime=$(date +%Y%m%d%H%M)   
start()   
{   
#实现增量备份   
mongobackup --port 27017 -h 127.0.0.1 -o ${targetpath}/${nowtime} -stream   
}   
execute()   
{   
start   
if [ $? -eq 0 ]   
then   
echo "back successfully"   
else   
echo "back failure!"   
fi   
}   
if [ ! -d "${targetpath}/${nowtime}/" ]   
then   
mkdir ${targetpath}/${nowtime}   
fi   
execute   
echo "===========back end ${nowtime}==================="  
