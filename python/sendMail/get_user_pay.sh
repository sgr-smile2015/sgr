#!/bin/bash

BASE_DIR=$(cd `dirname $0`; pwd)

yesterday=`date "+%F" -d "1 days ago"`
today=`date "+%F"`
weeksago=`date '+%F' -d '1 week ago'`

#yesterday=`date '+%s' -d '1 days ago'`
#weeksago=`date '+%s' -d '1 week ago'`
#today=`date '+%s'`

week_flag=`date +%w`
#echo $weeksago

mail_subject="WMZY*客户端每周统计*"
if [ ${week_flag} -eq '5' ]; then
echo 'sending mail'
/usr/bin/python ${BASE_DIR}/get_user_pay.py $weeksago $today
/usr/bin/python ${BASE_DIR}/sendmail.py reciver.txt.test $mail_subject

fi

subject="wmzy客户每日端统计"
/usr/bin/python ${BASE_DIR}/get_user_pay.py $yesterday $today
/usr/bin/python ${BASE_DIR}/sendmail.py reciver.txt.test $subject
#/usr/bin/python /home/admin/cron/get_reg_user/sendmail.py reciver.txt
