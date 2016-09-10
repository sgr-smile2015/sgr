#! /bin/bash
#CVS backup for CentOS 6.3 release
#file name cvs_backup.sh
#time: 2015/12/23

CVSDIR=/home/cvsroot/project
DATE=`date +%Y%m%d`
#OLDDATE=`date -v -10d +%Y%m%d`
OLDDATE=`date -d "10 days ago" +%Y%m%d`
echo $DATE
echo $OLDDATE

#BACKDIR=/data/backup/cvs_backup
#FILENAME=cvsbackup_${DATE}

#if [ ! -d ${BACKDIR}/${DATE} ]
#    then
#mkdir ${BACKDIR}/${DATE}
#fi
#
#HOST=192.168.2.22
#FTP_NAME=cvs_user
#FTP_PASSWD=cvs101
#
#cd $CVSDIR
#tar zcvf $FILENAME.tar.gz $CVSDIR
#
#ftp -i -n -v << !
#open ${HOST}
#user ${FTP_NAME} ${FTP_PASSWD}
#bin
#rmdir ${OLDDATE}
#mkdir ${DATE}
#cd ${DATE}
#mput *
#bye
#!
