#! /bin/bash
# the scripts is usefull auto link to something
#author by lol
		
#find the locat dir link file such as test.war
LN_FILE=`find -type l |awk -F / '{print $2}'` 

#if the link file use .war end , rm the test dir
FLAG=`echo $LN_FILE |awk -F . '{print $2}'`
DIR_WAR=`echo $LN_FILE |awk -F . '{print $1}'`

if [ ${FLAG} = 'war' ] 
	then
	echo "rm ${DIR_WAR}"
	rm -r ${DIR_WAR}
	fi


#LA_FILE=`find  test/ -type f -mmin -2 |awk -F / '{print $2}'` 
LA_FILE=`find  release/ -type f -mmin -1` 

if [ ! -z $LA_FILE ]
	then 
	echo "link ${LA_FILE} --> ${LN_FILE}"
	ln -sf ${LA_FILE} ${LN_FILE} 
fi
