#! /bin/bash
#testing locat network alive system

fun(){
for i in {100..200}
do
    host=192.168.1.$i
    #Flag=`ping -c2 $host | sed -n '2p' | awk '{ print $1}'`
	Flag=`ping -c2 $host |sed -n '6p' |awk '{print $4}'`
    #ping -c2 $host > /dev/null 2>&1 &

    if [  "$Flag" == 2 ] 
	then
	echo "$host is UP"
	echo "$host" >> ./live.txt
    else
	echo "$host is DOWN"
    fi
done
}

fun
