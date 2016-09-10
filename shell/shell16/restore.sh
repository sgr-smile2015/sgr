#! /bin/bash
#mongoDB restore for Ubuntu 14.04 server
#file name restore.sh
#time: 2016/04/23

MONGODIR=/home/mongodb/bin
DATE=`date +%Y%m%d`
OLDDATE=`date -d "10 days ago" +%Y%m%d`
echo $DATE
echo $OLDDATE
BACKDIR=/home/backup
#restore mongodb data

#/mongorestore -h 127.0.0.1 -d sgr --dir /home/backup/sgr/
$MONGODIR/mongorestore -h 127.0.0.1  --dir ${BACKDIR}/${DATE}/

if [ $? = 0 ] 
   then
echo "sucessfull!"
fi
