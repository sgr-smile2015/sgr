#! /bin/bash 
#file name test-root.sh
#if root login system . the base will record

HISTSIZE=5000
export HISTTIMEFORMAT="%F %T "
user=`whoami`
if [ $user = root ]
then
ip=`who -u am i | awk '{print $NF}' | sed 's/[()]//g'`
dt=`who -u am i | awk '{print $3" "$4}'`
date=`date "+%Y-%m-%d"`
user_date=/tmp/.history/$user/$date
history_file=$user_date/${user}_history_$date.txt
login_file=$user_date/${user}_login_$date.txt
mkdir -p $user_date
echo "$user\t$dt\t$ip\n" >> $login_file
chmod 600 $login_file
touch $history_file
export HISTFILE="$history_file"
chmod 600 $history_file
fi
