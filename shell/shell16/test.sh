#! /bin/bash
#mongoDB backup for Ubuntu 14.04 server
#file name backup.sh
#time: 2016/04/23

MONGODIR=/home/mongodb/bin/
DATE=`date +%Y%m%d`
OLDDATE=`date -d "3 days ago" +%Y%m%d`
oldDATE=`date -d "6 days ago" +%Y%m%d`
echo "taday--$DATE"
echo "3 days ago --$OLDDATE"
echo "6 days ago go -->$oldDATE"

for((i=$oldDATE; i<$OLDDATE; i++)) 
do
#mkdir $i
echo $i
rm -r $i > /dev/null 2>&1

done

#BACKDIR=/home/backup/
#
#if [ ! -d ${BACKDIR}/${DATE} ]
#    then
#mkdir ${BACKDIR}/${DATE}
#fi
#
##backup mongodb data
#
##$MONGODIR/mongodump -h 127.0.0.1 -d sgr -o ${BACKDIR}/${DATE} 
#$MONGODIR/mongodump -h 127.0.0.1 -o ${BACKDIR}/${DATE} 
#
#if [ $? = 0 ] 
#   then
#echo "sucessfull!"
#fi
